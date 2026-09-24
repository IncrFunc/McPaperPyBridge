# InventoryCloseEvent

[[Home-en|Home]] / [[Category-inventory-en|inventory]]

- Java class: `org.bukkit.event.inventory.InventoryCloseEvent`
- Parent class: `org.bukkit.event.inventory.InventoryEvent`
- Python subscription: `InventoryCloseEvent`
- Python constant: `Events.INVENTORY_CLOSE`
- Cancellable: No
- Player available: Possible at runtime
- HandlerList owner: `org.bukkit.event.inventory.InventoryCloseEvent`
- [Official Paper Javadoc](https://jd.papermc.io/paper/1.16.5/org/bukkit/event/inventory/InventoryCloseEvent.html)

## Python example

```python
from paperpybridge import Events

@bridge.on(Events.INVENTORY_CLOSE)
def on_event(event):
    print(event.event, event.data)
```

## `data` fields

| Field | JSON type | Java getter | Java return type | Declared in |
| --- | --- | --- | --- | --- |
| `reason` | string | `getReason()` | `org.bukkit.event.inventory.InventoryCloseEvent$Reason` | `org.bukkit.event.inventory.InventoryCloseEvent` |

[[Data-Format-en|Wire format and limits]] · [[Event-org-bukkit-event-inventory-inventorycloseevent|中文]]

If this event is not enabled, add its Java class or simple name to `events.include` in the Paper plugin configuration.
