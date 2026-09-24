# HangingPlaceEvent

[[Home-en|Home]] / [[Category-hanging-en|hanging]]

- Java class: `org.bukkit.event.hanging.HangingPlaceEvent`
- Parent class: `org.bukkit.event.hanging.HangingEvent`
- Python subscription: `HangingPlaceEvent`
- Python constant: `Events.HANGING_PLACE`
- Cancellable: Yes
- Player available: Possible at runtime
- HandlerList owner: `org.bukkit.event.hanging.HangingPlaceEvent`
- [Official Paper Javadoc](https://jd.papermc.io/paper/1.16.5/org/bukkit/event/hanging/HangingPlaceEvent.html)

## Python example

```python
from paperpybridge import Events

@bridge.on(Events.HANGING_PLACE)
def on_event(event):
    print(event.event, event.data)
```

## `data` fields

| Field | JSON type | Java getter | Java return type | Declared in |
| --- | --- | --- | --- | --- |
| `block` | block summary | `getBlock()` | `org.bukkit.block.Block` | `org.bukkit.event.hanging.HangingPlaceEvent` |
| `blockFace` | string | `getBlockFace()` | `org.bukkit.block.BlockFace` | `org.bukkit.event.hanging.HangingPlaceEvent` |
| `entity` | entity summary | `getEntity()` | `org.bukkit.entity.Hanging` | `org.bukkit.event.hanging.HangingEvent` |

[[Data-Format-en|Wire format and limits]] · [[Event-org-bukkit-event-hanging-hangingplaceevent|中文]]

If this event is not enabled, add its Java class or simple name to `events.include` in the Paper plugin configuration.
