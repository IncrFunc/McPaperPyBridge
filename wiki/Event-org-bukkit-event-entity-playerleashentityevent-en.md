# PlayerLeashEntityEvent

[[Home-en|Home]] / [[Category-entity-en|entity]]

- Java class: `org.bukkit.event.entity.PlayerLeashEntityEvent`
- Parent class: `org.bukkit.event.Event`
- Python subscription: `PlayerLeashEntityEvent`
- Python constant: `Events.PLAYER_LEASH_ENTITY`
- Cancellable: Yes
- Player available: Possible at runtime
- HandlerList owner: `org.bukkit.event.entity.PlayerLeashEntityEvent`
- [Official Paper Javadoc](https://jd.papermc.io/paper/1.16.5/org/bukkit/event/entity/PlayerLeashEntityEvent.html)

## Python example

```python
from paperpybridge import Events

@bridge.on(Events.PLAYER_LEASH_ENTITY)
def on_event(event):
    print(event.event, event.data)
```

## `data` fields

| Field | JSON type | Java getter | Java return type | Declared in |
| --- | --- | --- | --- | --- |
| `entity` | entity summary | `getEntity()` | `org.bukkit.entity.Entity` | `org.bukkit.event.entity.PlayerLeashEntityEvent` |
| `leashHolder` | entity summary | `getLeashHolder()` | `org.bukkit.entity.Entity` | `org.bukkit.event.entity.PlayerLeashEntityEvent` |

[[Data-Format-en|Wire format and limits]] · [[Event-org-bukkit-event-entity-playerleashentityevent|中文]]

If this event is not enabled, add its Java class or simple name to `events.include` in the Paper plugin configuration.
