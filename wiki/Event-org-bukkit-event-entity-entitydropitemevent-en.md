# EntityDropItemEvent

[[Home-en|Home]] / [[Category-entity-en|entity]]

- Java class: `org.bukkit.event.entity.EntityDropItemEvent`
- Parent class: `org.bukkit.event.entity.EntityEvent`
- Python subscription: `EntityDropItemEvent`
- Python constant: `Events.ENTITY_DROP_ITEM`
- Cancellable: Yes
- Player available: Possible at runtime
- HandlerList owner: `org.bukkit.event.entity.EntityDropItemEvent`
- [Official Paper Javadoc](https://jd.papermc.io/paper/1.16.5/org/bukkit/event/entity/EntityDropItemEvent.html)

## Python example

```python
from paperpybridge import Events

@bridge.on(Events.ENTITY_DROP_ITEM)
def on_event(event):
    print(event.event, event.data)
```

## `data` fields

| Field | JSON type | Java getter | Java return type | Declared in |
| --- | --- | --- | --- | --- |
| `entity` | entity summary | `getEntity()` | `org.bukkit.entity.Entity` | `org.bukkit.event.entity.EntityEvent` |
| `entityType` | string | `getEntityType()` | `org.bukkit.entity.EntityType` | `org.bukkit.event.entity.EntityEvent` |
| `itemDrop` | entity summary | `getItemDrop()` | `org.bukkit.entity.Item` | `org.bukkit.event.entity.EntityDropItemEvent` |

[[Data-Format-en|Wire format and limits]] · [[Event-org-bukkit-event-entity-entitydropitemevent|中文]]

If this event is not enabled, add its Java class or simple name to `events.include` in the Paper plugin configuration.
