# EntityPickupItemEvent

[[Home-en|Home]] / [[Category-entity-en|entity]]

- Java class: `org.bukkit.event.entity.EntityPickupItemEvent`
- Parent class: `org.bukkit.event.entity.EntityEvent`
- Python subscription: `EntityPickupItemEvent`
- Python constant: `Events.ENTITY_PICKUP_ITEM`
- Cancellable: Yes
- Player available: Possible at runtime
- HandlerList owner: `org.bukkit.event.entity.EntityPickupItemEvent`
- [Official Paper Javadoc](https://jd.papermc.io/paper/1.16.5/org/bukkit/event/entity/EntityPickupItemEvent.html)

## Python example

```python
from paperpybridge import Events

@bridge.on(Events.ENTITY_PICKUP_ITEM)
def on_event(event):
    print(event.event, event.data)
```

## `data` fields

| Field | JSON type | Java getter | Java return type | Declared in |
| --- | --- | --- | --- | --- |
| `entity` | entity summary | `getEntity()` | `org.bukkit.entity.Entity` | `org.bukkit.event.entity.EntityPickupItemEvent` |
| `entityType` | string | `getEntityType()` | `org.bukkit.entity.EntityType` | `org.bukkit.event.entity.EntityEvent` |
| `item` | entity summary | `getItem()` | `org.bukkit.entity.Item` | `org.bukkit.event.entity.EntityPickupItemEvent` |
| `remaining` | number | `getRemaining()` | `int` | `org.bukkit.event.entity.EntityPickupItemEvent` |

[[Data-Format-en|Wire format and limits]] · [[Event-org-bukkit-event-entity-entitypickupitemevent|中文]]

If this event is not enabled, add its Java class or simple name to `events.include` in the Paper plugin configuration.
