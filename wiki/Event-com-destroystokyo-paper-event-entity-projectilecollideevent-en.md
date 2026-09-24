# ProjectileCollideEvent

[[Home-en|Home]] / [[Category-entity-en|entity]]

- Java class: `com.destroystokyo.paper.event.entity.ProjectileCollideEvent`
- Parent class: `org.bukkit.event.entity.EntityEvent`
- Python subscription: `ProjectileCollideEvent`
- Python constant: `Events.PROJECTILE_COLLIDE`
- Cancellable: Yes
- Player available: Possible at runtime
- HandlerList owner: `com.destroystokyo.paper.event.entity.ProjectileCollideEvent`
- [Official Paper Javadoc](https://jd.papermc.io/paper/1.16.5/com/destroystokyo/paper/event/entity/ProjectileCollideEvent.html)

## Python example

```python
from paperpybridge import Events

@bridge.on(Events.PROJECTILE_COLLIDE)
def on_event(event):
    print(event.event, event.data)
```

## `data` fields

| Field | JSON type | Java getter | Java return type | Declared in |
| --- | --- | --- | --- | --- |
| `collidedWith` | entity summary | `getCollidedWith()` | `org.bukkit.entity.Entity` | `com.destroystokyo.paper.event.entity.ProjectileCollideEvent` |
| `entity` | entity summary | `getEntity()` | `org.bukkit.entity.Projectile` | `com.destroystokyo.paper.event.entity.ProjectileCollideEvent` |
| `entityType` | string | `getEntityType()` | `org.bukkit.entity.EntityType` | `org.bukkit.event.entity.EntityEvent` |

[[Data-Format-en|Wire format and limits]] · [[Event-com-destroystokyo-paper-event-entity-projectilecollideevent|中文]]

If this event is not enabled, add its Java class or simple name to `events.include` in the Paper plugin configuration.
