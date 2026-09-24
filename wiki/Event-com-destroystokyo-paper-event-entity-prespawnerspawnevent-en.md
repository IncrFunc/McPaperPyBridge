# PreSpawnerSpawnEvent

[[Home-en|Home]] / [[Category-entity-en|entity]]

- Java class: `com.destroystokyo.paper.event.entity.PreSpawnerSpawnEvent`
- Parent class: `com.destroystokyo.paper.event.entity.PreCreatureSpawnEvent`
- Python subscription: `PreSpawnerSpawnEvent`
- Python constant: `Events.PRE_SPAWNER_SPAWN`
- Cancellable: Yes
- Player available: No known player getter
- HandlerList owner: `com.destroystokyo.paper.event.entity.PreCreatureSpawnEvent`
- [Official Paper Javadoc](https://jd.papermc.io/paper/1.16.5/com/destroystokyo/paper/event/entity/PreSpawnerSpawnEvent.html)

## Python example

```python
from paperpybridge import Events

@bridge.on(Events.PRE_SPAWNER_SPAWN)
def on_event(event):
    print(event.event, event.data)
```

## `data` fields

| Field | JSON type | Java getter | Java return type | Declared in |
| --- | --- | --- | --- | --- |
| `reason` | string | `getReason()` | `org.bukkit.event.entity.CreatureSpawnEvent$SpawnReason` | `com.destroystokyo.paper.event.entity.PreCreatureSpawnEvent` |
| `spawnLocation` | location summary | `getSpawnLocation()` | `org.bukkit.Location` | `com.destroystokyo.paper.event.entity.PreCreatureSpawnEvent` |
| `spawnerLocation` | location summary | `getSpawnerLocation()` | `org.bukkit.Location` | `com.destroystokyo.paper.event.entity.PreSpawnerSpawnEvent` |
| `type` | string | `getType()` | `org.bukkit.entity.EntityType` | `com.destroystokyo.paper.event.entity.PreCreatureSpawnEvent` |

[[Data-Format-en|Wire format and limits]] · [[Event-com-destroystokyo-paper-event-entity-prespawnerspawnevent|中文]]

If this event is not enabled, add its Java class or simple name to `events.include` in the Paper plugin configuration.
