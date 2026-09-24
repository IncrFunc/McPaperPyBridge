# PrepareItemCraftEvent

[[Home-en|Home]] / [[Category-inventory-en|inventory]]

- Java class: `org.bukkit.event.inventory.PrepareItemCraftEvent`
- Parent class: `org.bukkit.event.inventory.InventoryEvent`
- Python subscription: `PrepareItemCraftEvent`
- Python constant: `Events.PREPARE_ITEM_CRAFT`
- Cancellable: No
- Player available: No known player getter
- HandlerList owner: `org.bukkit.event.inventory.PrepareItemCraftEvent`
- [Official Paper Javadoc](https://jd.papermc.io/paper/1.16.5/org/bukkit/event/inventory/PrepareItemCraftEvent.html)

## Python example

```python
from paperpybridge import Events

@bridge.on(Events.PREPARE_ITEM_CRAFT)
def on_event(event):
    print(event.event, event.data)
```

## `data` fields

| Field | JSON type | Java getter | Java return type | Declared in |
| --- | --- | --- | --- | --- |
| `repair` | boolean | `isRepair()` | `boolean` | `org.bukkit.event.inventory.PrepareItemCraftEvent` |

[[Data-Format-en|Wire format and limits]] · [[Event-org-bukkit-event-inventory-prepareitemcraftevent|中文]]

If this event is not enabled, add its Java class or simple name to `events.include` in the Paper plugin configuration.
