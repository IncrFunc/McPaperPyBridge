# ChunkLoadEvent

[[Home-en|Home]] / [[Category-world-en|world]]

- Java class: `org.bukkit.event.world.ChunkLoadEvent`
- Parent class: `org.bukkit.event.world.ChunkEvent`
- Python subscription: `ChunkLoadEvent`
- Python constant: `Events.CHUNK_LOAD`
- Cancellable: No
- Player available: No known player getter
- HandlerList owner: `org.bukkit.event.world.ChunkLoadEvent`
- [Official Paper Javadoc](https://jd.papermc.io/paper/1.16.5/org/bukkit/event/world/ChunkLoadEvent.html)

## Python example

```python
from paperpybridge import Events

@bridge.on(Events.CHUNK_LOAD)
def on_event(event):
    print(event.event, event.data)
```

## `data` fields

| Field | JSON type | Java getter | Java return type | Declared in |
| --- | --- | --- | --- | --- |
| `world` | world summary | `getWorld()` | `org.bukkit.World` | `org.bukkit.event.world.WorldEvent` |
| `newChunk` | boolean | `isNewChunk()` | `boolean` | `org.bukkit.event.world.ChunkLoadEvent` |

[[Data-Format-en|Wire format and limits]] · [[Event-org-bukkit-event-world-chunkloadevent|中文]]

If this event is not enabled, add its Java class or simple name to `events.include` in the Paper plugin configuration.
