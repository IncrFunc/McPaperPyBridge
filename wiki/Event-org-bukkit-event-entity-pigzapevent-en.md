# PigZapEvent

[[Home-en|Home]] / [[Category-entity-en|entity]]

- Java class: `org.bukkit.event.entity.PigZapEvent`
- Parent class: `com.destroystokyo.paper.event.entity.EntityZapEvent`
- Python subscription: `PigZapEvent`
- Python constant: `Events.PIG_ZAP`
- Cancellable: Yes
- Player available: Possible at runtime
- HandlerList owner: `com.destroystokyo.paper.event.entity.EntityZapEvent`
- [Official Paper Javadoc](https://jd.papermc.io/paper/1.16.5/org/bukkit/event/entity/PigZapEvent.html)

## Python example

```python
from paperpybridge import Events

@bridge.on(Events.PIG_ZAP)
def on_event(event):
    print(event.event, event.data)
```

## `data` fields

| Field | JSON type | Java getter | Java return type | Declared in |
| --- | --- | --- | --- | --- |
| `bolt` | entity summary | `getBolt()` | `org.bukkit.entity.LightningStrike` | `com.destroystokyo.paper.event.entity.EntityZapEvent` |
| `entity` | entity summary | `getEntity()` | `org.bukkit.entity.Entity` | `org.bukkit.event.entity.PigZapEvent` |
| `entityType` | string | `getEntityType()` | `org.bukkit.entity.EntityType` | `org.bukkit.event.entity.EntityEvent` |
| `lightning` | entity summary | `getLightning()` | `org.bukkit.entity.LightningStrike` | `org.bukkit.event.entity.PigZapEvent` |
| `pigZombie` | entity summary | `getPigZombie()` | `org.bukkit.entity.PigZombie` | `org.bukkit.event.entity.PigZapEvent` |
| `replacementEntity` | entity summary | `getReplacementEntity()` | `org.bukkit.entity.Entity` | `com.destroystokyo.paper.event.entity.EntityZapEvent` |
| `transformReason` | string | `getTransformReason()` | `org.bukkit.event.entity.EntityTransformEvent$TransformReason` | `org.bukkit.event.entity.EntityTransformEvent` |
| `transformedEntity` | entity summary | `getTransformedEntity()` | `org.bukkit.entity.Entity` | `org.bukkit.event.entity.EntityTransformEvent` |

[[Data-Format-en|Wire format and limits]] · [[Event-org-bukkit-event-entity-pigzapevent|中文]]

If this event is not enabled, add its Java class or simple name to `events.include` in the Paper plugin configuration.
