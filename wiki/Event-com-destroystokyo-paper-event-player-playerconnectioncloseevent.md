# PlayerConnectionCloseEvent

[[Home|首页]] / [[Category-player|玩家]]

- Java 类: `com.destroystokyo.paper.event.player.PlayerConnectionCloseEvent`
- 父类: `org.bukkit.event.Event`
- Python 订阅名: `PlayerConnectionCloseEvent`
- Python 常量: `Events.PLAYER_CONNECTION_CLOSE`
- 可取消: 否
- 可能关联玩家: 没有已知玩家 getter
- 处理器列表定义于: `com.destroystokyo.paper.event.player.PlayerConnectionCloseEvent`
- [Paper 官方 Javadoc](https://jd.papermc.io/paper/1.16.5/com/destroystokyo/paper/event/player/PlayerConnectionCloseEvent.html)

## Python 示例

```python
from paperpybridge import Events

@bridge.on(Events.PLAYER_CONNECTION_CLOSE)
def on_event(event):
    print(event.event, event.data)
```

## `data` 字段

| 字段 | JSON 类型 | Java getter | Java 返回类型 | 定义于 |
| --- | --- | --- | --- | --- |
| `playerName` | 字符串 | `getPlayerName()` | `java.lang.String` | `com.destroystokyo.paper.event.player.PlayerConnectionCloseEvent` |
| `playerUniqueId` | 字符串 | `getPlayerUniqueId()` | `java.util.UUID` | `com.destroystokyo.paper.event.player.PlayerConnectionCloseEvent` |

[[Data-Format|通用字段、数据格式和限制]] · [[Event-com-destroystokyo-paper-event-player-playerconnectioncloseevent-en|English]]

若此事件尚未启用，请将其 Java 完整类名或简单类名加入 Paper 插件配置的 `events.include`。
