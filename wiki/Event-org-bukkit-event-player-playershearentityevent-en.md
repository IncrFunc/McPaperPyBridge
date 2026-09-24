# PlayerShearEntityEvent

[[Home-en|Home]] / [[Category-player-en|player]]

- Java class: `org.bukkit.event.player.PlayerShearEntityEvent`
- Parent class: `org.bukkit.event.player.PlayerEvent`
- Python subscription: `PlayerShearEntityEvent`
- Python constant: `Events.PLAYER_SHEAR_ENTITY`
- Cancellable: Yes
- Player available: Possible at runtime
- HandlerList owner: `org.bukkit.event.player.PlayerShearEntityEvent`
- [Official Paper Javadoc](https://jd.papermc.io/paper/1.16.5/org/bukkit/event/player/PlayerShearEntityEvent.html)

## Python example

```python
from paperpybridge import Events

@bridge.on(Events.PLAYER_SHEAR_ENTITY)
def on_event(event):
    print(event.event, event.data)
```

## `data` fields

| Field | JSON type | Java getter | Java return type | Declared in |
| --- | --- | --- | --- | --- |
| `entity` | entity summary | `getEntity()` | `org.bukkit.entity.Entity` | `org.bukkit.event.player.PlayerShearEntityEvent` |
| `hand` | string | `getHand()` | `org.bukkit.inventory.EquipmentSlot` | `org.bukkit.event.player.PlayerShearEntityEvent` |
| `item` | item summary | `getItem()` | `org.bukkit.inventory.ItemStack` | `org.bukkit.event.player.PlayerShearEntityEvent` |

[[Data-Format-en|Wire format and limits]] · [[Event-org-bukkit-event-player-playershearentityevent|中文]]

If this event is not enabled, add its Java class or simple name to `events.include` in the Paper plugin configuration.
