# PlayerDeathEvent

[[Home-en|Home]] / [[Category-entity-en|entity]]

- Java class: `org.bukkit.event.entity.PlayerDeathEvent`
- Parent class: `org.bukkit.event.entity.EntityDeathEvent`
- Python subscription: `PlayerDeathEvent`
- Python constant: `Events.PLAYER_DEATH`
- Cancellable: Yes
- Player available: Possible at runtime
- HandlerList owner: `org.bukkit.event.entity.EntityDeathEvent`
- [Official Paper Javadoc](https://jd.papermc.io/paper/1.16.5/org/bukkit/event/entity/PlayerDeathEvent.html)

## Python example

```python
from paperpybridge import Events

@bridge.on(Events.PLAYER_DEATH)
def on_event(event):
    print(event.event, event.data)
```

## `data` fields

| Field | JSON type | Java getter | Java return type | Declared in |
| --- | --- | --- | --- | --- |
| `deathMessage` | string | `getDeathMessage()` | `java.lang.String` | `org.bukkit.event.entity.PlayerDeathEvent` |
| `deathSound` | string | `getDeathSound()` | `org.bukkit.Sound` | `org.bukkit.event.entity.EntityDeathEvent` |
| `deathSoundCategory` | string | `getDeathSoundCategory()` | `org.bukkit.SoundCategory` | `org.bukkit.event.entity.EntityDeathEvent` |
| `deathSoundPitch` | number | `getDeathSoundPitch()` | `float` | `org.bukkit.event.entity.EntityDeathEvent` |
| `deathSoundVolume` | number | `getDeathSoundVolume()` | `float` | `org.bukkit.event.entity.EntityDeathEvent` |
| `droppedExp` | number | `getDroppedExp()` | `int` | `org.bukkit.event.entity.EntityDeathEvent` |
| `entity` | entity summary | `getEntity()` | `org.bukkit.entity.LivingEntity` | `org.bukkit.event.entity.PlayerDeathEvent` |
| `entityType` | string | `getEntityType()` | `org.bukkit.entity.EntityType` | `org.bukkit.event.entity.EntityEvent` |
| `keepInventory` | boolean | `getKeepInventory()` | `boolean` | `org.bukkit.event.entity.PlayerDeathEvent` |
| `keepLevel` | boolean | `getKeepLevel()` | `boolean` | `org.bukkit.event.entity.PlayerDeathEvent` |
| `newExp` | number | `getNewExp()` | `int` | `org.bukkit.event.entity.PlayerDeathEvent` |
| `newLevel` | number | `getNewLevel()` | `int` | `org.bukkit.event.entity.PlayerDeathEvent` |
| `newTotalExp` | number | `getNewTotalExp()` | `int` | `org.bukkit.event.entity.PlayerDeathEvent` |
| `reviveHealth` | number | `getReviveHealth()` | `double` | `org.bukkit.event.entity.EntityDeathEvent` |

[[Data-Format-en|Wire format and limits]] · [[Event-org-bukkit-event-entity-playerdeathevent|中文]]

If this event is not enabled, add its Java class or simple name to `events.include` in the Paper plugin configuration.
