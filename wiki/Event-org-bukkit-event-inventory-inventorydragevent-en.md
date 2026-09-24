# InventoryDragEvent

[[Home-en|Home]] / [[Category-inventory-en|inventory]]

- Java class: `org.bukkit.event.inventory.InventoryDragEvent`
- Parent class: `org.bukkit.event.inventory.InventoryInteractEvent`
- Python subscription: `InventoryDragEvent`
- Python constant: `Events.INVENTORY_DRAG`
- Cancellable: Yes
- Player available: Possible at runtime
- HandlerList owner: `org.bukkit.event.inventory.InventoryDragEvent`
- [Official Paper Javadoc](https://jd.papermc.io/paper/1.16.5/org/bukkit/event/inventory/InventoryDragEvent.html)

## Python example

```python
from paperpybridge import Events

@bridge.on(Events.INVENTORY_DRAG)
def on_event(event):
    print(event.event, event.data)
```

## `data` fields

| Field | JSON type | Java getter | Java return type | Declared in |
| --- | --- | --- | --- | --- |
| `cursor` | item summary | `getCursor()` | `org.bukkit.inventory.ItemStack` | `org.bukkit.event.inventory.InventoryDragEvent` |
| `oldCursor` | item summary | `getOldCursor()` | `org.bukkit.inventory.ItemStack` | `org.bukkit.event.inventory.InventoryDragEvent` |
| `result` | string | `getResult()` | `org.bukkit.event.Event$Result` | `org.bukkit.event.inventory.InventoryInteractEvent` |
| `type` | string | `getType()` | `org.bukkit.event.inventory.DragType` | `org.bukkit.event.inventory.InventoryDragEvent` |
| `whoClicked` | entity summary | `getWhoClicked()` | `org.bukkit.entity.HumanEntity` | `org.bukkit.event.inventory.InventoryInteractEvent` |

[[Data-Format-en|Wire format and limits]] · [[Event-org-bukkit-event-inventory-inventorydragevent|中文]]

If this event is not enabled, add its Java class or simple name to `events.include` in the Paper plugin configuration.
