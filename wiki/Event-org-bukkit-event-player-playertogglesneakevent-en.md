# PlayerToggleSneakEvent

[[Home-en|Home]] / [[Category-player-en|player]]

- Java class: `org.bukkit.event.player.PlayerToggleSneakEvent`
- Parent class: `org.bukkit.event.player.PlayerEvent`
- Python subscription: `PlayerToggleSneakEvent`
- Python constant: `Events.PLAYER_TOGGLE_SNEAK`
- Cancellable: Yes
- Player available: Possible at runtime
- HandlerList owner: `org.bukkit.event.player.PlayerToggleSneakEvent`
- [Official Paper Javadoc](https://jd.papermc.io/paper/1.16.5/org/bukkit/event/player/PlayerToggleSneakEvent.html)

## Python example

```python
from paperpybridge import Events

@bridge.on(Events.PLAYER_TOGGLE_SNEAK)
def on_event(event):
    print(event.event, event.data)
```

## `data` fields

| Field | JSON type | Java getter | Java return type | Declared in |
| --- | --- | --- | --- | --- |
| `sneaking` | boolean | `isSneaking()` | `boolean` | `org.bukkit.event.player.PlayerToggleSneakEvent` |

[[Data-Format-en|Wire format and limits]] · [[Event-org-bukkit-event-player-playertogglesneakevent|中文]]

If this event is not enabled, add its Java class or simple name to `events.include` in the Paper plugin configuration.
