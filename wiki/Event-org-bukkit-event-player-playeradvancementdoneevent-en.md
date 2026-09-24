# PlayerAdvancementDoneEvent

[[Home-en|Home]] / [[Category-player-en|player]]

- Java class: `org.bukkit.event.player.PlayerAdvancementDoneEvent`
- Parent class: `org.bukkit.event.player.PlayerEvent`
- Python subscription: `PlayerAdvancementDoneEvent`
- Python constant: `Events.PLAYER_ADVANCEMENT_DONE`
- Cancellable: No
- Player available: Possible at runtime
- HandlerList owner: `org.bukkit.event.player.PlayerAdvancementDoneEvent`
- [Official Paper Javadoc](https://jd.papermc.io/paper/1.16.5/org/bukkit/event/player/PlayerAdvancementDoneEvent.html)

## Python example

```python
from paperpybridge import Events

@bridge.on(Events.PLAYER_ADVANCEMENT_DONE)
def on_event(event):
    print(event.event, event.data)
```

## `data` fields

No supported serializable fields; common event fields are still sent.

[[Data-Format-en|Wire format and limits]] · [[Event-org-bukkit-event-player-playeradvancementdoneevent|中文]]

If this event is not enabled, add its Java class or simple name to `events.include` in the Paper plugin configuration.
