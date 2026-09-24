# PaperPyBridge

[简体中文](README.zh-CN.md) · [Changelog](CHANGELOG.md) · Version **0.1.0** · Paper **1.16.5**

PaperPyBridge is an installable Python package plus a small Paper 1.16.5 plugin. Python developers use `import paperpybridge` to subscribe to Minecraft events and send messages to players. The package hides the HTTP transport, token checks, and JSON wire format. Paper never connects to NapCat; a QQ bot can use this package alongside its own OneBot client.

```text
Minecraft/Paper -- selected events --> Python package / QQ bot
Minecraft/Paper <-- messages, queries, commands -- Python package
```

## Requirements

- A Paper 1.16.5 server. Paper recommends Java 16 for this version; the plugin JAR targets Java 8 bytecode for compatibility.
- Maven to build the plugin.
- Python 3.9 or newer for the dependency-free package.

## Quick start

1. Run `mvn package` in this directory and copy `target/paper-py-bridge-0.1.0.jar` to the Paper server's `plugins` directory.
2. Start the server once to create `plugins/PaperPyBridge/config.yml`, then stop it. Replace `change-this-secret` with a private token. The plugin deliberately refuses to start with the placeholder token.
3. Run `python -m pip install -e .` to install the Python package locally. The example first reads `PAPERPY_TOKEN`; if unset, it reads this project's local Paper configuration.
4. Run `python python/example.py`, then start Paper. On the same machine, keep the default loopback addresses. If Paper and Python run on different machines, configure reachable private addresses and `PAPERPY_TOKEN`; do not expose these endpoints publicly.
5. Send a chat message in the game. The Python terminal continuously prints chat events, and you receive a `Hello from Python!` reply.

Only chat, player join, and player quit events are sent by default. The example handles chat events. If Python is offline, normal game behavior continues and the plugin logs delivery errors.

## Python package API

```python
from paperpybridge import Bridge, Events

bridge = Bridge(token="your-private-token")

@bridge.on(Events.ASYNC_PLAYER_CHAT)
def on_chat(event):
    if event.message == "!py ping":
        return event.reply("[Python] pong")

bridge.start()  # background receiver; call bridge.close() on shutdown
bridge.broadcast("Hello from Python")
# In an async QQ bot handler: await bridge.abroadcast("Hello from QQ")
```

Use `bridge.serve_forever()` instead of `start()` for a standalone script. Registered callbacks are synchronous and run in the receiver's worker threads. `bridge.handle(data)` can be used when your bot already runs its own HTTP server; it accepts a decoded event and returns a response dictionary. For proactive messages, use `bridge.broadcast(text)` or `bridge.tell(player_uuid, text)`; `abroadcast` and `atell` are async-friendly wrappers.

### Python → MC queries and operations

```python
players = bridge.online_players()  # List of Player(uuid, name)
if players:
    result = bridge.send_title(players[0].uuid, "Welcome", "From Python")
    print(result.ok, result.error)

result = bridge.run_command("list")
print(result.ok, result.error)
```

`online_players()` snapshots online players on the Paper main thread and raises `BridgeError` if the query fails. `send_title()` and `run_command()` return `OperationResult(ok, error)`. For example, an offline target returns `player_offline`, and a command outside the allowlist returns `command_not_allowed`. For commands, `ok=True` means Paper accepted and dispatched the command; it does not prove the intended game effect occurred. Async bot code can use `aonline_players()`, `asend_title()`, and `arun_command()`.

Configure command roots under `actions.allowed-commands` in `server/plugins/PaperPyBridge/config.yml`; only `list` is allowed by default. To run `time set day`, add `time` and restart Paper. Commands run as the console and must not begin with `/`; titles target online players only.

The package receives version 1 events in this shape:

```json
{"protocol_version":1,"type":"chat","server":"survival","player":{"uuid":"...","name":"Steve"},"message":"Hello"}
```

The plugin registers only chat, player join, and player quit by default; the Wiki lists every event that can be enabled. `Events` constants contain fully qualified Java class names, for example `Events.ASYNC_PLAYER_CHAT`. `chat`, `join`, and `quit` remain compatibility aliases. A handler can return `event.reply(text)`, `Broadcast(text)`, `PlayerMessage(uuid, text)`, a list of actions, or `None`. On the wire, actions look like:

```json
{"type":"player_message","player_uuid":"...","text":"Private reply"}
{"type":"broadcast","text":"Message to all online players"}
```

