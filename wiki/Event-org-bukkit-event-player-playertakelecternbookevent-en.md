# PlayerTakeLecternBookEvent

[[Home-en|Home]] / [[Category-player-en|player]]

- Java class: `org.bukkit.event.player.PlayerTakeLecternBookEvent`
- Parent class: `org.bukkit.event.player.PlayerEvent`
- Python subscription: `PlayerTakeLecternBookEvent`
- Python constant: `Events.PLAYER_TAKE_LECTERN_BOOK`
- Cancellable: Yes
- Player available: Possible at runtime
- HandlerList owner: `org.bukkit.event.player.PlayerTakeLecternBookEvent`
- [Official Paper Javadoc](https://jd.papermc.io/paper/1.16.5/org/bukkit/event/player/PlayerTakeLecternBookEvent.html)

## Python example

```python
from paperpybridge import Events

@bridge.on(Events.PLAYER_TAKE_LECTERN_BOOK)
def on_event(event):
    print(event.event, event.data)
```

## `data` fields

| Field | JSON type | Java getter | Java return type | Declared in |
| --- | --- | --- | --- | --- |
| `book` | item summary | `getBook()` | `org.bukkit.inventory.ItemStack` | `org.bukkit.event.player.PlayerTakeLecternBookEvent` |

[[Data-Format-en|Wire format and limits]] · [[Event-org-bukkit-event-player-playertakelecternbookevent|中文]]

If this event is not enabled, add its Java class or simple name to `events.include` in the Paper plugin configuration.
