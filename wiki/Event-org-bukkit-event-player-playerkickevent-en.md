# PlayerKickEvent

[[Home-en|Home]] / [[Category-player-en|player]]

- Java class: `org.bukkit.event.player.PlayerKickEvent`
- Parent class: `org.bukkit.event.player.PlayerEvent`
- Python subscription: `PlayerKickEvent`
- Python constant: `Events.PLAYER_KICK`
- Cancellable: Yes
- Player available: Possible at runtime
- HandlerList owner: `org.bukkit.event.player.PlayerKickEvent`
- [Official Paper Javadoc](https://jd.papermc.io/paper/1.16.5/org/bukkit/event/player/PlayerKickEvent.html)

## Python example

```python
from paperpybridge import Events

@bridge.on(Events.PLAYER_KICK)
def on_event(event):
    print(event.event, event.data)
```

## `data` fields

| Field | JSON type | Java getter | Java return type | Declared in |
| --- | --- | --- | --- | --- |
| `cause` | string | `getCause()` | `org.bukkit.event.player.PlayerKickEvent$Cause` | `org.bukkit.event.player.PlayerKickEvent` |
| `leaveMessage` | string | `getLeaveMessage()` | `java.lang.String` | `org.bukkit.event.player.PlayerKickEvent` |
| `reason` | string | `getReason()` | `java.lang.String` | `org.bukkit.event.player.PlayerKickEvent` |

[[Data-Format-en|Wire format and limits]] · [[Event-org-bukkit-event-player-playerkickevent|中文]]

If this event is not enabled, add its Java class or simple name to `events.include` in the Paper plugin configuration.
