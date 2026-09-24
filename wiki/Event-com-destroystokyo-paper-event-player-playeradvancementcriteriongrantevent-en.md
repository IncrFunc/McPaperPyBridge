# PlayerAdvancementCriterionGrantEvent

[[Home-en|Home]] / [[Category-player-en|player]]

- Java class: `com.destroystokyo.paper.event.player.PlayerAdvancementCriterionGrantEvent`
- Parent class: `org.bukkit.event.player.PlayerEvent`
- Python subscription: `PlayerAdvancementCriterionGrantEvent`
- Python constant: `Events.PLAYER_ADVANCEMENT_CRITERION_GRANT`
- Cancellable: Yes
- Player available: Possible at runtime
- HandlerList owner: `com.destroystokyo.paper.event.player.PlayerAdvancementCriterionGrantEvent`
- [Official Paper Javadoc](https://jd.papermc.io/paper/1.16.5/com/destroystokyo/paper/event/player/PlayerAdvancementCriterionGrantEvent.html)

## Python example

```python
from paperpybridge import Events

@bridge.on(Events.PLAYER_ADVANCEMENT_CRITERION_GRANT)
def on_event(event):
    print(event.event, event.data)
```

## `data` fields

| Field | JSON type | Java getter | Java return type | Declared in |
| --- | --- | --- | --- | --- |
| `criterion` | string | `getCriterion()` | `java.lang.String` | `com.destroystokyo.paper.event.player.PlayerAdvancementCriterionGrantEvent` |

[[Data-Format-en|Wire format and limits]] · [[Event-com-destroystokyo-paper-event-player-playeradvancementcriteriongrantevent|中文]]

If this event is not enabled, add its Java class or simple name to `events.include` in the Paper plugin configuration.
