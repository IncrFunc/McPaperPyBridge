# PlayerTeleportEndGatewayEvent

[[Home-en|Home]] / [[Category-player-en|player]]

- Java class: `com.destroystokyo.paper.event.player.PlayerTeleportEndGatewayEvent`
- Parent class: `org.bukkit.event.player.PlayerTeleportEvent`
- Python subscription: `PlayerTeleportEndGatewayEvent`
- Python constant: `Events.PLAYER_TELEPORT_END_GATEWAY`
- Cancellable: Yes
- Player available: Possible at runtime
- HandlerList owner: `org.bukkit.event.player.PlayerTeleportEvent`
- [Official Paper Javadoc](https://jd.papermc.io/paper/1.16.5/com/destroystokyo/paper/event/player/PlayerTeleportEndGatewayEvent.html)

## Python example

```python
from paperpybridge import Events

@bridge.on(Events.PLAYER_TELEPORT_END_GATEWAY)
def on_event(event):
    print(event.event, event.data)
```

## `data` fields

| Field | JSON type | Java getter | Java return type | Declared in |
| --- | --- | --- | --- | --- |
| `cause` | string | `getCause()` | `org.bukkit.event.player.PlayerTeleportEvent$TeleportCause` | `org.bukkit.event.player.PlayerTeleportEvent` |
| `from` | location summary | `getFrom()` | `org.bukkit.Location` | `org.bukkit.event.player.PlayerMoveEvent` |
| `to` | location summary | `getTo()` | `org.bukkit.Location` | `org.bukkit.event.player.PlayerMoveEvent` |

[[Data-Format-en|Wire format and limits]] · [[Event-com-destroystokyo-paper-event-player-playerteleportendgatewayevent|中文]]

If this event is not enabled, add its Java class or simple name to `events.include` in the Paper plugin configuration.
