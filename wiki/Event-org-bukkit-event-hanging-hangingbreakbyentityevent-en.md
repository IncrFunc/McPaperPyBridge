# HangingBreakByEntityEvent

[[Home-en|Home]] / [[Category-hanging-en|hanging]]

- Java class: `org.bukkit.event.hanging.HangingBreakByEntityEvent`
- Parent class: `org.bukkit.event.hanging.HangingBreakEvent`
- Python subscription: `HangingBreakByEntityEvent`
- Python constant: `Events.HANGING_BREAK_BY_ENTITY`
- Cancellable: Yes
- Player available: Possible at runtime
- HandlerList owner: `org.bukkit.event.hanging.HangingBreakEvent`
- [Official Paper Javadoc](https://jd.papermc.io/paper/1.16.5/org/bukkit/event/hanging/HangingBreakByEntityEvent.html)

## Python example

```python
from paperpybridge import Events

@bridge.on(Events.HANGING_BREAK_BY_ENTITY)
def on_event(event):
    print(event.event, event.data)
```

## `data` fields

| Field | JSON type | Java getter | Java return type | Declared in |
| --- | --- | --- | --- | --- |
| `cause` | string | `getCause()` | `org.bukkit.event.hanging.HangingBreakEvent$RemoveCause` | `org.bukkit.event.hanging.HangingBreakEvent` |
| `entity` | entity summary | `getEntity()` | `org.bukkit.entity.Hanging` | `org.bukkit.event.hanging.HangingEvent` |
| `remover` | entity summary | `getRemover()` | `org.bukkit.entity.Entity` | `org.bukkit.event.hanging.HangingBreakByEntityEvent` |

[[Data-Format-en|Wire format and limits]] · [[Event-org-bukkit-event-hanging-hangingbreakbyentityevent|中文]]

If this event is not enabled, add its Java class or simple name to `events.include` in the Paper plugin configuration.
