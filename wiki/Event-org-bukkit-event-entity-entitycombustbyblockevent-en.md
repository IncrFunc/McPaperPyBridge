# EntityCombustByBlockEvent

[[Home-en|Home]] / [[Category-entity-en|entity]]

- Java class: `org.bukkit.event.entity.EntityCombustByBlockEvent`
- Parent class: `org.bukkit.event.entity.EntityCombustEvent`
- Python subscription: `EntityCombustByBlockEvent`
- Python constant: `Events.ENTITY_COMBUST_BY_BLOCK`
- Cancellable: Yes
- Player available: Possible at runtime
- HandlerList owner: `org.bukkit.event.entity.EntityCombustEvent`
- [Official Paper Javadoc](https://jd.papermc.io/paper/1.16.5/org/bukkit/event/entity/EntityCombustByBlockEvent.html)

## Python example

```python
from paperpybridge import Events

@bridge.on(Events.ENTITY_COMBUST_BY_BLOCK)
def on_event(event):
    print(event.event, event.data)
```

## `data` fields

| Field | JSON type | Java getter | Java return type | Declared in |
| --- | --- | --- | --- | --- |
| `combuster` | block summary | `getCombuster()` | `org.bukkit.block.Block` | `org.bukkit.event.entity.EntityCombustByBlockEvent` |
| `duration` | number | `getDuration()` | `int` | `org.bukkit.event.entity.EntityCombustEvent` |
| `entity` | entity summary | `getEntity()` | `org.bukkit.entity.Entity` | `org.bukkit.event.entity.EntityEvent` |
| `entityType` | string | `getEntityType()` | `org.bukkit.entity.EntityType` | `org.bukkit.event.entity.EntityEvent` |

[[Data-Format-en|Wire format and limits]] · [[Event-org-bukkit-event-entity-entitycombustbyblockevent|中文]]

If this event is not enabled, add its Java class or simple name to `events.include` in the Paper plugin configuration.
