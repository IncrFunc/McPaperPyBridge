# EntityExplodeEvent

[[Home-en|Home]] / [[Category-entity-en|entity]]

- Java class: `org.bukkit.event.entity.EntityExplodeEvent`
- Parent class: `org.bukkit.event.entity.EntityEvent`
- Python subscription: `EntityExplodeEvent`
- Python constant: `Events.ENTITY_EXPLODE`
- Cancellable: Yes
- Player available: Possible at runtime
- HandlerList owner: `org.bukkit.event.entity.EntityExplodeEvent`
- [Official Paper Javadoc](https://jd.papermc.io/paper/1.16.5/org/bukkit/event/entity/EntityExplodeEvent.html)

## Python example

```python
from paperpybridge import Events

@bridge.on(Events.ENTITY_EXPLODE)
def on_event(event):
    print(event.event, event.data)
```

## `data` fields

| Field | JSON type | Java getter | Java return type | Declared in |
| --- | --- | --- | --- | --- |
| `entity` | entity summary | `getEntity()` | `org.bukkit.entity.Entity` | `org.bukkit.event.entity.EntityEvent` |
| `entityType` | string | `getEntityType()` | `org.bukkit.entity.EntityType` | `org.bukkit.event.entity.EntityEvent` |
| `location` | location summary | `getLocation()` | `org.bukkit.Location` | `org.bukkit.event.entity.EntityExplodeEvent` |
| `yield` | number | `getYield()` | `float` | `org.bukkit.event.entity.EntityExplodeEvent` |

[[Data-Format-en|Wire format and limits]] · [[Event-org-bukkit-event-entity-entityexplodeevent|中文]]

If this event is not enabled, add its Java class or simple name to `events.include` in the Paper plugin configuration.
