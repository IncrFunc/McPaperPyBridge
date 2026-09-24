# PlayerUnleashEntityEvent

[[Home-en|Home]] / [[Category-player-en|player]]

- Java class: `org.bukkit.event.player.PlayerUnleashEntityEvent`
- Parent class: `org.bukkit.event.entity.EntityUnleashEvent`
- Python subscription: `PlayerUnleashEntityEvent`
- Python constant: `Events.PLAYER_UNLEASH_ENTITY`
- Cancellable: Yes
- Player available: Possible at runtime
- HandlerList owner: `org.bukkit.event.entity.EntityUnleashEvent`
- [Official Paper Javadoc](https://jd.papermc.io/paper/1.16.5/org/bukkit/event/player/PlayerUnleashEntityEvent.html)

## Python example

```python
from paperpybridge import Events

@bridge.on(Events.PLAYER_UNLEASH_ENTITY)
def on_event(event):
    print(event.event, event.data)
```

## `data` fields

| Field | JSON type | Java getter | Java return type | Declared in |
| --- | --- | --- | --- | --- |
| `entity` | entity summary | `getEntity()` | `org.bukkit.entity.Entity` | `org.bukkit.event.entity.EntityEvent` |
| `entityType` | string | `getEntityType()` | `org.bukkit.entity.EntityType` | `org.bukkit.event.entity.EntityEvent` |
| `reason` | string | `getReason()` | `org.bukkit.event.entity.EntityUnleashEvent$UnleashReason` | `org.bukkit.event.entity.EntityUnleashEvent` |
| `dropLeash` | boolean | `isDropLeash()` | `boolean` | `org.bukkit.event.entity.EntityUnleashEvent` |

[[Data-Format-en|Wire format and limits]] · [[Event-org-bukkit-event-player-playerunleashentityevent|中文]]

If this event is not enabled, add its Java class or simple name to `events.include` in the Paper plugin configuration.
