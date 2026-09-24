# EntityDeathEvent

[[Home-en|Home]] / [[Category-entity-en|entity]]

- Java class: `org.bukkit.event.entity.EntityDeathEvent`
- Parent class: `org.bukkit.event.entity.EntityEvent`
- Python subscription: `EntityDeathEvent`
- Python constant: `Events.ENTITY_DEATH`
- Cancellable: Yes
- Player available: Possible at runtime
- HandlerList owner: `org.bukkit.event.entity.EntityDeathEvent`
- [Official Paper Javadoc](https://jd.papermc.io/paper/1.16.5/org/bukkit/event/entity/EntityDeathEvent.html)

## Python example

```python
from paperpybridge import Events

@bridge.on(Events.ENTITY_DEATH)
def on_event(event):
    print(event.event, event.data)
```

## `data` fields

| Field | JSON type | Java getter | Java return type | Declared in |
| --- | --- | --- | --- | --- |
| `deathSound` | string | `getDeathSound()` | `org.bukkit.Sound` | `org.bukkit.event.entity.EntityDeathEvent` |
| `deathSoundCategory` | string | `getDeathSoundCategory()` | `org.bukkit.SoundCategory` | `org.bukkit.event.entity.EntityDeathEvent` |
| `deathSoundPitch` | number | `getDeathSoundPitch()` | `float` | `org.bukkit.event.entity.EntityDeathEvent` |
| `deathSoundVolume` | number | `getDeathSoundVolume()` | `float` | `org.bukkit.event.entity.EntityDeathEvent` |
| `droppedExp` | number | `getDroppedExp()` | `int` | `org.bukkit.event.entity.EntityDeathEvent` |
| `entity` | entity summary | `getEntity()` | `org.bukkit.entity.LivingEntity` | `org.bukkit.event.entity.EntityDeathEvent` |
| `entityType` | string | `getEntityType()` | `org.bukkit.entity.EntityType` | `org.bukkit.event.entity.EntityEvent` |
| `reviveHealth` | number | `getReviveHealth()` | `double` | `org.bukkit.event.entity.EntityDeathEvent` |

[[Data-Format-en|Wire format and limits]] · [[Event-org-bukkit-event-entity-entitydeathevent|中文]]

If this event is not enabled, add its Java class or simple name to `events.include` in the Paper plugin configuration.
