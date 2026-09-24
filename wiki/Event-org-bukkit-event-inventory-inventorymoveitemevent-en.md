# InventoryMoveItemEvent

[[Home-en|Home]] / [[Category-inventory-en|inventory]]

- Java class: `org.bukkit.event.inventory.InventoryMoveItemEvent`
- Parent class: `org.bukkit.event.Event`
- Python subscription: `InventoryMoveItemEvent`
- Python constant: `Events.INVENTORY_MOVE_ITEM`
- Cancellable: Yes
- Player available: No known player getter
- HandlerList owner: `org.bukkit.event.inventory.InventoryMoveItemEvent`
- [Official Paper Javadoc](https://jd.papermc.io/paper/1.16.5/org/bukkit/event/inventory/InventoryMoveItemEvent.html)

## Python example

```python
from paperpybridge import Events

@bridge.on(Events.INVENTORY_MOVE_ITEM)
def on_event(event):
    print(event.event, event.data)
```

## `data` fields

| Field | JSON type | Java getter | Java return type | Declared in |
| --- | --- | --- | --- | --- |
| `item` | item summary | `getItem()` | `org.bukkit.inventory.ItemStack` | `org.bukkit.event.inventory.InventoryMoveItemEvent` |

[[Data-Format-en|Wire format and limits]] · [[Event-org-bukkit-event-inventory-inventorymoveitemevent|中文]]

If this event is not enabled, add its Java class or simple name to `events.include` in the Paper plugin configuration.
