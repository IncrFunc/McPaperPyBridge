# PigZapEvent

[[Home|首页]] / [[Category-entity|实体]]

- Java 类: `org.bukkit.event.entity.PigZapEvent`
- 父类: `com.destroystokyo.paper.event.entity.EntityZapEvent`
- Python 订阅名: `PigZapEvent`
- Python 常量: `Events.PIG_ZAP`
- 可取消: 是
- 可能关联玩家: 取决于实际对象
- 处理器列表定义于: `com.destroystokyo.paper.event.entity.EntityZapEvent`
- [Paper 官方 Javadoc](https://jd.papermc.io/paper/1.16.5/org/bukkit/event/entity/PigZapEvent.html)

## Python 示例

```python
from paperpybridge import Events

@bridge.on(Events.PIG_ZAP)
def on_event(event):
    print(event.event, event.data)
```

## `data` 字段

| 字段 | JSON 类型 | Java getter | Java 返回类型 | 定义于 |
| --- | --- | --- | --- | --- |
| `bolt` | 实体摘要 | `getBolt()` | `org.bukkit.entity.LightningStrike` | `com.destroystokyo.paper.event.entity.EntityZapEvent` |
| `entity` | 实体摘要 | `getEntity()` | `org.bukkit.entity.Entity` | `org.bukkit.event.entity.PigZapEvent` |
| `entityType` | 字符串 | `getEntityType()` | `org.bukkit.entity.EntityType` | `org.bukkit.event.entity.EntityEvent` |
| `lightning` | 实体摘要 | `getLightning()` | `org.bukkit.entity.LightningStrike` | `org.bukkit.event.entity.PigZapEvent` |
| `pigZombie` | 实体摘要 | `getPigZombie()` | `org.bukkit.entity.PigZombie` | `org.bukkit.event.entity.PigZapEvent` |
| `replacementEntity` | 实体摘要 | `getReplacementEntity()` | `org.bukkit.entity.Entity` | `com.destroystokyo.paper.event.entity.EntityZapEvent` |
| `transformReason` | 字符串 | `getTransformReason()` | `org.bukkit.event.entity.EntityTransformEvent$TransformReason` | `org.bukkit.event.entity.EntityTransformEvent` |
| `transformedEntity` | 实体摘要 | `getTransformedEntity()` | `org.bukkit.entity.Entity` | `org.bukkit.event.entity.EntityTransformEvent` |

[[Data-Format|通用字段、数据格式和限制]] · [[Event-org-bukkit-event-entity-pigzapevent-en|English]]

若此事件尚未启用，请将其 Java 完整类名或简单类名加入 Paper 插件配置的 `events.include`。
