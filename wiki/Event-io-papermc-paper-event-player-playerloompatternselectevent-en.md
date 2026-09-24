# PlayerLoomPatternSelectEvent

[[Home-en|Home]] / [[Category-player-en|player]]

- Java class: `io.papermc.paper.event.player.PlayerLoomPatternSelectEvent`
- Parent class: `org.bukkit.event.player.PlayerEvent`
- Python subscription: `PlayerLoomPatternSelectEvent`
- Python constant: `Events.PLAYER_LOOM_PATTERN_SELECT`
- Cancellable: Yes
- Player available: Possible at runtime
- HandlerList owner: `io.papermc.paper.event.player.PlayerLoomPatternSelectEvent`
- [Official Paper Javadoc](https://jd.papermc.io/paper/1.16.5/io/papermc/paper/event/player/PlayerLoomPatternSelectEvent.html)

## Python example

```python
from paperpybridge import Events

@bridge.on(Events.PLAYER_LOOM_PATTERN_SELECT)
def on_event(event):
    print(event.event, event.data)
```

## `data` fields

| Field | JSON type | Java getter | Java return type | Declared in |
| --- | --- | --- | --- | --- |
| `patternType` | string | `getPatternType()` | `org.bukkit.block.banner.PatternType` | `io.papermc.paper.event.player.PlayerLoomPatternSelectEvent` |

[[Data-Format-en|Wire format and limits]] · [[Event-io-papermc-paper-event-player-playerloompatternselectevent|中文]]

If this event is not enabled, add its Java class or simple name to `events.include` in the Paper plugin configuration.
