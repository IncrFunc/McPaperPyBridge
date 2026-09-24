# Python → MC operations

[[Home-en|Home]] · [[Python-to-MC|中文]]

The Paper plugin serves authenticated requests at `/rpc`. These methods can be called without starting the Python event receiver.

```python
from paperpybridge import Bridge

bridge = Bridge(token="your-private-token")
players = bridge.online_players()  # list[Player] with uuid and name
title = bridge.send_title(players[0].uuid, "Welcome", "From Python") if players else None
command = bridge.run_command("list")
```

| Method | Return value | Notes |
| --- | --- | --- |
| `online_players()` | `list[Player]` | Raises `BridgeError` on query failure. |
| `send_title(uuid, title, subtitle= )` | `OperationResult` | Target must be online; `player_offline` otherwise. |
| `run_command(command)` | `OperationResult` | Console dispatch only for allowed command roots. |

`OperationResult.ok` is a boolean; `error` is a code such as `command_not_allowed`. A successful command result means Paper dispatched it, not that its intended game effect occurred. Async variants: `aonline_players`, `asend_title`, and `arun_command`.

## Command allowlist

```yaml
actions:
  allowed-commands:
    - "list"
```

Add `time` before calling `run_command("time set day")`. Restart Paper after editing its config. Commands run as the console and must not start with `/`.
