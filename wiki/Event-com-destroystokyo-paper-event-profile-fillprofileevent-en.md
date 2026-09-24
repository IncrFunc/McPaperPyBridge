# FillProfileEvent

[[Home-en|Home]] / [[Category-profile-en|profile]]

- Java class: `com.destroystokyo.paper.event.profile.FillProfileEvent`
- Parent class: `org.bukkit.event.Event`
- Python subscription: `FillProfileEvent`
- Python constant: `Events.FILL_PROFILE`
- Cancellable: No
- Player available: No known player getter
- HandlerList owner: `com.destroystokyo.paper.event.profile.FillProfileEvent`
- [Official Paper Javadoc](https://jd.papermc.io/paper/1.16.5/com/destroystokyo/paper/event/profile/FillProfileEvent.html)

## Python example

```python
from paperpybridge import Events

@bridge.on(Events.FILL_PROFILE)
def on_event(event):
    print(event.event, event.data)
```

## `data` fields

No supported serializable fields; common event fields are still sent.

[[Data-Format-en|Wire format and limits]] · [[Event-com-destroystokyo-paper-event-profile-fillprofileevent|中文]]

If this event is not enabled, add its Java class or simple name to `events.include` in the Paper plugin configuration.
