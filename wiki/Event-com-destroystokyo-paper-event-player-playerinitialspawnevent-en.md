# PlayerInitialSpawnEvent

[[Home-en|Home]] / [[Category-player-en|player]]

- Java class: `com.destroystokyo.paper.event.player.PlayerInitialSpawnEvent`
- Parent class: `org.spigotmc.event.player.PlayerSpawnLocationEvent`
- Python subscription: `PlayerInitialSpawnEvent`
- Python constant: `Events.PLAYER_INITIAL_SPAWN`
- Cancellable: No
- Player available: Possible at runtime
- HandlerList owner: `org.spigotmc.event.player.PlayerSpawnLocationEvent`
- [Official Paper Javadoc](https://jd.papermc.io/paper/1.16.5/com/destroystokyo/paper/event/player/PlayerInitialSpawnEvent.html)

## Python example

```python
from paperpybridge import Events

@bridge.on(Events.PLAYER_INITIAL_SPAWN)
def on_event(event):
    print(event.event, event.data)
```

## `data` fields

| Field | JSON type | Java getter | Java return type | Declared in |
| --- | --- | --- | --- | --- |
| `spawnLocation` | location summary | `getSpawnLocation()` | `org.bukkit.Location` | `org.spigotmc.event.player.PlayerSpawnLocationEvent` |

[[Data-Format-en|Wire format and limits]] · [[Event-com-destroystokyo-paper-event-player-playerinitialspawnevent|中文]]

If this event is not enabled, add its Java class or simple name to `events.include` in the Paper plugin configuration.
