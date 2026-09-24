# EntityChangeBlockEvent

[[Home-en|Home]] / [[Category-entity-en|entity]]

- Java class: `org.bukkit.event.entity.EntityChangeBlockEvent`
- Parent class: `org.bukkit.event.entity.EntityEvent`
- Python subscription: `EntityChangeBlockEvent`
- Python constant: `Events.ENTITY_CHANGE_BLOCK`
- Cancellable: Yes
- Player available: Possible at runtime
- HandlerList owner: `org.bukkit.event.entity.EntityChangeBlockEvent`
- [Official Paper Javadoc](https://jd.papermc.io/paper/1.16.5/org/bukkit/event/entity/EntityChangeBlockEvent.html)

## Python example

```python
from paperpybridge import Events

@bridge.on(Events.ENTITY_CHANGE_BLOCK)
def on_event(event):
    print(event.event, event.data)
```

## `data` fields

| Field | JSON type | Java getter | Java return type | Declared in |
| --- | --- | --- | --- | --- |
| `block` | block summary | `getBlock()` | `org.bukkit.block.Block` | `org.bukkit.event.entity.EntityChangeBlockEvent` |
| `entity` | entity summary | `getEntity()` | `org.bukkit.entity.Entity` | `org.bukkit.event.entity.EntityEvent` |
| `entityType` | string | `getEntityType()` | `org.bukkit.entity.EntityType` | `org.bukkit.event.entity.EntityEvent` |
| `to` | string | `getTo()` | `org.bukkit.Material` | `org.bukkit.event.entity.EntityChangeBlockEvent` |

[[Data-Format-en|Wire format and limits]] · [[Event-org-bukkit-event-entity-entitychangeblockevent|中文]]

If this event is not enabled, add its Java class or simple name to `events.include` in the Paper plugin configuration.
