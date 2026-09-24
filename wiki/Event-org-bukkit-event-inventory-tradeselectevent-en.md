# TradeSelectEvent

[[Home-en|Home]] / [[Category-inventory-en|inventory]]

- Java class: `org.bukkit.event.inventory.TradeSelectEvent`
- Parent class: `org.bukkit.event.inventory.InventoryInteractEvent`
- Python subscription: `TradeSelectEvent`
- Python constant: `Events.TRADE_SELECT`
- Cancellable: Yes
- Player available: Possible at runtime
- HandlerList owner: `org.bukkit.event.inventory.TradeSelectEvent`
- [Official Paper Javadoc](https://jd.papermc.io/paper/1.16.5/org/bukkit/event/inventory/TradeSelectEvent.html)

## Python example

```python
from paperpybridge import Events

@bridge.on(Events.TRADE_SELECT)
def on_event(event):
    print(event.event, event.data)
```

## `data` fields

| Field | JSON type | Java getter | Java return type | Declared in |
| --- | --- | --- | --- | --- |
| `index` | number | `getIndex()` | `int` | `org.bukkit.event.inventory.TradeSelectEvent` |
| `result` | string | `getResult()` | `org.bukkit.event.Event$Result` | `org.bukkit.event.inventory.InventoryInteractEvent` |
| `whoClicked` | entity summary | `getWhoClicked()` | `org.bukkit.entity.HumanEntity` | `org.bukkit.event.inventory.InventoryInteractEvent` |

[[Data-Format-en|Wire format and limits]] · [[Event-org-bukkit-event-inventory-tradeselectevent|中文]]

If this event is not enabled, add its Java class or simple name to `events.include` in the Paper plugin configuration.
