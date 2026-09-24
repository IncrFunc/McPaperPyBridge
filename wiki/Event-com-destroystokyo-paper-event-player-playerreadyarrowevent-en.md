# PlayerReadyArrowEvent

[[Home-en|Home]] / [[Category-player-en|player]]

- Java class: `com.destroystokyo.paper.event.player.PlayerReadyArrowEvent`
- Parent class: `org.bukkit.event.player.PlayerEvent`
- Python subscription: `PlayerReadyArrowEvent`
- Python constant: `Events.PLAYER_READY_ARROW`
- Cancellable: Yes
- Player available: Possible at runtime
- HandlerList owner: `com.destroystokyo.paper.event.player.PlayerReadyArrowEvent`
- [Official Paper Javadoc](https://jd.papermc.io/paper/1.16.5/com/destroystokyo/paper/event/player/PlayerReadyArrowEvent.html)

## Python example

```python
from paperpybridge import Events

@bridge.on(Events.PLAYER_READY_ARROW)
def on_event(event):
    print(event.event, event.data)
```

## `data` fields

| Field | JSON type | Java getter | Java return type | Declared in |
| --- | --- | --- | --- | --- |
| `arrow` | item summary | `getArrow()` | `org.bukkit.inventory.ItemStack` | `com.destroystokyo.paper.event.player.PlayerReadyArrowEvent` |
| `bow` | item summary | `getBow()` | `org.bukkit.inventory.ItemStack` | `com.destroystokyo.paper.event.player.PlayerReadyArrowEvent` |

[[Data-Format-en|Wire format and limits]] · [[Event-com-destroystokyo-paper-event-player-playerreadyarrowevent|中文]]

If this event is not enabled, add its Java class or simple name to `events.include` in the Paper plugin configuration.
