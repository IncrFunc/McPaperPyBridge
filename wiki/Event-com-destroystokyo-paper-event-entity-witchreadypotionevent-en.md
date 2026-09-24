# WitchReadyPotionEvent

[[Home-en|Home]] / [[Category-entity-en|entity]]

- Java class: `com.destroystokyo.paper.event.entity.WitchReadyPotionEvent`
- Parent class: `org.bukkit.event.entity.EntityEvent`
- Python subscription: `WitchReadyPotionEvent`
- Python constant: `Events.WITCH_READY_POTION`
- Cancellable: Yes
- Player available: Possible at runtime
- HandlerList owner: `com.destroystokyo.paper.event.entity.WitchReadyPotionEvent`
- [Official Paper Javadoc](https://jd.papermc.io/paper/1.16.5/com/destroystokyo/paper/event/entity/WitchReadyPotionEvent.html)

## Python example

```python
from paperpybridge import Events

@bridge.on(Events.WITCH_READY_POTION)
def on_event(event):
    print(event.event, event.data)
```

## `data` fields

| Field | JSON type | Java getter | Java return type | Declared in |
| --- | --- | --- | --- | --- |
| `entity` | entity summary | `getEntity()` | `org.bukkit.entity.Witch` | `com.destroystokyo.paper.event.entity.WitchReadyPotionEvent` |
| `entityType` | string | `getEntityType()` | `org.bukkit.entity.EntityType` | `org.bukkit.event.entity.EntityEvent` |
| `potion` | item summary | `getPotion()` | `org.bukkit.inventory.ItemStack` | `com.destroystokyo.paper.event.entity.WitchReadyPotionEvent` |

[[Data-Format-en|Wire format and limits]] · [[Event-com-destroystokyo-paper-event-entity-witchreadypotionevent|中文]]

If this event is not enabled, add its Java class or simple name to `events.include` in the Paper plugin configuration.
