# EntityLoadCrossbowEvent

[[Home-en|Home]] / [[Category-entity-en|entity]]

- Java class: `io.papermc.paper.event.entity.EntityLoadCrossbowEvent`
- Parent class: `org.bukkit.event.entity.EntityEvent`
- Python subscription: `EntityLoadCrossbowEvent`
- Python constant: `Events.ENTITY_LOAD_CROSSBOW`
- Cancellable: Yes
- Player available: Possible at runtime
- HandlerList owner: `io.papermc.paper.event.entity.EntityLoadCrossbowEvent`
- [Official Paper Javadoc](https://jd.papermc.io/paper/1.16.5/io/papermc/paper/event/entity/EntityLoadCrossbowEvent.html)

## Python example

```python
from paperpybridge import Events

@bridge.on(Events.ENTITY_LOAD_CROSSBOW)
def on_event(event):
    print(event.event, event.data)
```

## `data` fields

| Field | JSON type | Java getter | Java return type | Declared in |
| --- | --- | --- | --- | --- |
| `crossbow` | item summary | `getCrossbow()` | `org.bukkit.inventory.ItemStack` | `io.papermc.paper.event.entity.EntityLoadCrossbowEvent` |
| `entity` | entity summary | `getEntity()` | `org.bukkit.entity.Entity` | `io.papermc.paper.event.entity.EntityLoadCrossbowEvent` |
| `entityType` | string | `getEntityType()` | `org.bukkit.entity.EntityType` | `org.bukkit.event.entity.EntityEvent` |
| `hand` | string | `getHand()` | `org.bukkit.inventory.EquipmentSlot` | `io.papermc.paper.event.entity.EntityLoadCrossbowEvent` |

[[Data-Format-en|Wire format and limits]] · [[Event-io-papermc-paper-event-entity-entityloadcrossbowevent|中文]]

If this event is not enabled, add its Java class or simple name to `events.include` in the Paper plugin configuration.
