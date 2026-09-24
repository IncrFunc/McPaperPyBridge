# PlayerConnectionCloseEvent

[[Home-en|Home]] / [[Category-player-en|player]]

- Java class: `com.destroystokyo.paper.event.player.PlayerConnectionCloseEvent`
- Parent class: `org.bukkit.event.Event`
- Python subscription: `PlayerConnectionCloseEvent`
- Python constant: `Events.PLAYER_CONNECTION_CLOSE`
- Cancellable: No
- Player available: No known player getter
- HandlerList owner: `com.destroystokyo.paper.event.player.PlayerConnectionCloseEvent`
- [Official Paper Javadoc](https://jd.papermc.io/paper/1.16.5/com/destroystokyo/paper/event/player/PlayerConnectionCloseEvent.html)

## Python example

```python
from paperpybridge import Events

@bridge.on(Events.PLAYER_CONNECTION_CLOSE)
def on_event(event):
    print(event.event, event.data)
```

## `data` fields

| Field | JSON type | Java getter | Java return type | Declared in |
| --- | --- | --- | --- | --- |
| `playerName` | string | `getPlayerName()` | `java.lang.String` | `com.destroystokyo.paper.event.player.PlayerConnectionCloseEvent` |
| `playerUniqueId` | string | `getPlayerUniqueId()` | `java.util.UUID` | `com.destroystokyo.paper.event.player.PlayerConnectionCloseEvent` |

[[Data-Format-en|Wire format and limits]] · [[Event-com-destroystokyo-paper-event-player-playerconnectioncloseevent|中文]]

If this event is not enabled, add its Java class or simple name to `events.include` in the Paper plugin configuration.
