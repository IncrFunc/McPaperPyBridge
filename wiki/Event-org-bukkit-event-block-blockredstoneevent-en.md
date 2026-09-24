# BlockRedstoneEvent

[[Home-en|Home]] / [[Category-block-en|block]]

- Java class: `org.bukkit.event.block.BlockRedstoneEvent`
- Parent class: `org.bukkit.event.block.BlockEvent`
- Python subscription: `BlockRedstoneEvent`
- Python constant: `Events.BLOCK_REDSTONE`
- Cancellable: No
- Player available: No known player getter
- HandlerList owner: `org.bukkit.event.block.BlockRedstoneEvent`
- [Official Paper Javadoc](https://jd.papermc.io/paper/1.16.5/org/bukkit/event/block/BlockRedstoneEvent.html)

## Python example

```python
from paperpybridge import Events

@bridge.on(Events.BLOCK_REDSTONE)
def on_event(event):
    print(event.event, event.data)
```

## `data` fields

| Field | JSON type | Java getter | Java return type | Declared in |
| --- | --- | --- | --- | --- |
| `block` | block summary | `getBlock()` | `org.bukkit.block.Block` | `org.bukkit.event.block.BlockEvent` |
| `newCurrent` | number | `getNewCurrent()` | `int` | `org.bukkit.event.block.BlockRedstoneEvent` |
| `oldCurrent` | number | `getOldCurrent()` | `int` | `org.bukkit.event.block.BlockRedstoneEvent` |

[[Data-Format-en|Wire format and limits]] · [[Event-org-bukkit-event-block-blockredstoneevent|中文]]

If this event is not enabled, add its Java class or simple name to `events.include` in the Paper plugin configuration.
