# PlayerEditBookEvent

[[Home-en|Home]] / [[Category-player-en|player]]

- Java class: `org.bukkit.event.player.PlayerEditBookEvent`
- Parent class: `org.bukkit.event.player.PlayerEvent`
- Python subscription: `PlayerEditBookEvent`
- Python constant: `Events.PLAYER_EDIT_BOOK`
- Cancellable: Yes
- Player available: Possible at runtime
- HandlerList owner: `org.bukkit.event.player.PlayerEditBookEvent`
- [Official Paper Javadoc](https://jd.papermc.io/paper/1.16.5/org/bukkit/event/player/PlayerEditBookEvent.html)

## Python example

```python
from paperpybridge import Events

@bridge.on(Events.PLAYER_EDIT_BOOK)
def on_event(event):
    print(event.event, event.data)
```

## `data` fields

| Field | JSON type | Java getter | Java return type | Declared in |
| --- | --- | --- | --- | --- |
| `slot` | number | `getSlot()` | `int` | `org.bukkit.event.player.PlayerEditBookEvent` |
| `signing` | boolean | `isSigning()` | `boolean` | `org.bukkit.event.player.PlayerEditBookEvent` |

[[Data-Format-en|Wire format and limits]] · [[Event-org-bukkit-event-player-playereditbookevent|中文]]

If this event is not enabled, add its Java class or simple name to `events.include` in the Paper plugin configuration.
