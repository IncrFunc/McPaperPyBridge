# PlayerChunkUnloadEvent

[[Home-en|Home]] / [[Category-packet-en|packet]]

- Java class: `io.papermc.paper.event.packet.PlayerChunkUnloadEvent`
- Parent class: `org.bukkit.event.world.ChunkEvent`
- Python subscription: `PlayerChunkUnloadEvent`
- Python constant: `Events.PLAYER_CHUNK_UNLOAD`
- Cancellable: No
- Player available: Possible at runtime
- HandlerList owner: `io.papermc.paper.event.packet.PlayerChunkUnloadEvent`
- [Official Paper Javadoc](https://jd.papermc.io/paper/1.16.5/io/papermc/paper/event/packet/PlayerChunkUnloadEvent.html)

## Python example

```python
from paperpybridge import Events

@bridge.on(Events.PLAYER_CHUNK_UNLOAD)
def on_event(event):
    print(event.event, event.data)
```

## `data` fields

| Field | JSON type | Java getter | Java return type | Declared in |
| --- | --- | --- | --- | --- |
| `world` | world summary | `getWorld()` | `org.bukkit.World` | `org.bukkit.event.world.WorldEvent` |

[[Data-Format-en|Wire format and limits]] · [[Event-io-papermc-paper-event-packet-playerchunkunloadevent|中文]]

If this event is not enabled, add its Java class or simple name to `events.include` in the Paper plugin configuration.
