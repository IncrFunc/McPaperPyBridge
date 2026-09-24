"""Versioned HTTP transport and friendly event/action API for Python bots."""

import asyncio
import hmac
import json
import logging
import threading
from dataclasses import dataclass, field
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from typing import Callable, Dict, List, Optional, Union
from urllib.error import HTTPError, URLError
from urllib.parse import urlsplit, urlunsplit
from urllib.request import Request, urlopen

PROTOCOL_VERSION = 1
MAX_BODY_BYTES = 16_384
MAX_ACTIONS = 20
LOGGER = logging.getLogger(__name__)


class BridgeError(Exception):
    """The local protocol request or a registered handler failed."""


@dataclass(frozen=True)
class Player:
    uuid: str
    name: str


@dataclass(frozen=True)
class Broadcast:
    text: str

    def to_wire(self):
        return {"type": "broadcast", "text": self.text}


@dataclass(frozen=True)
class PlayerMessage:
    player_uuid: str
    text: str

    def to_wire(self):
        return {"type": "player_message", "player_uuid": self.player_uuid, "text": self.text}


@dataclass(frozen=True)
class OperationResult:
    """Result of a Paper operation; error is a stable machine-readable code."""

    ok: bool
    error: Optional[str] = None

    def __bool__(self):
        return self.ok


Action = Union[Broadcast, PlayerMessage]
Handler = Callable[["Event"], Optional[Union[Action, List[Action]]]]


@dataclass(frozen=True)
class Event:
    type: str
    server: str
    player: Optional[Player] = None
    message: Optional[str] = None
    event: Optional[str] = None
    name: Optional[str] = None
    data: Dict[str, object] = field(default_factory=dict)
    asynchronous: bool = False
    cancelled: Optional[bool] = None
    timestamp_ms: Optional[int] = None

    def reply(self, text: str) -> PlayerMessage:
        if self.player is None:
            raise BridgeError("This event has no player to reply to")
        return PlayerMessage(self.player.uuid, text)

    @classmethod
    def from_wire(cls, data):
        if not isinstance(data, dict) or data.get("protocol_version") != PROTOCOL_VERSION:
            raise BridgeError("Unsupported protocol version")
        event_type, server = data.get("type"), data.get("server")
        if not all(isinstance(value, str) and value for value in (event_type, server)):
            raise BridgeError("Invalid event type or server")
        player_data = data.get("player")
        player = None
        if player_data is not None:
            if not isinstance(player_data, dict):
                raise BridgeError("Invalid player")
            uuid, name = player_data.get("uuid"), player_data.get("name")
            if not all(isinstance(value, str) and value for value in (uuid, name)):
                raise BridgeError("Invalid player")
            player = Player(uuid, name)
        message = data.get("message")
        if message is not None and not isinstance(message, str):
            raise BridgeError("Invalid message")
        event_name = data.get("event", event_type)
        if not isinstance(event_name, str) or not event_name:
            raise BridgeError("Invalid event name")
        name = data.get("name", event_name.rsplit(".", 1)[-1])
        details = data.get("data", {})
        asynchronous = data.get("asynchronous", False)
        cancelled = data.get("cancelled")
        timestamp_ms = data.get("timestamp_ms")
        if not isinstance(event_name, str) or not event_name or not isinstance(name, str) or not name:
            raise BridgeError("Invalid event name")
        if not isinstance(details, dict) or not isinstance(asynchronous, bool):
            raise BridgeError("Invalid event data")
        if cancelled is not None and not isinstance(cancelled, bool):
            raise BridgeError("Invalid cancellation state")
        if timestamp_ms is not None and (isinstance(timestamp_ms, bool) or not isinstance(timestamp_ms, int)):
            raise BridgeError("Invalid timestamp")
        return cls(event_type, server, player, message, event_name, name, details,
                   asynchronous, cancelled, timestamp_ms)


