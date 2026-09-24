# BlockExpEvent

[[Home-en|Home]] / [[Category-block-en|block]]

- Java class: `org.bukkit.event.block.BlockExpEvent`
- Parent class: `org.bukkit.event.block.BlockEvent`
- Python subscription: `BlockExpEvent`
- Python constant: `Events.BLOCK_EXP`
- Cancellable: No
- Player available: No known player getter
- HandlerList owner: `org.bukkit.event.block.BlockExpEvent`
- [Official Paper Javadoc](https://jd.papermc.io/paper/1.16.5/org/bukkit/event/block/BlockExpEvent.html)

## Python example

```python
from paperpybridge import Events

@bridge.on(Events.BLOCK_EXP)
def on_event(event):
    print(event.event, event.data)
```

## `data` fields

| Field | JSON type | Java getter | Java return type | Declared in |
| --- | --- | --- | --- | --- |
| `block` | block summary | `getBlock()` | `org.bukkit.block.Block` | `org.bukkit.event.block.BlockEvent` |
| `expToDrop` | number | `getExpToDrop()` | `int` | `org.bukkit.event.block.BlockExpEvent` |

[[Data-Format-en|Wire format and limits]] · [[Event-org-bukkit-event-block-blockexpevent|中文]]

If this event is not enabled, add its Java class or simple name to `events.include` in the Paper plugin configuration.
