# PlayerInteractAtEntityEvent

[[Home-en|Home]] / [[Category-player-en|player]]

- Java class: `org.bukkit.event.player.PlayerInteractAtEntityEvent`
- Parent class: `org.bukkit.event.player.PlayerInteractEntityEvent`
- Python subscription: `PlayerInteractAtEntityEvent`
- Python constant: `Events.PLAYER_INTERACT_AT_ENTITY`
- Cancellable: Yes
- Player available: Possible at runtime
- HandlerList owner: `org.bukkit.event.player.PlayerInteractAtEntityEvent`
- [Official Paper Javadoc](https://jd.papermc.io/paper/1.16.5/org/bukkit/event/player/PlayerInteractAtEntityEvent.html)

## Python example

```python
from paperpybridge import Events

@bridge.on(Events.PLAYER_INTERACT_AT_ENTITY)
def on_event(event):
    print(event.event, event.data)
```

## `data` fields

| Field | JSON type | Java getter | Java return type | Declared in |
| --- | --- | --- | --- | --- |
| `hand` | string | `getHand()` | `org.bukkit.inventory.EquipmentSlot` | `org.bukkit.event.player.PlayerInteractEntityEvent` |
| `rightClicked` | entity summary | `getRightClicked()` | `org.bukkit.entity.Entity` | `org.bukkit.event.player.PlayerInteractEntityEvent` |

[[Data-Format-en|Wire format and limits]] · [[Event-org-bukkit-event-player-playerinteractatentityevent|中文]]

If this event is not enabled, add its Java class or simple name to `events.include` in the Paper plugin configuration.
