# SlimeSwimEvent

[[Home|首页]] / [[Category-entity|实体]]

- Java 类: `com.destroystokyo.paper.event.entity.SlimeSwimEvent`
- 父类: `com.destroystokyo.paper.event.entity.SlimeWanderEvent`
- Python 订阅名: `SlimeSwimEvent`
- Python 常量: `Events.SLIME_SWIM`
- 可取消: 是
- 可能关联玩家: 取决于实际对象
- 处理器列表定义于: `com.destroystokyo.paper.event.entity.SlimePathfindEvent`
- [Paper 官方 Javadoc](https://jd.papermc.io/paper/1.16.5/com/destroystokyo/paper/event/entity/SlimeSwimEvent.html)

## Python 示例

```python
from paperpybridge import Events

@bridge.on(Events.SLIME_SWIM)
def on_event(event):
    print(event.event, event.data)
```

## `data` 字段

| 字段 | JSON 类型 | Java getter | Java 返回类型 | 定义于 |
| --- | --- | --- | --- | --- |
| `entity` | 实体摘要 | `getEntity()` | `org.bukkit.entity.Slime` | `com.destroystokyo.paper.event.entity.SlimePathfindEvent` |
| `entityType` | 字符串 | `getEntityType()` | `org.bukkit.entity.EntityType` | `org.bukkit.event.entity.EntityEvent` |

[[Data-Format|通用字段、数据格式和限制]] · [[Event-com-destroystokyo-paper-event-entity-slimeswimevent-en|English]]

若此事件尚未启用，请将其 Java 完整类名或简单类名加入 Paper 插件配置的 `events.include`。
