# PluginDisableEvent

[[Home-en|Home]] / [[Category-server-en|server]]

- Java class: `org.bukkit.event.server.PluginDisableEvent`
- Parent class: `org.bukkit.event.server.PluginEvent`
- Python subscription: `PluginDisableEvent`
- Python constant: `Events.PLUGIN_DISABLE`
- Cancellable: No
- Player available: No known player getter
- HandlerList owner: `org.bukkit.event.server.PluginDisableEvent`
- [Official Paper Javadoc](https://jd.papermc.io/paper/1.16.5/org/bukkit/event/server/PluginDisableEvent.html)

## Python example

```python
from paperpybridge import Events

@bridge.on(Events.PLUGIN_DISABLE)
def on_event(event):
    print(event.event, event.data)
```

## `data` fields

No supported serializable fields; common event fields are still sent.

[[Data-Format-en|Wire format and limits]] · [[Event-org-bukkit-event-server-plugindisableevent|中文]]

If this event is not enabled, add its Java class or simple name to `events.include` in the Paper plugin configuration.
