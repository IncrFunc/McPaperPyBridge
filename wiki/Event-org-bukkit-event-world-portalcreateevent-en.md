# PortalCreateEvent

[[Home-en|Home]] / [[Category-world-en|world]]

- Java class: `org.bukkit.event.world.PortalCreateEvent`
- Parent class: `org.bukkit.event.world.WorldEvent`
- Python subscription: `PortalCreateEvent`
- Python constant: `Events.PORTAL_CREATE`
- Cancellable: Yes
- Player available: Possible at runtime
- HandlerList owner: `org.bukkit.event.world.PortalCreateEvent`
- [Official Paper Javadoc](https://jd.papermc.io/paper/1.16.5/org/bukkit/event/world/PortalCreateEvent.html)

## Python example

```python
from paperpybridge import Events

@bridge.on(Events.PORTAL_CREATE)
def on_event(event):
    print(event.event, event.data)
```

## `data` fields

| Field | JSON type | Java getter | Java return type | Declared in |
| --- | --- | --- | --- | --- |
| `entity` | entity summary | `getEntity()` | `org.bukkit.entity.Entity` | `org.bukkit.event.world.PortalCreateEvent` |
| `reason` | string | `getReason()` | `org.bukkit.event.world.PortalCreateEvent$CreateReason` | `org.bukkit.event.world.PortalCreateEvent` |
| `world` | world summary | `getWorld()` | `org.bukkit.World` | `org.bukkit.event.world.WorldEvent` |

[[Data-Format-en|Wire format and limits]] · [[Event-org-bukkit-event-world-portalcreateevent|中文]]

If this event is not enabled, add its Java class or simple name to `events.include` in the Paper plugin configuration.