To react to a QQ command, call `await bridge.abroadcast(text)` in your existing async bot. NapCat/OneBot stays on the Python side of this boundary.

The plugin makes outbound HTTP requests away from the Paper main thread. It schedules all game actions back on the main thread. Event, action, and query endpoints require the shared token. The private wire protocol is versioned (`protocol_version: 1`); it accepts at most 16 KiB per message and limits each event response to 20 actions and 512 characters per action. The outbound queue is bounded so a slow Python process cannot accumulate unlimited pending requests.

## Check

```sh
mvn package
python -m pip wheel --no-deps -w dist .
python -m unittest discover -s python -v
```

The builds and Python tests check compilation, package installation metadata, and the HTTP contract. They do not replace a live Paper 1.16.5 smoke test; run the quick start against your own server before relying on it.

## Project structure

- `src/main/java/dev/paperpybridge/PaperPyBridgePlugin.java`: Paper event listener, HTTP client, and action endpoint.
- `src/main/resources/config.yml`: URLs, token, timeouts, and server identity.
- `python/paperpybridge/`: the reusable Python package.
- `python/example.py`: a small runnable example.
- `python/test_bridge.py`: behavior and HTTP authentication checks.


## Local Paper 1.16.5 server

The `server/` directory is ignored by Git and is **not included in this repository**. For local testing, create it and place a Paper 1.16.5 JAR named `paper-1.16.5-794.jar` inside. Install Java 16 on `PATH` or place a portable JDK under `server/runtime/`. Before the first full start, read and accept the [Minecraft EULA](https://aka.ms/MinecraftEULA), then set `server/eula.txt` to `eula=true`.

Run `./start-server.ps1` from the project root. It starts the server with 1–2 GiB of memory. Connect to `localhost:25565` from Minecraft; type `stop` in the server console to shut it down cleanly.


## Event subscriptions

On startup, the plugin scans its Paper 1.16.5 event catalog but registers only types selected by `events.include`. The default selection is `AsyncPlayerChatEvent`, `PlayerJoinEvent`, and `PlayerQuitEvent`. Add simple or fully qualified class names to `events.include` in `server/plugins/PaperPyBridge/config.yml` to enable more events; `"*"` opts into all events. `events.exclude` suppresses selected types. Restart Paper after changing the configuration. A Python constant names an event but does not enable forwarding on the server.

Events are snapshotted on their originating thread and sent to Python in batches of up to 32. Events without a player omit `player`. Each snapshot has `type` (legacy alias or simple name), `event` (fully qualified class name), `name`, `server`, `timestamp_ms`, `asynchronous`, optional `cancelled`, `player`, `message`, and `data`. `data` contains bounded basic fields and summaries of blocks, entities, items, and locations, not the complete Bukkit object. Python cannot synchronously cancel or modify an event. The queue is bounded; events are dropped with a log warning when Python falls behind.

```python
from paperpybridge import Events

@bridge.on(Events.PLAYER_MOVE)  # First enable PlayerMoveEvent in events.include
def on_move(event):
    print(event.player.name if event.player else None, event.data.get("to"))

@bridge.on("*")
def on_any_event(event):
    print(event.event, event.data)
```

Run `python python/example.py` locally to continuously print chat events.

`bridge.on()` also accepts fully qualified class names and `Events` constants, such as `Events.PLAYER_MOVE`. Existing `@bridge.on("chat")` handlers keep working. `@bridge.on("*")` receives only events enabled on the Paper server. High volume events such as movement and block physics can generate heavy traffic; configure `events.include` accordingly.

## Event reference

[Event Wiki home](wiki/Home-en.md) provides a category index and a separate page for each of the 333 events, with Chinese and English versions, wire format pages, a sidebar, and a footer. The versioned `wiki/` directory also contains the [Python → MC operation guide](wiki/Python-to-MC-en.md).

[All forwardable Paper 1.16.5 events and Python fields](docs/events.md) lists 333 concrete event classes by category. Each entry has its full class name, Python constant, cancellation status, actual `data` fields, and a link to the official Paper Javadoc. Enabling all of them would use 292 handler lists; the current default registers only three.

After changing `EventSnapshot` or upgrading the Paper API, run `mvn package`, `python tools/generate_event_types.py`, `python tools/generate_event_docs.py`, and `python tools/generate_wiki.py` to rebuild the constants, both language versions, and the Wiki. The generators need the local `server/cache/patched_1.16.5.jar` and Java 16 in `server/runtime`; `--paper-jar` and `--java-home` can override those paths.
