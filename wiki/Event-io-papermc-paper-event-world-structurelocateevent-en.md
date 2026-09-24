# StructureLocateEvent

[[Home-en|Home]] / [[Category-world-en|world]]

- Java class: `io.papermc.paper.event.world.StructureLocateEvent`
- Parent class: `org.bukkit.event.world.WorldEvent`
- Python subscription: `StructureLocateEvent`
- Python constant: `Events.STRUCTURE_LOCATE`
- Cancellable: Yes
- Player available: No known player getter
- HandlerList owner: `io.papermc.paper.event.world.StructureLocateEvent`
- [Official Paper Javadoc](https://jd.papermc.io/paper/1.16.5/io/papermc/paper/event/world/StructureLocateEvent.html)

## Python example

```python
from paperpybridge import Events

@bridge.on(Events.STRUCTURE_LOCATE)
def on_event(event):
    print(event.event, event.data)
```

## `data` fields

| Field | JSON type | Java getter | Java return type | Declared in |
| --- | --- | --- | --- | --- |
| `origin` | location summary | `getOrigin()` | `org.bukkit.Location` | `io.papermc.paper.event.world.StructureLocateEvent` |
| `radius` | number | `getRadius()` | `int` | `io.papermc.paper.event.world.StructureLocateEvent` |
| `result` | location summary | `getResult()` | `org.bukkit.Location` | `io.papermc.paper.event.world.StructureLocateEvent` |
| `world` | world summary | `getWorld()` | `org.bukkit.World` | `org.bukkit.event.world.WorldEvent` |

[[Data-Format-en|Wire format and limits]] · [[Event-io-papermc-paper-event-world-structurelocateevent|中文]]

If this event is not enabled, add its Java class or simple name to `events.include` in the Paper plugin configuration.
