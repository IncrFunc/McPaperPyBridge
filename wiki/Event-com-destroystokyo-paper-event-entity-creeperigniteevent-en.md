# CreeperIgniteEvent

[[Home-en|Home]] / [[Category-entity-en|entity]]

- Java class: `com.destroystokyo.paper.event.entity.CreeperIgniteEvent`
- Parent class: `org.bukkit.event.entity.EntityEvent`
- Python subscription: `CreeperIgniteEvent`
- Python constant: `Events.CREEPER_IGNITE`
- Cancellable: Yes
- Player available: Possible at runtime
- HandlerList owner: `com.destroystokyo.paper.event.entity.CreeperIgniteEvent`
- [Official Paper Javadoc](https://jd.papermc.io/paper/1.16.5/com/destroystokyo/paper/event/entity/CreeperIgniteEvent.html)

## Python example

```python
from paperpybridge import Events

@bridge.on(Events.CREEPER_IGNITE)
def on_event(event):
    print(event.event, event.data)
```

## `data` fields

| Field | JSON type | Java getter | Java return type | Declared in |
| --- | --- | --- | --- | --- |
| `entity` | entity summary | `getEntity()` | `org.bukkit.entity.Creeper` | `com.destroystokyo.paper.event.entity.CreeperIgniteEvent` |
| `entityType` | string | `getEntityType()` | `org.bukkit.entity.EntityType` | `org.bukkit.event.entity.EntityEvent` |
| `ignited` | boolean | `isIgnited()` | `boolean` | `com.destroystokyo.paper.event.entity.CreeperIgniteEvent` |

[[Data-Format-en|Wire format and limits]] · [[Event-com-destroystokyo-paper-event-entity-creeperigniteevent|中文]]

If this event is not enabled, add its Java class or simple name to `events.include` in the Paper plugin configuration.
