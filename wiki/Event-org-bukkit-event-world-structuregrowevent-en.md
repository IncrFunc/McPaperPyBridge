# StructureGrowEvent

[[Home-en|Home]] / [[Category-world-en|world]]

- Java class: `org.bukkit.event.world.StructureGrowEvent`
- Parent class: `org.bukkit.event.world.WorldEvent`
- Python subscription: `StructureGrowEvent`
- Python constant: `Events.STRUCTURE_GROW`
- Cancellable: Yes
- Player available: Possible at runtime
- HandlerList owner: `org.bukkit.event.world.StructureGrowEvent`
- [Official Paper Javadoc](https://jd.papermc.io/paper/1.16.5/org/bukkit/event/world/StructureGrowEvent.html)

## Python example

```python
from paperpybridge import Events

@bridge.on(Events.STRUCTURE_GROW)
def on_event(event):
    print(event.event, event.data)
```

## `data` fields

| Field | JSON type | Java getter | Java return type | Declared in |
| --- | --- | --- | --- | --- |
| `location` | location summary | `getLocation()` | `org.bukkit.Location` | `org.bukkit.event.world.StructureGrowEvent` |
| `species` | string | `getSpecies()` | `org.bukkit.TreeType` | `org.bukkit.event.world.StructureGrowEvent` |
| `world` | world summary | `getWorld()` | `org.bukkit.World` | `org.bukkit.event.world.WorldEvent` |
| `fromBonemeal` | boolean | `isFromBonemeal()` | `boolean` | `org.bukkit.event.world.StructureGrowEvent` |

[[Data-Format-en|Wire format and limits]] · [[Event-org-bukkit-event-world-structuregrowevent|中文]]

If this event is not enabled, add its Java class or simple name to `events.include` in the Paper plugin configuration.
