# BlockPhysicsEvent

[[Home-en|Home]] / [[Category-block-en|block]]

- Java class: `org.bukkit.event.block.BlockPhysicsEvent`
- Parent class: `org.bukkit.event.block.BlockEvent`
- Python subscription: `BlockPhysicsEvent`
- Python constant: `Events.BLOCK_PHYSICS`
- Cancellable: Yes
- Player available: No known player getter
- HandlerList owner: `org.bukkit.event.block.BlockPhysicsEvent`
- [Official Paper Javadoc](https://jd.papermc.io/paper/1.16.5/org/bukkit/event/block/BlockPhysicsEvent.html)

## Python example

```python
from paperpybridge import Events

@bridge.on(Events.BLOCK_PHYSICS)
def on_event(event):
    print(event.event, event.data)
```

## `data` fields

| Field | JSON type | Java getter | Java return type | Declared in |
| --- | --- | --- | --- | --- |
| `block` | block summary | `getBlock()` | `org.bukkit.block.Block` | `org.bukkit.event.block.BlockEvent` |
| `changedType` | string | `getChangedType()` | `org.bukkit.Material` | `org.bukkit.event.block.BlockPhysicsEvent` |
| `sourceBlock` | block summary | `getSourceBlock()` | `org.bukkit.block.Block` | `org.bukkit.event.block.BlockPhysicsEvent` |

[[Data-Format-en|Wire format and limits]] · [[Event-org-bukkit-event-block-blockphysicsevent|中文]]

If this event is not enabled, add its Java class or simple name to `events.include` in the Paper plugin configuration.
