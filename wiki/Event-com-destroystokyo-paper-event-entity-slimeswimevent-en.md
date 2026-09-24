# SlimeSwimEvent

[[Home-en|Home]] / [[Category-entity-en|entity]]

- Java class: `com.destroystokyo.paper.event.entity.SlimeSwimEvent`
- Parent class: `com.destroystokyo.paper.event.entity.SlimeWanderEvent`
- Python subscription: `SlimeSwimEvent`
- Python constant: `Events.SLIME_SWIM`
- Cancellable: Yes
- Player available: Possible at runtime
- HandlerList owner: `com.destroystokyo.paper.event.entity.SlimePathfindEvent`
- [Official Paper Javadoc](https://jd.papermc.io/paper/1.16.5/com/destroystokyo/paper/event/entity/SlimeSwimEvent.html)

## Python example

```python
from paperpybridge import Events

@bridge.on(Events.SLIME_SWIM)
def on_event(event):
    print(event.event, event.data)
```

## `data` fields

| Field | JSON type | Java getter | Java return type | Declared in |
| --- | --- | --- | --- | --- |
| `entity` | entity summary | `getEntity()` | `org.bukkit.entity.Slime` | `com.destroystokyo.paper.event.entity.SlimePathfindEvent` |
| `entityType` | string | `getEntityType()` | `org.bukkit.entity.EntityType` | `org.bukkit.event.entity.EntityEvent` |

[[Data-Format-en|Wire format and limits]] · [[Event-com-destroystokyo-paper-event-entity-slimeswimevent|中文]]

If this event is not enabled, add its Java class or simple name to `events.include` in the Paper plugin configuration.
