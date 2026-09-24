# PlayerLecternPageChangeEvent

[[Home-en|Home]] / [[Category-player-en|player]]

- Java class: `io.papermc.paper.event.player.PlayerLecternPageChangeEvent`
- Parent class: `org.bukkit.event.player.PlayerEvent`
- Python subscription: `PlayerLecternPageChangeEvent`
- Python constant: `Events.PLAYER_LECTERN_PAGE_CHANGE`
- Cancellable: Yes
- Player available: Possible at runtime
- HandlerList owner: `io.papermc.paper.event.player.PlayerLecternPageChangeEvent`
- [Official Paper Javadoc](https://jd.papermc.io/paper/1.16.5/io/papermc/paper/event/player/PlayerLecternPageChangeEvent.html)

## Python example

```python
from paperpybridge import Events

@bridge.on(Events.PLAYER_LECTERN_PAGE_CHANGE)
def on_event(event):
    print(event.event, event.data)
```

## `data` fields

| Field | JSON type | Java getter | Java return type | Declared in |
| --- | --- | --- | --- | --- |
| `book` | item summary | `getBook()` | `org.bukkit.inventory.ItemStack` | `io.papermc.paper.event.player.PlayerLecternPageChangeEvent` |
| `newPage` | number | `getNewPage()` | `int` | `io.papermc.paper.event.player.PlayerLecternPageChangeEvent` |
| `oldPage` | number | `getOldPage()` | `int` | `io.papermc.paper.event.player.PlayerLecternPageChangeEvent` |
| `pageChangeDirection` | string | `getPageChangeDirection()` | `io.papermc.paper.event.player.PlayerLecternPageChangeEvent$PageChangeDirection` | `io.papermc.paper.event.player.PlayerLecternPageChangeEvent` |

[[Data-Format-en|Wire format and limits]] · [[Event-io-papermc-paper-event-player-playerlecternpagechangeevent|中文]]

If this event is not enabled, add its Java class or simple name to `events.include` in the Paper plugin configuration.
