# PlayerFishEvent

[[Home-en|Home]] / [[Category-player-en|player]]

- Java class: `org.bukkit.event.player.PlayerFishEvent`
- Parent class: `org.bukkit.event.player.PlayerEvent`
- Python subscription: `PlayerFishEvent`
- Python constant: `Events.PLAYER_FISH`
- Cancellable: Yes
- Player available: Possible at runtime
- HandlerList owner: `org.bukkit.event.player.PlayerFishEvent`
- [Official Paper Javadoc](https://jd.papermc.io/paper/1.16.5/org/bukkit/event/player/PlayerFishEvent.html)

## Python example

```python
from paperpybridge import Events

@bridge.on(Events.PLAYER_FISH)
def on_event(event):
    print(event.event, event.data)
```

## `data` fields

| Field | JSON type | Java getter | Java return type | Declared in |
| --- | --- | --- | --- | --- |
| `caught` | entity summary | `getCaught()` | `org.bukkit.entity.Entity` | `org.bukkit.event.player.PlayerFishEvent` |
| `expToDrop` | number | `getExpToDrop()` | `int` | `org.bukkit.event.player.PlayerFishEvent` |
| `hook` | entity summary | `getHook()` | `org.bukkit.entity.FishHook` | `org.bukkit.event.player.PlayerFishEvent` |
| `state` | string | `getState()` | `org.bukkit.event.player.PlayerFishEvent$State` | `org.bukkit.event.player.PlayerFishEvent` |

[[Data-Format-en|Wire format and limits]] · [[Event-org-bukkit-event-player-playerfishevent|中文]]

If this event is not enabled, add its Java class or simple name to `events.include` in the Paper plugin configuration.
