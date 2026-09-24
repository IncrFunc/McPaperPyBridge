# EntityTeleportEvent

[[Home-en|Home]] / [[Category-entity-en|entity]]

- Java class: `org.bukkit.event.entity.EntityTeleportEvent`
- Parent class: `org.bukkit.event.entity.EntityEvent`
- Python subscription: `EntityTeleportEvent`
- Python constant: `Events.ENTITY_TELEPORT`
- Cancellable: Yes
- Player available: Possible at runtime
- HandlerList owner: `org.bukkit.event.entity.EntityTeleportEvent`
- [Official Paper Javadoc](https://jd.papermc.io/paper/1.16.5/org/bukkit/event/entity/EntityTeleportEvent.html)

## Python example

```python
from paperpybridge import Events

@bridge.on(Events.ENTITY_TELEPORT)
def on_event(event):
    print(event.event, event.data)
```

## `data` fields

| Field | JSON type | Java getter | Java return type | Declared in |
| --- | --- | --- | --- | --- |
| `entity` | entity summary | `getEntity()` | `org.bukkit.entity.Entity` | `org.bukkit.event.entity.EntityEvent` |
| `entityType` | string | `getEntityType()` | `org.bukkit.entity.EntityType` | `org.bukkit.event.entity.EntityEvent` |
| `from` | location summary | `getFrom()` | `org.bukkit.Location` | `org.bukkit.event.entity.EntityTeleportEvent` |
| `to` | location summary | `getTo()` | `org.bukkit.Location` | `org.bukkit.event.entity.EntityTeleportEvent` |

[[Data-Format-en|Wire format and limits]] · [[Event-org-bukkit-event-entity-entityteleportevent|中文]]

If this event is not enabled, add its Java class or simple name to `events.include` in the Paper plugin configuration.
