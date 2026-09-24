# BellRevealRaiderEvent

[[Home-en|Home]] / [[Category-block-en|block]]

- Java class: `io.papermc.paper.event.block.BellRevealRaiderEvent`
- Parent class: `org.bukkit.event.block.BlockEvent`
- Python subscription: `BellRevealRaiderEvent`
- Python constant: `Events.BELL_REVEAL_RAIDER`
- Cancellable: Yes
- Player available: Possible at runtime
- HandlerList owner: `io.papermc.paper.event.block.BellRevealRaiderEvent`
- [Official Paper Javadoc](https://jd.papermc.io/paper/1.16.5/io/papermc/paper/event/block/BellRevealRaiderEvent.html)

## Python example

```python
from paperpybridge import Events

@bridge.on(Events.BELL_REVEAL_RAIDER)
def on_event(event):
    print(event.event, event.data)
```

## `data` fields

| Field | JSON type | Java getter | Java return type | Declared in |
| --- | --- | --- | --- | --- |
| `block` | block summary | `getBlock()` | `org.bukkit.block.Block` | `org.bukkit.event.block.BlockEvent` |
| `entity` | entity summary | `getEntity()` | `org.bukkit.entity.Raider` | `io.papermc.paper.event.block.BellRevealRaiderEvent` |

[[Data-Format-en|Wire format and limits]] · [[Event-io-papermc-paper-event-block-bellrevealraiderevent|中文]]

If this event is not enabled, add its Java class or simple name to `events.include` in the Paper plugin configuration.
