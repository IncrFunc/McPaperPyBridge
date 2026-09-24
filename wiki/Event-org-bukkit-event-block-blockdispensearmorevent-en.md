# BlockDispenseArmorEvent

[[Home-en|Home]] / [[Category-block-en|block]]

- Java class: `org.bukkit.event.block.BlockDispenseArmorEvent`
- Parent class: `org.bukkit.event.block.BlockDispenseEvent`
- Python subscription: `BlockDispenseArmorEvent`
- Python constant: `Events.BLOCK_DISPENSE_ARMOR`
- Cancellable: Yes
- Player available: No known player getter
- HandlerList owner: `org.bukkit.event.block.BlockDispenseEvent`
- [Official Paper Javadoc](https://jd.papermc.io/paper/1.16.5/org/bukkit/event/block/BlockDispenseArmorEvent.html)

## Python example

```python
from paperpybridge import Events

@bridge.on(Events.BLOCK_DISPENSE_ARMOR)
def on_event(event):
    print(event.event, event.data)
```

## `data` fields

| Field | JSON type | Java getter | Java return type | Declared in |
| --- | --- | --- | --- | --- |
| `block` | block summary | `getBlock()` | `org.bukkit.block.Block` | `org.bukkit.event.block.BlockEvent` |
| `item` | item summary | `getItem()` | `org.bukkit.inventory.ItemStack` | `org.bukkit.event.block.BlockDispenseEvent` |
| `targetEntity` | entity summary | `getTargetEntity()` | `org.bukkit.entity.LivingEntity` | `org.bukkit.event.block.BlockDispenseArmorEvent` |

[[Data-Format-en|Wire format and limits]] · [[Event-org-bukkit-event-block-blockdispensearmorevent|中文]]

If this event is not enabled, add its Java class or simple name to `events.include` in the Paper plugin configuration.
