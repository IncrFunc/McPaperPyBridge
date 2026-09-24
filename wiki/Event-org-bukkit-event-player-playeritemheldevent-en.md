# PlayerItemHeldEvent

[[Home-en|Home]] / [[Category-player-en|player]]

- Java class: `org.bukkit.event.player.PlayerItemHeldEvent`
- Parent class: `org.bukkit.event.player.PlayerEvent`
- Python subscription: `PlayerItemHeldEvent`
- Python constant: `Events.PLAYER_ITEM_HELD`
- Cancellable: Yes
- Player available: Possible at runtime
- HandlerList owner: `org.bukkit.event.player.PlayerItemHeldEvent`
- [Official Paper Javadoc](https://jd.papermc.io/paper/1.16.5/org/bukkit/event/player/PlayerItemHeldEvent.html)

## Python example

```python
from paperpybridge import Events

@bridge.on(Events.PLAYER_ITEM_HELD)
def on_event(event):
    print(event.event, event.data)
```

## `data` fields

| Field | JSON type | Java getter | Java return type | Declared in |
| --- | --- | --- | --- | --- |
| `newSlot` | number | `getNewSlot()` | `int` | `org.bukkit.event.player.PlayerItemHeldEvent` |
| `previousSlot` | number | `getPreviousSlot()` | `int` | `org.bukkit.event.player.PlayerItemHeldEvent` |

[[Data-Format-en|Wire format and limits]] · [[Event-org-bukkit-event-player-playeritemheldevent|中文]]

If this event is not enabled, add its Java class or simple name to `events.include` in the Paper plugin configuration.
