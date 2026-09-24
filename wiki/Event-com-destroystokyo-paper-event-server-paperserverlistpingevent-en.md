# PaperServerListPingEvent

[[Home-en|Home]] / [[Category-server-en|server]]

- Java class: `com.destroystokyo.paper.event.server.PaperServerListPingEvent`
- Parent class: `org.bukkit.event.server.ServerListPingEvent`
- Python subscription: `PaperServerListPingEvent`
- Python constant: `Events.PAPER_SERVER_LIST_PING`
- Cancellable: Yes
- Player available: No known player getter
- HandlerList owner: `org.bukkit.event.server.ServerListPingEvent`
- [Official Paper Javadoc](https://jd.papermc.io/paper/1.16.5/com/destroystokyo/paper/event/server/PaperServerListPingEvent.html)

## Python example

```python
from paperpybridge import Events

@bridge.on(Events.PAPER_SERVER_LIST_PING)
def on_event(event):
    print(event.event, event.data)
```

## `data` fields

| Field | JSON type | Java getter | Java return type | Declared in |
| --- | --- | --- | --- | --- |
| `maxPlayers` | number | `getMaxPlayers()` | `int` | `com.destroystokyo.paper.event.server.PaperServerListPingEvent` |
| `motd` | string | `getMotd()` | `java.lang.String` | `org.bukkit.event.server.ServerListPingEvent` |
| `numPlayers` | number | `getNumPlayers()` | `int` | `com.destroystokyo.paper.event.server.PaperServerListPingEvent` |
| `protocolVersion` | number | `getProtocolVersion()` | `int` | `com.destroystokyo.paper.event.server.PaperServerListPingEvent` |
| `version` | string | `getVersion()` | `java.lang.String` | `com.destroystokyo.paper.event.server.PaperServerListPingEvent` |

[[Data-Format-en|Wire format and limits]] · [[Event-com-destroystokyo-paper-event-server-paperserverlistpingevent|中文]]

If this event is not enabled, add its Java class or simple name to `events.include` in the Paper plugin configuration.
