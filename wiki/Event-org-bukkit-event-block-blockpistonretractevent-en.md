# BlockPistonRetractEvent

[[Home-en|Home]] / [[Category-block-en|block]]

- Java class: `org.bukkit.event.block.BlockPistonRetractEvent`
- Parent class: `org.bukkit.event.block.BlockPistonEvent`
- Python subscription: `BlockPistonRetractEvent`
- Python constant: `Events.BLOCK_PISTON_RETRACT`
- Cancellable: Yes
- Player available: No known player getter
- HandlerList owner: `org.bukkit.event.block.BlockPistonRetractEvent`
- [Official Paper Javadoc](https://jd.papermc.io/paper/1.16.5/org/bukkit/event/block/BlockPistonRetractEvent.html)

## Python example

```python
from paperpybridge import Events

@bridge.on(Events.BLOCK_PISTON_RETRACT)
def on_event(event):
    print(event.event, event.data)
```

## `data` fields

| Field | JSON type | Java getter | Java return type | Declared in |
| --- | --- | --- | --- | --- |
| `block` | block summary | `getBlock()` | `org.bukkit.block.Block` | `org.bukkit.event.block.BlockEvent` |
| `direction` | string | `getDirection()` | `org.bukkit.block.BlockFace` | `org.bukkit.event.block.BlockPistonEvent` |
| `retractLocation` | location summary | `getRetractLocation()` | `org.bukkit.Location` | `org.bukkit.event.block.BlockPistonRetractEvent` |
| `sticky` | boolean | `isSticky()` | `boolean` | `org.bukkit.event.block.BlockPistonEvent` |

[[Data-Format-en|Wire format and limits]] · [[Event-org-bukkit-event-block-blockpistonretractevent|中文]]

If this event is not enabled, add its Java class or simple name to `events.include` in the Paper plugin configuration.
