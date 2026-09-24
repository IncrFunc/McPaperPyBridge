# TurtleStartDiggingEvent

[[Home-en|Home]] / [[Category-entity-en|entity]]

- Java class: `com.destroystokyo.paper.event.entity.TurtleStartDiggingEvent`
- Parent class: `org.bukkit.event.entity.EntityEvent`
- Python subscription: `TurtleStartDiggingEvent`
- Python constant: `Events.TURTLE_START_DIGGING`
- Cancellable: Yes
- Player available: Possible at runtime
- HandlerList owner: `com.destroystokyo.paper.event.entity.TurtleStartDiggingEvent`
- [Official Paper Javadoc](https://jd.papermc.io/paper/1.16.5/com/destroystokyo/paper/event/entity/TurtleStartDiggingEvent.html)

## Python example

```python
from paperpybridge import Events

@bridge.on(Events.TURTLE_START_DIGGING)
def on_event(event):
    print(event.event, event.data)
```

## `data` fields

| Field | JSON type | Java getter | Java return type | Declared in |
| --- | --- | --- | --- | --- |
| `entity` | entity summary | `getEntity()` | `org.bukkit.entity.Entity` | `com.destroystokyo.paper.event.entity.TurtleStartDiggingEvent` |
| `entityType` | string | `getEntityType()` | `org.bukkit.entity.EntityType` | `org.bukkit.event.entity.EntityEvent` |
| `location` | location summary | `getLocation()` | `org.bukkit.Location` | `com.destroystokyo.paper.event.entity.TurtleStartDiggingEvent` |

[[Data-Format-en|Wire format and limits]] · [[Event-com-destroystokyo-paper-event-entity-turtlestartdiggingevent|中文]]

If this event is not enabled, add its Java class or simple name to `events.include` in the Paper plugin configuration.
