# PlayerRespawnEvent

[[Home-en|Home]] / [[Category-player-en|player]]

- Java class: `org.bukkit.event.player.PlayerRespawnEvent`
- Parent class: `org.bukkit.event.player.PlayerEvent`
- Python subscription: `PlayerRespawnEvent`
- Python constant: `Events.PLAYER_RESPAWN`
- Cancellable: No
- Player available: Possible at runtime
- HandlerList owner: `org.bukkit.event.player.PlayerRespawnEvent`
- [Official Paper Javadoc](https://jd.papermc.io/paper/1.16.5/org/bukkit/event/player/PlayerRespawnEvent.html)

## Python example

```python
from paperpybridge import Events

@bridge.on(Events.PLAYER_RESPAWN)
def on_event(event):
    print(event.event, event.data)
```

## `data` fields

| Field | JSON type | Java getter | Java return type | Declared in |
| --- | --- | --- | --- | --- |
| `respawnLocation` | location summary | `getRespawnLocation()` | `org.bukkit.Location` | `org.bukkit.event.player.PlayerRespawnEvent` |
| `anchorSpawn` | boolean | `isAnchorSpawn()` | `boolean` | `org.bukkit.event.player.PlayerRespawnEvent` |
| `bedSpawn` | boolean | `isBedSpawn()` | `boolean` | `org.bukkit.event.player.PlayerRespawnEvent` |

[[Data-Format-en|Wire format and limits]] · [[Event-org-bukkit-event-player-playerrespawnevent|中文]]

If this event is not enabled, add its Java class or simple name to `events.include` in the Paper plugin configuration.
