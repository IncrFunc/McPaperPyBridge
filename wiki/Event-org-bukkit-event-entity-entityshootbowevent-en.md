# EntityShootBowEvent

[[Home-en|Home]] / [[Category-entity-en|entity]]

- Java class: `org.bukkit.event.entity.EntityShootBowEvent`
- Parent class: `org.bukkit.event.entity.EntityEvent`
- Python subscription: `EntityShootBowEvent`
- Python constant: `Events.ENTITY_SHOOT_BOW`
- Cancellable: Yes
- Player available: Possible at runtime
- HandlerList owner: `org.bukkit.event.entity.EntityShootBowEvent`
- [Official Paper Javadoc](https://jd.papermc.io/paper/1.16.5/org/bukkit/event/entity/EntityShootBowEvent.html)

## Python example

```python
from paperpybridge import Events

@bridge.on(Events.ENTITY_SHOOT_BOW)
def on_event(event):
    print(event.event, event.data)
```

## `data` fields

| Field | JSON type | Java getter | Java return type | Declared in |
| --- | --- | --- | --- | --- |
| `arrowItem` | item summary | `getArrowItem()` | `org.bukkit.inventory.ItemStack` | `org.bukkit.event.entity.EntityShootBowEvent` |
| `bow` | item summary | `getBow()` | `org.bukkit.inventory.ItemStack` | `org.bukkit.event.entity.EntityShootBowEvent` |
| `consumable` | item summary | `getConsumable()` | `org.bukkit.inventory.ItemStack` | `org.bukkit.event.entity.EntityShootBowEvent` |
| `consumeArrow` | boolean | `getConsumeArrow()` | `boolean` | `org.bukkit.event.entity.EntityShootBowEvent` |
| `entity` | entity summary | `getEntity()` | `org.bukkit.entity.Entity` | `org.bukkit.event.entity.EntityShootBowEvent` |
| `entityType` | string | `getEntityType()` | `org.bukkit.entity.EntityType` | `org.bukkit.event.entity.EntityEvent` |
| `force` | number | `getForce()` | `float` | `org.bukkit.event.entity.EntityShootBowEvent` |
| `hand` | string | `getHand()` | `org.bukkit.inventory.EquipmentSlot` | `org.bukkit.event.entity.EntityShootBowEvent` |
| `projectile` | entity summary | `getProjectile()` | `org.bukkit.entity.Entity` | `org.bukkit.event.entity.EntityShootBowEvent` |

[[Data-Format-en|Wire format and limits]] · [[Event-org-bukkit-event-entity-entityshootbowevent|中文]]

If this event is not enabled, add its Java class or simple name to `events.include` in the Paper plugin configuration.
