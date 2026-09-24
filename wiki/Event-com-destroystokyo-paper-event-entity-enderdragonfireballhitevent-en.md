# EnderDragonFireballHitEvent

[[Home-en|Home]] / [[Category-entity-en|entity]]

- Java class: `com.destroystokyo.paper.event.entity.EnderDragonFireballHitEvent`
- Parent class: `org.bukkit.event.entity.EntityEvent`
- Python subscription: `EnderDragonFireballHitEvent`
- Python constant: `Events.ENDER_DRAGON_FIREBALL_HIT`
- Cancellable: Yes
- Player available: Possible at runtime
- HandlerList owner: `com.destroystokyo.paper.event.entity.EnderDragonFireballHitEvent`
- [Official Paper Javadoc](https://jd.papermc.io/paper/1.16.5/com/destroystokyo/paper/event/entity/EnderDragonFireballHitEvent.html)

## Python example

```python
from paperpybridge import Events

@bridge.on(Events.ENDER_DRAGON_FIREBALL_HIT)
def on_event(event):
    print(event.event, event.data)
```

## `data` fields

| Field | JSON type | Java getter | Java return type | Declared in |
| --- | --- | --- | --- | --- |
| `areaEffectCloud` | entity summary | `getAreaEffectCloud()` | `org.bukkit.entity.AreaEffectCloud` | `com.destroystokyo.paper.event.entity.EnderDragonFireballHitEvent` |
| `entity` | entity summary | `getEntity()` | `org.bukkit.entity.DragonFireball` | `com.destroystokyo.paper.event.entity.EnderDragonFireballHitEvent` |
| `entityType` | string | `getEntityType()` | `org.bukkit.entity.EntityType` | `org.bukkit.event.entity.EntityEvent` |

[[Data-Format-en|Wire format and limits]] · [[Event-com-destroystokyo-paper-event-entity-enderdragonfireballhitevent|中文]]

If this event is not enabled, add its Java class or simple name to `events.include` in the Paper plugin configuration.
