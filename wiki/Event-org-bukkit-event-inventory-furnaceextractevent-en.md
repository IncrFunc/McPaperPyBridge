# FurnaceExtractEvent

[[Home-en|Home]] / [[Category-inventory-en|inventory]]

- Java class: `org.bukkit.event.inventory.FurnaceExtractEvent`
- Parent class: `org.bukkit.event.block.BlockExpEvent`
- Python subscription: `FurnaceExtractEvent`
- Python constant: `Events.FURNACE_EXTRACT`
- Cancellable: No
- Player available: Possible at runtime
- HandlerList owner: `org.bukkit.event.block.BlockExpEvent`
- [Official Paper Javadoc](https://jd.papermc.io/paper/1.16.5/org/bukkit/event/inventory/FurnaceExtractEvent.html)

## Python example

```python
from paperpybridge import Events

@bridge.on(Events.FURNACE_EXTRACT)
def on_event(event):
    print(event.event, event.data)
```

## `data` fields

| Field | JSON type | Java getter | Java return type | Declared in |
| --- | --- | --- | --- | --- |
| `block` | block summary | `getBlock()` | `org.bukkit.block.Block` | `org.bukkit.event.block.BlockEvent` |
| `expToDrop` | number | `getExpToDrop()` | `int` | `org.bukkit.event.block.BlockExpEvent` |
| `itemAmount` | number | `getItemAmount()` | `int` | `org.bukkit.event.inventory.FurnaceExtractEvent` |
| `itemType` | string | `getItemType()` | `org.bukkit.Material` | `org.bukkit.event.inventory.FurnaceExtractEvent` |

[[Data-Format-en|Wire format and limits]] · [[Event-org-bukkit-event-inventory-furnaceextractevent|中文]]

If this event is not enabled, add its Java class or simple name to `events.include` in the Paper plugin configuration.
