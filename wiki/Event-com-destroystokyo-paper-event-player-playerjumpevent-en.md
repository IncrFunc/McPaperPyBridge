# PlayerJumpEvent

[[Home-en|Home]] / [[Category-player-en|player]]

- Java class: `com.destroystokyo.paper.event.player.PlayerJumpEvent`
- Parent class: `org.bukkit.event.player.PlayerEvent`
- Python subscription: `PlayerJumpEvent`
- Python constant: `Events.PLAYER_JUMP`
- Cancellable: Yes
- Player available: Possible at runtime
- HandlerList owner: `com.destroystokyo.paper.event.player.PlayerJumpEvent`
- [Official Paper Javadoc](https://jd.papermc.io/paper/1.16.5/com/destroystokyo/paper/event/player/PlayerJumpEvent.html)

## Python example

```python
from paperpybridge import Events

@bridge.on(Events.PLAYER_JUMP)
def on_event(event):
    print(event.event, event.data)
```

## `data` fields

| Field | JSON type | Java getter | Java return type | Declared in |
| --- | --- | --- | --- | --- |
| `from` | location summary | `getFrom()` | `org.bukkit.Location` | `com.destroystokyo.paper.event.player.PlayerJumpEvent` |
| `to` | location summary | `getTo()` | `org.bukkit.Location` | `com.destroystokyo.paper.event.player.PlayerJumpEvent` |

[[Data-Format-en|Wire format and limits]] · [[Event-com-destroystokyo-paper-event-player-playerjumpevent|中文]]

If this event is not enabled, add its Java class or simple name to `events.include` in the Paper plugin configuration.
