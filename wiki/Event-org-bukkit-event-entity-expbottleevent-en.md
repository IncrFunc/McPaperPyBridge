# ExpBottleEvent

[[Home-en|Home]] / [[Category-entity-en|entity]]

- Java class: `org.bukkit.event.entity.ExpBottleEvent`
- Parent class: `org.bukkit.event.entity.ProjectileHitEvent`
- Python subscription: `ExpBottleEvent`
- Python constant: `Events.EXP_BOTTLE`
- Cancellable: Yes
- Player available: Possible at runtime
- HandlerList owner: `org.bukkit.event.entity.ExpBottleEvent`
- [Official Paper Javadoc](https://jd.papermc.io/paper/1.16.5/org/bukkit/event/entity/ExpBottleEvent.html)

## Python example

```python
from paperpybridge import Events

@bridge.on(Events.EXP_BOTTLE)
def on_event(event):
    print(event.event, event.data)
```

## `data` fields

| Field | JSON type | Java getter | Java return type | Declared in |
| --- | --- | --- | --- | --- |
| `entity` | entity summary | `getEntity()` | `org.bukkit.entity.Entity` | `org.bukkit.event.entity.ExpBottleEvent` |
| `entityType` | string | `getEntityType()` | `org.bukkit.entity.EntityType` | `org.bukkit.event.entity.EntityEvent` |
| `experience` | number | `getExperience()` | `int` | `org.bukkit.event.entity.ExpBottleEvent` |
| `hitBlock` | block summary | `getHitBlock()` | `org.bukkit.block.Block` | `org.bukkit.event.entity.ProjectileHitEvent` |
| `hitBlockFace` | string | `getHitBlockFace()` | `org.bukkit.block.BlockFace` | `org.bukkit.event.entity.ProjectileHitEvent` |
| `hitEntity` | entity summary | `getHitEntity()` | `org.bukkit.entity.Entity` | `org.bukkit.event.entity.ProjectileHitEvent` |
| `showEffect` | boolean | `getShowEffect()` | `boolean` | `org.bukkit.event.entity.ExpBottleEvent` |

[[Data-Format-en|Wire format and limits]] · [[Event-org-bukkit-event-entity-expbottleevent|中文]]

If this event is not enabled, add its Java class or simple name to `events.include` in the Paper plugin configuration.
