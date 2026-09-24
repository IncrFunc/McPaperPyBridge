# PlayerNaturallySpawnCreaturesEvent

[[Home-en|Home]] / [[Category-entity-en|entity]]

- Java class: `com.destroystokyo.paper.event.entity.PlayerNaturallySpawnCreaturesEvent`
- Parent class: `org.bukkit.event.player.PlayerEvent`
- Python subscription: `PlayerNaturallySpawnCreaturesEvent`
- Python constant: `Events.PLAYER_NATURALLY_SPAWN_CREATURES`
- Cancellable: Yes
- Player available: Possible at runtime
- HandlerList owner: `com.destroystokyo.paper.event.entity.PlayerNaturallySpawnCreaturesEvent`
- [Official Paper Javadoc](https://jd.papermc.io/paper/1.16.5/com/destroystokyo/paper/event/entity/PlayerNaturallySpawnCreaturesEvent.html)

## Python example

```python
from paperpybridge import Events

@bridge.on(Events.PLAYER_NATURALLY_SPAWN_CREATURES)
def on_event(event):
    print(event.event, event.data)
```

## `data` fields

| Field | JSON type | Java getter | Java return type | Declared in |
| --- | --- | --- | --- | --- |
| `spawnRadius` | number | `getSpawnRadius()` | `byte` | `com.destroystokyo.paper.event.entity.PlayerNaturallySpawnCreaturesEvent` |

[[Data-Format-en|Wire format and limits]] · [[Event-com-destroystokyo-paper-event-entity-playernaturallyspawncreaturesevent|中文]]

If this event is not enabled, add its Java class or simple name to `events.include` in the Paper plugin configuration.
