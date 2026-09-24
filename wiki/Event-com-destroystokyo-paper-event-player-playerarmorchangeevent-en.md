# PlayerArmorChangeEvent

[[Home-en|Home]] / [[Category-player-en|player]]

- Java class: `com.destroystokyo.paper.event.player.PlayerArmorChangeEvent`
- Parent class: `org.bukkit.event.player.PlayerEvent`
- Python subscription: `PlayerArmorChangeEvent`
- Python constant: `Events.PLAYER_ARMOR_CHANGE`
- Cancellable: No
- Player available: Possible at runtime
- HandlerList owner: `com.destroystokyo.paper.event.player.PlayerArmorChangeEvent`
- [Official Paper Javadoc](https://jd.papermc.io/paper/1.16.5/com/destroystokyo/paper/event/player/PlayerArmorChangeEvent.html)

## Python example

```python
from paperpybridge import Events

@bridge.on(Events.PLAYER_ARMOR_CHANGE)
def on_event(event):
    print(event.event, event.data)
```

## `data` fields

| Field | JSON type | Java getter | Java return type | Declared in |
| --- | --- | --- | --- | --- |
| `newItem` | item summary | `getNewItem()` | `org.bukkit.inventory.ItemStack` | `com.destroystokyo.paper.event.player.PlayerArmorChangeEvent` |
| `oldItem` | item summary | `getOldItem()` | `org.bukkit.inventory.ItemStack` | `com.destroystokyo.paper.event.player.PlayerArmorChangeEvent` |
| `slotType` | string | `getSlotType()` | `com.destroystokyo.paper.event.player.PlayerArmorChangeEvent$SlotType` | `com.destroystokyo.paper.event.player.PlayerArmorChangeEvent` |

[[Data-Format-en|Wire format and limits]] · [[Event-com-destroystokyo-paper-event-player-playerarmorchangeevent|中文]]

If this event is not enabled, add its Java class or simple name to `events.include` in the Paper plugin configuration.
