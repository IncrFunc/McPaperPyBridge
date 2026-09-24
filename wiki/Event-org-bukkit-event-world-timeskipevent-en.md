# TimeSkipEvent

[[Home-en|Home]] / [[Category-world-en|world]]

- Java class: `org.bukkit.event.world.TimeSkipEvent`
- Parent class: `org.bukkit.event.world.WorldEvent`
- Python subscription: `TimeSkipEvent`
- Python constant: `Events.TIME_SKIP`
- Cancellable: Yes
- Player available: No known player getter
- HandlerList owner: `org.bukkit.event.world.TimeSkipEvent`
- [Official Paper Javadoc](https://jd.papermc.io/paper/1.16.5/org/bukkit/event/world/TimeSkipEvent.html)

## Python example

```python
from paperpybridge import Events

@bridge.on(Events.TIME_SKIP)
def on_event(event):
    print(event.event, event.data)
```

## `data` fields

| Field | JSON type | Java getter | Java return type | Declared in |
| --- | --- | --- | --- | --- |
| `skipAmount` | number | `getSkipAmount()` | `long` | `org.bukkit.event.world.TimeSkipEvent` |
| `skipReason` | string | `getSkipReason()` | `org.bukkit.event.world.TimeSkipEvent$SkipReason` | `org.bukkit.event.world.TimeSkipEvent` |
| `world` | world summary | `getWorld()` | `org.bukkit.World` | `org.bukkit.event.world.WorldEvent` |

[[Data-Format-en|Wire format and limits]] · [[Event-org-bukkit-event-world-timeskipevent|中文]]

If this event is not enabled, add its Java class or simple name to `events.include` in the Paper plugin configuration.
