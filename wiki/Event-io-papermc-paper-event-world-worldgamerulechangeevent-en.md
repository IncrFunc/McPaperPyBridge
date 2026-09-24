# WorldGameRuleChangeEvent

[[Home-en|Home]] / [[Category-world-en|world]]

- Java class: `io.papermc.paper.event.world.WorldGameRuleChangeEvent`
- Parent class: `org.bukkit.event.world.WorldEvent`
- Python subscription: `WorldGameRuleChangeEvent`
- Python constant: `Events.WORLD_GAME_RULE_CHANGE`
- Cancellable: Yes
- Player available: No known player getter
- HandlerList owner: `io.papermc.paper.event.world.WorldGameRuleChangeEvent`
- [Official Paper Javadoc](https://jd.papermc.io/paper/1.16.5/io/papermc/paper/event/world/WorldGameRuleChangeEvent.html)

## Python example

```python
from paperpybridge import Events

@bridge.on(Events.WORLD_GAME_RULE_CHANGE)
def on_event(event):
    print(event.event, event.data)
```

## `data` fields

| Field | JSON type | Java getter | Java return type | Declared in |
| --- | --- | --- | --- | --- |
| `value` | string | `getValue()` | `java.lang.String` | `io.papermc.paper.event.world.WorldGameRuleChangeEvent` |
| `world` | world summary | `getWorld()` | `org.bukkit.World` | `org.bukkit.event.world.WorldEvent` |

[[Data-Format-en|Wire format and limits]] · [[Event-io-papermc-paper-event-world-worldgamerulechangeevent|中文]]

If this event is not enabled, add its Java class or simple name to `events.include` in the Paper plugin configuration.
