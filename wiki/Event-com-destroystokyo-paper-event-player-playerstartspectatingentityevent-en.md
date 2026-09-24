# PlayerStartSpectatingEntityEvent

[[Home-en|Home]] / [[Category-player-en|player]]

- Java class: `com.destroystokyo.paper.event.player.PlayerStartSpectatingEntityEvent`
- Parent class: `org.bukkit.event.player.PlayerEvent`
- Python subscription: `PlayerStartSpectatingEntityEvent`
- Python constant: `Events.PLAYER_START_SPECTATING_ENTITY`
- Cancellable: Yes
- Player available: Possible at runtime
- HandlerList owner: `com.destroystokyo.paper.event.player.PlayerStartSpectatingEntityEvent`
- [Official Paper Javadoc](https://jd.papermc.io/paper/1.16.5/com/destroystokyo/paper/event/player/PlayerStartSpectatingEntityEvent.html)

## Python example

```python
from paperpybridge import Events

@bridge.on(Events.PLAYER_START_SPECTATING_ENTITY)
def on_event(event):
    print(event.event, event.data)
```

## `data` fields

| Field | JSON type | Java getter | Java return type | Declared in |
| --- | --- | --- | --- | --- |
| `currentSpectatorTarget` | entity summary | `getCurrentSpectatorTarget()` | `org.bukkit.entity.Entity` | `com.destroystokyo.paper.event.player.PlayerStartSpectatingEntityEvent` |
| `newSpectatorTarget` | entity summary | `getNewSpectatorTarget()` | `org.bukkit.entity.Entity` | `com.destroystokyo.paper.event.player.PlayerStartSpectatingEntityEvent` |

[[Data-Format-en|Wire format and limits]] · [[Event-com-destroystokyo-paper-event-player-playerstartspectatingentityevent|中文]]

If this event is not enabled, add its Java class or simple name to `events.include` in the Paper plugin configuration.
