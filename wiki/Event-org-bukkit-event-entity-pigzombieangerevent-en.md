# PigZombieAngerEvent

[[Home-en|Home]] / [[Category-entity-en|entity]]

- Java class: `org.bukkit.event.entity.PigZombieAngerEvent`
- Parent class: `org.bukkit.event.entity.EntityEvent`
- Python subscription: `PigZombieAngerEvent`
- Python constant: `Events.PIG_ZOMBIE_ANGER`
- Cancellable: Yes
- Player available: Possible at runtime
- HandlerList owner: `org.bukkit.event.entity.PigZombieAngerEvent`
- [Official Paper Javadoc](https://jd.papermc.io/paper/1.16.5/org/bukkit/event/entity/PigZombieAngerEvent.html)

## Python example

```python
from paperpybridge import Events

@bridge.on(Events.PIG_ZOMBIE_ANGER)
def on_event(event):
    print(event.event, event.data)
```

## `data` fields

| Field | JSON type | Java getter | Java return type | Declared in |
| --- | --- | --- | --- | --- |
| `entity` | entity summary | `getEntity()` | `org.bukkit.entity.Entity` | `org.bukkit.event.entity.PigZombieAngerEvent` |
| `entityType` | string | `getEntityType()` | `org.bukkit.entity.EntityType` | `org.bukkit.event.entity.EntityEvent` |
| `newAnger` | number | `getNewAnger()` | `int` | `org.bukkit.event.entity.PigZombieAngerEvent` |
| `target` | entity summary | `getTarget()` | `org.bukkit.entity.Entity` | `org.bukkit.event.entity.PigZombieAngerEvent` |

[[Data-Format-en|Wire format and limits]] · [[Event-org-bukkit-event-entity-pigzombieangerevent|中文]]

If this event is not enabled, add its Java class or simple name to `events.include` in the Paper plugin configuration.
