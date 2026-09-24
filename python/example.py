import json
import os
from pathlib import Path

from paperpybridge import Bridge, Events


def local_token():
    token = os.environ.get("PAPERPY_TOKEN")
    if token:
        return token
    config = Path(__file__).resolve().parents[1] / "server/plugins/PaperPyBridge/config.yml"
    if config.is_file():
        for line in config.read_text(encoding="utf-8").splitlines():
            if line.startswith("token:"):
                return line.split(":", 1)[1].strip().strip('"\'')
    raise SystemExit("Set PAPERPY_TOKEN to the token from PaperPyBridge/config.yml")


bridge = Bridge(
    local_token(),
    host="127.0.0.1",
    port=8765,
    paper_url="http://127.0.0.1:8766/actions"
)


@bridge.on(Events.ASYNC_PLAYER_CHAT)
def show(event):
    print(json.dumps({"event": event.event, "data": event.data},
                     ensure_ascii=False), flush=True)
    return event.reply("Hello from Python!")

@bridge.on(Events.PLAYER_QUIT)
def show_exit(event):
    print(json.dumps({"event": event.event, "data": event.data},
                     ensure_ascii=False), flush=True)

print(bridge.online_players())
bridge.serve_forever()
