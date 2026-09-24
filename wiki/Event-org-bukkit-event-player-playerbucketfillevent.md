# PlayerBucketFillEvent

[[Home|首页]] / [[Category-player|玩家]]

- Java 类: `org.bukkit.event.player.PlayerBucketFillEvent`
- 父类: `org.bukkit.event.player.PlayerBucketEvent`
- Python 订阅名: `PlayerBucketFillEvent`
- Python 常量: `Events.PLAYER_BUCKET_FILL`
- 可取消: 是
- 可能关联玩家: 取决于实际对象
- 处理器列表定义于: `org.bukkit.event.player.PlayerBucketFillEvent`
- [Paper 官方 Javadoc](https://jd.papermc.io/paper/1.16.5/org/bukkit/event/player/PlayerBucketFillEvent.html)

## Python 示例

```python
from paperpybridge import Events

@bridge.on(Events.PLAYER_BUCKET_FILL)
def on_event(event):
    print(event.event, event.data)
```

## `data` 字段

| 字段 | JSON 类型 | Java getter | Java 返回类型 | 定义于 |
| --- | --- | --- | --- | --- |
| `block` | 方块摘要 | `getBlock()` | `org.bukkit.block.Block` | `org.bukkit.event.player.PlayerBucketEvent` |
| `blockClicked` | 方块摘要 | `getBlockClicked()` | `org.bukkit.block.Block` | `org.bukkit.event.player.PlayerBucketEvent` |
| `blockFace` | 字符串 | `getBlockFace()` | `org.bukkit.block.BlockFace` | `org.bukkit.event.player.PlayerBucketEvent` |
| `bucket` | 字符串 | `getBucket()` | `org.bukkit.Material` | `org.bukkit.event.player.PlayerBucketEvent` |
| `hand` | 字符串 | `getHand()` | `org.bukkit.inventory.EquipmentSlot` | `org.bukkit.event.player.PlayerBucketEvent` |
| `itemStack` | 物品摘要 | `getItemStack()` | `org.bukkit.inventory.ItemStack` | `org.bukkit.event.player.PlayerBucketEvent` |

[[Data-Format|通用字段、数据格式和限制]] · [[Event-org-bukkit-event-player-playerbucketfillevent-en|English]]

若此事件尚未启用，请将其 Java 完整类名或简单类名加入 Paper 插件配置的 `events.include`。
