# ExplosionPrimeEvent

[[Home-en|Home]] / [[Category-entity-en|entity]]

- Java class: `org.bukkit.event.entity.ExplosionPrimeEvent`
- Parent class: `org.bukkit.event.entity.EntityEvent`
- Python subscription: `ExplosionPrimeEvent`
- Python constant: `Events.EXPLOSION_PRIME`
- Cancellable: Yes
- Player available: Possible at runtime
- HandlerList owner: `org.bukkit.event.entity.ExplosionPrimeEvent`
- [Official Paper Javadoc](https://jd.papermc.io/paper/1.16.5/org/bukkit/event/entity/ExplosionPrimeEvent.html)

## Python example

```python
from paperpybridge import Events

@bridge.on(Events.EXPLOSION_PRIME)
def on_event(event):
    print(event.event, event.data)
```

## `data` fields

| Field | JSON type | Java getter | Java return type | Declared in |
| --- | --- | --- | --- | --- |
| `entity` | entity summary | `getEntity()` | `org.bukkit.entity.Entity` | `org.bukkit.event.entity.EntityEvent` |
| `entityType` | string | `getEntityType()` | `org.bukkit.entity.EntityType` | `org.bukkit.event.entity.EntityEvent` |
| `fire` | boolean | `getFire()` | `boolean` | `org.bukkit.event.entity.ExplosionPrimeEvent` |
| `radius` | number | `getRadius()` | `float` | `org.bukkit.event.entity.ExplosionPrimeEvent` |

[[Data-Format-en|Wire format and limits]] · [[Event-org-bukkit-event-entity-explosionprimeevent|中文]]

If this event is not enabled, add its Java class or simple name to `events.include` in the Paper plugin configuration.
