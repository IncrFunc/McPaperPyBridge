# ServerExceptionEvent

[[Home-en|Home]] / [[Category-server-en|server]]

- Java class: `com.destroystokyo.paper.event.server.ServerExceptionEvent`
- Parent class: `org.bukkit.event.Event`
- Python subscription: `ServerExceptionEvent`
- Python constant: `Events.SERVER_EXCEPTION`
- Cancellable: No
- Player available: No known player getter
- HandlerList owner: `com.destroystokyo.paper.event.server.ServerExceptionEvent`
- [Official Paper Javadoc](https://jd.papermc.io/paper/1.16.5/com/destroystokyo/paper/event/server/ServerExceptionEvent.html)

## Python example

```python
from paperpybridge import Events

@bridge.on(Events.SERVER_EXCEPTION)
def on_event(event):
    print(event.event, event.data)
```

## `data` fields

No supported serializable fields; common event fields are still sent.

[[Data-Format-en|Wire format and limits]] · [[Event-com-destroystokyo-paper-event-server-serverexceptionevent|中文]]

If this event is not enabled, add its Java class or simple name to `events.include` in the Paper plugin configuration.
