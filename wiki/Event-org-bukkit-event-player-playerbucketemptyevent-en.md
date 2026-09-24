# PlayerBucketEmptyEvent

[[Home-en|Home]] / [[Category-player-en|player]]

- Java class: `org.bukkit.event.player.PlayerBucketEmptyEvent`
- Parent class: `org.bukkit.event.player.PlayerBucketEvent`
- Python subscription: `PlayerBucketEmptyEvent`
- Python constant: `Events.PLAYER_BUCKET_EMPTY`
- Cancellable: Yes
- Player available: Possible at runtime
- HandlerList owner: `org.bukkit.event.player.PlayerBucketEmptyEvent`
- [Official Paper Javadoc](https://jd.papermc.io/paper/1.16.5/org/bukkit/event/player/PlayerBucketEmptyEvent.html)

## Python example

```python
from paperpybridge import Events

@bridge.on(Events.PLAYER_BUCKET_EMPTY)
def on_event(event):
    print(event.event, event.data)
```

## `data` fields

| Field | JSON type | Java getter | Java return type | Declared in |
| --- | --- | --- | --- | --- |
| `block` | block summary | `getBlock()` | `org.bukkit.block.Block` | `org.bukkit.event.player.PlayerBucketEvent` |
| `blockClicked` | block summary | `getBlockClicked()` | `org.bukkit.block.Block` | `org.bukkit.event.player.PlayerBucketEvent` |
| `blockFace` | string | `getBlockFace()` | `org.bukkit.block.BlockFace` | `org.bukkit.event.player.PlayerBucketEvent` |
| `bucket` | string | `getBucket()` | `org.bukkit.Material` | `org.bukkit.event.player.PlayerBucketEvent` |
| `hand` | string | `getHand()` | `org.bukkit.inventory.EquipmentSlot` | `org.bukkit.event.player.PlayerBucketEvent` |
| `itemStack` | item summary | `getItemStack()` | `org.bukkit.inventory.ItemStack` | `org.bukkit.event.player.PlayerBucketEvent` |

[[Data-Format-en|Wire format and limits]] · [[Event-org-bukkit-event-player-playerbucketemptyevent|中文]]

If this event is not enabled, add its Java class or simple name to `events.include` in the Paper plugin configuration.
