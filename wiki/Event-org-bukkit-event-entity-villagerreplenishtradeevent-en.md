# VillagerReplenishTradeEvent

[[Home-en|Home]] / [[Category-entity-en|entity]]

- Java class: `org.bukkit.event.entity.VillagerReplenishTradeEvent`
- Parent class: `org.bukkit.event.entity.EntityEvent`
- Python subscription: `VillagerReplenishTradeEvent`
- Python constant: `Events.VILLAGER_REPLENISH_TRADE`
- Cancellable: Yes
- Player available: Possible at runtime
- HandlerList owner: `org.bukkit.event.entity.VillagerReplenishTradeEvent`
- [Official Paper Javadoc](https://jd.papermc.io/paper/1.16.5/org/bukkit/event/entity/VillagerReplenishTradeEvent.html)

## Python example

```python
from paperpybridge import Events

@bridge.on(Events.VILLAGER_REPLENISH_TRADE)
def on_event(event):
    print(event.event, event.data)
```

## `data` fields

| Field | JSON type | Java getter | Java return type | Declared in |
| --- | --- | --- | --- | --- |
| `bonus` | number | `getBonus()` | `int` | `org.bukkit.event.entity.VillagerReplenishTradeEvent` |
| `entity` | entity summary | `getEntity()` | `org.bukkit.entity.Entity` | `org.bukkit.event.entity.VillagerReplenishTradeEvent` |
| `entityType` | string | `getEntityType()` | `org.bukkit.entity.EntityType` | `org.bukkit.event.entity.EntityEvent` |

[[Data-Format-en|Wire format and limits]] · [[Event-org-bukkit-event-entity-villagerreplenishtradeevent|中文]]

If this event is not enabled, add its Java class or simple name to `events.include` in the Paper plugin configuration.
