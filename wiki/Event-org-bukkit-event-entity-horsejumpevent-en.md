# HorseJumpEvent

[[Home-en|Home]] / [[Category-entity-en|entity]]

- Java class: `org.bukkit.event.entity.HorseJumpEvent`
- Parent class: `org.bukkit.event.entity.EntityEvent`
- Python subscription: `HorseJumpEvent`
- Python constant: `Events.HORSE_JUMP`
- Cancellable: Yes
- Player available: Possible at runtime
- HandlerList owner: `org.bukkit.event.entity.HorseJumpEvent`
- [Official Paper Javadoc](https://jd.papermc.io/paper/1.16.5/org/bukkit/event/entity/HorseJumpEvent.html)

## Python example

```python
from paperpybridge import Events

@bridge.on(Events.HORSE_JUMP)
def on_event(event):
    print(event.event, event.data)
```

## `data` fields

| Field | JSON type | Java getter | Java return type | Declared in |
| --- | --- | --- | --- | --- |
| `entity` | entity summary | `getEntity()` | `org.bukkit.entity.AbstractHorse` | `org.bukkit.event.entity.HorseJumpEvent` |
| `entityType` | string | `getEntityType()` | `org.bukkit.entity.EntityType` | `org.bukkit.event.entity.EntityEvent` |
| `power` | number | `getPower()` | `float` | `org.bukkit.event.entity.HorseJumpEvent` |

[[Data-Format-en|Wire format and limits]] · [[Event-org-bukkit-event-entity-horsejumpevent|中文]]

If this event is not enabled, add its Java class or simple name to `events.include` in the Paper plugin configuration.
