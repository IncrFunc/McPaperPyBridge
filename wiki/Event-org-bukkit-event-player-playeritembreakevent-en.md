# PlayerItemBreakEvent

[[Home-en|Home]] / [[Category-player-en|player]]

- Java class: `org.bukkit.event.player.PlayerItemBreakEvent`
- Parent class: `org.bukkit.event.player.PlayerEvent`
- Python subscription: `PlayerItemBreakEvent`
- Python constant: `Events.PLAYER_ITEM_BREAK`
- Cancellable: No
- Player available: Possible at runtime
- HandlerList owner: `org.bukkit.event.player.PlayerItemBreakEvent`
- [Official Paper Javadoc](https://jd.papermc.io/paper/1.16.5/org/bukkit/event/player/PlayerItemBreakEvent.html)

## Python example

```python
from paperpybridge import Events

@bridge.on(Events.PLAYER_ITEM_BREAK)
def on_event(event):
    print(event.event, event.data)
```

## `data` fields

| Field | JSON type | Java getter | Java return type | Declared in |
| --- | --- | --- | --- | --- |
| `brokenItem` | item summary | `getBrokenItem()` | `org.bukkit.inventory.ItemStack` | `org.bukkit.event.player.PlayerItemBreakEvent` |

[[Data-Format-en|Wire format and limits]] · [[Event-org-bukkit-event-player-playeritembreakevent|中文]]

If this event is not enabled, add its Java class or simple name to `events.include` in the Paper plugin configuration.
