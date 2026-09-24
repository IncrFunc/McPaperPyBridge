# PlayerItemDamageEvent

[[Home-en|Home]] / [[Category-player-en|player]]

- Java class: `org.bukkit.event.player.PlayerItemDamageEvent`
- Parent class: `org.bukkit.event.player.PlayerEvent`
- Python subscription: `PlayerItemDamageEvent`
- Python constant: `Events.PLAYER_ITEM_DAMAGE`
- Cancellable: Yes
- Player available: Possible at runtime
- HandlerList owner: `org.bukkit.event.player.PlayerItemDamageEvent`
- [Official Paper Javadoc](https://jd.papermc.io/paper/1.16.5/org/bukkit/event/player/PlayerItemDamageEvent.html)

## Python example

```python
from paperpybridge import Events

@bridge.on(Events.PLAYER_ITEM_DAMAGE)
def on_event(event):
    print(event.event, event.data)
```

## `data` fields

| Field | JSON type | Java getter | Java return type | Declared in |
| --- | --- | --- | --- | --- |
| `damage` | number | `getDamage()` | `int` | `org.bukkit.event.player.PlayerItemDamageEvent` |
| `item` | item summary | `getItem()` | `org.bukkit.inventory.ItemStack` | `org.bukkit.event.player.PlayerItemDamageEvent` |

[[Data-Format-en|Wire format and limits]] · [[Event-org-bukkit-event-player-playeritemdamageevent|中文]]

If this event is not enabled, add its Java class or simple name to `events.include` in the Paper plugin configuration.
