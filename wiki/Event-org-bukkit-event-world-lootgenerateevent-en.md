# LootGenerateEvent

[[Home-en|Home]] / [[Category-world-en|world]]

- Java class: `org.bukkit.event.world.LootGenerateEvent`
- Parent class: `org.bukkit.event.world.WorldEvent`
- Python subscription: `LootGenerateEvent`
- Python constant: `Events.LOOT_GENERATE`
- Cancellable: Yes
- Player available: Possible at runtime
- HandlerList owner: `org.bukkit.event.world.LootGenerateEvent`
- [Official Paper Javadoc](https://jd.papermc.io/paper/1.16.5/org/bukkit/event/world/LootGenerateEvent.html)

## Python example

```python
from paperpybridge import Events

@bridge.on(Events.LOOT_GENERATE)
def on_event(event):
    print(event.event, event.data)
```

## `data` fields

| Field | JSON type | Java getter | Java return type | Declared in |
| --- | --- | --- | --- | --- |
| `entity` | entity summary | `getEntity()` | `org.bukkit.entity.Entity` | `org.bukkit.event.world.LootGenerateEvent` |
| `world` | world summary | `getWorld()` | `org.bukkit.World` | `org.bukkit.event.world.WorldEvent` |
| `plugin` | boolean | `isPlugin()` | `boolean` | `org.bukkit.event.world.LootGenerateEvent` |

[[Data-Format-en|Wire format and limits]] · [[Event-org-bukkit-event-world-lootgenerateevent|中文]]

If this event is not enabled, add its Java class or simple name to `events.include` in the Paper plugin configuration.
