# PlayerChangedWorldEvent

[[Home-en|Home]] / [[Category-player-en|player]]

- Java class: `org.bukkit.event.player.PlayerChangedWorldEvent`
- Parent class: `org.bukkit.event.player.PlayerEvent`
- Python subscription: `PlayerChangedWorldEvent`
- Python constant: `Events.PLAYER_CHANGED_WORLD`
- Cancellable: No
- Player available: Possible at runtime
- HandlerList owner: `org.bukkit.event.player.PlayerChangedWorldEvent`
- [Official Paper Javadoc](https://jd.papermc.io/paper/1.16.5/org/bukkit/event/player/PlayerChangedWorldEvent.html)

## Python example

```python
from paperpybridge import Events

@bridge.on(Events.PLAYER_CHANGED_WORLD)
def on_event(event):
    print(event.event, event.data)
```

## `data` fields

| Field | JSON type | Java getter | Java return type | Declared in |
| --- | --- | --- | --- | --- |
| `from` | world summary | `getFrom()` | `org.bukkit.World` | `org.bukkit.event.player.PlayerChangedWorldEvent` |

[[Data-Format-en|Wire format and limits]] · [[Event-org-bukkit-event-player-playerchangedworldevent|中文]]

If this event is not enabled, add its Java class or simple name to `events.include` in the Paper plugin configuration.
