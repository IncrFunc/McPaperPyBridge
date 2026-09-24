# BlockSpreadEvent

[[Home|首页]] / [[Category-block|方块]]

- Java 类: `org.bukkit.event.block.BlockSpreadEvent`
- 父类: `org.bukkit.event.block.BlockFormEvent`
- Python 订阅名: `BlockSpreadEvent`
- Python 常量: `Events.BLOCK_SPREAD`
- 可取消: 是
- 可能关联玩家: 没有已知玩家 getter
- 处理器列表定义于: `org.bukkit.event.block.BlockSpreadEvent`
- [Paper 官方 Javadoc](https://jd.papermc.io/paper/1.16.5/org/bukkit/event/block/BlockSpreadEvent.html)

## Python 示例

```python
from paperpybridge import Events

@bridge.on(Events.BLOCK_SPREAD)
def on_event(event):
    print(event.event, event.data)
```

## `data` 字段

| 字段 | JSON 类型 | Java getter | Java 返回类型 | 定义于 |
| --- | --- | --- | --- | --- |
| `block` | 方块摘要 | `getBlock()` | `org.bukkit.block.Block` | `org.bukkit.event.block.BlockEvent` |
| `source` | 方块摘要 | `getSource()` | `org.bukkit.block.Block` | `org.bukkit.event.block.BlockSpreadEvent` |

[[Data-Format|通用字段、数据格式和限制]] · [[Event-org-bukkit-event-block-blockspreadevent-en|English]]

若此事件尚未启用，请将其 Java 完整类名或简单类名加入 Paper 插件配置的 `events.include`。
