# FurnaceSmeltEvent

[[Home-en|Home]] / [[Category-inventory-en|inventory]]

- Java class: `org.bukkit.event.inventory.FurnaceSmeltEvent`
- Parent class: `org.bukkit.event.block.BlockCookEvent`
- Python subscription: `FurnaceSmeltEvent`
- Python constant: `Events.FURNACE_SMELT`
- Cancellable: Yes
- Player available: No known player getter
- HandlerList owner: `org.bukkit.event.block.BlockCookEvent`
- [Official Paper Javadoc](https://jd.papermc.io/paper/1.16.5/org/bukkit/event/inventory/FurnaceSmeltEvent.html)

## Python example

```python
from paperpybridge import Events

@bridge.on(Events.FURNACE_SMELT)
def on_event(event):
    print(event.event, event.data)
```

## `data` fields

| Field | JSON type | Java getter | Java return type | Declared in |
| --- | --- | --- | --- | --- |
| `block` | block summary | `getBlock()` | `org.bukkit.block.Block` | `org.bukkit.event.block.BlockEvent` |
| `result` | item summary | `getResult()` | `org.bukkit.inventory.ItemStack` | `org.bukkit.event.block.BlockCookEvent` |
| `source` | item summary | `getSource()` | `org.bukkit.inventory.ItemStack` | `org.bukkit.event.block.BlockCookEvent` |

[[Data-Format-en|Wire format and limits]] · [[Event-org-bukkit-event-inventory-furnacesmeltevent|中文]]

If this event is not enabled, add its Java class or simple name to `events.include` in the Paper plugin configuration.
