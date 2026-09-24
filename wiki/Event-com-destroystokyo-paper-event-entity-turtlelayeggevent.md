# TurtleLayEggEvent

[[Home|首页]] / [[Category-entity|实体]]

- Java 类: `com.destroystokyo.paper.event.entity.TurtleLayEggEvent`
- 父类: `org.bukkit.event.entity.EntityEvent`
- Python 订阅名: `TurtleLayEggEvent`
- Python 常量: `Events.TURTLE_LAY_EGG`
- 可取消: 是
- 可能关联玩家: 取决于实际对象
- 处理器列表定义于: `com.destroystokyo.paper.event.entity.TurtleLayEggEvent`
- [Paper 官方 Javadoc](https://jd.papermc.io/paper/1.16.5/com/destroystokyo/paper/event/entity/TurtleLayEggEvent.html)

## Python 示例

```python
from paperpybridge import Events

@bridge.on(Events.TURTLE_LAY_EGG)
def on_event(event):
    print(event.event, event.data)
```

## `data` 字段

| 字段 | JSON 类型 | Java getter | Java 返回类型 | 定义于 |
| --- | --- | --- | --- | --- |
| `eggCount` | 数字 | `getEggCount()` | `int` | `com.destroystokyo.paper.event.entity.TurtleLayEggEvent` |
| `entity` | 实体摘要 | `getEntity()` | `org.bukkit.entity.Entity` | `com.destroystokyo.paper.event.entity.TurtleLayEggEvent` |
| `entityType` | 字符串 | `getEntityType()` | `org.bukkit.entity.EntityType` | `org.bukkit.event.entity.EntityEvent` |
| `location` | 位置摘要 | `getLocation()` | `org.bukkit.Location` | `com.destroystokyo.paper.event.entity.TurtleLayEggEvent` |

[[Data-Format|通用字段、数据格式和限制]] · [[Event-com-destroystokyo-paper-event-entity-turtlelayeggevent-en|English]]

若此事件尚未启用，请将其 Java 完整类名或简单类名加入 Paper 插件配置的 `events.include`。
