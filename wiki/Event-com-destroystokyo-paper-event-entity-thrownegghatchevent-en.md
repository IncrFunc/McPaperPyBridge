# ThrownEggHatchEvent

[[Home-en|Home]] / [[Category-entity-en|entity]]

- Java class: `com.destroystokyo.paper.event.entity.ThrownEggHatchEvent`
- Parent class: `org.bukkit.event.Event`
- Python subscription: `ThrownEggHatchEvent`
- Python constant: `Events.THROWN_EGG_HATCH`
- Cancellable: No
- Player available: No known player getter
- HandlerList owner: `com.destroystokyo.paper.event.entity.ThrownEggHatchEvent`
- [Official Paper Javadoc](https://jd.papermc.io/paper/1.16.5/com/destroystokyo/paper/event/entity/ThrownEggHatchEvent.html)

## Python example

```python
from paperpybridge import Events

@bridge.on(Events.THROWN_EGG_HATCH)
def on_event(event):
    print(event.event, event.data)
```

## `data` fields

| Field | JSON type | Java getter | Java return type | Declared in |
| --- | --- | --- | --- | --- |
| `egg` | entity summary | `getEgg()` | `org.bukkit.entity.Egg` | `com.destroystokyo.paper.event.entity.ThrownEggHatchEvent` |
| `hatchingType` | string | `getHatchingType()` | `org.bukkit.entity.EntityType` | `com.destroystokyo.paper.event.entity.ThrownEggHatchEvent` |
| `numHatches` | number | `getNumHatches()` | `byte` | `com.destroystokyo.paper.event.entity.ThrownEggHatchEvent` |
| `hatching` | boolean | `isHatching()` | `boolean` | `com.destroystokyo.paper.event.entity.ThrownEggHatchEvent` |

[[Data-Format-en|Wire format and limits]] · [[Event-com-destroystokyo-paper-event-entity-thrownegghatchevent|中文]]

If this event is not enabled, add its Java class or simple name to `events.include` in the Paper plugin configuration.
