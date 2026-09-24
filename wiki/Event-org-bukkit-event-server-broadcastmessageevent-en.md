# BroadcastMessageEvent

[[Home-en|Home]] / [[Category-server-en|server]]

- Java class: `org.bukkit.event.server.BroadcastMessageEvent`
- Parent class: `org.bukkit.event.server.ServerEvent`
- Python subscription: `BroadcastMessageEvent`
- Python constant: `Events.BROADCAST_MESSAGE`
- Cancellable: Yes
- Player available: No known player getter
- HandlerList owner: `org.bukkit.event.server.BroadcastMessageEvent`
- [Official Paper Javadoc](https://jd.papermc.io/paper/1.16.5/org/bukkit/event/server/BroadcastMessageEvent.html)

## Python example

```python
from paperpybridge import Events

@bridge.on(Events.BROADCAST_MESSAGE)
def on_event(event):
    print(event.event, event.data)
```

## `data` fields

| Field | JSON type | Java getter | Java return type | Declared in |
| --- | --- | --- | --- | --- |
| `message` | string | `getMessage()` | `java.lang.String` | `org.bukkit.event.server.BroadcastMessageEvent` |

[[Data-Format-en|Wire format and limits]] · [[Event-org-bukkit-event-server-broadcastmessageevent|中文]]

If this event is not enabled, add its Java class or simple name to `events.include` in the Paper plugin configuration.
