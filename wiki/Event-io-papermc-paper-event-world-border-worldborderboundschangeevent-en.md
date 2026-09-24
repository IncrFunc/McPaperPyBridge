# WorldBorderBoundsChangeEvent

[[Home-en|Home]] / [[Category-world-en|world]]

- Java class: `io.papermc.paper.event.world.border.WorldBorderBoundsChangeEvent`
- Parent class: `io.papermc.paper.event.world.border.WorldBorderEvent`
- Python subscription: `WorldBorderBoundsChangeEvent`
- Python constant: `Events.WORLD_BORDER_BOUNDS_CHANGE`
- Cancellable: Yes
- Player available: No known player getter
- HandlerList owner: `io.papermc.paper.event.world.border.WorldBorderBoundsChangeEvent`
- [Official Paper Javadoc](https://jd.papermc.io/paper/1.16.5/io/papermc/paper/event/world/border/WorldBorderBoundsChangeEvent.html)

## Python example

```python
from paperpybridge import Events

@bridge.on(Events.WORLD_BORDER_BOUNDS_CHANGE)
def on_event(event):
    print(event.event, event.data)
```

## `data` fields

| Field | JSON type | Java getter | Java return type | Declared in |
| --- | --- | --- | --- | --- |
| `duration` | number | `getDuration()` | `long` | `io.papermc.paper.event.world.border.WorldBorderBoundsChangeEvent` |
| `newSize` | number | `getNewSize()` | `double` | `io.papermc.paper.event.world.border.WorldBorderBoundsChangeEvent` |
| `oldSize` | number | `getOldSize()` | `double` | `io.papermc.paper.event.world.border.WorldBorderBoundsChangeEvent` |
| `type` | string | `getType()` | `io.papermc.paper.event.world.border.WorldBorderBoundsChangeEvent$Type` | `io.papermc.paper.event.world.border.WorldBorderBoundsChangeEvent` |
| `world` | world summary | `getWorld()` | `org.bukkit.World` | `org.bukkit.event.world.WorldEvent` |

[[Data-Format-en|Wire format and limits]] · [[Event-io-papermc-paper-event-world-border-worldborderboundschangeevent|中文]]

If this event is not enabled, add its Java class or simple name to `events.include` in the Paper plugin configuration.
