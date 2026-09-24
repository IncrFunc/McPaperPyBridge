# EntityTransformedEvent

[[Home-en|Home]] / [[Category-entity-en|entity]]

- Java class: `com.destroystokyo.paper.event.entity.EntityTransformedEvent`
- Parent class: `org.bukkit.event.entity.EntityEvent`
- Python subscription: `EntityTransformedEvent`
- Python constant: `Events.ENTITY_TRANSFORMED`
- Cancellable: Yes
- Player available: Possible at runtime
- HandlerList owner: `com.destroystokyo.paper.event.entity.EntityTransformedEvent`
- [Official Paper Javadoc](https://jd.papermc.io/paper/1.16.5/com/destroystokyo/paper/event/entity/EntityTransformedEvent.html)

## Python example

```python
from paperpybridge import Events

@bridge.on(Events.ENTITY_TRANSFORMED)
def on_event(event):
    print(event.event, event.data)
```

## `data` fields

| Field | JSON type | Java getter | Java return type | Declared in |
| --- | --- | --- | --- | --- |
| `entity` | entity summary | `getEntity()` | `org.bukkit.entity.Entity` | `org.bukkit.event.entity.EntityEvent` |
| `entityType` | string | `getEntityType()` | `org.bukkit.entity.EntityType` | `org.bukkit.event.entity.EntityEvent` |
| `reason` | string | `getReason()` | `com.destroystokyo.paper.event.entity.EntityTransformedEvent$TransformedReason` | `com.destroystokyo.paper.event.entity.EntityTransformedEvent` |
| `transformed` | entity summary | `getTransformed()` | `org.bukkit.entity.Entity` | `com.destroystokyo.paper.event.entity.EntityTransformedEvent` |

[[Data-Format-en|Wire format and limits]] · [[Event-com-destroystokyo-paper-event-entity-entitytransformedevent|中文]]

If this event is not enabled, add its Java class or simple name to `events.include` in the Paper plugin configuration.
