# PlayerStartSpectatingEntityEvent

[[Home|首页]] / [[Category-player|玩家]]

- Java 类: `com.destroystokyo.paper.event.player.PlayerStartSpectatingEntityEvent`
- 父类: `org.bukkit.event.player.PlayerEvent`
- Python 订阅名: `PlayerStartSpectatingEntityEvent`
- Python 常量: `Events.PLAYER_START_SPECTATING_ENTITY`
- 可取消: 是
- 可能关联玩家: 取决于实际对象
- 处理器列表定义于: `com.destroystokyo.paper.event.player.PlayerStartSpectatingEntityEvent`
- [Paper 官方 Javadoc](https://jd.papermc.io/paper/1.16.5/com/destroystokyo/paper/event/player/PlayerStartSpectatingEntityEvent.html)

## Python 示例

```python
from paperpybridge import Events

@bridge.on(Events.PLAYER_START_SPECTATING_ENTITY)
def on_event(event):
    print(event.event, event.data)
```

## `data` 字段

| 字段 | JSON 类型 | Java getter | Java 返回类型 | 定义于 |
| --- | --- | --- | --- | --- |
| `currentSpectatorTarget` | 实体摘要 | `getCurrentSpectatorTarget()` | `org.bukkit.entity.Entity` | `com.destroystokyo.paper.event.player.PlayerStartSpectatingEntityEvent` |
| `newSpectatorTarget` | 实体摘要 | `getNewSpectatorTarget()` | `org.bukkit.entity.Entity` | `com.destroystokyo.paper.event.player.PlayerStartSpectatingEntityEvent` |

[[Data-Format|通用字段、数据格式和限制]] · [[Event-com-destroystokyo-paper-event-player-playerstartspectatingentityevent-en|English]]

若此事件尚未启用，请将其 Java 完整类名或简单类名加入 Paper 插件配置的 `events.include`。
