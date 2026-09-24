# PlayerSwapHandItemsEvent

[[Home-en|Home]] / [[Category-player-en|player]]

- Java class: `org.bukkit.event.player.PlayerSwapHandItemsEvent`
- Parent class: `org.bukkit.event.player.PlayerEvent`
- Python subscription: `PlayerSwapHandItemsEvent`
- Python constant: `Events.PLAYER_SWAP_HAND_ITEMS`
- Cancellable: Yes
- Player available: Possible at runtime
- HandlerList owner: `org.bukkit.event.player.PlayerSwapHandItemsEvent`
- [Official Paper Javadoc](https://jd.papermc.io/paper/1.16.5/org/bukkit/event/player/PlayerSwapHandItemsEvent.html)

## Python example

```python
from paperpybridge import Events

@bridge.on(Events.PLAYER_SWAP_HAND_ITEMS)
def on_event(event):
    print(event.event, event.data)
```

## `data` fields

| Field | JSON type | Java getter | Java return type | Declared in |
| --- | --- | --- | --- | --- |
| `mainHandItem` | item summary | `getMainHandItem()` | `org.bukkit.inventory.ItemStack` | `org.bukkit.event.player.PlayerSwapHandItemsEvent` |
| `offHandItem` | item summary | `getOffHandItem()` | `org.bukkit.inventory.ItemStack` | `org.bukkit.event.player.PlayerSwapHandItemsEvent` |

[[Data-Format-en|Wire format and limits]] · [[Event-org-bukkit-event-player-playerswaphanditemsevent|中文]]

If this event is not enabled, add its Java class or simple name to `events.include` in the Paper plugin configuration.
