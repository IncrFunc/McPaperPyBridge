# ServerResourcesReloadedEvent

[[Home-en|Home]] / [[Category-server-en|server]]

- Java class: `io.papermc.paper.event.server.ServerResourcesReloadedEvent`
- Parent class: `org.bukkit.event.server.ServerEvent`
- Python subscription: `ServerResourcesReloadedEvent`
- Python constant: `Events.SERVER_RESOURCES_RELOADED`
- Cancellable: No
- Player available: No known player getter
- HandlerList owner: `io.papermc.paper.event.server.ServerResourcesReloadedEvent`
- [Official Paper Javadoc](https://jd.papermc.io/paper/1.16.5/io/papermc/paper/event/server/ServerResourcesReloadedEvent.html)

## Python example

```python
from paperpybridge import Events

@bridge.on(Events.SERVER_RESOURCES_RELOADED)
def on_event(event):
    print(event.event, event.data)
```

## `data` fields

| Field | JSON type | Java getter | Java return type | Declared in |
| --- | --- | --- | --- | --- |
| `cause` | string | `getCause()` | `io.papermc.paper.event.server.ServerResourcesReloadedEvent$Cause` | `io.papermc.paper.event.server.ServerResourcesReloadedEvent` |

[[Data-Format-en|Wire format and limits]] · [[Event-io-papermc-paper-event-server-serverresourcesreloadedevent|中文]]

If this event is not enabled, add its Java class or simple name to `events.include` in the Paper plugin configuration.
