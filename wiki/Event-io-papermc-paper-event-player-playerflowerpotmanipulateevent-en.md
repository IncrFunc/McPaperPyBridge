# PlayerFlowerPotManipulateEvent

[[Home-en|Home]] / [[Category-player-en|player]]

- Java class: `io.papermc.paper.event.player.PlayerFlowerPotManipulateEvent`
- Parent class: `org.bukkit.event.player.PlayerEvent`
- Python subscription: `PlayerFlowerPotManipulateEvent`
- Python constant: `Events.PLAYER_FLOWER_POT_MANIPULATE`
- Cancellable: Yes
- Player available: Possible at runtime
- HandlerList owner: `io.papermc.paper.event.player.PlayerFlowerPotManipulateEvent`
- [Official Paper Javadoc](https://jd.papermc.io/paper/1.16.5/io/papermc/paper/event/player/PlayerFlowerPotManipulateEvent.html)

## Python example

```python
from paperpybridge import Events

@bridge.on(Events.PLAYER_FLOWER_POT_MANIPULATE)
def on_event(event):
    print(event.event, event.data)
```

## `data` fields

| Field | JSON type | Java getter | Java return type | Declared in |
| --- | --- | --- | --- | --- |
| `flowerpot` | block summary | `getFlowerpot()` | `org.bukkit.block.Block` | `io.papermc.paper.event.player.PlayerFlowerPotManipulateEvent` |
| `item` | item summary | `getItem()` | `org.bukkit.inventory.ItemStack` | `io.papermc.paper.event.player.PlayerFlowerPotManipulateEvent` |
| `placing` | boolean | `isPlacing()` | `boolean` | `io.papermc.paper.event.player.PlayerFlowerPotManipulateEvent` |

[[Data-Format-en|Wire format and limits]] · [[Event-io-papermc-paper-event-player-playerflowerpotmanipulateevent|中文]]

If this event is not enabled, add its Java class or simple name to `events.include` in the Paper plugin configuration.
