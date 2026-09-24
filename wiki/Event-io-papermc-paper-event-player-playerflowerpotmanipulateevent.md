# PlayerFlowerPotManipulateEvent

[[Home|首页]] / [[Category-player|玩家]]

- Java 类: `io.papermc.paper.event.player.PlayerFlowerPotManipulateEvent`
- 父类: `org.bukkit.event.player.PlayerEvent`
- Python 订阅名: `PlayerFlowerPotManipulateEvent`
- Python 常量: `Events.PLAYER_FLOWER_POT_MANIPULATE`
- 可取消: 是
- 可能关联玩家: 取决于实际对象
- 处理器列表定义于: `io.papermc.paper.event.player.PlayerFlowerPotManipulateEvent`
- [Paper 官方 Javadoc](https://jd.papermc.io/paper/1.16.5/io/papermc/paper/event/player/PlayerFlowerPotManipulateEvent.html)

## Python 示例

```python
from paperpybridge import Events

@bridge.on(Events.PLAYER_FLOWER_POT_MANIPULATE)
def on_event(event):
    print(event.event, event.data)
```

## `data` 字段

| 字段 | JSON 类型 | Java getter | Java 返回类型 | 定义于 |
| --- | --- | --- | --- | --- |
| `flowerpot` | 方块摘要 | `getFlowerpot()` | `org.bukkit.block.Block` | `io.papermc.paper.event.player.PlayerFlowerPotManipulateEvent` |
| `item` | 物品摘要 | `getItem()` | `org.bukkit.inventory.ItemStack` | `io.papermc.paper.event.player.PlayerFlowerPotManipulateEvent` |
| `placing` | 布尔值 | `isPlacing()` | `boolean` | `io.papermc.paper.event.player.PlayerFlowerPotManipulateEvent` |

[[Data-Format|通用字段、数据格式和限制]] · [[Event-io-papermc-paper-event-player-playerflowerpotmanipulateevent-en|English]]

若此事件尚未启用，请将其 Java 完整类名或简单类名加入 Paper 插件配置的 `events.include`。
