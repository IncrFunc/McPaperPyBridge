# PlayerNameEntityEvent

[[Home-en|Home]] / [[Category-player-en|player]]

- Java class: `io.papermc.paper.event.player.PlayerNameEntityEvent`
- Parent class: `org.bukkit.event.player.PlayerEvent`
- Python subscription: `PlayerNameEntityEvent`
- Python constant: `Events.PLAYER_NAME_ENTITY`
- Cancellable: Yes
- Player available: Possible at runtime
- HandlerList owner: `io.papermc.paper.event.player.PlayerNameEntityEvent`
- [Official Paper Javadoc](https://jd.papermc.io/paper/1.16.5/io/papermc/paper/event/player/PlayerNameEntityEvent.html)

## Python example

```python
from paperpybridge import Events

@bridge.on(Events.PLAYER_NAME_ENTITY)
def on_event(event):
    print(event.event, event.data)
```

## `data` fields

| Field | JSON type | Java getter | Java return type | Declared in |
| --- | --- | --- | --- | --- |
| `entity` | entity summary | `getEntity()` | `org.bukkit.entity.LivingEntity` | `io.papermc.paper.event.player.PlayerNameEntityEvent` |
| `persistent` | boolean | `isPersistent()` | `boolean` | `io.papermc.paper.event.player.PlayerNameEntityEvent` |

[[Data-Format-en|Wire format and limits]] · [[Event-io-papermc-paper-event-player-playernameentityevent|中文]]

If this event is not enabled, add its Java class or simple name to `events.include` in the Paper plugin configuration.
