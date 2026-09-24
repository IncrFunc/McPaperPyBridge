# PufferFishStateChangeEvent

[[Home-en|Home]] / [[Category-entity-en|entity]]

- Java class: `io.papermc.paper.event.entity.PufferFishStateChangeEvent`
- Parent class: `org.bukkit.event.entity.EntityEvent`
- Python subscription: `PufferFishStateChangeEvent`
- Python constant: `Events.PUFFER_FISH_STATE_CHANGE`
- Cancellable: Yes
- Player available: Possible at runtime
- HandlerList owner: `io.papermc.paper.event.entity.PufferFishStateChangeEvent`
- [Official Paper Javadoc](https://jd.papermc.io/paper/1.16.5/io/papermc/paper/event/entity/PufferFishStateChangeEvent.html)

## Python example

```python
from paperpybridge import Events

@bridge.on(Events.PUFFER_FISH_STATE_CHANGE)
def on_event(event):
    print(event.event, event.data)
```

## `data` fields

| Field | JSON type | Java getter | Java return type | Declared in |
| --- | --- | --- | --- | --- |
| `entity` | entity summary | `getEntity()` | `org.bukkit.entity.PufferFish` | `io.papermc.paper.event.entity.PufferFishStateChangeEvent` |
| `entityType` | string | `getEntityType()` | `org.bukkit.entity.EntityType` | `org.bukkit.event.entity.EntityEvent` |
| `newPuffState` | number | `getNewPuffState()` | `int` | `io.papermc.paper.event.entity.PufferFishStateChangeEvent` |
| `deflating` | boolean | `isDeflating()` | `boolean` | `io.papermc.paper.event.entity.PufferFishStateChangeEvent` |
| `inflating` | boolean | `isInflating()` | `boolean` | `io.papermc.paper.event.entity.PufferFishStateChangeEvent` |

[[Data-Format-en|Wire format and limits]] · [[Event-io-papermc-paper-event-entity-pufferfishstatechangeevent|中文]]

If this event is not enabled, add its Java class or simple name to `events.include` in the Paper plugin configuration.
