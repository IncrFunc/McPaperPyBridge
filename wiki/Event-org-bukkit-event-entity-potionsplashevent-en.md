# PotionSplashEvent

[[Home-en|Home]] / [[Category-entity-en|entity]]

- Java class: `org.bukkit.event.entity.PotionSplashEvent`
- Parent class: `org.bukkit.event.entity.ProjectileHitEvent`
- Python subscription: `PotionSplashEvent`
- Python constant: `Events.POTION_SPLASH`
- Cancellable: Yes
- Player available: Possible at runtime
- HandlerList owner: `org.bukkit.event.entity.PotionSplashEvent`
- [Official Paper Javadoc](https://jd.papermc.io/paper/1.16.5/org/bukkit/event/entity/PotionSplashEvent.html)

## Python example

```python
from paperpybridge import Events

@bridge.on(Events.POTION_SPLASH)
def on_event(event):
    print(event.event, event.data)
```

## `data` fields

| Field | JSON type | Java getter | Java return type | Declared in |
| --- | --- | --- | --- | --- |
| `entity` | entity summary | `getEntity()` | `org.bukkit.entity.Projectile` | `org.bukkit.event.entity.PotionSplashEvent` |
| `entityType` | string | `getEntityType()` | `org.bukkit.entity.EntityType` | `org.bukkit.event.entity.EntityEvent` |
| `hitBlock` | block summary | `getHitBlock()` | `org.bukkit.block.Block` | `org.bukkit.event.entity.ProjectileHitEvent` |
| `hitBlockFace` | string | `getHitBlockFace()` | `org.bukkit.block.BlockFace` | `org.bukkit.event.entity.ProjectileHitEvent` |
| `hitEntity` | entity summary | `getHitEntity()` | `org.bukkit.entity.Entity` | `org.bukkit.event.entity.ProjectileHitEvent` |
| `potion` | entity summary | `getPotion()` | `org.bukkit.entity.ThrownPotion` | `org.bukkit.event.entity.PotionSplashEvent` |

[[Data-Format-en|Wire format and limits]] · [[Event-org-bukkit-event-entity-potionsplashevent|中文]]

If this event is not enabled, add its Java class or simple name to `events.include` in the Paper plugin configuration.
