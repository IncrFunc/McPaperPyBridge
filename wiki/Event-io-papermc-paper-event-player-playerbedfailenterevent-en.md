# PlayerBedFailEnterEvent

[[Home-en|Home]] / [[Category-player-en|player]]

- Java class: `io.papermc.paper.event.player.PlayerBedFailEnterEvent`
- Parent class: `org.bukkit.event.player.PlayerEvent`
- Python subscription: `PlayerBedFailEnterEvent`
- Python constant: `Events.PLAYER_BED_FAIL_ENTER`
- Cancellable: Yes
- Player available: Possible at runtime
- HandlerList owner: `io.papermc.paper.event.player.PlayerBedFailEnterEvent`
- [Official Paper Javadoc](https://jd.papermc.io/paper/1.16.5/io/papermc/paper/event/player/PlayerBedFailEnterEvent.html)

## Python example

```python
from paperpybridge import Events

@bridge.on(Events.PLAYER_BED_FAIL_ENTER)
def on_event(event):
    print(event.event, event.data)
```

## `data` fields

| Field | JSON type | Java getter | Java return type | Declared in |
| --- | --- | --- | --- | --- |
| `bed` | block summary | `getBed()` | `org.bukkit.block.Block` | `io.papermc.paper.event.player.PlayerBedFailEnterEvent` |
| `failReason` | string | `getFailReason()` | `io.papermc.paper.event.player.PlayerBedFailEnterEvent$FailReason` | `io.papermc.paper.event.player.PlayerBedFailEnterEvent` |
| `willExplode` | boolean | `getWillExplode()` | `boolean` | `io.papermc.paper.event.player.PlayerBedFailEnterEvent` |

[[Data-Format-en|Wire format and limits]] · [[Event-io-papermc-paper-event-player-playerbedfailenterevent|中文]]

If this event is not enabled, add its Java class or simple name to `events.include` in the Paper plugin configuration.
