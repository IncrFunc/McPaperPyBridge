# TurtleLayEggEvent

[[Home-en|Home]] / [[Category-entity-en|entity]]

- Java class: `com.destroystokyo.paper.event.entity.TurtleLayEggEvent`
- Parent class: `org.bukkit.event.entity.EntityEvent`
- Python subscription: `TurtleLayEggEvent`
- Python constant: `Events.TURTLE_LAY_EGG`
- Cancellable: Yes
- Player available: Possible at runtime
- HandlerList owner: `com.destroystokyo.paper.event.entity.TurtleLayEggEvent`
- [Official Paper Javadoc](https://jd.papermc.io/paper/1.16.5/com/destroystokyo/paper/event/entity/TurtleLayEggEvent.html)

## Python example

```python
from paperpybridge import Events

@bridge.on(Events.TURTLE_LAY_EGG)
def on_event(event):
    print(event.event, event.data)
```

## `data` fields

| Field | JSON type | Java getter | Java return type | Declared in |
| --- | --- | --- | --- | --- |
| `eggCount` | number | `getEggCount()` | `int` | `com.destroystokyo.paper.event.entity.TurtleLayEggEvent` |
| `entity` | entity summary | `getEntity()` | `org.bukkit.entity.Entity` | `com.destroystokyo.paper.event.entity.TurtleLayEggEvent` |
| `entityType` | string | `getEntityType()` | `org.bukkit.entity.EntityType` | `org.bukkit.event.entity.EntityEvent` |
| `location` | location summary | `getLocation()` | `org.bukkit.Location` | `com.destroystokyo.paper.event.entity.TurtleLayEggEvent` |

[[Data-Format-en|Wire format and limits]] · [[Event-com-destroystokyo-paper-event-entity-turtlelayeggevent|中文]]

If this event is not enabled, add its Java class or simple name to `events.include` in the Paper plugin configuration.
