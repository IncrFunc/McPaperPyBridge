# RaidStopEvent

[[Home-en|Home]] / [[Category-raid-en|raid]]

- Java class: `org.bukkit.event.raid.RaidStopEvent`
- Parent class: `org.bukkit.event.raid.RaidEvent`
- Python subscription: `RaidStopEvent`
- Python constant: `Events.RAID_STOP`
- Cancellable: No
- Player available: No known player getter
- HandlerList owner: `org.bukkit.event.raid.RaidStopEvent`
- [Official Paper Javadoc](https://jd.papermc.io/paper/1.16.5/org/bukkit/event/raid/RaidStopEvent.html)

## Python example

```python
from paperpybridge import Events

@bridge.on(Events.RAID_STOP)
def on_event(event):
    print(event.event, event.data)
```

## `data` fields

| Field | JSON type | Java getter | Java return type | Declared in |
| --- | --- | --- | --- | --- |
| `reason` | string | `getReason()` | `org.bukkit.event.raid.RaidStopEvent$Reason` | `org.bukkit.event.raid.RaidStopEvent` |
| `world` | world summary | `getWorld()` | `org.bukkit.World` | `org.bukkit.event.world.WorldEvent` |

[[Data-Format-en|Wire format and limits]] · [[Event-org-bukkit-event-raid-raidstopevent|中文]]

If this event is not enabled, add its Java class or simple name to `events.include` in the Paper plugin configuration.
