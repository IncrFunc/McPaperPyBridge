# ChunkPopulateEvent

[[Home-en|Home]] / [[Category-world-en|world]]

- Java class: `org.bukkit.event.world.ChunkPopulateEvent`
- Parent class: `org.bukkit.event.world.ChunkEvent`
- Python subscription: `ChunkPopulateEvent`
- Python constant: `Events.CHUNK_POPULATE`
- Cancellable: No
- Player available: No known player getter
- HandlerList owner: `org.bukkit.event.world.ChunkPopulateEvent`
- [Official Paper Javadoc](https://jd.papermc.io/paper/1.16.5/org/bukkit/event/world/ChunkPopulateEvent.html)

## Python example

```python
from paperpybridge import Events

@bridge.on(Events.CHUNK_POPULATE)
def on_event(event):
    print(event.event, event.data)
```

## `data` fields

| Field | JSON type | Java getter | Java return type | Declared in |
| --- | --- | --- | --- | --- |
| `world` | world summary | `getWorld()` | `org.bukkit.World` | `org.bukkit.event.world.WorldEvent` |

[[Data-Format-en|Wire format and limits]] · [[Event-org-bukkit-event-world-chunkpopulateevent|中文]]

If this event is not enabled, add its Java class or simple name to `events.include` in the Paper plugin configuration.
