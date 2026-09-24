# AsyncPlayerPreLoginEvent

[[Home-en|Home]] / [[Category-player-en|player]]

- Java class: `org.bukkit.event.player.AsyncPlayerPreLoginEvent`
- Parent class: `org.bukkit.event.Event`
- Python subscription: `AsyncPlayerPreLoginEvent`
- Python constant: `Events.ASYNC_PLAYER_PRE_LOGIN`
- Cancellable: No
- Player available: No known player getter
- HandlerList owner: `org.bukkit.event.player.AsyncPlayerPreLoginEvent`
- [Official Paper Javadoc](https://jd.papermc.io/paper/1.16.5/org/bukkit/event/player/AsyncPlayerPreLoginEvent.html)

## Python example

```python
from paperpybridge import Events

@bridge.on(Events.ASYNC_PLAYER_PRE_LOGIN)
def on_event(event):
    print(event.event, event.data)
```

## `data` fields

| Field | JSON type | Java getter | Java return type | Declared in |
| --- | --- | --- | --- | --- |
| `kickMessage` | string | `getKickMessage()` | `java.lang.String` | `org.bukkit.event.player.AsyncPlayerPreLoginEvent` |
| `loginResult` | string | `getLoginResult()` | `org.bukkit.event.player.AsyncPlayerPreLoginEvent$Result` | `org.bukkit.event.player.AsyncPlayerPreLoginEvent` |
| `name` | string | `getName()` | `java.lang.String` | `org.bukkit.event.player.AsyncPlayerPreLoginEvent` |
| `result` | string | `getResult()` | `org.bukkit.event.player.PlayerPreLoginEvent$Result` | `org.bukkit.event.player.AsyncPlayerPreLoginEvent` |
| `uniqueId` | string | `getUniqueId()` | `java.util.UUID` | `org.bukkit.event.player.AsyncPlayerPreLoginEvent` |

[[Data-Format-en|Wire format and limits]] · [[Event-org-bukkit-event-player-asyncplayerpreloginevent|中文]]

If this event is not enabled, add its Java class or simple name to `events.include` in the Paper plugin configuration.
