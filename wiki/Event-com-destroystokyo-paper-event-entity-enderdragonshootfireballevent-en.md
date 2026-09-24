# EnderDragonShootFireballEvent

[[Home-en|Home]] / [[Category-entity-en|entity]]

- Java class: `com.destroystokyo.paper.event.entity.EnderDragonShootFireballEvent`
- Parent class: `org.bukkit.event.entity.EntityEvent`
- Python subscription: `EnderDragonShootFireballEvent`
- Python constant: `Events.ENDER_DRAGON_SHOOT_FIREBALL`
- Cancellable: Yes
- Player available: Possible at runtime
- HandlerList owner: `com.destroystokyo.paper.event.entity.EnderDragonShootFireballEvent`
- [Official Paper Javadoc](https://jd.papermc.io/paper/1.16.5/com/destroystokyo/paper/event/entity/EnderDragonShootFireballEvent.html)

## Python example

```python
from paperpybridge import Events

@bridge.on(Events.ENDER_DRAGON_SHOOT_FIREBALL)
def on_event(event):
    print(event.event, event.data)
```

## `data` fields

| Field | JSON type | Java getter | Java return type | Declared in |
| --- | --- | --- | --- | --- |
| `entity` | entity summary | `getEntity()` | `org.bukkit.entity.EnderDragon` | `com.destroystokyo.paper.event.entity.EnderDragonShootFireballEvent` |
| `entityType` | string | `getEntityType()` | `org.bukkit.entity.EntityType` | `org.bukkit.event.entity.EntityEvent` |
| `fireball` | entity summary | `getFireball()` | `org.bukkit.entity.DragonFireball` | `com.destroystokyo.paper.event.entity.EnderDragonShootFireballEvent` |

[[Data-Format-en|Wire format and limits]] · [[Event-com-destroystokyo-paper-event-entity-enderdragonshootfireballevent|中文]]

If this event is not enabled, add its Java class or simple name to `events.include` in the Paper plugin configuration.
