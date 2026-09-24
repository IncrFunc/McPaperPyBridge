# InventoryEvent

[[Home-en|Home]] / [[Category-inventory-en|inventory]]

- Java class: `org.bukkit.event.inventory.InventoryEvent`
- Parent class: `org.bukkit.event.Event`
- Python subscription: `InventoryEvent`
- Python constant: `Events.INVENTORY`
- Cancellable: No
- Player available: No known player getter
- HandlerList owner: `org.bukkit.event.inventory.InventoryEvent`
- [Official Paper Javadoc](https://jd.papermc.io/paper/1.16.5/org/bukkit/event/inventory/InventoryEvent.html)

## Python example

```python
from paperpybridge import Events

@bridge.on(Events.INVENTORY)
def on_event(event):
    print(event.event, event.data)
```

## `data` fields

No supported serializable fields; common event fields are still sent.

[[Data-Format-en|Wire format and limits]] · [[Event-org-bukkit-event-inventory-inventoryevent|中文]]

If this event is not enabled, add its Java class or simple name to `events.include` in the Paper plugin configuration.
