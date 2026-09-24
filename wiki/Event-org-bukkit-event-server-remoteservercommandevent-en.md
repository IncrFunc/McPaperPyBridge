# RemoteServerCommandEvent

[[Home-en|Home]] / [[Category-server-en|server]]

- Java class: `org.bukkit.event.server.RemoteServerCommandEvent`
- Parent class: `org.bukkit.event.server.ServerCommandEvent`
- Python subscription: `RemoteServerCommandEvent`
- Python constant: `Events.REMOTE_SERVER_COMMAND`
- Cancellable: Yes
- Player available: No known player getter
- HandlerList owner: `org.bukkit.event.server.RemoteServerCommandEvent`
- [Official Paper Javadoc](https://jd.papermc.io/paper/1.16.5/org/bukkit/event/server/RemoteServerCommandEvent.html)

## Python example

```python
from paperpybridge import Events

@bridge.on(Events.REMOTE_SERVER_COMMAND)
def on_event(event):
    print(event.event, event.data)
```

## `data` fields

| Field | JSON type | Java getter | Java return type | Declared in |
| --- | --- | --- | --- | --- |
| `command` | string | `getCommand()` | `java.lang.String` | `org.bukkit.event.server.ServerCommandEvent` |

[[Data-Format-en|Wire format and limits]] · [[Event-org-bukkit-event-server-remoteservercommandevent|中文]]

If this event is not enabled, add its Java class or simple name to `events.include` in the Paper plugin configuration.
