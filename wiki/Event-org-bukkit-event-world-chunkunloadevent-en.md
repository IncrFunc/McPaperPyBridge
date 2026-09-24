# ChunkUnloadEvent

[[Home-en|Home]] / [[Category-world-en|world]]

- Java class: `org.bukkit.event.world.ChunkUnloadEvent`
- Parent class: `org.bukkit.event.world.ChunkEvent`
- Python subscription: `ChunkUnloadEvent`
- Python constant: `Events.CHUNK_UNLOAD`
- Cancellable: No
- Player available: No known player getter
- HandlerList owner: `org.bukkit.event.world.ChunkUnloadEvent`
- [Official Paper Javadoc](https://jd.papermc.io/paper/1.16.5/org/bukkit/event/world/ChunkUnloadEvent.html)

## Python example

```python
from paperpybridge import Events

@bridge.on(Events.CHUNK_UNLOAD)
def on_event(event):
    print(event.event, event.data)
```

## `data` fields

| Field | JSON type | Java getter | Java return type | Declared in |
| --- | --- | --- | --- | --- |
| `world` | world summary | `getWorld()` | `org.bukkit.World` | `org.bukkit.event.world.WorldEvent` |
| `saveChunk` | boolean | `isSaveChunk()` | `boolean` | `org.bukkit.event.world.ChunkUnloadEvent` |

[[Data-Format-en|Wire format and limits]] · [[Event-org-bukkit-event-world-chunkunloadevent|中文]]

If this event is not enabled, add its Java class or simple name to `events.include` in the Paper plugin configuration.
