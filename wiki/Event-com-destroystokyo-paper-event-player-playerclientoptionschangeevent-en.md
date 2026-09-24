# PlayerClientOptionsChangeEvent

[[Home-en|Home]] / [[Category-player-en|player]]

- Java class: `com.destroystokyo.paper.event.player.PlayerClientOptionsChangeEvent`
- Parent class: `org.bukkit.event.player.PlayerEvent`
- Python subscription: `PlayerClientOptionsChangeEvent`
- Python constant: `Events.PLAYER_CLIENT_OPTIONS_CHANGE`
- Cancellable: No
- Player available: Possible at runtime
- HandlerList owner: `com.destroystokyo.paper.event.player.PlayerClientOptionsChangeEvent`
- [Official Paper Javadoc](https://jd.papermc.io/paper/1.16.5/com/destroystokyo/paper/event/player/PlayerClientOptionsChangeEvent.html)

## Python example

```python
from paperpybridge import Events

@bridge.on(Events.PLAYER_CLIENT_OPTIONS_CHANGE)
def on_event(event):
    print(event.event, event.data)
```

## `data` fields

| Field | JSON type | Java getter | Java return type | Declared in |
| --- | --- | --- | --- | --- |
| `chatVisibility` | string | `getChatVisibility()` | `com.destroystokyo.paper.ClientOption$ChatVisibility` | `com.destroystokyo.paper.event.player.PlayerClientOptionsChangeEvent` |
| `locale` | string | `getLocale()` | `java.lang.String` | `com.destroystokyo.paper.event.player.PlayerClientOptionsChangeEvent` |
| `mainHand` | string | `getMainHand()` | `org.bukkit.inventory.MainHand` | `com.destroystokyo.paper.event.player.PlayerClientOptionsChangeEvent` |
| `viewDistance` | number | `getViewDistance()` | `int` | `com.destroystokyo.paper.event.player.PlayerClientOptionsChangeEvent` |

[[Data-Format-en|Wire format and limits]] · [[Event-com-destroystokyo-paper-event-player-playerclientoptionschangeevent|中文]]

If this event is not enabled, add its Java class or simple name to `events.include` in the Paper plugin configuration.
