# PlayerPortalEvent

[[Home-en|Home]] / [[Category-player-en|player]]

- Java class: `org.bukkit.event.player.PlayerPortalEvent`
- Parent class: `org.bukkit.event.player.PlayerTeleportEvent`
- Python subscription: `PlayerPortalEvent`
- Python constant: `Events.PLAYER_PORTAL`
- Cancellable: Yes
- Player available: Possible at runtime
- HandlerList owner: `org.bukkit.event.player.PlayerPortalEvent`
- [Official Paper Javadoc](https://jd.papermc.io/paper/1.16.5/org/bukkit/event/player/PlayerPortalEvent.html)

## Python example

```python
from paperpybridge import Events

@bridge.on(Events.PLAYER_PORTAL)
def on_event(event):
    print(event.event, event.data)
```

## `data` fields

| Field | JSON type | Java getter | Java return type | Declared in |
| --- | --- | --- | --- | --- |
| `canCreatePortal` | boolean | `getCanCreatePortal()` | `boolean` | `org.bukkit.event.player.PlayerPortalEvent` |
| `cause` | string | `getCause()` | `org.bukkit.event.player.PlayerTeleportEvent$TeleportCause` | `org.bukkit.event.player.PlayerTeleportEvent` |
| `creationRadius` | number | `getCreationRadius()` | `int` | `org.bukkit.event.player.PlayerPortalEvent` |
| `from` | location summary | `getFrom()` | `org.bukkit.Location` | `org.bukkit.event.player.PlayerMoveEvent` |
| `searchRadius` | number | `getSearchRadius()` | `int` | `org.bukkit.event.player.PlayerPortalEvent` |
| `to` | location summary | `getTo()` | `org.bukkit.Location` | `org.bukkit.event.player.PlayerMoveEvent` |

[[Data-Format-en|Wire format and limits]] · [[Event-org-bukkit-event-player-playerportalevent|中文]]

If this event is not enabled, add its Java class or simple name to `events.include` in the Paper plugin configuration.
