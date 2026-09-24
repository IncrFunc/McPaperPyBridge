# PlayerAttemptPickupItemEvent

[[Home-en|Home]] / [[Category-player-en|player]]

- Java class: `org.bukkit.event.player.PlayerAttemptPickupItemEvent`
- Parent class: `org.bukkit.event.player.PlayerEvent`
- Python subscription: `PlayerAttemptPickupItemEvent`
- Python constant: `Events.PLAYER_ATTEMPT_PICKUP_ITEM`
- Cancellable: Yes
- Player available: Possible at runtime
- HandlerList owner: `org.bukkit.event.player.PlayerAttemptPickupItemEvent`
- [Official Paper Javadoc](https://jd.papermc.io/paper/1.16.5/org/bukkit/event/player/PlayerAttemptPickupItemEvent.html)

## Python example

```python
from paperpybridge import Events

@bridge.on(Events.PLAYER_ATTEMPT_PICKUP_ITEM)
def on_event(event):
    print(event.event, event.data)
```

## `data` fields

| Field | JSON type | Java getter | Java return type | Declared in |
| --- | --- | --- | --- | --- |
| `flyAtPlayer` | boolean | `getFlyAtPlayer()` | `boolean` | `org.bukkit.event.player.PlayerAttemptPickupItemEvent` |
| `item` | entity summary | `getItem()` | `org.bukkit.entity.Item` | `org.bukkit.event.player.PlayerAttemptPickupItemEvent` |
| `remaining` | number | `getRemaining()` | `int` | `org.bukkit.event.player.PlayerAttemptPickupItemEvent` |

[[Data-Format-en|Wire format and limits]] · [[Event-org-bukkit-event-player-playerattemptpickupitemevent|中文]]

If this event is not enabled, add its Java class or simple name to `events.include` in the Paper plugin configuration.
