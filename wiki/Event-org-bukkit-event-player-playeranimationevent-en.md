# PlayerAnimationEvent

[[Home-en|Home]] / [[Category-player-en|player]]

- Java class: `org.bukkit.event.player.PlayerAnimationEvent`
- Parent class: `org.bukkit.event.player.PlayerEvent`
- Python subscription: `PlayerAnimationEvent`
- Python constant: `Events.PLAYER_ANIMATION`
- Cancellable: Yes
- Player available: Possible at runtime
- HandlerList owner: `org.bukkit.event.player.PlayerAnimationEvent`
- [Official Paper Javadoc](https://jd.papermc.io/paper/1.16.5/org/bukkit/event/player/PlayerAnimationEvent.html)

## Python example

```python
from paperpybridge import Events

@bridge.on(Events.PLAYER_ANIMATION)
def on_event(event):
    print(event.event, event.data)
```

## `data` fields

| Field | JSON type | Java getter | Java return type | Declared in |
| --- | --- | --- | --- | --- |
| `animationType` | string | `getAnimationType()` | `org.bukkit.event.player.PlayerAnimationType` | `org.bukkit.event.player.PlayerAnimationEvent` |

[[Data-Format-en|Wire format and limits]] · [[Event-org-bukkit-event-player-playeranimationevent|中文]]

If this event is not enabled, add its Java class or simple name to `events.include` in the Paper plugin configuration.
