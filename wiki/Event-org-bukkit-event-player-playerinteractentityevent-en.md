# PlayerInteractEntityEvent

[[Home-en|Home]] / [[Category-player-en|player]]

- Java class: `org.bukkit.event.player.PlayerInteractEntityEvent`
- Parent class: `org.bukkit.event.player.PlayerEvent`
- Python subscription: `PlayerInteractEntityEvent`
- Python constant: `Events.PLAYER_INTERACT_ENTITY`
- Cancellable: Yes
- Player available: Possible at runtime
- HandlerList owner: `org.bukkit.event.player.PlayerInteractEntityEvent`
- [Official Paper Javadoc](https://jd.papermc.io/paper/1.16.5/org/bukkit/event/player/PlayerInteractEntityEvent.html)

## Python example

```python
from paperpybridge import Events

@bridge.on(Events.PLAYER_INTERACT_ENTITY)
def on_event(event):
    print(event.event, event.data)
```

## `data` fields

| Field | JSON type | Java getter | Java return type | Declared in |
| --- | --- | --- | --- | --- |
| `hand` | string | `getHand()` | `org.bukkit.inventory.EquipmentSlot` | `org.bukkit.event.player.PlayerInteractEntityEvent` |
| `rightClicked` | entity summary | `getRightClicked()` | `org.bukkit.entity.Entity` | `org.bukkit.event.player.PlayerInteractEntityEvent` |

[[Data-Format-en|Wire format and limits]] · [[Event-org-bukkit-event-player-playerinteractentityevent|中文]]

If this event is not enabled, add its Java class or simple name to `events.include` in the Paper plugin configuration.
