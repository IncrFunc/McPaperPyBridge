# FurnaceBurnEvent

[[Home-en|Home]] / [[Category-inventory-en|inventory]]

- Java class: `org.bukkit.event.inventory.FurnaceBurnEvent`
- Parent class: `org.bukkit.event.block.BlockEvent`
- Python subscription: `FurnaceBurnEvent`
- Python constant: `Events.FURNACE_BURN`
- Cancellable: Yes
- Player available: No known player getter
- HandlerList owner: `org.bukkit.event.inventory.FurnaceBurnEvent`
- [Official Paper Javadoc](https://jd.papermc.io/paper/1.16.5/org/bukkit/event/inventory/FurnaceBurnEvent.html)

## Python example

```python
from paperpybridge import Events

@bridge.on(Events.FURNACE_BURN)
def on_event(event):
    print(event.event, event.data)
```

## `data` fields

| Field | JSON type | Java getter | Java return type | Declared in |
| --- | --- | --- | --- | --- |
| `block` | block summary | `getBlock()` | `org.bukkit.block.Block` | `org.bukkit.event.block.BlockEvent` |
| `burnTime` | number | `getBurnTime()` | `int` | `org.bukkit.event.inventory.FurnaceBurnEvent` |
| `fuel` | item summary | `getFuel()` | `org.bukkit.inventory.ItemStack` | `org.bukkit.event.inventory.FurnaceBurnEvent` |
| `burning` | boolean | `isBurning()` | `boolean` | `org.bukkit.event.inventory.FurnaceBurnEvent` |

[[Data-Format-en|Wire format and limits]] · [[Event-org-bukkit-event-inventory-furnaceburnevent|中文]]

If this event is not enabled, add its Java class or simple name to `events.include` in the Paper plugin configuration.
