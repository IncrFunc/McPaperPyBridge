# EntityTargetLivingEntityEvent

[[Home-en|Home]] / [[Category-entity-en|entity]]

- Java class: `org.bukkit.event.entity.EntityTargetLivingEntityEvent`
- Parent class: `org.bukkit.event.entity.EntityTargetEvent`
- Python subscription: `EntityTargetLivingEntityEvent`
- Python constant: `Events.ENTITY_TARGET_LIVING_ENTITY`
- Cancellable: Yes
- Player available: Possible at runtime
- HandlerList owner: `org.bukkit.event.entity.EntityTargetEvent`
- [Official Paper Javadoc](https://jd.papermc.io/paper/1.16.5/org/bukkit/event/entity/EntityTargetLivingEntityEvent.html)

## Python example

```python
from paperpybridge import Events

@bridge.on(Events.ENTITY_TARGET_LIVING_ENTITY)
def on_event(event):
    print(event.event, event.data)
```

## `data` fields

| Field | JSON type | Java getter | Java return type | Declared in |
| --- | --- | --- | --- | --- |
| `entity` | entity summary | `getEntity()` | `org.bukkit.entity.Entity` | `org.bukkit.event.entity.EntityEvent` |
| `entityType` | string | `getEntityType()` | `org.bukkit.entity.EntityType` | `org.bukkit.event.entity.EntityEvent` |
| `reason` | string | `getReason()` | `org.bukkit.event.entity.EntityTargetEvent$TargetReason` | `org.bukkit.event.entity.EntityTargetEvent` |
| `target` | entity summary | `getTarget()` | `org.bukkit.entity.LivingEntity` | `org.bukkit.event.entity.EntityTargetLivingEntityEvent` |

[[Data-Format-en|Wire format and limits]] · [[Event-org-bukkit-event-entity-entitytargetlivingentityevent|中文]]

If this event is not enabled, add its Java class or simple name to `events.include` in the Paper plugin configuration.
