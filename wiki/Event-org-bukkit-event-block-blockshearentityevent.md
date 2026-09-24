# BlockShearEntityEvent

[[Home|首页]] / [[Category-block|方块]]

- Java 类: `org.bukkit.event.block.BlockShearEntityEvent`
- 父类: `org.bukkit.event.block.BlockEvent`
- Python 订阅名: `BlockShearEntityEvent`
- Python 常量: `Events.BLOCK_SHEAR_ENTITY`
- 可取消: 是
- 可能关联玩家: 取决于实际对象
- 处理器列表定义于: `org.bukkit.event.block.BlockShearEntityEvent`
- [Paper 官方 Javadoc](https://jd.papermc.io/paper/1.16.5/org/bukkit/event/block/BlockShearEntityEvent.html)

## Python 示例

```python
from paperpybridge import Events

@bridge.on(Events.BLOCK_SHEAR_ENTITY)
def on_event(event):
    print(event.event, event.data)
```

## `data` 字段

| 字段 | JSON 类型 | Java getter | Java 返回类型 | 定义于 |
| --- | --- | --- | --- | --- |
| `block` | 方块摘要 | `getBlock()` | `org.bukkit.block.Block` | `org.bukkit.event.block.BlockEvent` |
| `entity` | 实体摘要 | `getEntity()` | `org.bukkit.entity.Entity` | `org.bukkit.event.block.BlockShearEntityEvent` |
| `tool` | 物品摘要 | `getTool()` | `org.bukkit.inventory.ItemStack` | `org.bukkit.event.block.BlockShearEntityEvent` |

[[Data-Format|通用字段、数据格式和限制]] · [[Event-org-bukkit-event-block-blockshearentityevent-en|English]]

若此事件尚未启用，请将其 Java 完整类名或简单类名加入 Paper 插件配置的 `events.include`。
