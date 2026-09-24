# PlayerToggleSprintEvent

[[Home-en|Home]] / [[Category-player-en|player]]

- Java class: `org.bukkit.event.player.PlayerToggleSprintEvent`
- Parent class: `org.bukkit.event.player.PlayerEvent`
- Python subscription: `PlayerToggleSprintEvent`
- Python constant: `Events.PLAYER_TOGGLE_SPRINT`
- Cancellable: Yes
- Player available: Possible at runtime
- HandlerList owner: `org.bukkit.event.player.PlayerToggleSprintEvent`
- [Official Paper Javadoc](https://jd.papermc.io/paper/1.16.5/org/bukkit/event/player/PlayerToggleSprintEvent.html)

## Python example

```python
from paperpybridge import Events

@bridge.on(Events.PLAYER_TOGGLE_SPRINT)
def on_event(event):
    print(event.event, event.data)
```

## `data` fields

| Field | JSON type | Java getter | Java return type | Declared in |
| --- | --- | --- | --- | --- |
| `sprinting` | boolean | `isSprinting()` | `boolean` | `org.bukkit.event.player.PlayerToggleSprintEvent` |

[[Data-Format-en|Wire format and limits]] · [[Event-org-bukkit-event-player-playertogglesprintevent|中文]]

If this event is not enabled, add its Java class or simple name to `events.include` in the Paper plugin configuration.
