# EntityDamageByEntityEvent

[[Home|首页]] / [[Category-entity|实体]]

- Java 类: `org.bukkit.event.entity.EntityDamageByEntityEvent`
- 父类: `org.bukkit.event.entity.EntityDamageEvent`
- Python 订阅名: `EntityDamageByEntityEvent`
- Python 常量: `Events.ENTITY_DAMAGE_BY_ENTITY`
- 可取消: 是
- 可能关联玩家: 取决于实际对象
- 处理器列表定义于: `org.bukkit.event.entity.EntityDamageEvent`
- [Paper 官方 Javadoc](https://jd.papermc.io/paper/1.16.5/org/bukkit/event/entity/EntityDamageByEntityEvent.html)

## Python 示例

```python
from paperpybridge import Events

@bridge.on(Events.ENTITY_DAMAGE_BY_ENTITY)
def on_event(event):
    print(event.event, event.data)
```

## `data` 字段

| 字段 | JSON 类型 | Java getter | Java 返回类型 | 定义于 |
| --- | --- | --- | --- | --- |
| `cause` | 字符串 | `getCause()` | `org.bukkit.event.entity.EntityDamageEvent$DamageCause` | `org.bukkit.event.entity.EntityDamageEvent` |
| `damage` | 数字 | `getDamage()` | `double` | `org.bukkit.event.entity.EntityDamageEvent` |
| `damager` | 实体摘要 | `getDamager()` | `org.bukkit.entity.Entity` | `org.bukkit.event.entity.EntityDamageByEntityEvent` |
| `entity` | 实体摘要 | `getEntity()` | `org.bukkit.entity.Entity` | `org.bukkit.event.entity.EntityEvent` |
| `entityType` | 字符串 | `getEntityType()` | `org.bukkit.entity.EntityType` | `org.bukkit.event.entity.EntityEvent` |
| `finalDamage` | 数字 | `getFinalDamage()` | `double` | `org.bukkit.event.entity.EntityDamageEvent` |

[[Data-Format|通用字段、数据格式和限制]] · [[Event-org-bukkit-event-entity-entitydamagebyentityevent-en|English]]

若此事件尚未启用，请将其 Java 完整类名或简单类名加入 Paper 插件配置的 `events.include`。
