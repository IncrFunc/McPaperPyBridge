# PlayerAttackEntityCooldownResetEvent

[[Home-en|Home]] / [[Category-player-en|player]]

- Java class: `com.destroystokyo.paper.event.player.PlayerAttackEntityCooldownResetEvent`
- Parent class: `org.bukkit.event.player.PlayerEvent`
- Python subscription: `PlayerAttackEntityCooldownResetEvent`
- Python constant: `Events.PLAYER_ATTACK_ENTITY_COOLDOWN_RESET`
- Cancellable: Yes
- Player available: Possible at runtime
- HandlerList owner: `com.destroystokyo.paper.event.player.PlayerAttackEntityCooldownResetEvent`
- [Official Paper Javadoc](https://jd.papermc.io/paper/1.16.5/com/destroystokyo/paper/event/player/PlayerAttackEntityCooldownResetEvent.html)

## Python example

```python
from paperpybridge import Events

@bridge.on(Events.PLAYER_ATTACK_ENTITY_COOLDOWN_RESET)
def on_event(event):
    print(event.event, event.data)
```

## `data` fields

| Field | JSON type | Java getter | Java return type | Declared in |
| --- | --- | --- | --- | --- |
| `attackedEntity` | entity summary | `getAttackedEntity()` | `org.bukkit.entity.Entity` | `com.destroystokyo.paper.event.player.PlayerAttackEntityCooldownResetEvent` |
| `cooledAttackStrength` | number | `getCooledAttackStrength()` | `float` | `com.destroystokyo.paper.event.player.PlayerAttackEntityCooldownResetEvent` |

[[Data-Format-en|Wire format and limits]] · [[Event-com-destroystokyo-paper-event-player-playerattackentitycooldownresetevent|中文]]

If this event is not enabled, add its Java class or simple name to `events.include` in the Paper plugin configuration.
