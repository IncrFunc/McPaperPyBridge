# PlayerHarvestBlockEvent

[[Home-en|Home]] / [[Category-player-en|player]]

- Java class: `org.bukkit.event.player.PlayerHarvestBlockEvent`
- Parent class: `org.bukkit.event.player.PlayerEvent`
- Python subscription: `PlayerHarvestBlockEvent`
- Python constant: `Events.PLAYER_HARVEST_BLOCK`
- Cancellable: Yes
- Player available: Possible at runtime
- HandlerList owner: `org.bukkit.event.player.PlayerHarvestBlockEvent`
- [Official Paper Javadoc](https://jd.papermc.io/paper/1.16.5/org/bukkit/event/player/PlayerHarvestBlockEvent.html)

## Python example

```python
from paperpybridge import Events

@bridge.on(Events.PLAYER_HARVEST_BLOCK)
def on_event(event):
    print(event.event, event.data)
```

## `data` fields

| Field | JSON type | Java getter | Java return type | Declared in |
| --- | --- | --- | --- | --- |
| `harvestedBlock` | block summary | `getHarvestedBlock()` | `org.bukkit.block.Block` | `org.bukkit.event.player.PlayerHarvestBlockEvent` |

[[Data-Format-en|Wire format and limits]] · [[Event-org-bukkit-event-player-playerharvestblockevent|中文]]

If this event is not enabled, add its Java class or simple name to `events.include` in the Paper plugin configuration.
