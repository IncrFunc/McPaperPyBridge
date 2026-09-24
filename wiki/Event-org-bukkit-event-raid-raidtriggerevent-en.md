# RaidTriggerEvent

[[Home-en|Home]] / [[Category-raid-en|raid]]

- Java class: `org.bukkit.event.raid.RaidTriggerEvent`
- Parent class: `org.bukkit.event.raid.RaidEvent`
- Python subscription: `RaidTriggerEvent`
- Python constant: `Events.RAID_TRIGGER`
- Cancellable: Yes
- Player available: Possible at runtime
- HandlerList owner: `org.bukkit.event.raid.RaidTriggerEvent`
- [Official Paper Javadoc](https://jd.papermc.io/paper/1.16.5/org/bukkit/event/raid/RaidTriggerEvent.html)

## Python example

```python
from paperpybridge import Events

@bridge.on(Events.RAID_TRIGGER)
def on_event(event):
    print(event.event, event.data)
```

## `data` fields

| Field | JSON type | Java getter | Java return type | Declared in |
| --- | --- | --- | --- | --- |
| `world` | world summary | `getWorld()` | `org.bukkit.World` | `org.bukkit.event.world.WorldEvent` |

[[Data-Format-en|Wire format and limits]] · [[Event-org-bukkit-event-raid-raidtriggerevent|中文]]

If this event is not enabled, add its Java class or simple name to `events.include` in the Paper plugin configuration.
