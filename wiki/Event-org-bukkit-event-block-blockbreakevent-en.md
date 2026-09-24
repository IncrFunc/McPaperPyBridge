# BlockBreakEvent

[[Home-en|Home]] / [[Category-block-en|block]]

- Java class: `org.bukkit.event.block.BlockBreakEvent`
- Parent class: `org.bukkit.event.block.BlockExpEvent`
- Python subscription: `BlockBreakEvent`
- Python constant: `Events.BLOCK_BREAK`
- Cancellable: Yes
- Player available: Possible at runtime
- HandlerList owner: `org.bukkit.event.block.BlockExpEvent`
- [Official Paper Javadoc](https://jd.papermc.io/paper/1.16.5/org/bukkit/event/block/BlockBreakEvent.html)

## Python example

```python
from paperpybridge import Events

@bridge.on(Events.BLOCK_BREAK)
def on_event(event):
    print(event.event, event.data)
```

## `data` fields

| Field | JSON type | Java getter | Java return type | Declared in |
| --- | --- | --- | --- | --- |
| `block` | block summary | `getBlock()` | `org.bukkit.block.Block` | `org.bukkit.event.block.BlockEvent` |
| `expToDrop` | number | `getExpToDrop()` | `int` | `org.bukkit.event.block.BlockExpEvent` |
| `dropItems` | boolean | `isDropItems()` | `boolean` | `org.bukkit.event.block.BlockBreakEvent` |

[[Data-Format-en|Wire format and limits]] · [[Event-org-bukkit-event-block-blockbreakevent|中文]]

If this event is not enabled, add its Java class or simple name to `events.include` in the Paper plugin configuration.
