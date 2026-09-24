# EntityRemoveFromWorldEvent

[[Home-en|Home]] / [[Category-entity-en|entity]]

- Java class: `com.destroystokyo.paper.event.entity.EntityRemoveFromWorldEvent`
- Parent class: `org.bukkit.event.entity.EntityEvent`
- Python subscription: `EntityRemoveFromWorldEvent`
- Python constant: `Events.ENTITY_REMOVE_FROM_WORLD`
- Cancellable: No
- Player available: Possible at runtime
- HandlerList owner: `com.destroystokyo.paper.event.entity.EntityRemoveFromWorldEvent`
- [Official Paper Javadoc](https://jd.papermc.io/paper/1.16.5/com/destroystokyo/paper/event/entity/EntityRemoveFromWorldEvent.html)

## Python example

```python
from paperpybridge import Events

@bridge.on(Events.ENTITY_REMOVE_FROM_WORLD)
def on_event(event):
    print(event.event, event.data)
```

## `data` fields

| Field | JSON type | Java getter | Java return type | Declared in |
| --- | --- | --- | --- | --- |
| `entity` | entity summary | `getEntity()` | `org.bukkit.entity.Entity` | `org.bukkit.event.entity.EntityEvent` |
| `entityType` | string | `getEntityType()` | `org.bukkit.entity.EntityType` | `org.bukkit.event.entity.EntityEvent` |

[[Data-Format-en|Wire format and limits]] · [[Event-com-destroystokyo-paper-event-entity-entityremovefromworldevent|中文]]

If this event is not enabled, add its Java class or simple name to `events.include` in the Paper plugin configuration.
