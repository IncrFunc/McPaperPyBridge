# TabCompleteEvent

[[Home-en|Home]] / [[Category-server-en|server]]

- Java class: `org.bukkit.event.server.TabCompleteEvent`
- Parent class: `org.bukkit.event.Event`
- Python subscription: `TabCompleteEvent`
- Python constant: `Events.TAB_COMPLETE`
- Cancellable: Yes
- Player available: No known player getter
- HandlerList owner: `org.bukkit.event.server.TabCompleteEvent`
- [Official Paper Javadoc](https://jd.papermc.io/paper/1.16.5/org/bukkit/event/server/TabCompleteEvent.html)

## Python example

```python
from paperpybridge import Events

@bridge.on(Events.TAB_COMPLETE)
def on_event(event):
    print(event.event, event.data)
```

## `data` fields

| Field | JSON type | Java getter | Java return type | Declared in |
| --- | --- | --- | --- | --- |
| `buffer` | string | `getBuffer()` | `java.lang.String` | `org.bukkit.event.server.TabCompleteEvent` |
| `location` | location summary | `getLocation()` | `org.bukkit.Location` | `org.bukkit.event.server.TabCompleteEvent` |
| `command` | boolean | `isCommand()` | `boolean` | `org.bukkit.event.server.TabCompleteEvent` |

[[Data-Format-en|Wire format and limits]] · [[Event-org-bukkit-event-server-tabcompleteevent|中文]]

If this event is not enabled, add its Java class or simple name to `events.include` in the Paper plugin configuration.