class Bridge:
    """Receive Paper events and send safe, typed actions back to the game."""

    def __init__(self, token: str, *, host="127.0.0.1", port=8765,
                 paper_url="http://127.0.0.1:8766/actions"):
        if not token or token == "change-this-secret":
            raise ValueError("Use a private token shared with the Paper plugin")
        self.token = token
        self.host = host
        self.port = port
        self.paper_url = paper_url
        parts = urlsplit(paper_url)
        self.rpc_url = urlunsplit((parts.scheme, parts.netloc, "/rpc", "", ""))
        self._handlers: Dict[str, List[Handler]] = {}
        self._server = None
        self._thread = None

    def on(self, event_type: str):
        """Register a handler by alias, simple/full class name, or *."""
        def register(handler: Handler):
            self._handlers.setdefault(event_type, []).append(handler)
            return handler
        return register

    def handle(self, data):
        """Handle one event or a versioned batch of event snapshots."""
        if not isinstance(data, dict) or data.get("protocol_version") != PROTOCOL_VERSION:
            raise BridgeError("Unsupported protocol version")
        raw_events = data.get("events", [data])
        if not isinstance(raw_events, list) or len(raw_events) > 64:
            raise BridgeError("Invalid event batch")
        actions: List[Action] = []
        for raw_event in raw_events:
            event = Event.from_wire(raw_event)
            for key in dict.fromkeys((event.type, event.name, event.event, "*")):
                for handler in self._handlers.get(key, []):
                    result = handler(event)
                    if result is None:
                        continue
                    candidates = [result] if isinstance(result, (Broadcast, PlayerMessage)) else result
                    for action in candidates:
                        if not isinstance(action, (Broadcast, PlayerMessage)):
                            raise BridgeError("Handler returned an unsupported action")
                        actions.append(action)
                        if len(actions) > MAX_ACTIONS:
                            raise BridgeError("Too many actions in one response")
        return {"protocol_version": PROTOCOL_VERSION,
                "actions": [action.to_wire() for action in actions]}

    def send(self, action: Action) -> int:
        """Send an action to Paper; returns the HTTP status (normally 202)."""
        if not isinstance(action, (Broadcast, PlayerMessage)):
            raise TypeError("Expected Broadcast or PlayerMessage")
        payload = json.dumps({"protocol_version": PROTOCOL_VERSION,
                              "actions": [action.to_wire()]}, ensure_ascii=False).encode("utf-8")
        request = Request(self.paper_url, data=payload, method="POST", headers={
            "Authorization": "Bearer " + self.token,
            "Content-Type": "application/json; charset=utf-8",
        })
        with urlopen(request, timeout=5) as response:
            return response.status

    def broadcast(self, text: str) -> int:
        return self.send(Broadcast(text))

    def tell(self, player_uuid: str, text: str) -> int:
        return self.send(PlayerMessage(player_uuid, text))

    def _rpc(self, operation: str, **parameters):
        payload = json.dumps({"protocol_version": PROTOCOL_VERSION,
                              "operation": operation, **parameters}, ensure_ascii=False).encode("utf-8")
        request = Request(self.rpc_url, data=payload, method="POST", headers={
            "Authorization": "Bearer " + self.token,
            "Content-Type": "application/json; charset=utf-8",
        })
        try:
            with urlopen(request, timeout=7) as response:
                body = response.read(65_537)
        except HTTPError as error:
            raise BridgeError(f"Paper RPC returned HTTP {error.code}") from error
        except URLError as error:
            raise BridgeError(f"Cannot reach Paper RPC: {error.reason}") from error
        if len(body) > 65_536:
            raise BridgeError("Paper RPC response is too large")
        try:
            result = json.loads(body)
        except ValueError as error:
            raise BridgeError("Paper RPC returned invalid JSON") from error
        if not isinstance(result, dict) or result.get("protocol_version") != PROTOCOL_VERSION \
                or not isinstance(result.get("ok"), bool):
            raise BridgeError("Paper RPC returned an invalid response")
        if not result["ok"] and not isinstance(result.get("error"), str):
            raise BridgeError("Paper RPC returned an invalid error")
        return result

    def online_players(self) -> List[Player]:
        """Return a snapshot of the players currently online."""
        result = self._rpc("online_players")
        if not result["ok"]:
            raise BridgeError(result.get("error", "online_players_failed"))
        raw_players = result.get("players")
        if not isinstance(raw_players, list):
            raise BridgeError("Paper RPC returned an invalid player list")
        try:
            players = [Player(item["uuid"], item["name"]) for item in raw_players]
        except (KeyError, TypeError) as error:
            raise BridgeError("Paper RPC returned an invalid player list") from error
        if any(not isinstance(player.uuid, str) or not isinstance(player.name, str)
               for player in players):
            raise BridgeError("Paper RPC returned an invalid player list")
        return players

    def send_title(self, player_uuid: str, title: str, subtitle: str = "") -> OperationResult:
        """Show a title to one online player; return a reason if unavailable."""
        result = self._rpc("send_title", player_uuid=player_uuid,
                           title=title, subtitle=subtitle)
        return OperationResult(result["ok"], result.get("error"))

    def run_command(self, command: str) -> OperationResult:
        """Dispatch a command whose root is allowed by Paper configuration."""
        result = self._rpc("run_command", command=command)
        return OperationResult(result["ok"], result.get("error"))

    async def abroadcast(self, text: str) -> int:
        """Async-friendly wrapper for a QQ bot event loop."""
        return await asyncio.to_thread(self.broadcast, text)

    async def atell(self, player_uuid: str, text: str) -> int:
        return await asyncio.to_thread(self.tell, player_uuid, text)

    async def aonline_players(self) -> List[Player]:
        return await asyncio.to_thread(self.online_players)

    async def asend_title(self, player_uuid: str, title: str, subtitle: str = "") -> OperationResult:
        return await asyncio.to_thread(self.send_title, player_uuid, title, subtitle)

    async def arun_command(self, command: str) -> OperationResult:
        return await asyncio.to_thread(self.run_command, command)

    def _make_handler(self):
        bridge = self

        class EventHandler(BaseHTTPRequestHandler):
            def log_message(self, format, *args):
                LOGGER.debug("Paper HTTP: " + format, *args)

            def do_POST(self):
                if self.path != "/minecraft/events":
                    self.send_error(404)
                    return
                provided = self.headers.get("Authorization", "")
                if not hmac.compare_digest(provided, "Bearer " + bridge.token):
                    self.send_error(401)
                    return
                try:
                    length = int(self.headers.get("Content-Length", "0"))
                    if length <= 0 or length > MAX_BODY_BYTES:
                        self.send_error(413)
                        return
                    data = json.loads(self.rfile.read(length))
                    response = bridge.handle(data)
                except (ValueError, BridgeError) as error:
                    self.send_error(400, str(error))
                    return
                except Exception:
                    LOGGER.exception("Minecraft event handler failed")
                    self.send_error(500)
                    return
                body = json.dumps(response, ensure_ascii=False).encode("utf-8")
                self.send_response(200)
                self.send_header("Content-Type", "application/json; charset=utf-8")
                self.send_header("Content-Length", str(len(body)))
                self.end_headers()
                self.wfile.write(body)

        return EventHandler

    def start(self):
        """Start the event receiver in a background thread."""
        if self._server is not None:
            raise RuntimeError("Bridge is already running")
        self._server = ThreadingHTTPServer((self.host, self.port), self._make_handler())
        self._thread = threading.Thread(target=self._server.serve_forever, daemon=True)
        self._thread.start()
        return self

    def close(self):
        if self._server is not None:
            self._server.shutdown()
            self._server.server_close()
            self._thread.join(timeout=5)
            self._server = None
            self._thread = None

    def serve_forever(self):
        """Run the event receiver until Ctrl+C."""
        self.start()
        try:
            self._thread.join()
        except KeyboardInterrupt:
            pass
        finally:
            self.close()

