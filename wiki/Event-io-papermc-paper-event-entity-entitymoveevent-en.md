# EntityMoveEvent

[[Home-en|Home]] / [[Category-entity-en|entity]]

- Java class: `io.papermc.paper.event.entity.EntityMoveEvent`
- Parent class: `org.bukkit.event.entity.EntityEvent`
- Python subscription: `EntityMoveEvent`
- Python constant: `Events.ENTITY_MOVE`
- Cancellable: Yes
- Player available: Possible at runtime
- HandlerList owner: `io.papermc.paper.event.entity.EntityMoveEvent`
- [Official Paper Javadoc](https://jd.papermc.io/paper/1.16.5/io/papermc/paper/event/entity/EntityMoveEvent.html)

## Python example

```python
from paperpybridge import Events

@bridge.on(Events.ENTITY_MOVE)
def on_event(event):
    print(event.event, event.data)
```

## `data` fields

| Field | JSON type | Java getter | Java return type | Declared in |
| --- | --- | --- | --- | --- |
| `entity` | entity summary | `getEntity()` | `org.bukkit.entity.Entity` | `io.papermc.paper.event.entity.EntityMoveEvent` |
| `entityType` | string | `getEntityType()` | `org.bukkit.entity.EntityType` | `org.bukkit.event.entity.EntityEvent` |
| `from` | location summary | `getFrom()` | `org.bukkit.Location` | `io.papermc.paper.event.entity.EntityMoveEvent` |
| `to` | location summary | `getTo()` | `org.bukkit.Location` | `io.papermc.paper.event.entity.EntityMoveEvent` |

[[Data-Format-en|Wire format and limits]] · [[Event-io-papermc-paper-event-entity-entitymoveevent|中文]]

If this event is not enabled, add its Java class or simple name to `events.include` in the Paper plugin configuration.
