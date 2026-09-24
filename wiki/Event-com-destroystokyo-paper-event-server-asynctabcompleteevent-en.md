# AsyncTabCompleteEvent

[[Home-en|Home]] / [[Category-server-en|server]]

- Java class: `com.destroystokyo.paper.event.server.AsyncTabCompleteEvent`
- Parent class: `org.bukkit.event.Event`
- Python subscription: `AsyncTabCompleteEvent`
- Python constant: `Events.ASYNC_TAB_COMPLETE`
- Cancellable: Yes
- Player available: No known player getter
- HandlerList owner: `com.destroystokyo.paper.event.server.AsyncTabCompleteEvent`
- [Official Paper Javadoc](https://jd.papermc.io/paper/1.16.5/com/destroystokyo/paper/event/server/AsyncTabCompleteEvent.html)

## Python example

```python
from paperpybridge import Events

@bridge.on(Events.ASYNC_TAB_COMPLETE)
def on_event(event):
    print(event.event, event.data)
```

## `data` fields

| Field | JSON type | Java getter | Java return type | Declared in |
| --- | --- | --- | --- | --- |
| `buffer` | string | `getBuffer()` | `java.lang.String` | `com.destroystokyo.paper.event.server.AsyncTabCompleteEvent` |
| `location` | location summary | `getLocation()` | `org.bukkit.Location` | `com.destroystokyo.paper.event.server.AsyncTabCompleteEvent` |
| `command` | boolean | `isCommand()` | `boolean` | `com.destroystokyo.paper.event.server.AsyncTabCompleteEvent` |
| `handled` | boolean | `isHandled()` | `boolean` | `com.destroystokyo.paper.event.server.AsyncTabCompleteEvent` |

[[Data-Format-en|Wire format and limits]] · [[Event-com-destroystokyo-paper-event-server-asynctabcompleteevent|中文]]

If this event is not enabled, add its Java class or simple name to `events.include` in the Paper plugin configuration.
