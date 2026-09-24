# PlayerUseUnknownEntityEvent

[[Home-en|Home]] / [[Category-player-en|player]]

- Java class: `com.destroystokyo.paper.event.player.PlayerUseUnknownEntityEvent`
- Parent class: `org.bukkit.event.player.PlayerEvent`
- Python subscription: `PlayerUseUnknownEntityEvent`
- Python constant: `Events.PLAYER_USE_UNKNOWN_ENTITY`
- Cancellable: No
- Player available: Possible at runtime
- HandlerList owner: `com.destroystokyo.paper.event.player.PlayerUseUnknownEntityEvent`
- [Official Paper Javadoc](https://jd.papermc.io/paper/1.16.5/com/destroystokyo/paper/event/player/PlayerUseUnknownEntityEvent.html)

## Python example

```python
from paperpybridge import Events

@bridge.on(Events.PLAYER_USE_UNKNOWN_ENTITY)
def on_event(event):
    print(event.event, event.data)
```

## `data` fields

| Field | JSON type | Java getter | Java return type | Declared in |
| --- | --- | --- | --- | --- |
| `entityId` | number | `getEntityId()` | `int` | `com.destroystokyo.paper.event.player.PlayerUseUnknownEntityEvent` |
| `hand` | string | `getHand()` | `org.bukkit.inventory.EquipmentSlot` | `com.destroystokyo.paper.event.player.PlayerUseUnknownEntityEvent` |
| `attack` | boolean | `isAttack()` | `boolean` | `com.destroystokyo.paper.event.player.PlayerUseUnknownEntityEvent` |

[[Data-Format-en|Wire format and limits]] · [[Event-com-destroystokyo-paper-event-player-playeruseunknownentityevent|中文]]

If this event is not enabled, add its Java class or simple name to `events.include` in the Paper plugin configuration.
