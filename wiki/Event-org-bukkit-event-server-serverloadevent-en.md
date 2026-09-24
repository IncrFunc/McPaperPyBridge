# ServerLoadEvent

[[Home-en|Home]] / [[Category-server-en|server]]

- Java class: `org.bukkit.event.server.ServerLoadEvent`
- Parent class: `org.bukkit.event.server.ServerEvent`
- Python subscription: `ServerLoadEvent`
- Python constant: `Events.SERVER_LOAD`
- Cancellable: No
- Player available: No known player getter
- HandlerList owner: `org.bukkit.event.server.ServerLoadEvent`
- [Official Paper Javadoc](https://jd.papermc.io/paper/1.16.5/org/bukkit/event/server/ServerLoadEvent.html)

## Python example

```python
from paperpybridge import Events

@bridge.on(Events.SERVER_LOAD)
def on_event(event):
    print(event.event, event.data)
```

## `data` fields

| Field | JSON type | Java getter | Java return type | Declared in |
| --- | --- | --- | --- | --- |
| `type` | string | `getType()` | `org.bukkit.event.server.ServerLoadEvent$LoadType` | `org.bukkit.event.server.ServerLoadEvent` |

[[Data-Format-en|Wire format and limits]] · [[Event-org-bukkit-event-server-serverloadevent|中文]]

If this event is not enabled, add its Java class or simple name to `events.include` in the Paper plugin configuration.
