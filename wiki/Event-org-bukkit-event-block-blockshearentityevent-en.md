# BlockShearEntityEvent

[[Home-en|Home]] / [[Category-block-en|block]]

- Java class: `org.bukkit.event.block.BlockShearEntityEvent`
- Parent class: `org.bukkit.event.block.BlockEvent`
- Python subscription: `BlockShearEntityEvent`
- Python constant: `Events.BLOCK_SHEAR_ENTITY`
- Cancellable: Yes
- Player available: Possible at runtime
- HandlerList owner: `org.bukkit.event.block.BlockShearEntityEvent`
- [Official Paper Javadoc](https://jd.papermc.io/paper/1.16.5/org/bukkit/event/block/BlockShearEntityEvent.html)

## Python example

```python
from paperpybridge import Events

@bridge.on(Events.BLOCK_SHEAR_ENTITY)
def on_event(event):
    print(event.event, event.data)
```

## `data` fields

| Field | JSON type | Java getter | Java return type | Declared in |
| --- | --- | --- | --- | --- |
| `block` | block summary | `getBlock()` | `org.bukkit.block.Block` | `org.bukkit.event.block.BlockEvent` |
| `entity` | entity summary | `getEntity()` | `org.bukkit.entity.Entity` | `org.bukkit.event.block.BlockShearEntityEvent` |
| `tool` | item summary | `getTool()` | `org.bukkit.inventory.ItemStack` | `org.bukkit.event.block.BlockShearEntityEvent` |

[[Data-Format-en|Wire format and limits]] · [[Event-org-bukkit-event-block-blockshearentityevent|中文]]

If this event is not enabled, add its Java class or simple name to `events.include` in the Paper plugin configuration.
