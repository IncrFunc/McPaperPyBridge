# PlayerResourcePackStatusEvent

[[Home-en|Home]] / [[Category-player-en|player]]

- Java class: `org.bukkit.event.player.PlayerResourcePackStatusEvent`
- Parent class: `org.bukkit.event.player.PlayerEvent`
- Python subscription: `PlayerResourcePackStatusEvent`
- Python constant: `Events.PLAYER_RESOURCE_PACK_STATUS`
- Cancellable: No
- Player available: Possible at runtime
- HandlerList owner: `org.bukkit.event.player.PlayerResourcePackStatusEvent`
- [Official Paper Javadoc](https://jd.papermc.io/paper/1.16.5/org/bukkit/event/player/PlayerResourcePackStatusEvent.html)

## Python example

```python
from paperpybridge import Events

@bridge.on(Events.PLAYER_RESOURCE_PACK_STATUS)
def on_event(event):
    print(event.event, event.data)
```

## `data` fields

| Field | JSON type | Java getter | Java return type | Declared in |
| --- | --- | --- | --- | --- |
| `hash` | string | `getHash()` | `java.lang.String` | `org.bukkit.event.player.PlayerResourcePackStatusEvent` |
| `status` | string | `getStatus()` | `org.bukkit.event.player.PlayerResourcePackStatusEvent$Status` | `org.bukkit.event.player.PlayerResourcePackStatusEvent` |

[[Data-Format-en|Wire format and limits]] · [[Event-org-bukkit-event-player-playerresourcepackstatusevent|中文]]

If this event is not enabled, add its Java class or simple name to `events.include` in the Paper plugin configuration.
