# SpawnChangeEvent

[[Home-en|Home]] / [[Category-world-en|world]]

- Java class: `org.bukkit.event.world.SpawnChangeEvent`
- Parent class: `org.bukkit.event.world.WorldEvent`
- Python subscription: `SpawnChangeEvent`
- Python constant: `Events.SPAWN_CHANGE`
- Cancellable: No
- Player available: No known player getter
- HandlerList owner: `org.bukkit.event.world.SpawnChangeEvent`
- [Official Paper Javadoc](https://jd.papermc.io/paper/1.16.5/org/bukkit/event/world/SpawnChangeEvent.html)

## Python example

```python
from paperpybridge import Events

@bridge.on(Events.SPAWN_CHANGE)
def on_event(event):
    print(event.event, event.data)
```

## `data` fields

| Field | JSON type | Java getter | Java return type | Declared in |
| --- | --- | --- | --- | --- |
| `previousLocation` | location summary | `getPreviousLocation()` | `org.bukkit.Location` | `org.bukkit.event.world.SpawnChangeEvent` |
| `world` | world summary | `getWorld()` | `org.bukkit.World` | `org.bukkit.event.world.WorldEvent` |

[[Data-Format-en|Wire format and limits]] · [[Event-org-bukkit-event-world-spawnchangeevent|中文]]

If this event is not enabled, add its Java class or simple name to `events.include` in the Paper plugin configuration.
