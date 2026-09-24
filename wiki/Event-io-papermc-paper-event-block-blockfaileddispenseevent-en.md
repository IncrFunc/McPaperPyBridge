# BlockFailedDispenseEvent

[[Home-en|Home]] / [[Category-block-en|block]]

- Java class: `io.papermc.paper.event.block.BlockFailedDispenseEvent`
- Parent class: `org.bukkit.event.block.BlockEvent`
- Python subscription: `BlockFailedDispenseEvent`
- Python constant: `Events.BLOCK_FAILED_DISPENSE`
- Cancellable: No
- Player available: No known player getter
- HandlerList owner: `io.papermc.paper.event.block.BlockFailedDispenseEvent`
- [Official Paper Javadoc](https://jd.papermc.io/paper/1.16.5/io/papermc/paper/event/block/BlockFailedDispenseEvent.html)

## Python example

```python
from paperpybridge import Events

@bridge.on(Events.BLOCK_FAILED_DISPENSE)
def on_event(event):
    print(event.event, event.data)
```

## `data` fields

| Field | JSON type | Java getter | Java return type | Declared in |
| --- | --- | --- | --- | --- |
| `block` | block summary | `getBlock()` | `org.bukkit.block.Block` | `org.bukkit.event.block.BlockEvent` |

[[Data-Format-en|Wire format and limits]] · [[Event-io-papermc-paper-event-block-blockfaileddispenseevent|中文]]

If this event is not enabled, add its Java class or simple name to `events.include` in the Paper plugin configuration.
