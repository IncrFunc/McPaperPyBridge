# PlayerDropItemEvent

[[Home-en|Home]] / [[Category-player-en|player]]

- Java class: `org.bukkit.event.player.PlayerDropItemEvent`
- Parent class: `org.bukkit.event.player.PlayerEvent`
- Python subscription: `PlayerDropItemEvent`
- Python constant: `Events.PLAYER_DROP_ITEM`
- Cancellable: Yes
- Player available: Possible at runtime
- HandlerList owner: `org.bukkit.event.player.PlayerDropItemEvent`
- [Official Paper Javadoc](https://jd.papermc.io/paper/1.16.5/org/bukkit/event/player/PlayerDropItemEvent.html)

## Python example

```python
from paperpybridge import Events

@bridge.on(Events.PLAYER_DROP_ITEM)
def on_event(event):
    print(event.event, event.data)
```

## `data` fields

| Field | JSON type | Java getter | Java return type | Declared in |
| --- | --- | --- | --- | --- |
| `itemDrop` | entity summary | `getItemDrop()` | `org.bukkit.entity.Item` | `org.bukkit.event.player.PlayerDropItemEvent` |

[[Data-Format-en|Wire format and limits]] · [[Event-org-bukkit-event-player-playerdropitemevent|中文]]

If this event is not enabled, add its Java class or simple name to `events.include` in the Paper plugin configuration.
