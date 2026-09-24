# CreatureSpawnEvent

[[Home-en|Home]] / [[Category-entity-en|entity]]

- Java class: `org.bukkit.event.entity.CreatureSpawnEvent`
- Parent class: `org.bukkit.event.entity.EntitySpawnEvent`
- Python subscription: `CreatureSpawnEvent`
- Python constant: `Events.CREATURE_SPAWN`
- Cancellable: Yes
- Player available: Possible at runtime
- HandlerList owner: `org.bukkit.event.entity.EntitySpawnEvent`
- [Official Paper Javadoc](https://jd.papermc.io/paper/1.16.5/org/bukkit/event/entity/CreatureSpawnEvent.html)

## Python example

```python
from paperpybridge import Events

@bridge.on(Events.CREATURE_SPAWN)
def on_event(event):
    print(event.event, event.data)
```

## `data` fields

| Field | JSON type | Java getter | Java return type | Declared in |
| --- | --- | --- | --- | --- |
| `entity` | entity summary | `getEntity()` | `org.bukkit.entity.LivingEntity` | `org.bukkit.event.entity.CreatureSpawnEvent` |
| `entityType` | string | `getEntityType()` | `org.bukkit.entity.EntityType` | `org.bukkit.event.entity.EntityEvent` |
| `location` | location summary | `getLocation()` | `org.bukkit.Location` | `org.bukkit.event.entity.EntitySpawnEvent` |
| `spawnReason` | string | `getSpawnReason()` | `org.bukkit.event.entity.CreatureSpawnEvent$SpawnReason` | `org.bukkit.event.entity.CreatureSpawnEvent` |

[[Data-Format-en|Wire format and limits]] · [[Event-org-bukkit-event-entity-creaturespawnevent|中文]]

If this event is not enabled, add its Java class or simple name to `events.include` in the Paper plugin configuration.
