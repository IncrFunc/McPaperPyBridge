# PlayerRecipeBookClickEvent

[[Home-en|Home]] / [[Category-player-en|player]]

- Java class: `com.destroystokyo.paper.event.player.PlayerRecipeBookClickEvent`
- Parent class: `org.bukkit.event.player.PlayerEvent`
- Python subscription: `PlayerRecipeBookClickEvent`
- Python constant: `Events.PLAYER_RECIPE_BOOK_CLICK`
- Cancellable: Yes
- Player available: Possible at runtime
- HandlerList owner: `com.destroystokyo.paper.event.player.PlayerRecipeBookClickEvent`
- [Official Paper Javadoc](https://jd.papermc.io/paper/1.16.5/com/destroystokyo/paper/event/player/PlayerRecipeBookClickEvent.html)

## Python example

```python
from paperpybridge import Events

@bridge.on(Events.PLAYER_RECIPE_BOOK_CLICK)
def on_event(event):
    print(event.event, event.data)
```

## `data` fields

| Field | JSON type | Java getter | Java return type | Declared in |
| --- | --- | --- | --- | --- |
| `makeAll` | boolean | `isMakeAll()` | `boolean` | `com.destroystokyo.paper.event.player.PlayerRecipeBookClickEvent` |

[[Data-Format-en|Wire format and limits]] · [[Event-com-destroystokyo-paper-event-player-playerrecipebookclickevent|中文]]

If this event is not enabled, add its Java class or simple name to `events.include` in the Paper plugin configuration.
