# PlayerInteractEvent

[[Home|首页]] / [[Category-player|玩家]]

- Java 类: `org.bukkit.event.player.PlayerInteractEvent`
- 父类: `org.bukkit.event.player.PlayerEvent`
- Python 订阅名: `PlayerInteractEvent`
- Python 常量: `Events.PLAYER_INTERACT`
- 可取消: 是
- 可能关联玩家: 取决于实际对象
- 处理器列表定义于: `org.bukkit.event.player.PlayerInteractEvent`
- [Paper 官方 Javadoc](https://jd.papermc.io/paper/1.16.5/org/bukkit/event/player/PlayerInteractEvent.html)

## Python 示例

```python
from paperpybridge import Events

@bridge.on(Events.PLAYER_INTERACT)
def on_event(event):
    print(event.event, event.data)
```

## `data` 字段

| 字段 | JSON 类型 | Java getter | Java 返回类型 | 定义于 |
| --- | --- | --- | --- | --- |
| `action` | 字符串 | `getAction()` | `org.bukkit.event.block.Action` | `org.bukkit.event.player.PlayerInteractEvent` |
| `blockFace` | 字符串 | `getBlockFace()` | `org.bukkit.block.BlockFace` | `org.bukkit.event.player.PlayerInteractEvent` |
| `clickedBlock` | 方块摘要 | `getClickedBlock()` | `org.bukkit.block.Block` | `org.bukkit.event.player.PlayerInteractEvent` |
| `hand` | 字符串 | `getHand()` | `org.bukkit.inventory.EquipmentSlot` | `org.bukkit.event.player.PlayerInteractEvent` |
| `interactionPoint` | 位置摘要 | `getInteractionPoint()` | `org.bukkit.Location` | `org.bukkit.event.player.PlayerInteractEvent` |
| `item` | 物品摘要 | `getItem()` | `org.bukkit.inventory.ItemStack` | `org.bukkit.event.player.PlayerInteractEvent` |
| `material` | 字符串 | `getMaterial()` | `org.bukkit.Material` | `org.bukkit.event.player.PlayerInteractEvent` |
| `blockInHand` | 布尔值 | `isBlockInHand()` | `boolean` | `org.bukkit.event.player.PlayerInteractEvent` |

[[Data-Format|通用字段、数据格式和限制]] · [[Event-org-bukkit-event-player-playerinteractevent-en|English]]

若此事件尚未启用，请将其 Java 完整类名或简单类名加入 Paper 插件配置的 `events.include`。
