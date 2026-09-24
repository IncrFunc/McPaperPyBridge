# BlockPlaceEvent

[[Home-en|Home]] / [[Category-block-en|block]]

- Java class: `org.bukkit.event.block.BlockPlaceEvent`
- Parent class: `org.bukkit.event.block.BlockEvent`
- Python subscription: `BlockPlaceEvent`
- Python constant: `Events.BLOCK_PLACE`
- Cancellable: Yes
- Player available: Possible at runtime
- HandlerList owner: `org.bukkit.event.block.BlockPlaceEvent`
- [Official Paper Javadoc](https://jd.papermc.io/paper/1.16.5/org/bukkit/event/block/BlockPlaceEvent.html)

## Python example

```python
from paperpybridge import Events

@bridge.on(Events.BLOCK_PLACE)
def on_event(event):
    print(event.event, event.data)
```

## `data` fields

| Field | JSON type | Java getter | Java return type | Declared in |
| --- | --- | --- | --- | --- |
| `block` | block summary | `getBlock()` | `org.bukkit.block.Block` | `org.bukkit.event.block.BlockEvent` |
| `blockAgainst` | block summary | `getBlockAgainst()` | `org.bukkit.block.Block` | `org.bukkit.event.block.BlockPlaceEvent` |
| `blockPlaced` | block summary | `getBlockPlaced()` | `org.bukkit.block.Block` | `org.bukkit.event.block.BlockPlaceEvent` |
| `hand` | string | `getHand()` | `org.bukkit.inventory.EquipmentSlot` | `org.bukkit.event.block.BlockPlaceEvent` |
| `itemInHand` | item summary | `getItemInHand()` | `org.bukkit.inventory.ItemStack` | `org.bukkit.event.block.BlockPlaceEvent` |

[[Data-Format-en|Wire format and limits]] · [[Event-org-bukkit-event-block-blockplaceevent|中文]]

If this event is not enabled, add its Java class or simple name to `events.include` in the Paper plugin configuration.
