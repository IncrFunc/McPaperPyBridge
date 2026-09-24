# WorldBorderCenterChangeEvent

[[Home-en|Home]] / [[Category-world-en|world]]

- Java class: `io.papermc.paper.event.world.border.WorldBorderCenterChangeEvent`
- Parent class: `io.papermc.paper.event.world.border.WorldBorderEvent`
- Python subscription: `WorldBorderCenterChangeEvent`
- Python constant: `Events.WORLD_BORDER_CENTER_CHANGE`
- Cancellable: Yes
- Player available: No known player getter
- HandlerList owner: `io.papermc.paper.event.world.border.WorldBorderCenterChangeEvent`
- [Official Paper Javadoc](https://jd.papermc.io/paper/1.16.5/io/papermc/paper/event/world/border/WorldBorderCenterChangeEvent.html)

## Python example

```python
from paperpybridge import Events

@bridge.on(Events.WORLD_BORDER_CENTER_CHANGE)
def on_event(event):
    print(event.event, event.data)
```

## `data` fields

| Field | JSON type | Java getter | Java return type | Declared in |
| --- | --- | --- | --- | --- |
| `newCenter` | location summary | `getNewCenter()` | `org.bukkit.Location` | `io.papermc.paper.event.world.border.WorldBorderCenterChangeEvent` |
| `oldCenter` | location summary | `getOldCenter()` | `org.bukkit.Location` | `io.papermc.paper.event.world.border.WorldBorderCenterChangeEvent` |
| `world` | world summary | `getWorld()` | `org.bukkit.World` | `org.bukkit.event.world.WorldEvent` |

[[Data-Format-en|Wire format and limits]] · [[Event-io-papermc-paper-event-world-border-worldbordercenterchangeevent|中文]]

If this event is not enabled, add its Java class or simple name to `events.include` in the Paper plugin configuration.
