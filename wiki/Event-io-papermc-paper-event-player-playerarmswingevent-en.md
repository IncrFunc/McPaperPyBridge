# PlayerArmSwingEvent

[[Home-en|Home]] / [[Category-player-en|player]]

- Java class: `io.papermc.paper.event.player.PlayerArmSwingEvent`
- Parent class: `org.bukkit.event.player.PlayerAnimationEvent`
- Python subscription: `PlayerArmSwingEvent`
- Python constant: `Events.PLAYER_ARM_SWING`
- Cancellable: Yes
- Player available: Possible at runtime
- HandlerList owner: `org.bukkit.event.player.PlayerAnimationEvent`
- [Official Paper Javadoc](https://jd.papermc.io/paper/1.16.5/io/papermc/paper/event/player/PlayerArmSwingEvent.html)

## Python example

```python
from paperpybridge import Events

@bridge.on(Events.PLAYER_ARM_SWING)
def on_event(event):
    print(event.event, event.data)
```

## `data` fields

| Field | JSON type | Java getter | Java return type | Declared in |
| --- | --- | --- | --- | --- |
| `animationType` | string | `getAnimationType()` | `org.bukkit.event.player.PlayerAnimationType` | `org.bukkit.event.player.PlayerAnimationEvent` |
| `hand` | string | `getHand()` | `org.bukkit.inventory.EquipmentSlot` | `io.papermc.paper.event.player.PlayerArmSwingEvent` |

[[Data-Format-en|Wire format and limits]] · [[Event-io-papermc-paper-event-player-playerarmswingevent|中文]]

If this event is not enabled, add its Java class or simple name to `events.include` in the Paper plugin configuration.
