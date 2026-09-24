# PlayerChatEvent

[[Home-en|Home]] / [[Category-player-en|player]]

- Java class: `org.bukkit.event.player.PlayerChatEvent`
- Parent class: `org.bukkit.event.player.PlayerEvent`
- Python subscription: `PlayerChatEvent`
- Python constant: `Events.PLAYER_CHAT`
- Cancellable: Yes
- Player available: Possible at runtime
- HandlerList owner: `org.bukkit.event.player.PlayerChatEvent`
- [Official Paper Javadoc](https://jd.papermc.io/paper/1.16.5/org/bukkit/event/player/PlayerChatEvent.html)

## Python example

```python
from paperpybridge import Events

@bridge.on(Events.PLAYER_CHAT)
def on_event(event):
    print(event.event, event.data)
```

## `data` fields

| Field | JSON type | Java getter | Java return type | Declared in |
| --- | --- | --- | --- | --- |
| `format` | string | `getFormat()` | `java.lang.String` | `org.bukkit.event.player.PlayerChatEvent` |
| `message` | string | `getMessage()` | `java.lang.String` | `org.bukkit.event.player.PlayerChatEvent` |

[[Data-Format-en|Wire format and limits]] · [[Event-org-bukkit-event-player-playerchatevent|中文]]

If this event is not enabled, add its Java class or simple name to `events.include` in the Paper plugin configuration.
