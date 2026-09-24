# BlockPistonExtendEvent

[[Home|首页]] / [[Category-block|方块]]

- Java 类: `org.bukkit.event.block.BlockPistonExtendEvent`
- 父类: `org.bukkit.event.block.BlockPistonEvent`
- Python 订阅名: `BlockPistonExtendEvent`
- Python 常量: `Events.BLOCK_PISTON_EXTEND`
- 可取消: 是
- 可能关联玩家: 没有已知玩家 getter
- 处理器列表定义于: `org.bukkit.event.block.BlockPistonExtendEvent`
- [Paper 官方 Javadoc](https://jd.papermc.io/paper/1.16.5/org/bukkit/event/block/BlockPistonExtendEvent.html)

## Python 示例

```python
from paperpybridge import Events

@bridge.on(Events.BLOCK_PISTON_EXTEND)
def on_event(event):
    print(event.event, event.data)
```

## `data` 字段

| 字段 | JSON 类型 | Java getter | Java 返回类型 | 定义于 |
| --- | --- | --- | --- | --- |
| `block` | 方块摘要 | `getBlock()` | `org.bukkit.block.Block` | `org.bukkit.event.block.BlockEvent` |
| `direction` | 字符串 | `getDirection()` | `org.bukkit.block.BlockFace` | `org.bukkit.event.block.BlockPistonEvent` |
| `length` | 数字 | `getLength()` | `int` | `org.bukkit.event.block.BlockPistonExtendEvent` |
| `sticky` | 布尔值 | `isSticky()` | `boolean` | `org.bukkit.event.block.BlockPistonEvent` |

[[Data-Format|通用字段、数据格式和限制]] · [[Event-org-bukkit-event-block-blockpistonextendevent-en|English]]

若此事件尚未启用，请将其 Java 完整类名或简单类名加入 Paper 插件配置的 `events.include`。
