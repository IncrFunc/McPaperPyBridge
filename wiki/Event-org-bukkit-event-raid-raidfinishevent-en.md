# RaidFinishEvent

[[Home-en|Home]] / [[Category-raid-en|raid]]

- Java class: `org.bukkit.event.raid.RaidFinishEvent`
- Parent class: `org.bukkit.event.raid.RaidEvent`
- Python subscription: `RaidFinishEvent`
- Python constant: `Events.RAID_FINISH`
- Cancellable: No
- Player available: No known player getter
- HandlerList owner: `org.bukkit.event.raid.RaidFinishEvent`
- [Official Paper Javadoc](https://jd.papermc.io/paper/1.16.5/org/bukkit/event/raid/RaidFinishEvent.html)

## Python example

```python
from paperpybridge import Events

@bridge.on(Events.RAID_FINISH)
def on_event(event):
    print(event.event, event.data)
```

## `data` fields

| Field | JSON type | Java getter | Java return type | Declared in |
| --- | --- | --- | --- | --- |
| `world` | world summary | `getWorld()` | `org.bukkit.World` | `org.bukkit.event.world.WorldEvent` |

[[Data-Format-en|Wire format and limits]] · [[Event-org-bukkit-event-raid-raidfinishevent|中文]]

If this event is not enabled, add its Java class or simple name to `events.include` in the Paper plugin configuration.
