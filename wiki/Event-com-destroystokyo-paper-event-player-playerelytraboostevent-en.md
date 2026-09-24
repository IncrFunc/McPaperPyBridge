# PlayerElytraBoostEvent

[[Home-en|Home]] / [[Category-player-en|player]]

- Java class: `com.destroystokyo.paper.event.player.PlayerElytraBoostEvent`
- Parent class: `org.bukkit.event.player.PlayerEvent`
- Python subscription: `PlayerElytraBoostEvent`
- Python constant: `Events.PLAYER_ELYTRA_BOOST`
- Cancellable: Yes
- Player available: Possible at runtime
- HandlerList owner: `com.destroystokyo.paper.event.player.PlayerElytraBoostEvent`
- [Official Paper Javadoc](https://jd.papermc.io/paper/1.16.5/com/destroystokyo/paper/event/player/PlayerElytraBoostEvent.html)

## Python example

```python
from paperpybridge import Events

@bridge.on(Events.PLAYER_ELYTRA_BOOST)
def on_event(event):
    print(event.event, event.data)
```

## `data` fields

| Field | JSON type | Java getter | Java return type | Declared in |
| --- | --- | --- | --- | --- |
| `firework` | entity summary | `getFirework()` | `org.bukkit.entity.Firework` | `com.destroystokyo.paper.event.player.PlayerElytraBoostEvent` |
| `itemStack` | item summary | `getItemStack()` | `org.bukkit.inventory.ItemStack` | `com.destroystokyo.paper.event.player.PlayerElytraBoostEvent` |

[[Data-Format-en|Wire format and limits]] · [[Event-com-destroystokyo-paper-event-player-playerelytraboostevent|中文]]

If this event is not enabled, add its Java class or simple name to `events.include` in the Paper plugin configuration.
