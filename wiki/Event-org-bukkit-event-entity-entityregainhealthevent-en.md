# EntityRegainHealthEvent

[[Home-en|Home]] / [[Category-entity-en|entity]]

- Java class: `org.bukkit.event.entity.EntityRegainHealthEvent`
- Parent class: `org.bukkit.event.entity.EntityEvent`
- Python subscription: `EntityRegainHealthEvent`
- Python constant: `Events.ENTITY_REGAIN_HEALTH`
- Cancellable: Yes
- Player available: Possible at runtime
- HandlerList owner: `org.bukkit.event.entity.EntityRegainHealthEvent`
- [Official Paper Javadoc](https://jd.papermc.io/paper/1.16.5/org/bukkit/event/entity/EntityRegainHealthEvent.html)

## Python example

```python
from paperpybridge import Events

@bridge.on(Events.ENTITY_REGAIN_HEALTH)
def on_event(event):
    print(event.event, event.data)
```

## `data` fields

| Field | JSON type | Java getter | Java return type | Declared in |
| --- | --- | --- | --- | --- |
| `amount` | number | `getAmount()` | `double` | `org.bukkit.event.entity.EntityRegainHealthEvent` |
| `entity` | entity summary | `getEntity()` | `org.bukkit.entity.Entity` | `org.bukkit.event.entity.EntityEvent` |
| `entityType` | string | `getEntityType()` | `org.bukkit.entity.EntityType` | `org.bukkit.event.entity.EntityEvent` |
| `regainReason` | string | `getRegainReason()` | `org.bukkit.event.entity.EntityRegainHealthEvent$RegainReason` | `org.bukkit.event.entity.EntityRegainHealthEvent` |
| `fastRegen` | boolean | `isFastRegen()` | `boolean` | `org.bukkit.event.entity.EntityRegainHealthEvent` |

[[Data-Format-en|Wire format and limits]] · [[Event-org-bukkit-event-entity-entityregainhealthevent|中文]]

If this event is not enabled, add its Java class or simple name to `events.include` in the Paper plugin configuration.
