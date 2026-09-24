# BlockPreDispenseEvent

[[Home-en|Home]] / [[Category-block-en|block]]

- Java class: `io.papermc.paper.event.block.BlockPreDispenseEvent`
- Parent class: `org.bukkit.event.block.BlockEvent`
- Python subscription: `BlockPreDispenseEvent`
- Python constant: `Events.BLOCK_PRE_DISPENSE`
- Cancellable: Yes
- Player available: No known player getter
- HandlerList owner: `io.papermc.paper.event.block.BlockPreDispenseEvent`
- [Official Paper Javadoc](https://jd.papermc.io/paper/1.16.5/io/papermc/paper/event/block/BlockPreDispenseEvent.html)

## Python example

```python
from paperpybridge import Events

@bridge.on(Events.BLOCK_PRE_DISPENSE)
def on_event(event):
    print(event.event, event.data)
```

## `data` fields

| Field | JSON type | Java getter | Java return type | Declared in |
| --- | --- | --- | --- | --- |
| `block` | block summary | `getBlock()` | `org.bukkit.block.Block` | `org.bukkit.event.block.BlockEvent` |
| `itemStack` | item summary | `getItemStack()` | `org.bukkit.inventory.ItemStack` | `io.papermc.paper.event.block.BlockPreDispenseEvent` |
| `slot` | number | `getSlot()` | `int` | `io.papermc.paper.event.block.BlockPreDispenseEvent` |

[[Data-Format-en|Wire format and limits]] · [[Event-io-papermc-paper-event-block-blockpredispenseevent|中文]]

If this event is not enabled, add its Java class or simple name to `events.include` in the Paper plugin configuration.
