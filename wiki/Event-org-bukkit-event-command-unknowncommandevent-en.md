# UnknownCommandEvent

[[Home-en|Home]] / [[Category-command-en|command]]

- Java class: `org.bukkit.event.command.UnknownCommandEvent`
- Parent class: `org.bukkit.event.Event`
- Python subscription: `UnknownCommandEvent`
- Python constant: `Events.UNKNOWN_COMMAND`
- Cancellable: No
- Player available: No known player getter
- HandlerList owner: `org.bukkit.event.command.UnknownCommandEvent`
- [Official Paper Javadoc](https://jd.papermc.io/paper/1.16.5/org/bukkit/event/command/UnknownCommandEvent.html)

## Python example

```python
from paperpybridge import Events

@bridge.on(Events.UNKNOWN_COMMAND)
def on_event(event):
    print(event.event, event.data)
```

## `data` fields

| Field | JSON type | Java getter | Java return type | Declared in |
| --- | --- | --- | --- | --- |
| `commandLine` | string | `getCommandLine()` | `java.lang.String` | `org.bukkit.event.command.UnknownCommandEvent` |
| `message` | string | `getMessage()` | `java.lang.String` | `org.bukkit.event.command.UnknownCommandEvent` |

[[Data-Format-en|Wire format and limits]] · [[Event-org-bukkit-event-command-unknowncommandevent|中文]]

If this event is not enabled, add its Java class or simple name to `events.include` in the Paper plugin configuration.
