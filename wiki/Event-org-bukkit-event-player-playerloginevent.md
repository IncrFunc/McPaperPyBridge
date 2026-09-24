# PlayerLoginEvent

[[Home|首页]] / [[Category-player|玩家]]

- Java 类: `org.bukkit.event.player.PlayerLoginEvent`
- 父类: `org.bukkit.event.player.PlayerEvent`
- Python 订阅名: `PlayerLoginEvent`
- Python 常量: `Events.PLAYER_LOGIN`
- 可取消: 否
- 可能关联玩家: 取决于实际对象
- 处理器列表定义于: `org.bukkit.event.player.PlayerLoginEvent`
- [Paper 官方 Javadoc](https://jd.papermc.io/paper/1.16.5/org/bukkit/event/player/PlayerLoginEvent.html)

## Python 示例

```python
from paperpybridge import Events

@bridge.on(Events.PLAYER_LOGIN)
def on_event(event):
    print(event.event, event.data)
```

## `data` 字段

| 字段 | JSON 类型 | Java getter | Java 返回类型 | 定义于 |
| --- | --- | --- | --- | --- |
| `hostname` | 字符串 | `getHostname()` | `java.lang.String` | `org.bukkit.event.player.PlayerLoginEvent` |
| `kickMessage` | 字符串 | `getKickMessage()` | `java.lang.String` | `org.bukkit.event.player.PlayerLoginEvent` |
| `result` | 字符串 | `getResult()` | `org.bukkit.event.player.PlayerLoginEvent$Result` | `org.bukkit.event.player.PlayerLoginEvent` |

[[Data-Format|通用字段、数据格式和限制]] · [[Event-org-bukkit-event-player-playerloginevent-en|English]]

若此事件尚未启用，请将其 Java 完整类名或简单类名加入 Paper 插件配置的 `events.include`。
