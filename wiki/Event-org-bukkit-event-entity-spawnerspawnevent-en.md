# SpawnerSpawnEvent

[[Home-en|Home]] / [[Category-entity-en|entity]]

- Java class: `org.bukkit.event.entity.SpawnerSpawnEvent`
- Parent class: `org.bukkit.event.entity.EntitySpawnEvent`
- Python subscription: `SpawnerSpawnEvent`
- Python constant: `Events.SPAWNER_SPAWN`
- Cancellable: Yes
- Player available: Possible at runtime
- HandlerList owner: `org.bukkit.event.entity.EntitySpawnEvent`
- [Official Paper Javadoc](https://jd.papermc.io/paper/1.16.5/org/bukkit/event/entity/SpawnerSpawnEvent.html)

## Python example

```python
from paperpybridge import Events

@bridge.on(Events.SPAWNER_SPAWN)
def on_event(event):
    print(event.event, event.data)
```

## `data` fields

| Field | JSON type | Java getter | Java return type | Declared in |
| --- | --- | --- | --- | --- |
| `entity` | entity summary | `getEntity()` | `org.bukkit.entity.Entity` | `org.bukkit.event.entity.EntityEvent` |
| `entityType` | string | `getEntityType()` | `org.bukkit.entity.EntityType` | `org.bukkit.event.entity.EntityEvent` |
| `location` | location summary | `getLocation()` | `org.bukkit.Location` | `org.bukkit.event.entity.EntitySpawnEvent` |

[[Data-Format-en|Wire format and limits]] · [[Event-org-bukkit-event-entity-spawnerspawnevent|中文]]

If this event is not enabled, add its Java class or simple name to `events.include` in the Paper plugin configuration.
