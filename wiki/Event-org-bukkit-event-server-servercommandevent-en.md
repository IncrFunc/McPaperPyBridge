# ServerCommandEvent

[[Home-en|Home]] / [[Category-server-en|server]]

- Java class: `org.bukkit.event.server.ServerCommandEvent`
- Parent class: `org.bukkit.event.server.ServerEvent`
- Python subscription: `ServerCommandEvent`
- Python constant: `Events.SERVER_COMMAND`
- Cancellable: Yes
- Player available: No known player getter
- HandlerList owner: `org.bukkit.event.server.ServerCommandEvent`
- [Official Paper Javadoc](https://jd.papermc.io/paper/1.16.5/org/bukkit/event/server/ServerCommandEvent.html)

## Python example

```python
from paperpybridge import Events

@bridge.on(Events.SERVER_COMMAND)
def on_event(event):
    print(event.event, event.data)
```

## `data` fields

| Field | JSON type | Java getter | Java return type | Declared in |
| --- | --- | --- | --- | --- |
| `command` | string | `getCommand()` | `java.lang.String` | `org.bukkit.event.server.ServerCommandEvent` |

[[Data-Format-en|Wire format and limits]] · [[Event-org-bukkit-event-server-servercommandevent|中文]]

If this event is not enabled, add its Java class or simple name to `events.include` in the Paper plugin configuration.
