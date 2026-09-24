# BlockFromToEvent

[[Home-en|Home]] / [[Category-block-en|block]]

- Java class: `org.bukkit.event.block.BlockFromToEvent`
- Parent class: `org.bukkit.event.block.BlockEvent`
- Python subscription: `BlockFromToEvent`
- Python constant: `Events.BLOCK_FROM_TO`
- Cancellable: Yes
- Player available: No known player getter
- HandlerList owner: `org.bukkit.event.block.BlockFromToEvent`
- [Official Paper Javadoc](https://jd.papermc.io/paper/1.16.5/org/bukkit/event/block/BlockFromToEvent.html)

## Python example

```python
from paperpybridge import Events

@bridge.on(Events.BLOCK_FROM_TO)
def on_event(event):
    print(event.event, event.data)
```

## `data` fields

| Field | JSON type | Java getter | Java return type | Declared in |
| --- | --- | --- | --- | --- |
| `block` | block summary | `getBlock()` | `org.bukkit.block.Block` | `org.bukkit.event.block.BlockEvent` |
| `face` | string | `getFace()` | `org.bukkit.block.BlockFace` | `org.bukkit.event.block.BlockFromToEvent` |
| `toBlock` | block summary | `getToBlock()` | `org.bukkit.block.Block` | `org.bukkit.event.block.BlockFromToEvent` |

[[Data-Format-en|Wire format and limits]] · [[Event-org-bukkit-event-block-blockfromtoevent|中文]]

If this event is not enabled, add its Java class or simple name to `events.include` in the Paper plugin configuration.
