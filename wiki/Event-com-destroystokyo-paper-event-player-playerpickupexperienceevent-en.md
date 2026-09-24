# PlayerPickupExperienceEvent

[[Home-en|Home]] / [[Category-player-en|player]]

- Java class: `com.destroystokyo.paper.event.player.PlayerPickupExperienceEvent`
- Parent class: `org.bukkit.event.player.PlayerEvent`
- Python subscription: `PlayerPickupExperienceEvent`
- Python constant: `Events.PLAYER_PICKUP_EXPERIENCE`
- Cancellable: Yes
- Player available: Possible at runtime
- HandlerList owner: `com.destroystokyo.paper.event.player.PlayerPickupExperienceEvent`
- [Official Paper Javadoc](https://jd.papermc.io/paper/1.16.5/com/destroystokyo/paper/event/player/PlayerPickupExperienceEvent.html)

## Python example

```python
from paperpybridge import Events

@bridge.on(Events.PLAYER_PICKUP_EXPERIENCE)
def on_event(event):
    print(event.event, event.data)
```

## `data` fields

| Field | JSON type | Java getter | Java return type | Declared in |
| --- | --- | --- | --- | --- |
| `experienceOrb` | entity summary | `getExperienceOrb()` | `org.bukkit.entity.ExperienceOrb` | `com.destroystokyo.paper.event.player.PlayerPickupExperienceEvent` |

[[Data-Format-en|Wire format and limits]] · [[Event-com-destroystokyo-paper-event-player-playerpickupexperienceevent|中文]]

If this event is not enabled, add its Java class or simple name to `events.include` in the Paper plugin configuration.
