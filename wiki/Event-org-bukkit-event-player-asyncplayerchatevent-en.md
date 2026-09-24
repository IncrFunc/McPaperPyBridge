# AsyncPlayerChatEvent

[[Home-en|Home]] / [[Category-player-en|player]]

- Java class: `org.bukkit.event.player.AsyncPlayerChatEvent`
- Parent class: `org.bukkit.event.player.PlayerEvent`
- Python subscription: `chat`
- Python constant: `Events.ASYNC_PLAYER_CHAT`
- Cancellable: Yes
- Player available: Possible at runtime
- HandlerList owner: `org.bukkit.event.player.AsyncPlayerChatEvent`
- [Official Paper Javadoc](https://jd.papermc.io/paper/1.16.5/org/bukkit/event/player/AsyncPlayerChatEvent.html)

## Python example

```python
from paperpybridge import Events

@bridge.on(Events.ASYNC_PLAYER_CHAT)
def on_event(event):
    print(event.event, event.data)
```

## `data` fields

| Field | JSON type | Java getter | Java return type | Declared in |
| --- | --- | --- | --- | --- |
| `format` | string | `getFormat()` | `java.lang.String` | `org.bukkit.event.player.AsyncPlayerChatEvent` |
| `message` | string | `getMessage()` | `java.lang.String` | `org.bukkit.event.player.AsyncPlayerChatEvent` |

[[Data-Format-en|Wire format and limits]] · [[Event-org-bukkit-event-player-asyncplayerchatevent|中文]]

If this event is not enabled, add its Java class or simple name to `events.include` in the Paper plugin configuration.
