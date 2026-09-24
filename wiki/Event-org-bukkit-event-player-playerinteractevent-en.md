# PlayerInteractEvent

[[Home-en|Home]] / [[Category-player-en|player]]

- Java class: `org.bukkit.event.player.PlayerInteractEvent`
- Parent class: `org.bukkit.event.player.PlayerEvent`
- Python subscription: `PlayerInteractEvent`
- Python constant: `Events.PLAYER_INTERACT`
- Cancellable: Yes
- Player available: Possible at runtime
- HandlerList owner: `org.bukkit.event.player.PlayerInteractEvent`
- [Official Paper Javadoc](https://jd.papermc.io/paper/1.16.5/org/bukkit/event/player/PlayerInteractEvent.html)

## Python example

```python
from paperpybridge import Events

@bridge.on(Events.PLAYER_INTERACT)
def on_event(event):
    print(event.event, event.data)
```

## `data` fields

| Field | JSON type | Java getter | Java return type | Declared in |
| --- | --- | --- | --- | --- |
| `action` | string | `getAction()` | `org.bukkit.event.block.Action` | `org.bukkit.event.player.PlayerInteractEvent` |
| `blockFace` | string | `getBlockFace()` | `org.bukkit.block.BlockFace` | `org.bukkit.event.player.PlayerInteractEvent` |
| `clickedBlock` | block summary | `getClickedBlock()` | `org.bukkit.block.Block` | `org.bukkit.event.player.PlayerInteractEvent` |
| `hand` | string | `getHand()` | `org.bukkit.inventory.EquipmentSlot` | `org.bukkit.event.player.PlayerInteractEvent` |
| `interactionPoint` | location summary | `getInteractionPoint()` | `org.bukkit.Location` | `org.bukkit.event.player.PlayerInteractEvent` |
| `item` | item summary | `getItem()` | `org.bukkit.inventory.ItemStack` | `org.bukkit.event.player.PlayerInteractEvent` |
| `material` | string | `getMaterial()` | `org.bukkit.Material` | `org.bukkit.event.player.PlayerInteractEvent` |
| `blockInHand` | boolean | `isBlockInHand()` | `boolean` | `org.bukkit.event.player.PlayerInteractEvent` |

[[Data-Format-en|Wire format and limits]] · [[Event-org-bukkit-event-player-playerinteractevent|中文]]

If this event is not enabled, add its Java class or simple name to `events.include` in the Paper plugin configuration.
