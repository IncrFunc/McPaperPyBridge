# PlayerUnregisterChannelEvent

[[Home-en|Home]] / [[Category-player-en|player]]

- Java class: `org.bukkit.event.player.PlayerUnregisterChannelEvent`
- Parent class: `org.bukkit.event.player.PlayerChannelEvent`
- Python subscription: `PlayerUnregisterChannelEvent`
- Python constant: `Events.PLAYER_UNREGISTER_CHANNEL`
- Cancellable: No
- Player available: Possible at runtime
- HandlerList owner: `org.bukkit.event.player.PlayerChannelEvent`
- [Official Paper Javadoc](https://jd.papermc.io/paper/1.16.5/org/bukkit/event/player/PlayerUnregisterChannelEvent.html)

## Python example

```python
from paperpybridge import Events

@bridge.on(Events.PLAYER_UNREGISTER_CHANNEL)
def on_event(event):
    print(event.event, event.data)
```

## `data` fields

| Field | JSON type | Java getter | Java return type | Declared in |
| --- | --- | --- | --- | --- |
| `channel` | string | `getChannel()` | `java.lang.String` | `org.bukkit.event.player.PlayerChannelEvent` |

[[Data-Format-en|Wire format and limits]] · [[Event-org-bukkit-event-player-playerunregisterchannelevent|中文]]

If this event is not enabled, add its Java class or simple name to `events.include` in the Paper plugin configuration.
