# BlockIgniteEvent

[[Home-en|Home]] / [[Category-block-en|block]]

- Java class: `org.bukkit.event.block.BlockIgniteEvent`
- Parent class: `org.bukkit.event.block.BlockEvent`
- Python subscription: `BlockIgniteEvent`
- Python constant: `Events.BLOCK_IGNITE`
- Cancellable: Yes
- Player available: Possible at runtime
- HandlerList owner: `org.bukkit.event.block.BlockIgniteEvent`
- [Official Paper Javadoc](https://jd.papermc.io/paper/1.16.5/org/bukkit/event/block/BlockIgniteEvent.html)

## Python example

```python
from paperpybridge import Events

@bridge.on(Events.BLOCK_IGNITE)
def on_event(event):
    print(event.event, event.data)
```

## `data` fields

| Field | JSON type | Java getter | Java return type | Declared in |
| --- | --- | --- | --- | --- |
| `block` | block summary | `getBlock()` | `org.bukkit.block.Block` | `org.bukkit.event.block.BlockEvent` |
| `cause` | string | `getCause()` | `org.bukkit.event.block.BlockIgniteEvent$IgniteCause` | `org.bukkit.event.block.BlockIgniteEvent` |
| `ignitingBlock` | block summary | `getIgnitingBlock()` | `org.bukkit.block.Block` | `org.bukkit.event.block.BlockIgniteEvent` |
| `ignitingEntity` | entity summary | `getIgnitingEntity()` | `org.bukkit.entity.Entity` | `org.bukkit.event.block.BlockIgniteEvent` |

[[Data-Format-en|Wire format and limits]] · [[Event-org-bukkit-event-block-blockigniteevent|中文]]

If this event is not enabled, add its Java class or simple name to `events.include` in the Paper plugin configuration.
