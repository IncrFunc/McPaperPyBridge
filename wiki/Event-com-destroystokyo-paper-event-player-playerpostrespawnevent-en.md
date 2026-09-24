# PlayerPostRespawnEvent

[[Home-en|Home]] / [[Category-player-en|player]]

- Java class: `com.destroystokyo.paper.event.player.PlayerPostRespawnEvent`
- Parent class: `org.bukkit.event.player.PlayerEvent`
- Python subscription: `PlayerPostRespawnEvent`
- Python constant: `Events.PLAYER_POST_RESPAWN`
- Cancellable: No
- Player available: Possible at runtime
- HandlerList owner: `com.destroystokyo.paper.event.player.PlayerPostRespawnEvent`
- [Official Paper Javadoc](https://jd.papermc.io/paper/1.16.5/com/destroystokyo/paper/event/player/PlayerPostRespawnEvent.html)

## Python example

```python
from paperpybridge import Events

@bridge.on(Events.PLAYER_POST_RESPAWN)
def on_event(event):
    print(event.event, event.data)
```

## `data` fields

| Field | JSON type | Java getter | Java return type | Declared in |
| --- | --- | --- | --- | --- |
| `respawnedLocation` | location summary | `getRespawnedLocation()` | `org.bukkit.Location` | `com.destroystokyo.paper.event.player.PlayerPostRespawnEvent` |
| `bedSpawn` | boolean | `isBedSpawn()` | `boolean` | `com.destroystokyo.paper.event.player.PlayerPostRespawnEvent` |

[[Data-Format-en|Wire format and limits]] · [[Event-com-destroystokyo-paper-event-player-playerpostrespawnevent|中文]]

If this event is not enabled, add its Java class or simple name to `events.include` in the Paper plugin configuration.
