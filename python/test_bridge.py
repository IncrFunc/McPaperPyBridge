import json
import asyncio
import threading
import unittest
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from urllib.error import HTTPError
from urllib.request import Request, urlopen

from paperpybridge import Bridge, BridgeError, Event, Events


class BridgeTest(unittest.TestCase):
    def setUp(self):
        self.event = {
            "protocol_version": 1,
            "type": "chat",
            "server": "survival",
            "player": {"uuid": "player-id", "name": "Steve"},
            "message": "!py ping",
        }

    def test_event_handler_returns_typed_private_reply(self):
        bridge = Bridge("test-secret")

        @bridge.on("chat")
        def ping(event):
            return event.reply("pong") if event.message == "!py ping" else None

        self.assertEqual(bridge.handle(self.event), {
            "protocol_version": 1,
            "actions": [{"type": "player_message", "player_uuid": "player-id", "text": "pong"}],
        })
        self.event["message"] = "ordinary chat"
        self.assertEqual(bridge.handle(self.event)["actions"], [])
        self.event["protocol_version"] = 2
        with self.assertRaises(BridgeError):
            Event.from_wire(self.event)

    def test_join_event_can_be_subscribed_to(self):
        bridge = Bridge("test-secret")
        observed = []

        @bridge.on("join")
        def on_join(event):
            observed.append((event.player.name, event.server))

        self.event["type"] = "join"
        self.event.pop("message")
        self.assertEqual(bridge.handle(self.event)["actions"], [])
        self.assertEqual(observed, [("Steve", "survival")])

    def test_full_class_event_constant_matches_legacy_chat_alias(self):
        bridge = Bridge("test-secret")
        observed = []

        @bridge.on(Events.ASYNC_PLAYER_CHAT)
        def on_chat(event):
            observed.append(event.message)

        self.event.update({
            "event": Events.ASYNC_PLAYER_CHAT,
            "name": "AsyncPlayerChatEvent",
        })
        bridge.handle(self.event)
        self.assertEqual(observed, ["!py ping"])

    def test_http_requires_token_and_handles_event(self):
        bridge = Bridge("test-secret", port=0)

        @bridge.on("chat")
        def ping(event):
            return event.reply("pong")

        bridge.start()
        try:
            url = f"http://127.0.0.1:{bridge._server.server_port}/minecraft/events"
            payload = json.dumps(self.event).encode()
            with self.assertRaises(HTTPError) as error:
                urlopen(Request(url, data=payload, method="POST"), timeout=2)
            self.assertEqual(error.exception.code, 401)
            request = Request(url, data=payload, method="POST", headers={"Authorization": "Bearer test-secret"})
            with urlopen(request, timeout=2) as response:
                self.assertEqual(response.status, 200)
                self.assertEqual(json.load(response)["actions"][0]["text"], "pong")
        finally:
            bridge.close()

    def test_package_sends_versioned_action_to_paper(self):
        received = {}

        class PaperEndpoint(BaseHTTPRequestHandler):
            def do_POST(self):
                received["path"] = self.path
                received["authorization"] = self.headers.get("Authorization")
                received["body"] = json.loads(self.rfile.read(int(self.headers["Content-Length"])))
                self.send_response(202)
                self.end_headers()

        server = ThreadingHTTPServer(("127.0.0.1", 0), PaperEndpoint)
        thread = threading.Thread(target=server.serve_forever, daemon=True)
        thread.start()
        try:
            bridge = Bridge("test-secret", paper_url=f"http://127.0.0.1:{server.server_port}/actions")
            self.assertEqual(bridge.broadcast("hello"), 202)
            self.assertEqual(received, {
                "path": "/actions",
                "authorization": "Bearer test-secret",
                "body": {"protocol_version": 1, "actions": [{"type": "broadcast", "text": "hello"}]},
            })
        finally:
            server.shutdown()
            server.server_close()
            thread.join(timeout=2)

    def test_query_title_and_command_rpc(self):
        requests = []

        class PaperRpc(BaseHTTPRequestHandler):
            def do_POST(self):
                body = json.loads(self.rfile.read(int(self.headers["Content-Length"])))
                requests.append((self.path, self.headers.get("Authorization"), body))
                operation = body["operation"]
                if operation == "online_players":
                    result = {"protocol_version": 1, "ok": True,
                              "players": [{"uuid": "player-id", "name": "Steve"}]}
                elif operation == "send_title":
                    result = {"protocol_version": 1, "ok": False, "error": "player_offline"}
                else:
                    result = {"protocol_version": 1, "ok": True}
                payload = json.dumps(result).encode()
                self.send_response(200)
                self.send_header("Content-Length", str(len(payload)))
                self.end_headers()
                self.wfile.write(payload)

            def log_message(self, *_args):
                pass

        server = ThreadingHTTPServer(("127.0.0.1", 0), PaperRpc)
        thread = threading.Thread(target=server.serve_forever, daemon=True)
        thread.start()
        try:
            bridge = Bridge("test-secret", paper_url=f"http://127.0.0.1:{server.server_port}/actions")
            self.assertEqual([(player.uuid, player.name) for player in bridge.online_players()],
                             [("player-id", "Steve")])
            title = bridge.send_title("player-id", "Hello", "World")
            self.assertFalse(title)
            self.assertEqual(title.error, "player_offline")
            self.assertTrue(bridge.run_command("list"))
            self.assertEqual(len(asyncio.run(bridge.aonline_players())), 1)
            self.assertEqual([item[0] for item in requests], ["/rpc"] * 4)
            self.assertTrue(all(item[1] == "Bearer test-secret" for item in requests))
            self.assertEqual(requests[1][2]["title"], "Hello")
            self.assertEqual(requests[2][2]["command"], "list")
        finally:
            server.shutdown()
            server.server_close()
            thread.join(timeout=2)


    def test_generic_world_event_and_batch_subscriptions(self):
        bridge = Bridge("test-secret")
        seen = []

        @bridge.on("WorldSaveEvent")
        def on_world_save(event):
            seen.append((event.player, event.data["world"]["name"], event.name))
            with self.assertRaises(BridgeError):
                event.reply("no player")

        @bridge.on("*")
        def on_any(event):
            seen.append(event.event)

        world_event = {
            "protocol_version": 1,
            "type": "WorldSaveEvent",
            "event": "org.bukkit.event.world.WorldSaveEvent",
            "name": "WorldSaveEvent",
            "server": "survival",
            "asynchronous": False,
            "timestamp_ms": 123,
            "data": {"world": {"name": "world", "uuid": "world-id"}},
        }
        result = bridge.handle({"protocol_version": 1, "events": [world_event, self.event]})
        self.assertEqual(result["actions"], [])
        self.assertEqual(seen, [
            (None, "world", "WorldSaveEvent"),
            "org.bukkit.event.world.WorldSaveEvent",
            "chat",
        ])

    def test_generic_event_rejects_invalid_optional_fields(self):
        event = dict(self.event, player=None, data=[], cancelled="yes")
        with self.assertRaises(BridgeError):
            Event.from_wire(event)
        with self.assertRaises(BridgeError):
            Bridge("test-secret").handle({"protocol_version": 1, "events": "invalid"})


if __name__ == "__main__":
    unittest.main()

