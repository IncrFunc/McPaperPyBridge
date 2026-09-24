# ServiceUnregisterEvent

[[Home-en|Home]] / [[Category-server-en|server]]

- Java class: `org.bukkit.event.server.ServiceUnregisterEvent`
- Parent class: `org.bukkit.event.server.ServiceEvent`
- Python subscription: `ServiceUnregisterEvent`
- Python constant: `Events.SERVICE_UNREGISTER`
- Cancellable: No
- Player available: No known player getter
- HandlerList owner: `org.bukkit.event.server.ServiceUnregisterEvent`
- [Official Paper Javadoc](https://jd.papermc.io/paper/1.16.5/org/bukkit/event/server/ServiceUnregisterEvent.html)

## Python example

```python
from paperpybridge import Events

@bridge.on(Events.SERVICE_UNREGISTER)
def on_event(event):
    print(event.event, event.data)
```

## `data` fields

No supported serializable fields; common event fields are still sent.

[[Data-Format-en|Wire format and limits]] · [[Event-org-bukkit-event-server-serviceunregisterevent|中文]]

If this event is not enabled, add its Java class or simple name to `events.include` in the Paper plugin configuration.
