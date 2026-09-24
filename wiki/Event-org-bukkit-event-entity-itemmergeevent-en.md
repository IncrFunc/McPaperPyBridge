# ItemMergeEvent

[[Home-en|Home]] / [[Category-entity-en|entity]]

- Java class: `org.bukkit.event.entity.ItemMergeEvent`
- Parent class: `org.bukkit.event.entity.EntityEvent`
- Python subscription: `ItemMergeEvent`
- Python constant: `Events.ITEM_MERGE`
- Cancellable: Yes
- Player available: Possible at runtime
- HandlerList owner: `org.bukkit.event.entity.ItemMergeEvent`
- [Official Paper Javadoc](https://jd.papermc.io/paper/1.16.5/org/bukkit/event/entity/ItemMergeEvent.html)

## Python example

```python
from paperpybridge import Events

@bridge.on(Events.ITEM_MERGE)
def on_event(event):
    print(event.event, event.data)
```

## `data` fields

| Field | JSON type | Java getter | Java return type | Declared in |
| --- | --- | --- | --- | --- |
| `entity` | entity summary | `getEntity()` | `org.bukkit.entity.Entity` | `org.bukkit.event.entity.ItemMergeEvent` |
| `entityType` | string | `getEntityType()` | `org.bukkit.entity.EntityType` | `org.bukkit.event.entity.EntityEvent` |
| `target` | entity summary | `getTarget()` | `org.bukkit.entity.Item` | `org.bukkit.event.entity.ItemMergeEvent` |

[[Data-Format-en|Wire format and limits]] · [[Event-org-bukkit-event-entity-itemmergeevent|中文]]

If this event is not enabled, add its Java class or simple name to `events.include` in the Paper plugin configuration.
