# SlimeSplitEvent

[[Home-en|Home]] / [[Category-entity-en|entity]]

- Java class: `org.bukkit.event.entity.SlimeSplitEvent`
- Parent class: `org.bukkit.event.entity.EntityEvent`
- Python subscription: `SlimeSplitEvent`
- Python constant: `Events.SLIME_SPLIT`
- Cancellable: Yes
- Player available: Possible at runtime
- HandlerList owner: `org.bukkit.event.entity.SlimeSplitEvent`
- [Official Paper Javadoc](https://jd.papermc.io/paper/1.16.5/org/bukkit/event/entity/SlimeSplitEvent.html)

## Python example

```python
from paperpybridge import Events

@bridge.on(Events.SLIME_SPLIT)
def on_event(event):
    print(event.event, event.data)
```

## `data` fields

| Field | JSON type | Java getter | Java return type | Declared in |
| --- | --- | --- | --- | --- |
| `count` | number | `getCount()` | `int` | `org.bukkit.event.entity.SlimeSplitEvent` |
| `entity` | entity summary | `getEntity()` | `org.bukkit.entity.Entity` | `org.bukkit.event.entity.SlimeSplitEvent` |
| `entityType` | string | `getEntityType()` | `org.bukkit.entity.EntityType` | `org.bukkit.event.entity.EntityEvent` |

[[Data-Format-en|Wire format and limits]] · [[Event-org-bukkit-event-entity-slimesplitevent|中文]]

If this event is not enabled, add its Java class or simple name to `events.include` in the Paper plugin configuration.
