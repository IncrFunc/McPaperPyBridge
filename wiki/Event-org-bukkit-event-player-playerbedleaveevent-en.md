# PlayerBedLeaveEvent

[[Home-en|Home]] / [[Category-player-en|player]]

- Java class: `org.bukkit.event.player.PlayerBedLeaveEvent`
- Parent class: `org.bukkit.event.player.PlayerEvent`
- Python subscription: `PlayerBedLeaveEvent`
- Python constant: `Events.PLAYER_BED_LEAVE`
- Cancellable: Yes
- Player available: Possible at runtime
- HandlerList owner: `org.bukkit.event.player.PlayerBedLeaveEvent`
- [Official Paper Javadoc](https://jd.papermc.io/paper/1.16.5/org/bukkit/event/player/PlayerBedLeaveEvent.html)

## Python example

```python
from paperpybridge import Events

@bridge.on(Events.PLAYER_BED_LEAVE)
def on_event(event):
    print(event.event, event.data)
```

## `data` fields

| Field | JSON type | Java getter | Java return type | Declared in |
| --- | --- | --- | --- | --- |
| `bed` | block summary | `getBed()` | `org.bukkit.block.Block` | `org.bukkit.event.player.PlayerBedLeaveEvent` |

[[Data-Format-en|Wire format and limits]] · [[Event-org-bukkit-event-player-playerbedleaveevent|中文]]

If this event is not enabled, add its Java class or simple name to `events.include` in the Paper plugin configuration.
