# PlayerLaunchProjectileEvent

[[Home-en|Home]] / [[Category-player-en|player]]

- Java class: `com.destroystokyo.paper.event.player.PlayerLaunchProjectileEvent`
- Parent class: `org.bukkit.event.player.PlayerEvent`
- Python subscription: `PlayerLaunchProjectileEvent`
- Python constant: `Events.PLAYER_LAUNCH_PROJECTILE`
- Cancellable: Yes
- Player available: Possible at runtime
- HandlerList owner: `com.destroystokyo.paper.event.player.PlayerLaunchProjectileEvent`
- [Official Paper Javadoc](https://jd.papermc.io/paper/1.16.5/com/destroystokyo/paper/event/player/PlayerLaunchProjectileEvent.html)

## Python example

```python
from paperpybridge import Events

@bridge.on(Events.PLAYER_LAUNCH_PROJECTILE)
def on_event(event):
    print(event.event, event.data)
```

## `data` fields

| Field | JSON type | Java getter | Java return type | Declared in |
| --- | --- | --- | --- | --- |
| `itemStack` | item summary | `getItemStack()` | `org.bukkit.inventory.ItemStack` | `com.destroystokyo.paper.event.player.PlayerLaunchProjectileEvent` |
| `projectile` | entity summary | `getProjectile()` | `org.bukkit.entity.Projectile` | `com.destroystokyo.paper.event.player.PlayerLaunchProjectileEvent` |

[[Data-Format-en|Wire format and limits]] · [[Event-com-destroystokyo-paper-event-player-playerlaunchprojectileevent|中文]]

If this event is not enabled, add its Java class or simple name to `events.include` in the Paper plugin configuration.
