# PlayerUseUnknownEntityEvent

[[Home|首页]] / [[Category-player|玩家]]

- Java 类: `com.destroystokyo.paper.event.player.PlayerUseUnknownEntityEvent`
- 父类: `org.bukkit.event.player.PlayerEvent`
- Python 订阅名: `PlayerUseUnknownEntityEvent`
- Python 常量: `Events.PLAYER_USE_UNKNOWN_ENTITY`
- 可取消: 否
- 可能关联玩家: 取决于实际对象
- 处理器列表定义于: `com.destroystokyo.paper.event.player.PlayerUseUnknownEntityEvent`
- [Paper 官方 Javadoc](https://jd.papermc.io/paper/1.16.5/com/destroystokyo/paper/event/player/PlayerUseUnknownEntityEvent.html)

## Python 示例

```python
from paperpybridge import Events

@bridge.on(Events.PLAYER_USE_UNKNOWN_ENTITY)
def on_event(event):
    print(event.event, event.data)
```

## `data` 字段

| 字段 | JSON 类型 | Java getter | Java 返回类型 | 定义于 |
| --- | --- | --- | --- | --- |
| `entityId` | 数字 | `getEntityId()` | `int` | `com.destroystokyo.paper.event.player.PlayerUseUnknownEntityEvent` |
| `hand` | 字符串 | `getHand()` | `org.bukkit.inventory.EquipmentSlot` | `com.destroystokyo.paper.event.player.PlayerUseUnknownEntityEvent` |
| `attack` | 布尔值 | `isAttack()` | `boolean` | `com.destroystokyo.paper.event.player.PlayerUseUnknownEntityEvent` |

[[Data-Format|通用字段、数据格式和限制]] · [[Event-com-destroystokyo-paper-event-player-playeruseunknownentityevent-en|English]]

若此事件尚未启用，请将其 Java 完整类名或简单类名加入 Paper 插件配置的 `events.include`。
