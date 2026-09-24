# PlayerDeepSleepEvent

[[Home-en|Home]] / [[Category-player-en|player]]

- Java class: `io.papermc.paper.event.player.PlayerDeepSleepEvent`
- Parent class: `org.bukkit.event.player.PlayerEvent`
- Python subscription: `PlayerDeepSleepEvent`
- Python constant: `Events.PLAYER_DEEP_SLEEP`
- Cancellable: Yes
- Player available: Possible at runtime
- HandlerList owner: `io.papermc.paper.event.player.PlayerDeepSleepEvent`
- [Official Paper Javadoc](https://jd.papermc.io/paper/1.16.5/io/papermc/paper/event/player/PlayerDeepSleepEvent.html)

## Python example

```python
from paperpybridge import Events

@bridge.on(Events.PLAYER_DEEP_SLEEP)
def on_event(event):
    print(event.event, event.data)
```

## `data` fields

No supported serializable fields; common event fields are still sent.

[[Data-Format-en|Wire format and limits]] · [[Event-io-papermc-paper-event-player-playerdeepsleepevent|中文]]

If this event is not enabled, add its Java class or simple name to `events.include` in the Paper plugin configuration.
