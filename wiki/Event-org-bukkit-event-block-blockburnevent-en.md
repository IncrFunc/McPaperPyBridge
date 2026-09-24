# BlockBurnEvent

[[Home-en|Home]] / [[Category-block-en|block]]

- Java class: `org.bukkit.event.block.BlockBurnEvent`
- Parent class: `org.bukkit.event.block.BlockEvent`
- Python subscription: `BlockBurnEvent`
- Python constant: `Events.BLOCK_BURN`
- Cancellable: Yes
- Player available: No known player getter
- HandlerList owner: `org.bukkit.event.block.BlockBurnEvent`
- [Official Paper Javadoc](https://jd.papermc.io/paper/1.16.5/org/bukkit/event/block/BlockBurnEvent.html)

## Python example

```python
from paperpybridge import Events

@bridge.on(Events.BLOCK_BURN)
def on_event(event):
    print(event.event, event.data)
```

## `data` fields

| Field | JSON type | Java getter | Java return type | Declared in |
| --- | --- | --- | --- | --- |
| `block` | block summary | `getBlock()` | `org.bukkit.block.Block` | `org.bukkit.event.block.BlockEvent` |
| `ignitingBlock` | block summary | `getIgnitingBlock()` | `org.bukkit.block.Block` | `org.bukkit.event.block.BlockBurnEvent` |

[[Data-Format-en|Wire format and limits]] · [[Event-org-bukkit-event-block-blockburnevent|中文]]

If this event is not enabled, add its Java class or simple name to `events.include` in the Paper plugin configuration.
