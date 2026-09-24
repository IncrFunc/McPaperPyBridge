# BlockCanBuildEvent

[[Home-en|Home]] / [[Category-block-en|block]]

- Java class: `org.bukkit.event.block.BlockCanBuildEvent`
- Parent class: `org.bukkit.event.block.BlockEvent`
- Python subscription: `BlockCanBuildEvent`
- Python constant: `Events.BLOCK_CAN_BUILD`
- Cancellable: No
- Player available: Possible at runtime
- HandlerList owner: `org.bukkit.event.block.BlockCanBuildEvent`
- [Official Paper Javadoc](https://jd.papermc.io/paper/1.16.5/org/bukkit/event/block/BlockCanBuildEvent.html)

## Python example

```python
from paperpybridge import Events

@bridge.on(Events.BLOCK_CAN_BUILD)
def on_event(event):
    print(event.event, event.data)
```

## `data` fields

| Field | JSON type | Java getter | Java return type | Declared in |
| --- | --- | --- | --- | --- |
| `block` | block summary | `getBlock()` | `org.bukkit.block.Block` | `org.bukkit.event.block.BlockEvent` |
| `material` | string | `getMaterial()` | `org.bukkit.Material` | `org.bukkit.event.block.BlockCanBuildEvent` |
| `buildable` | boolean | `isBuildable()` | `boolean` | `org.bukkit.event.block.BlockCanBuildEvent` |

[[Data-Format-en|Wire format and limits]] · [[Event-org-bukkit-event-block-blockcanbuildevent|中文]]

If this event is not enabled, add its Java class or simple name to `events.include` in the Paper plugin configuration.
