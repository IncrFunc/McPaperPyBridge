# PlayerSignCommandPreprocessEvent

[[Home-en|Home]] / [[Category-player-en|player]]

- Java class: `io.papermc.paper.event.player.PlayerSignCommandPreprocessEvent`
- Parent class: `org.bukkit.event.player.PlayerCommandPreprocessEvent`
- Python subscription: `PlayerSignCommandPreprocessEvent`
- Python constant: `Events.PLAYER_SIGN_COMMAND_PREPROCESS`
- Cancellable: Yes
- Player available: Possible at runtime
- HandlerList owner: `org.bukkit.event.player.PlayerCommandPreprocessEvent`
- [Official Paper Javadoc](https://jd.papermc.io/paper/1.16.5/io/papermc/paper/event/player/PlayerSignCommandPreprocessEvent.html)

## Python example

```python
from paperpybridge import Events

@bridge.on(Events.PLAYER_SIGN_COMMAND_PREPROCESS)
def on_event(event):
    print(event.event, event.data)
```

## `data` fields

| Field | JSON type | Java getter | Java return type | Declared in |
| --- | --- | --- | --- | --- |
| `message` | string | `getMessage()` | `java.lang.String` | `org.bukkit.event.player.PlayerCommandPreprocessEvent` |

[[Data-Format-en|Wire format and limits]] · [[Event-io-papermc-paper-event-player-playersigncommandpreprocessevent|中文]]

If this event is not enabled, add its Java class or simple name to `events.include` in the Paper plugin configuration.
