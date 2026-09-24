# PlayerChangedMainHandEvent

[[Home-en|Home]] / [[Category-player-en|player]]

- Java class: `org.bukkit.event.player.PlayerChangedMainHandEvent`
- Parent class: `org.bukkit.event.player.PlayerEvent`
- Python subscription: `PlayerChangedMainHandEvent`
- Python constant: `Events.PLAYER_CHANGED_MAIN_HAND`
- Cancellable: No
- Player available: Possible at runtime
- HandlerList owner: `org.bukkit.event.player.PlayerChangedMainHandEvent`
- [Official Paper Javadoc](https://jd.papermc.io/paper/1.16.5/org/bukkit/event/player/PlayerChangedMainHandEvent.html)

## Python example

```python
from paperpybridge import Events

@bridge.on(Events.PLAYER_CHANGED_MAIN_HAND)
def on_event(event):
    print(event.event, event.data)
```

## `data` fields

| Field | JSON type | Java getter | Java return type | Declared in |
| --- | --- | --- | --- | --- |
| `mainHand` | string | `getMainHand()` | `org.bukkit.inventory.MainHand` | `org.bukkit.event.player.PlayerChangedMainHandEvent` |

[[Data-Format-en|Wire format and limits]] · [[Event-org-bukkit-event-player-playerchangedmainhandevent|中文]]

If this event is not enabled, add its Java class or simple name to `events.include` in the Paper plugin configuration.
