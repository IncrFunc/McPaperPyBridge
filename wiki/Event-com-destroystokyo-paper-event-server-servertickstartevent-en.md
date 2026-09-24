# ServerTickStartEvent

[[Home-en|Home]] / [[Category-server-en|server]]

- Java class: `com.destroystokyo.paper.event.server.ServerTickStartEvent`
- Parent class: `org.bukkit.event.Event`
- Python subscription: `ServerTickStartEvent`
- Python constant: `Events.SERVER_TICK_START`
- Cancellable: No
- Player available: No known player getter
- HandlerList owner: `com.destroystokyo.paper.event.server.ServerTickStartEvent`
- [Official Paper Javadoc](https://jd.papermc.io/paper/1.16.5/com/destroystokyo/paper/event/server/ServerTickStartEvent.html)

## Python example

```python
from paperpybridge import Events

@bridge.on(Events.SERVER_TICK_START)
def on_event(event):
    print(event.event, event.data)
```

## `data` fields

| Field | JSON type | Java getter | Java return type | Declared in |
| --- | --- | --- | --- | --- |
| `tickNumber` | number | `getTickNumber()` | `int` | `com.destroystokyo.paper.event.server.ServerTickStartEvent` |

[[Data-Format-en|Wire format and limits]] · [[Event-com-destroystokyo-paper-event-server-servertickstartevent|中文]]

If this event is not enabled, add its Java class or simple name to `events.include` in the Paper plugin configuration.
