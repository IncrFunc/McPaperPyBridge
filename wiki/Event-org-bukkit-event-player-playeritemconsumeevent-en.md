# PlayerItemConsumeEvent

[[Home-en|Home]] / [[Category-player-en|player]]

- Java class: `org.bukkit.event.player.PlayerItemConsumeEvent`
- Parent class: `org.bukkit.event.player.PlayerEvent`
- Python subscription: `PlayerItemConsumeEvent`
- Python constant: `Events.PLAYER_ITEM_CONSUME`
- Cancellable: Yes
- Player available: Possible at runtime
- HandlerList owner: `org.bukkit.event.player.PlayerItemConsumeEvent`
- [Official Paper Javadoc](https://jd.papermc.io/paper/1.16.5/org/bukkit/event/player/PlayerItemConsumeEvent.html)

## Python example

```python
from paperpybridge import Events

@bridge.on(Events.PLAYER_ITEM_CONSUME)
def on_event(event):
    print(event.event, event.data)
```

## `data` fields

| Field | JSON type | Java getter | Java return type | Declared in |
| --- | --- | --- | --- | --- |
| `item` | item summary | `getItem()` | `org.bukkit.inventory.ItemStack` | `org.bukkit.event.player.PlayerItemConsumeEvent` |
| `replacement` | item summary | `getReplacement()` | `org.bukkit.inventory.ItemStack` | `org.bukkit.event.player.PlayerItemConsumeEvent` |

[[Data-Format-en|Wire format and limits]] · [[Event-org-bukkit-event-player-playeritemconsumeevent|中文]]

If this event is not enabled, add its Java class or simple name to `events.include` in the Paper plugin configuration.
