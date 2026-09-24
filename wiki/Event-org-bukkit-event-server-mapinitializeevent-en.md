# MapInitializeEvent

[[Home-en|Home]] / [[Category-server-en|server]]

- Java class: `org.bukkit.event.server.MapInitializeEvent`
- Parent class: `org.bukkit.event.server.ServerEvent`
- Python subscription: `MapInitializeEvent`
- Python constant: `Events.MAP_INITIALIZE`
- Cancellable: No
- Player available: No known player getter
- HandlerList owner: `org.bukkit.event.server.MapInitializeEvent`
- [Official Paper Javadoc](https://jd.papermc.io/paper/1.16.5/org/bukkit/event/server/MapInitializeEvent.html)

## Python example

```python
from paperpybridge import Events

@bridge.on(Events.MAP_INITIALIZE)
def on_event(event):
    print(event.event, event.data)
```

## `data` fields

No supported serializable fields; common event fields are still sent.

[[Data-Format-en|Wire format and limits]] · [[Event-org-bukkit-event-server-mapinitializeevent|中文]]

If this event is not enabled, add its Java class or simple name to `events.include` in the Paper plugin configuration.
