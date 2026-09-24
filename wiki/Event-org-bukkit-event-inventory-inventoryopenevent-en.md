# InventoryOpenEvent

[[Home-en|Home]] / [[Category-inventory-en|inventory]]

- Java class: `org.bukkit.event.inventory.InventoryOpenEvent`
- Parent class: `org.bukkit.event.inventory.InventoryEvent`
- Python subscription: `InventoryOpenEvent`
- Python constant: `Events.INVENTORY_OPEN`
- Cancellable: Yes
- Player available: Possible at runtime
- HandlerList owner: `org.bukkit.event.inventory.InventoryOpenEvent`
- [Official Paper Javadoc](https://jd.papermc.io/paper/1.16.5/org/bukkit/event/inventory/InventoryOpenEvent.html)

## Python example

```python
from paperpybridge import Events

@bridge.on(Events.INVENTORY_OPEN)
def on_event(event):
    print(event.event, event.data)
```

## `data` fields

No supported serializable fields; common event fields are still sent.

[[Data-Format-en|Wire format and limits]] · [[Event-org-bukkit-event-inventory-inventoryopenevent|中文]]

If this event is not enabled, add its Java class or simple name to `events.include` in the Paper plugin configuration.
