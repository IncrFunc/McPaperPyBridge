# PlayerStatisticIncrementEvent

[[Home-en|Home]] / [[Category-player-en|player]]

- Java class: `org.bukkit.event.player.PlayerStatisticIncrementEvent`
- Parent class: `org.bukkit.event.player.PlayerEvent`
- Python subscription: `PlayerStatisticIncrementEvent`
- Python constant: `Events.PLAYER_STATISTIC_INCREMENT`
- Cancellable: Yes
- Player available: Possible at runtime
- HandlerList owner: `org.bukkit.event.player.PlayerStatisticIncrementEvent`
- [Official Paper Javadoc](https://jd.papermc.io/paper/1.16.5/org/bukkit/event/player/PlayerStatisticIncrementEvent.html)

## Python example

```python
from paperpybridge import Events

@bridge.on(Events.PLAYER_STATISTIC_INCREMENT)
def on_event(event):
    print(event.event, event.data)
```

## `data` fields

| Field | JSON type | Java getter | Java return type | Declared in |
| --- | --- | --- | --- | --- |
| `entityType` | string | `getEntityType()` | `org.bukkit.entity.EntityType` | `org.bukkit.event.player.PlayerStatisticIncrementEvent` |
| `material` | string | `getMaterial()` | `org.bukkit.Material` | `org.bukkit.event.player.PlayerStatisticIncrementEvent` |
| `newValue` | number | `getNewValue()` | `int` | `org.bukkit.event.player.PlayerStatisticIncrementEvent` |
| `previousValue` | number | `getPreviousValue()` | `int` | `org.bukkit.event.player.PlayerStatisticIncrementEvent` |
| `statistic` | string | `getStatistic()` | `org.bukkit.Statistic` | `org.bukkit.event.player.PlayerStatisticIncrementEvent` |

[[Data-Format-en|Wire format and limits]] · [[Event-org-bukkit-event-player-playerstatisticincrementevent|中文]]

If this event is not enabled, add its Java class or simple name to `events.include` in the Paper plugin configuration.
