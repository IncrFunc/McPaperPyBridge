# PlayerEggThrowEvent

[[Home-en|Home]] / [[Category-player-en|player]]

- Java class: `org.bukkit.event.player.PlayerEggThrowEvent`
- Parent class: `org.bukkit.event.player.PlayerEvent`
- Python subscription: `PlayerEggThrowEvent`
- Python constant: `Events.PLAYER_EGG_THROW`
- Cancellable: No
- Player available: Possible at runtime
- HandlerList owner: `org.bukkit.event.player.PlayerEggThrowEvent`
- [Official Paper Javadoc](https://jd.papermc.io/paper/1.16.5/org/bukkit/event/player/PlayerEggThrowEvent.html)

## Python example

```python
from paperpybridge import Events

@bridge.on(Events.PLAYER_EGG_THROW)
def on_event(event):
    print(event.event, event.data)
```

## `data` fields

| Field | JSON type | Java getter | Java return type | Declared in |
| --- | --- | --- | --- | --- |
| `egg` | entity summary | `getEgg()` | `org.bukkit.entity.Egg` | `org.bukkit.event.player.PlayerEggThrowEvent` |
| `hatchingType` | string | `getHatchingType()` | `org.bukkit.entity.EntityType` | `org.bukkit.event.player.PlayerEggThrowEvent` |
| `numHatches` | number | `getNumHatches()` | `byte` | `org.bukkit.event.player.PlayerEggThrowEvent` |
| `hatching` | boolean | `isHatching()` | `boolean` | `org.bukkit.event.player.PlayerEggThrowEvent` |

[[Data-Format-en|Wire format and limits]] · [[Event-org-bukkit-event-player-playereggthrowevent|中文]]

If this event is not enabled, add its Java class or simple name to `events.include` in the Paper plugin configuration.
