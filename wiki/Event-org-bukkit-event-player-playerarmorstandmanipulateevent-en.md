# PlayerArmorStandManipulateEvent

[[Home-en|Home]] / [[Category-player-en|player]]

- Java class: `org.bukkit.event.player.PlayerArmorStandManipulateEvent`
- Parent class: `org.bukkit.event.player.PlayerInteractEntityEvent`
- Python subscription: `PlayerArmorStandManipulateEvent`
- Python constant: `Events.PLAYER_ARMOR_STAND_MANIPULATE`
- Cancellable: Yes
- Player available: Possible at runtime
- HandlerList owner: `org.bukkit.event.player.PlayerArmorStandManipulateEvent`
- [Official Paper Javadoc](https://jd.papermc.io/paper/1.16.5/org/bukkit/event/player/PlayerArmorStandManipulateEvent.html)

## Python example

```python
from paperpybridge import Events

@bridge.on(Events.PLAYER_ARMOR_STAND_MANIPULATE)
def on_event(event):
    print(event.event, event.data)
```

## `data` fields

| Field | JSON type | Java getter | Java return type | Declared in |
| --- | --- | --- | --- | --- |
| `armorStandItem` | item summary | `getArmorStandItem()` | `org.bukkit.inventory.ItemStack` | `org.bukkit.event.player.PlayerArmorStandManipulateEvent` |
| `hand` | string | `getHand()` | `org.bukkit.inventory.EquipmentSlot` | `org.bukkit.event.player.PlayerInteractEntityEvent` |
| `playerItem` | item summary | `getPlayerItem()` | `org.bukkit.inventory.ItemStack` | `org.bukkit.event.player.PlayerArmorStandManipulateEvent` |
| `rightClicked` | entity summary | `getRightClicked()` | `org.bukkit.entity.ArmorStand` | `org.bukkit.event.player.PlayerArmorStandManipulateEvent` |
| `slot` | string | `getSlot()` | `org.bukkit.inventory.EquipmentSlot` | `org.bukkit.event.player.PlayerArmorStandManipulateEvent` |

[[Data-Format-en|Wire format and limits]] · [[Event-org-bukkit-event-player-playerarmorstandmanipulateevent|中文]]

If this event is not enabled, add its Java class or simple name to `events.include` in the Paper plugin configuration.
