# PlayerPickupArrowEvent

[[Home-en|Home]] / [[Category-player-en|player]]

- Java class: `org.bukkit.event.player.PlayerPickupArrowEvent`
- Parent class: `org.bukkit.event.player.PlayerPickupItemEvent`
- Python subscription: `PlayerPickupArrowEvent`
- Python constant: `Events.PLAYER_PICKUP_ARROW`
- Cancellable: Yes
- Player available: Possible at runtime
- HandlerList owner: `org.bukkit.event.player.PlayerPickupItemEvent`
- [Official Paper Javadoc](https://jd.papermc.io/paper/1.16.5/org/bukkit/event/player/PlayerPickupArrowEvent.html)

## Python example

```python
from paperpybridge import Events

@bridge.on(Events.PLAYER_PICKUP_ARROW)
def on_event(event):
    print(event.event, event.data)
```

## `data` fields

| Field | JSON type | Java getter | Java return type | Declared in |
| --- | --- | --- | --- | --- |
| `arrow` | entity summary | `getArrow()` | `org.bukkit.entity.AbstractArrow` | `org.bukkit.event.player.PlayerPickupArrowEvent` |
| `flyAtPlayer` | boolean | `getFlyAtPlayer()` | `boolean` | `org.bukkit.event.player.PlayerPickupItemEvent` |
| `item` | entity summary | `getItem()` | `org.bukkit.entity.Item` | `org.bukkit.event.player.PlayerPickupItemEvent` |
| `remaining` | number | `getRemaining()` | `int` | `org.bukkit.event.player.PlayerPickupItemEvent` |

[[Data-Format-en|Wire format and limits]] · [[Event-org-bukkit-event-player-playerpickuparrowevent|中文]]

If this event is not enabled, add its Java class or simple name to `events.include` in the Paper plugin configuration.
