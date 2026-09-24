# BlockDamageEvent

[[Home-en|Home]] / [[Category-block-en|block]]

- Java class: `org.bukkit.event.block.BlockDamageEvent`
- Parent class: `org.bukkit.event.block.BlockEvent`
- Python subscription: `BlockDamageEvent`
- Python constant: `Events.BLOCK_DAMAGE`
- Cancellable: Yes
- Player available: Possible at runtime
- HandlerList owner: `org.bukkit.event.block.BlockDamageEvent`
- [Official Paper Javadoc](https://jd.papermc.io/paper/1.16.5/org/bukkit/event/block/BlockDamageEvent.html)

## Python example

```python
from paperpybridge import Events

@bridge.on(Events.BLOCK_DAMAGE)
def on_event(event):
    print(event.event, event.data)
```

## `data` fields

| Field | JSON type | Java getter | Java return type | Declared in |
| --- | --- | --- | --- | --- |
| `block` | block summary | `getBlock()` | `org.bukkit.block.Block` | `org.bukkit.event.block.BlockEvent` |
| `instaBreak` | boolean | `getInstaBreak()` | `boolean` | `org.bukkit.event.block.BlockDamageEvent` |
| `itemInHand` | item summary | `getItemInHand()` | `org.bukkit.inventory.ItemStack` | `org.bukkit.event.block.BlockDamageEvent` |

[[Data-Format-en|Wire format and limits]] · [[Event-org-bukkit-event-block-blockdamageevent|中文]]

If this event is not enabled, add its Java class or simple name to `events.include` in the Paper plugin configuration.
