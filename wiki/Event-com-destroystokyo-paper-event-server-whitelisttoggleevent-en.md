# WhitelistToggleEvent

[[Home-en|Home]] / [[Category-server-en|server]]

- Java class: `com.destroystokyo.paper.event.server.WhitelistToggleEvent`
- Parent class: `org.bukkit.event.Event`
- Python subscription: `WhitelistToggleEvent`
- Python constant: `Events.WHITELIST_TOGGLE`
- Cancellable: No
- Player available: No known player getter
- HandlerList owner: `com.destroystokyo.paper.event.server.WhitelistToggleEvent`
- [Official Paper Javadoc](https://jd.papermc.io/paper/1.16.5/com/destroystokyo/paper/event/server/WhitelistToggleEvent.html)

## Python example

```python
from paperpybridge import Events

@bridge.on(Events.WHITELIST_TOGGLE)
def on_event(event):
    print(event.event, event.data)
```

## `data` fields

| Field | JSON type | Java getter | Java return type | Declared in |
| --- | --- | --- | --- | --- |
| `enabled` | boolean | `isEnabled()` | `boolean` | `com.destroystokyo.paper.event.server.WhitelistToggleEvent` |

[[Data-Format-en|Wire format and limits]] · [[Event-com-destroystokyo-paper-event-server-whitelisttoggleevent|中文]]

If this event is not enabled, add its Java class or simple name to `events.include` in the Paper plugin configuration.
