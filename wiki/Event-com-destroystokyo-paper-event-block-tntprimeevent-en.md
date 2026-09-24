# TNTPrimeEvent

[[Home-en|Home]] / [[Category-block-en|block]]

- Java class: `com.destroystokyo.paper.event.block.TNTPrimeEvent`
- Parent class: `org.bukkit.event.block.BlockEvent`
- Python subscription: `TNTPrimeEvent`
- Python constant: `Events.TNT_PRIME`
- Cancellable: Yes
- Player available: No known player getter
- HandlerList owner: `com.destroystokyo.paper.event.block.TNTPrimeEvent`
- [Official Paper Javadoc](https://jd.papermc.io/paper/1.16.5/com/destroystokyo/paper/event/block/TNTPrimeEvent.html)

## Python example

```python
from paperpybridge import Events

@bridge.on(Events.TNT_PRIME)
def on_event(event):
    print(event.event, event.data)
```

## `data` fields

| Field | JSON type | Java getter | Java return type | Declared in |
| --- | --- | --- | --- | --- |
| `block` | block summary | `getBlock()` | `org.bukkit.block.Block` | `org.bukkit.event.block.BlockEvent` |
| `primerEntity` | entity summary | `getPrimerEntity()` | `org.bukkit.entity.Entity` | `com.destroystokyo.paper.event.block.TNTPrimeEvent` |
| `reason` | string | `getReason()` | `com.destroystokyo.paper.event.block.TNTPrimeEvent$PrimeReason` | `com.destroystokyo.paper.event.block.TNTPrimeEvent` |

[[Data-Format-en|Wire format and limits]] · [[Event-com-destroystokyo-paper-event-block-tntprimeevent|中文]]

If this event is not enabled, add its Java class or simple name to `events.include` in the Paper plugin configuration.
