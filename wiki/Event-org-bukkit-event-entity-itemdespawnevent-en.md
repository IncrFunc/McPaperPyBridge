# ItemDespawnEvent

[[Home-en|Home]] / [[Category-entity-en|entity]]

- Java class: `org.bukkit.event.entity.ItemDespawnEvent`
- Parent class: `org.bukkit.event.entity.EntityEvent`
- Python subscription: `ItemDespawnEvent`
- Python constant: `Events.ITEM_DESPAWN`
- Cancellable: Yes
- Player available: Possible at runtime
- HandlerList owner: `org.bukkit.event.entity.ItemDespawnEvent`
- [Official Paper Javadoc](https://jd.papermc.io/paper/1.16.5/org/bukkit/event/entity/ItemDespawnEvent.html)

## Python example

```python
from paperpybridge import Events

@bridge.on(Events.ITEM_DESPAWN)
def on_event(event):
    print(event.event, event.data)
```

## `data` fields

| Field | JSON type | Java getter | Java return type | Declared in |
| --- | --- | --- | --- | --- |
| `entity` | entity summary | `getEntity()` | `org.bukkit.entity.Entity` | `org.bukkit.event.entity.ItemDespawnEvent` |
| `entityType` | string | `getEntityType()` | `org.bukkit.entity.EntityType` | `org.bukkit.event.entity.EntityEvent` |
| `location` | location summary | `getLocation()` | `org.bukkit.Location` | `org.bukkit.event.entity.ItemDespawnEvent` |

[[Data-Format-en|Wire format and limits]] · [[Event-org-bukkit-event-entity-itemdespawnevent|中文]]

If this event is not enabled, add its Java class or simple name to `events.include` in the Paper plugin configuration.
