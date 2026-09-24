# Python → MC 操作

[[Home|首页]] · [[Python-to-MC-en|English]]

Paper 插件通过需要令牌的 `/rpc` 接口处理请求。直接调用这些方法时，不必先启动 Python 事件接收服务。

```python
from paperpybridge import Bridge

bridge = Bridge(token="你的私密令牌")
players = bridge.online_players()  # Player(uuid, name) 列表
title = bridge.send_title(players[0].uuid, "欢迎", "来自 Python") if players else None
command = bridge.run_command("list")
```

| 方法 | 返回值 | 说明 |
| --- | --- | --- |
| `online_players()` | `list[Player]` | 查询失败抛出 `BridgeError`。 |
| `send_title(uuid, title, subtitle= )` | `OperationResult` | 玩家必须在线，否则返回 `player_offline`。 |
| `run_command(command)` | `OperationResult` | 仅以控制台身份分发白名单中的命令。 |

`OperationResult.ok` 是布尔值，`error` 是 `command_not_allowed` 等错误码。命令返回成功表示 Paper 已分发，不能证明游戏效果符合预期。异步版本为 `aonline_players`、`asend_title`、`arun_command`。

## 命令白名单

```yaml
actions:
  allowed-commands:
    - "list"
```

要调用 `run_command("time set day")`，先加入 `time` 并重启 Paper。命令以控制台身份执行，不能带前导 `/`。
