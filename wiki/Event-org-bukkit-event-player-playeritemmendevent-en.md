# PlayerItemMendEvent

[[Home-en|Home]] / [[Category-player-en|player]]

- Java class: `org.bukkit.event.player.PlayerItemMendEvent`
- Parent class: `org.bukkit.event.player.PlayerEvent`
- Python subscription: `PlayerItemMendEvent`
- Python constant: `Events.PLAYER_ITEM_MEND`
- Cancellable: Yes
- Player available: Possible at runtime
- HandlerList owner: `org.bukkit.event.player.PlayerItemMendEvent`
- [Official Paper Javadoc](https://jd.papermc.io/paper/1.16.5/org/bukkit/event/player/PlayerItemMendEvent.html)

## Python example

```python
from paperpybridge import Events

@bridge.on(Events.PLAYER_ITEM_MEND)
def on_event(event):
    print(event.event, event.data)
```

## `data` fields

| Field | JSON type | Java getter | Java return type | Declared in |
| --- | --- | --- | --- | --- |
| `experienceOrb` | entity summary | `getExperienceOrb()` | `org.bukkit.entity.ExperienceOrb` | `org.bukkit.event.player.PlayerItemMendEvent` |
| `item` | item summary | `getItem()` | `org.bukkit.inventory.ItemStack` | `org.bukkit.event.player.PlayerItemMendEvent` |
| `repairAmount` | number | `getRepairAmount()` | `int` | `org.bukkit.event.player.PlayerItemMendEvent` |

[[Data-Format-en|Wire format and limits]] · [[Event-org-bukkit-event-player-playeritemmendevent|中文]]

If this event is not enabled, add its Java class or simple name to `events.include` in the Paper plugin configuration.
