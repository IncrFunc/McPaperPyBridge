# PlayerLoginEvent

[[Home-en|Home]] / [[Category-player-en|player]]

- Java class: `org.bukkit.event.player.PlayerLoginEvent`
- Parent class: `org.bukkit.event.player.PlayerEvent`
- Python subscription: `PlayerLoginEvent`
- Python constant: `Events.PLAYER_LOGIN`
- Cancellable: No
- Player available: Possible at runtime
- HandlerList owner: `org.bukkit.event.player.PlayerLoginEvent`
- [Official Paper Javadoc](https://jd.papermc.io/paper/1.16.5/org/bukkit/event/player/PlayerLoginEvent.html)

## Python example

```python
from paperpybridge import Events

@bridge.on(Events.PLAYER_LOGIN)
def on_event(event):
    print(event.event, event.data)
```

## `data` fields

| Field | JSON type | Java getter | Java return type | Declared in |
| --- | --- | --- | --- | --- |
| `hostname` | string | `getHostname()` | `java.lang.String` | `org.bukkit.event.player.PlayerLoginEvent` |
| `kickMessage` | string | `getKickMessage()` | `java.lang.String` | `org.bukkit.event.player.PlayerLoginEvent` |
| `result` | string | `getResult()` | `org.bukkit.event.player.PlayerLoginEvent$Result` | `org.bukkit.event.player.PlayerLoginEvent` |

[[Data-Format-en|Wire format and limits]] · [[Event-org-bukkit-event-player-playerloginevent|中文]]

If this event is not enabled, add its Java class or simple name to `events.include` in the Paper plugin configuration.
