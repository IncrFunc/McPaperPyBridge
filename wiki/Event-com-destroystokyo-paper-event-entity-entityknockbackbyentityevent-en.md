# EntityKnockbackByEntityEvent

[[Home-en|Home]] / [[Category-entity-en|entity]]

- Java class: `com.destroystokyo.paper.event.entity.EntityKnockbackByEntityEvent`
- Parent class: `org.bukkit.event.entity.EntityEvent`
- Python subscription: `EntityKnockbackByEntityEvent`
- Python constant: `Events.ENTITY_KNOCKBACK_BY_ENTITY`
- Cancellable: Yes
- Player available: Possible at runtime
- HandlerList owner: `com.destroystokyo.paper.event.entity.EntityKnockbackByEntityEvent`
- [Official Paper Javadoc](https://jd.papermc.io/paper/1.16.5/com/destroystokyo/paper/event/entity/EntityKnockbackByEntityEvent.html)

## Python example

```python
from paperpybridge import Events

@bridge.on(Events.ENTITY_KNOCKBACK_BY_ENTITY)
def on_event(event):
    print(event.event, event.data)
```

## `data` fields

| Field | JSON type | Java getter | Java return type | Declared in |
| --- | --- | --- | --- | --- |
| `entity` | entity summary | `getEntity()` | `org.bukkit.entity.LivingEntity` | `com.destroystokyo.paper.event.entity.EntityKnockbackByEntityEvent` |
| `entityType` | string | `getEntityType()` | `org.bukkit.entity.EntityType` | `org.bukkit.event.entity.EntityEvent` |
| `hitBy` | entity summary | `getHitBy()` | `org.bukkit.entity.Entity` | `com.destroystokyo.paper.event.entity.EntityKnockbackByEntityEvent` |
| `knockbackStrength` | number | `getKnockbackStrength()` | `float` | `com.destroystokyo.paper.event.entity.EntityKnockbackByEntityEvent` |

[[Data-Format-en|Wire format and limits]] · [[Event-com-destroystokyo-paper-event-entity-entityknockbackbyentityevent|中文]]

If this event is not enabled, add its Java class or simple name to `events.include` in the Paper plugin configuration.
