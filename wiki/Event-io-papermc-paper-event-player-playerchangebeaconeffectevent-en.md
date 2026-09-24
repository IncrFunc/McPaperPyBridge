# PlayerChangeBeaconEffectEvent

[[Home-en|Home]] / [[Category-player-en|player]]

- Java class: `io.papermc.paper.event.player.PlayerChangeBeaconEffectEvent`
- Parent class: `org.bukkit.event.player.PlayerEvent`
- Python subscription: `PlayerChangeBeaconEffectEvent`
- Python constant: `Events.PLAYER_CHANGE_BEACON_EFFECT`
- Cancellable: Yes
- Player available: Possible at runtime
- HandlerList owner: `io.papermc.paper.event.player.PlayerChangeBeaconEffectEvent`
- [Official Paper Javadoc](https://jd.papermc.io/paper/1.16.5/io/papermc/paper/event/player/PlayerChangeBeaconEffectEvent.html)

## Python example

```python
from paperpybridge import Events

@bridge.on(Events.PLAYER_CHANGE_BEACON_EFFECT)
def on_event(event):
    print(event.event, event.data)
```

## `data` fields

| Field | JSON type | Java getter | Java return type | Declared in |
| --- | --- | --- | --- | --- |
| `beacon` | block summary | `getBeacon()` | `org.bukkit.block.Block` | `io.papermc.paper.event.player.PlayerChangeBeaconEffectEvent` |

[[Data-Format-en|Wire format and limits]] · [[Event-io-papermc-paper-event-player-playerchangebeaconeffectevent|中文]]

If this event is not enabled, add its Java class or simple name to `events.include` in the Paper plugin configuration.
