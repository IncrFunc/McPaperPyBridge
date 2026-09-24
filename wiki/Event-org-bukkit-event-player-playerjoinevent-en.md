# PlayerJoinEvent

[[Home-en|Home]] / [[Category-player-en|player]]

- Java class: `org.bukkit.event.player.PlayerJoinEvent`
- Parent class: `org.bukkit.event.player.PlayerEvent`
- Python subscription: `join`
- Python constant: `Events.PLAYER_JOIN`
- Cancellable: No
- Player available: Possible at runtime
- HandlerList owner: `org.bukkit.event.player.PlayerJoinEvent`
- [Official Paper Javadoc](https://jd.papermc.io/paper/1.16.5/org/bukkit/event/player/PlayerJoinEvent.html)

## Python example

```python
from paperpybridge import Events

@bridge.on(Events.PLAYER_JOIN)
def on_event(event):
    print(event.event, event.data)
```

## `data` fields

| Field | JSON type | Java getter | Java return type | Declared in |
| --- | --- | --- | --- | --- |
| `joinMessage` | string | `getJoinMessage()` | `java.lang.String` | `org.bukkit.event.player.PlayerJoinEvent` |

[[Data-Format-en|Wire format and limits]] · [[Event-org-bukkit-event-player-playerjoinevent|中文]]

If this event is not enabled, add its Java class or simple name to `events.include` in the Paper plugin configuration.
