# EntityZapEvent

[[Home-en|Home]] / [[Category-entity-en|entity]]

- Java class: `com.destroystokyo.paper.event.entity.EntityZapEvent`
- Parent class: `org.bukkit.event.entity.EntityTransformEvent`
- Python subscription: `EntityZapEvent`
- Python constant: `Events.ENTITY_ZAP`
- Cancellable: Yes
- Player available: Possible at runtime
- HandlerList owner: `com.destroystokyo.paper.event.entity.EntityZapEvent`
- [Official Paper Javadoc](https://jd.papermc.io/paper/1.16.5/com/destroystokyo/paper/event/entity/EntityZapEvent.html)

## Python example

```python
from paperpybridge import Events

@bridge.on(Events.ENTITY_ZAP)
def on_event(event):
    print(event.event, event.data)
```

## `data` fields

| Field | JSON type | Java getter | Java return type | Declared in |
| --- | --- | --- | --- | --- |
| `bolt` | entity summary | `getBolt()` | `org.bukkit.entity.LightningStrike` | `com.destroystokyo.paper.event.entity.EntityZapEvent` |
| `entity` | entity summary | `getEntity()` | `org.bukkit.entity.Entity` | `org.bukkit.event.entity.EntityEvent` |
| `entityType` | string | `getEntityType()` | `org.bukkit.entity.EntityType` | `org.bukkit.event.entity.EntityEvent` |
| `replacementEntity` | entity summary | `getReplacementEntity()` | `org.bukkit.entity.Entity` | `com.destroystokyo.paper.event.entity.EntityZapEvent` |
| `transformReason` | string | `getTransformReason()` | `org.bukkit.event.entity.EntityTransformEvent$TransformReason` | `org.bukkit.event.entity.EntityTransformEvent` |
| `transformedEntity` | entity summary | `getTransformedEntity()` | `org.bukkit.entity.Entity` | `org.bukkit.event.entity.EntityTransformEvent` |

[[Data-Format-en|Wire format and limits]] · [[Event-com-destroystokyo-paper-event-entity-entityzapevent|中文]]

If this event is not enabled, add its Java class or simple name to `events.include` in the Paper plugin configuration.
