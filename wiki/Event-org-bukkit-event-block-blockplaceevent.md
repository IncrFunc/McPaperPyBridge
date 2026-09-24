# BlockPlaceEvent

[[Home|首页]] / [[Category-block|方块]]

- Java 类: `org.bukkit.event.block.BlockPlaceEvent`
- 父类: `org.bukkit.event.block.BlockEvent`
- Python 订阅名: `BlockPlaceEvent`
- Python 常量: `Events.BLOCK_PLACE`
- 可取消: 是
- 可能关联玩家: 取决于实际对象
- 处理器列表定义于: `org.bukkit.event.block.BlockPlaceEvent`
- [Paper 官方 Javadoc](https://jd.papermc.io/paper/1.16.5/org/bukkit/event/block/BlockPlaceEvent.html)

## Python 示例

```python
from paperpybridge import Events

@bridge.on(Events.BLOCK_PLACE)
def on_event(event):
    print(event.event, event.data)
```

## `data` 字段

| 字段 | JSON 类型 | Java getter | Java 返回类型 | 定义于 |
| --- | --- | --- | --- | --- |
| `block` | 方块摘要 | `getBlock()` | `org.bukkit.block.Block` | `org.bukkit.event.block.BlockEvent` |
| `blockAgainst` | 方块摘要 | `getBlockAgainst()` | `org.bukkit.block.Block` | `org.bukkit.event.block.BlockPlaceEvent` |
| `blockPlaced` | 方块摘要 | `getBlockPlaced()` | `org.bukkit.block.Block` | `org.bukkit.event.block.BlockPlaceEvent` |
| `hand` | 字符串 | `getHand()` | `org.bukkit.inventory.EquipmentSlot` | `org.bukkit.event.block.BlockPlaceEvent` |
| `itemInHand` | 物品摘要 | `getItemInHand()` | `org.bukkit.inventory.ItemStack` | `org.bukkit.event.block.BlockPlaceEvent` |

[[Data-Format|通用字段、数据格式和限制]] · [[Event-org-bukkit-event-block-blockplaceevent-en|English]]

若此事件尚未启用，请将其 Java 完整类名或简单类名加入 Paper 插件配置的 `events.include`。
