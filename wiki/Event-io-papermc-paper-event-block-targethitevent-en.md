# TargetHitEvent

[[Home-en|Home]] / [[Category-block-en|block]]

- Java class: `io.papermc.paper.event.block.TargetHitEvent`
- Parent class: `org.bukkit.event.entity.ProjectileHitEvent`
- Python subscription: `TargetHitEvent`
- Python constant: `Events.TARGET_HIT`
- Cancellable: Yes
- Player available: Possible at runtime
- HandlerList owner: `io.papermc.paper.event.block.TargetHitEvent`
- [Official Paper Javadoc](https://jd.papermc.io/paper/1.16.5/io/papermc/paper/event/block/TargetHitEvent.html)

## Python example

```python
from paperpybridge import Events

@bridge.on(Events.TARGET_HIT)
def on_event(event):
    print(event.event, event.data)
```

## `data` fields

| Field | JSON type | Java getter | Java return type | Declared in |
| --- | --- | --- | --- | --- |
| `entity` | entity summary | `getEntity()` | `org.bukkit.entity.Projectile` | `org.bukkit.event.entity.ProjectileHitEvent` |
| `entityType` | string | `getEntityType()` | `org.bukkit.entity.EntityType` | `org.bukkit.event.entity.EntityEvent` |
| `hitBlock` | block summary | `getHitBlock()` | `org.bukkit.block.Block` | `org.bukkit.event.entity.ProjectileHitEvent` |
| `hitBlockFace` | string | `getHitBlockFace()` | `org.bukkit.block.BlockFace` | `org.bukkit.event.entity.ProjectileHitEvent` |
| `hitEntity` | entity summary | `getHitEntity()` | `org.bukkit.entity.Entity` | `org.bukkit.event.entity.ProjectileHitEvent` |
| `signalStrength` | number | `getSignalStrength()` | `int` | `io.papermc.paper.event.block.TargetHitEvent` |

[[Data-Format-en|Wire format and limits]] · [[Event-io-papermc-paper-event-block-targethitevent|中文]]

If this event is not enabled, add its Java class or simple name to `events.include` in the Paper plugin configuration.
