# EntityPathfindEvent

[[Home-en|Home]] / [[Category-entity-en|entity]]

- Java class: `com.destroystokyo.paper.event.entity.EntityPathfindEvent`
- Parent class: `org.bukkit.event.entity.EntityEvent`
- Python subscription: `EntityPathfindEvent`
- Python constant: `Events.ENTITY_PATHFIND`
- Cancellable: Yes
- Player available: Possible at runtime
- HandlerList owner: `com.destroystokyo.paper.event.entity.EntityPathfindEvent`
- [Official Paper Javadoc](https://jd.papermc.io/paper/1.16.5/com/destroystokyo/paper/event/entity/EntityPathfindEvent.html)

## Python example

```python
from paperpybridge import Events

@bridge.on(Events.ENTITY_PATHFIND)
def on_event(event):
    print(event.event, event.data)
```

## `data` fields

| Field | JSON type | Java getter | Java return type | Declared in |
| --- | --- | --- | --- | --- |
| `entity` | entity summary | `getEntity()` | `org.bukkit.entity.Entity` | `com.destroystokyo.paper.event.entity.EntityPathfindEvent` |
| `entityType` | string | `getEntityType()` | `org.bukkit.entity.EntityType` | `org.bukkit.event.entity.EntityEvent` |
| `loc` | location summary | `getLoc()` | `org.bukkit.Location` | `com.destroystokyo.paper.event.entity.EntityPathfindEvent` |
| `targetEntity` | entity summary | `getTargetEntity()` | `org.bukkit.entity.Entity` | `com.destroystokyo.paper.event.entity.EntityPathfindEvent` |

[[Data-Format-en|Wire format and limits]] · [[Event-com-destroystokyo-paper-event-entity-entitypathfindevent|中文]]

If this event is not enabled, add its Java class or simple name to `events.include` in the Paper plugin configuration.
