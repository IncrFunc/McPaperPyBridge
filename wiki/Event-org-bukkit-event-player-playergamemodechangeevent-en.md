# PlayerGameModeChangeEvent

[[Home-en|Home]] / [[Category-player-en|player]]

- Java class: `org.bukkit.event.player.PlayerGameModeChangeEvent`
- Parent class: `org.bukkit.event.player.PlayerEvent`
- Python subscription: `PlayerGameModeChangeEvent`
- Python constant: `Events.PLAYER_GAME_MODE_CHANGE`
- Cancellable: Yes
- Player available: Possible at runtime
- HandlerList owner: `org.bukkit.event.player.PlayerGameModeChangeEvent`
- [Official Paper Javadoc](https://jd.papermc.io/paper/1.16.5/org/bukkit/event/player/PlayerGameModeChangeEvent.html)

## Python example

```python
from paperpybridge import Events

@bridge.on(Events.PLAYER_GAME_MODE_CHANGE)
def on_event(event):
    print(event.event, event.data)
```

## `data` fields

| Field | JSON type | Java getter | Java return type | Declared in |
| --- | --- | --- | --- | --- |
| `cause` | string | `getCause()` | `org.bukkit.event.player.PlayerGameModeChangeEvent$Cause` | `org.bukkit.event.player.PlayerGameModeChangeEvent` |
| `newGameMode` | string | `getNewGameMode()` | `org.bukkit.GameMode` | `org.bukkit.event.player.PlayerGameModeChangeEvent` |

[[Data-Format-en|Wire format and limits]] · [[Event-org-bukkit-event-player-playergamemodechangeevent|中文]]

If this event is not enabled, add its Java class or simple name to `events.include` in the Paper plugin configuration.
