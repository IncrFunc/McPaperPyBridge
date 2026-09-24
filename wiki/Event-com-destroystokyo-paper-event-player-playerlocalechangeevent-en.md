# PlayerLocaleChangeEvent

[[Home-en|Home]] / [[Category-player-en|player]]

- Java class: `com.destroystokyo.paper.event.player.PlayerLocaleChangeEvent`
- Parent class: `org.bukkit.event.player.PlayerEvent`
- Python subscription: `PlayerLocaleChangeEvent`
- Python constant: `Events.PAPER_PLAYER_LOCALE_CHANGE`
- Cancellable: No
- Player available: Possible at runtime
- HandlerList owner: `com.destroystokyo.paper.event.player.PlayerLocaleChangeEvent`
- [Official Paper Javadoc](https://jd.papermc.io/paper/1.16.5/com/destroystokyo/paper/event/player/PlayerLocaleChangeEvent.html)

## Python example

```python
from paperpybridge import Events

@bridge.on(Events.PAPER_PLAYER_LOCALE_CHANGE)
def on_event(event):
    print(event.event, event.data)
```

## `data` fields

| Field | JSON type | Java getter | Java return type | Declared in |
| --- | --- | --- | --- | --- |
| `newLocale` | string | `getNewLocale()` | `java.lang.String` | `com.destroystokyo.paper.event.player.PlayerLocaleChangeEvent` |
| `oldLocale` | string | `getOldLocale()` | `java.lang.String` | `com.destroystokyo.paper.event.player.PlayerLocaleChangeEvent` |

[[Data-Format-en|Wire format and limits]] · [[Event-com-destroystokyo-paper-event-player-playerlocalechangeevent|中文]]

If this event is not enabled, add its Java class or simple name to `events.include` in the Paper plugin configuration.
