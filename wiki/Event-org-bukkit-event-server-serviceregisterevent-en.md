# ServiceRegisterEvent

[[Home-en|Home]] / [[Category-server-en|server]]

- Java class: `org.bukkit.event.server.ServiceRegisterEvent`
- Parent class: `org.bukkit.event.server.ServiceEvent`
- Python subscription: `ServiceRegisterEvent`
- Python constant: `Events.SERVICE_REGISTER`
- Cancellable: No
- Player available: No known player getter
- HandlerList owner: `org.bukkit.event.server.ServiceRegisterEvent`
- [Official Paper Javadoc](https://jd.papermc.io/paper/1.16.5/org/bukkit/event/server/ServiceRegisterEvent.html)

## Python example

```python
from paperpybridge import Events

@bridge.on(Events.SERVICE_REGISTER)
def on_event(event):
    print(event.event, event.data)
```

## `data` fields

No supported serializable fields; common event fields are still sent.

[[Data-Format-en|Wire format and limits]] · [[Event-org-bukkit-event-server-serviceregisterevent|中文]]

If this event is not enabled, add its Java class or simple name to `events.include` in the Paper plugin configuration.
