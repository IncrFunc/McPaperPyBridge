# EntityCreatePortalEvent

[[Home-en|Home]] / [[Category-entity-en|entity]]

- Java class: `org.bukkit.event.entity.EntityCreatePortalEvent`
- Parent class: `org.bukkit.event.entity.EntityEvent`
- Python subscription: `EntityCreatePortalEvent`
- Python constant: `Events.ENTITY_CREATE_PORTAL`
- Cancellable: Yes
- Player available: Possible at runtime
- HandlerList owner: `org.bukkit.event.entity.EntityCreatePortalEvent`
- [Official Paper Javadoc](https://jd.papermc.io/paper/1.16.5/org/bukkit/event/entity/EntityCreatePortalEvent.html)

## Python example

```python
from paperpybridge import Events

@bridge.on(Events.ENTITY_CREATE_PORTAL)
def on_event(event):
    print(event.event, event.data)
```

## `data` fields

| Field | JSON type | Java getter | Java return type | Declared in |
| --- | --- | --- | --- | --- |
| `entity` | entity summary | `getEntity()` | `org.bukkit.entity.Entity` | `org.bukkit.event.entity.EntityCreatePortalEvent` |
| `entityType` | string | `getEntityType()` | `org.bukkit.entity.EntityType` | `org.bukkit.event.entity.EntityEvent` |
| `portalType` | string | `getPortalType()` | `org.bukkit.PortalType` | `org.bukkit.event.entity.EntityCreatePortalEvent` |

[[Data-Format-en|Wire format and limits]] · [[Event-org-bukkit-event-entity-entitycreateportalevent|中文]]

If this event is not enabled, add its Java class or simple name to `events.include` in the Paper plugin configuration.
