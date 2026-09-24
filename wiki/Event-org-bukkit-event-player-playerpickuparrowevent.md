# PlayerPickupArrowEvent

[[Home|首页]] / [[Category-player|玩家]]

- Java 类: `org.bukkit.event.player.PlayerPickupArrowEvent`
- 父类: `org.bukkit.event.player.PlayerPickupItemEvent`
- Python 订阅名: `PlayerPickupArrowEvent`
- Python 常量: `Events.PLAYER_PICKUP_ARROW`
- 可取消: 是
- 可能关联玩家: 取决于实际对象
- 处理器列表定义于: `org.bukkit.event.player.PlayerPickupItemEvent`
- [Paper 官方 Javadoc](https://jd.papermc.io/paper/1.16.5/org/bukkit/event/player/PlayerPickupArrowEvent.html)

## Python 示例

```python
from paperpybridge import Events

@bridge.on(Events.PLAYER_PICKUP_ARROW)
def on_event(event):
    print(event.event, event.data)
```

## `data` 字段

| 字段 | JSON 类型 | Java getter | Java 返回类型 | 定义于 |
| --- | --- | --- | --- | --- |
| `arrow` | 实体摘要 | `getArrow()` | `org.bukkit.entity.AbstractArrow` | `org.bukkit.event.player.PlayerPickupArrowEvent` |
| `flyAtPlayer` | 布尔值 | `getFlyAtPlayer()` | `boolean` | `org.bukkit.event.player.PlayerPickupItemEvent` |
| `item` | 实体摘要 | `getItem()` | `org.bukkit.entity.Item` | `org.bukkit.event.player.PlayerPickupItemEvent` |
| `remaining` | 数字 | `getRemaining()` | `int` | `org.bukkit.event.player.PlayerPickupItemEvent` |

[[Data-Format|通用字段、数据格式和限制]] · [[Event-org-bukkit-event-player-playerpickuparrowevent-en|English]]

若此事件尚未启用，请将其 Java 完整类名或简单类名加入 Paper 插件配置的 `events.include`。
