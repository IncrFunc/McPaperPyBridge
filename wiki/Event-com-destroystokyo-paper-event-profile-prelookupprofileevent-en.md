# PreLookupProfileEvent

[[Home-en|Home]] / [[Category-profile-en|profile]]

- Java class: `com.destroystokyo.paper.event.profile.PreLookupProfileEvent`
- Parent class: `org.bukkit.event.Event`
- Python subscription: `PreLookupProfileEvent`
- Python constant: `Events.PRE_LOOKUP_PROFILE`
- Cancellable: No
- Player available: No known player getter
- HandlerList owner: `com.destroystokyo.paper.event.profile.PreLookupProfileEvent`
- [Official Paper Javadoc](https://jd.papermc.io/paper/1.16.5/com/destroystokyo/paper/event/profile/PreLookupProfileEvent.html)

## Python example

```python
from paperpybridge import Events

@bridge.on(Events.PRE_LOOKUP_PROFILE)
def on_event(event):
    print(event.event, event.data)
```

## `data` fields

| Field | JSON type | Java getter | Java return type | Declared in |
| --- | --- | --- | --- | --- |
| `name` | string | `getName()` | `java.lang.String` | `com.destroystokyo.paper.event.profile.PreLookupProfileEvent` |
| `uUID` | string | `getUUID()` | `java.util.UUID` | `com.destroystokyo.paper.event.profile.PreLookupProfileEvent` |

[[Data-Format-en|Wire format and limits]] · [[Event-com-destroystokyo-paper-event-profile-prelookupprofileevent|中文]]

If this event is not enabled, add its Java class or simple name to `events.include` in the Paper plugin configuration.
