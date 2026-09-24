# HangingPlaceEvent

[[Home|首页]] / [[Category-hanging|悬挂实体]]

- Java 类: `org.bukkit.event.hanging.HangingPlaceEvent`
- 父类: `org.bukkit.event.hanging.HangingEvent`
- Python 订阅名: `HangingPlaceEvent`
- Python 常量: `Events.HANGING_PLACE`
- 可取消: 是
- 可能关联玩家: 取决于实际对象
- 处理器列表定义于: `org.bukkit.event.hanging.HangingPlaceEvent`
- [Paper 官方 Javadoc](https://jd.papermc.io/paper/1.16.5/org/bukkit/event/hanging/HangingPlaceEvent.html)

## Python 示例

```python
from paperpybridge import Events

@bridge.on(Events.HANGING_PLACE)
def on_event(event):
    print(event.event, event.data)
```

## `data` 字段

| 字段 | JSON 类型 | Java getter | Java 返回类型 | 定义于 |
| --- | --- | --- | --- | --- |
| `block` | 方块摘要 | `getBlock()` | `org.bukkit.block.Block` | `org.bukkit.event.hanging.HangingPlaceEvent` |
| `blockFace` | 字符串 | `getBlockFace()` | `org.bukkit.block.BlockFace` | `org.bukkit.event.hanging.HangingPlaceEvent` |
| `entity` | 实体摘要 | `getEntity()` | `org.bukkit.entity.Hanging` | `org.bukkit.event.hanging.HangingEvent` |

[[Data-Format|通用字段、数据格式和限制]] · [[Event-org-bukkit-event-hanging-hangingplaceevent-en|English]]

若此事件尚未启用，请将其 Java 完整类名或简单类名加入 Paper 插件配置的 `events.include`。
