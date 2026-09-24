# BlockDropItemEvent

[[Home-en|Home]] / [[Category-block-en|block]]

- Java class: `org.bukkit.event.block.BlockDropItemEvent`
- Parent class: `org.bukkit.event.block.BlockEvent`
- Python subscription: `BlockDropItemEvent`
- Python constant: `Events.BLOCK_DROP_ITEM`
- Cancellable: Yes
- Player available: Possible at runtime
- HandlerList owner: `org.bukkit.event.block.BlockDropItemEvent`
- [Official Paper Javadoc](https://jd.papermc.io/paper/1.16.5/org/bukkit/event/block/BlockDropItemEvent.html)

## Python example

```python
from paperpybridge import Events

@bridge.on(Events.BLOCK_DROP_ITEM)
def on_event(event):
    print(event.event, event.data)
```

## `data` fields

| Field | JSON type | Java getter | Java return type | Declared in |
| --- | --- | --- | --- | --- |
| `block` | block summary | `getBlock()` | `org.bukkit.block.Block` | `org.bukkit.event.block.BlockEvent` |

[[Data-Format-en|Wire format and limits]] · [[Event-org-bukkit-event-block-blockdropitemevent|中文]]

If this event is not enabled, add its Java class or simple name to `events.include` in the Paper plugin configuration.
