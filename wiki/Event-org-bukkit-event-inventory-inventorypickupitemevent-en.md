# InventoryPickupItemEvent

[[Home-en|Home]] / [[Category-inventory-en|inventory]]

- Java class: `org.bukkit.event.inventory.InventoryPickupItemEvent`
- Parent class: `org.bukkit.event.Event`
- Python subscription: `InventoryPickupItemEvent`
- Python constant: `Events.INVENTORY_PICKUP_ITEM`
- Cancellable: Yes
- Player available: No known player getter
- HandlerList owner: `org.bukkit.event.inventory.InventoryPickupItemEvent`
- [Official Paper Javadoc](https://jd.papermc.io/paper/1.16.5/org/bukkit/event/inventory/InventoryPickupItemEvent.html)

## Python example

```python
from paperpybridge import Events

@bridge.on(Events.INVENTORY_PICKUP_ITEM)
def on_event(event):
    print(event.event, event.data)
```

## `data` fields

| Field | JSON type | Java getter | Java return type | Declared in |
| --- | --- | --- | --- | --- |
| `item` | entity summary | `getItem()` | `org.bukkit.entity.Item` | `org.bukkit.event.inventory.InventoryPickupItemEvent` |

[[Data-Format-en|Wire format and limits]] · [[Event-org-bukkit-event-inventory-inventorypickupitemevent|中文]]

If this event is not enabled, add its Java class or simple name to `events.include` in the Paper plugin configuration.
