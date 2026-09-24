# EntityTeleportEndGatewayEvent

[[Home-en|Home]] / [[Category-entity-en|entity]]

- Java class: `com.destroystokyo.paper.event.entity.EntityTeleportEndGatewayEvent`
- Parent class: `org.bukkit.event.entity.EntityTeleportEvent`
- Python subscription: `EntityTeleportEndGatewayEvent`
- Python constant: `Events.ENTITY_TELEPORT_END_GATEWAY`
- Cancellable: Yes
- Player available: Possible at runtime
- HandlerList owner: `org.bukkit.event.entity.EntityTeleportEvent`
- [Official Paper Javadoc](https://jd.papermc.io/paper/1.16.5/com/destroystokyo/paper/event/entity/EntityTeleportEndGatewayEvent.html)

## Python example

```python
from paperpybridge import Events

@bridge.on(Events.ENTITY_TELEPORT_END_GATEWAY)
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

[[Data-Format-en|Wire format and limits]] · [[Event-com-destroystokyo-paper-event-entity-entityteleportendgatewayevent|中文]]

If this event is not enabled, add its Java class or simple name to `events.include` in the Paper plugin configuration.
