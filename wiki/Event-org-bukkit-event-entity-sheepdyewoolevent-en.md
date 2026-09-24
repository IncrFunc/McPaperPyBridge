# SheepDyeWoolEvent

[[Home-en|Home]] / [[Category-entity-en|entity]]

- Java class: `org.bukkit.event.entity.SheepDyeWoolEvent`
- Parent class: `org.bukkit.event.entity.EntityEvent`
- Python subscription: `SheepDyeWoolEvent`
- Python constant: `Events.SHEEP_DYE_WOOL`
- Cancellable: Yes
- Player available: Possible at runtime
- HandlerList owner: `org.bukkit.event.entity.SheepDyeWoolEvent`
- [Official Paper Javadoc](https://jd.papermc.io/paper/1.16.5/org/bukkit/event/entity/SheepDyeWoolEvent.html)

## Python example

```python
from paperpybridge import Events

@bridge.on(Events.SHEEP_DYE_WOOL)
def on_event(event):
    print(event.event, event.data)
```

## `data` fields

| Field | JSON type | Java getter | Java return type | Declared in |
| --- | --- | --- | --- | --- |
| `color` | string | `getColor()` | `org.bukkit.DyeColor` | `org.bukkit.event.entity.SheepDyeWoolEvent` |
| `entity` | entity summary | `getEntity()` | `org.bukkit.entity.Entity` | `org.bukkit.event.entity.SheepDyeWoolEvent` |
| `entityType` | string | `getEntityType()` | `org.bukkit.entity.EntityType` | `org.bukkit.event.entity.EntityEvent` |

[[Data-Format-en|Wire format and limits]] · [[Event-org-bukkit-event-entity-sheepdyewoolevent|中文]]

If this event is not enabled, add its Java class or simple name to `events.include` in the Paper plugin configuration.
