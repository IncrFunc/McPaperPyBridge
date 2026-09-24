# ServerListPingEvent

[[Home-en|Home]] / [[Category-server-en|server]]

- Java class: `org.bukkit.event.server.ServerListPingEvent`
- Parent class: `org.bukkit.event.server.ServerEvent`
- Python subscription: `ServerListPingEvent`
- Python constant: `Events.SERVER_LIST_PING`
- Cancellable: No
- Player available: No known player getter
- HandlerList owner: `org.bukkit.event.server.ServerListPingEvent`
- [Official Paper Javadoc](https://jd.papermc.io/paper/1.16.5/org/bukkit/event/server/ServerListPingEvent.html)

## Python example

```python
from paperpybridge import Events

@bridge.on(Events.SERVER_LIST_PING)
def on_event(event):
    print(event.event, event.data)
```

## `data` fields

| Field | JSON type | Java getter | Java return type | Declared in |
| --- | --- | --- | --- | --- |
| `maxPlayers` | number | `getMaxPlayers()` | `int` | `org.bukkit.event.server.ServerListPingEvent` |
| `motd` | string | `getMotd()` | `java.lang.String` | `org.bukkit.event.server.ServerListPingEvent` |
| `numPlayers` | number | `getNumPlayers()` | `int` | `org.bukkit.event.server.ServerListPingEvent` |

[[Data-Format-en|Wire format and limits]] · [[Event-org-bukkit-event-server-serverlistpingevent|中文]]

If this event is not enabled, add its Java class or simple name to `events.include` in the Paper plugin configuration.
