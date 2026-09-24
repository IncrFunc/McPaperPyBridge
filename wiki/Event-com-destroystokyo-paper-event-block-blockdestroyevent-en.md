# BlockDestroyEvent

[[Home-en|Home]] / [[Category-block-en|block]]

- Java class: `com.destroystokyo.paper.event.block.BlockDestroyEvent`
- Parent class: `org.bukkit.event.block.BlockEvent`
- Python subscription: `BlockDestroyEvent`
- Python constant: `Events.BLOCK_DESTROY`
- Cancellable: Yes
- Player available: No known player getter
- HandlerList owner: `com.destroystokyo.paper.event.block.BlockDestroyEvent`
- [Official Paper Javadoc](https://jd.papermc.io/paper/1.16.5/com/destroystokyo/paper/event/block/BlockDestroyEvent.html)

## Python example

```python
from paperpybridge import Events

@bridge.on(Events.BLOCK_DESTROY)
def on_event(event):
    print(event.event, event.data)
```

## `data` fields

| Field | JSON type | Java getter | Java return type | Declared in |
| --- | --- | --- | --- | --- |
| `block` | block summary | `getBlock()` | `org.bukkit.block.Block` | `org.bukkit.event.block.BlockEvent` |

[[Data-Format-en|Wire format and limits]] · [[Event-com-destroystokyo-paper-event-block-blockdestroyevent|中文]]

If this event is not enabled, add its Java class or simple name to `events.include` in the Paper plugin configuration.
