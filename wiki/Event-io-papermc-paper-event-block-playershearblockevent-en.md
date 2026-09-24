# PlayerShearBlockEvent

[[Home-en|Home]] / [[Category-block-en|block]]

- Java class: `io.papermc.paper.event.block.PlayerShearBlockEvent`
- Parent class: `org.bukkit.event.player.PlayerEvent`
- Python subscription: `PlayerShearBlockEvent`
- Python constant: `Events.PLAYER_SHEAR_BLOCK`
- Cancellable: Yes
- Player available: Possible at runtime
- HandlerList owner: `io.papermc.paper.event.block.PlayerShearBlockEvent`
- [Official Paper Javadoc](https://jd.papermc.io/paper/1.16.5/io/papermc/paper/event/block/PlayerShearBlockEvent.html)

## Python example

```python
from paperpybridge import Events

@bridge.on(Events.PLAYER_SHEAR_BLOCK)
def on_event(event):
    print(event.event, event.data)
```

## `data` fields

| Field | JSON type | Java getter | Java return type | Declared in |
| --- | --- | --- | --- | --- |
| `block` | block summary | `getBlock()` | `org.bukkit.block.Block` | `io.papermc.paper.event.block.PlayerShearBlockEvent` |
| `hand` | string | `getHand()` | `org.bukkit.inventory.EquipmentSlot` | `io.papermc.paper.event.block.PlayerShearBlockEvent` |
| `item` | item summary | `getItem()` | `org.bukkit.inventory.ItemStack` | `io.papermc.paper.event.block.PlayerShearBlockEvent` |

[[Data-Format-en|Wire format and limits]] · [[Event-io-papermc-paper-event-block-playershearblockevent|中文]]

If this event is not enabled, add its Java class or simple name to `events.include` in the Paper plugin configuration.
