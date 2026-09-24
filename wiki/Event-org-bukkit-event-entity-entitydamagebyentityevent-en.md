# EntityDamageByEntityEvent

[[Home-en|Home]] / [[Category-entity-en|entity]]

- Java class: `org.bukkit.event.entity.EntityDamageByEntityEvent`
- Parent class: `org.bukkit.event.entity.EntityDamageEvent`
- Python subscription: `EntityDamageByEntityEvent`
- Python constant: `Events.ENTITY_DAMAGE_BY_ENTITY`
- Cancellable: Yes
- Player available: Possible at runtime
- HandlerList owner: `org.bukkit.event.entity.EntityDamageEvent`
- [Official Paper Javadoc](https://jd.papermc.io/paper/1.16.5/org/bukkit/event/entity/EntityDamageByEntityEvent.html)

## Python example

```python
from paperpybridge import Events

@bridge.on(Events.ENTITY_DAMAGE_BY_ENTITY)
def on_event(event):
    print(event.event, event.data)
```

## `data` fields

| Field | JSON type | Java getter | Java return type | Declared in |
| --- | --- | --- | --- | --- |
| `cause` | string | `getCause()` | `org.bukkit.event.entity.EntityDamageEvent$DamageCause` | `org.bukkit.event.entity.EntityDamageEvent` |
| `damage` | number | `getDamage()` | `double` | `org.bukkit.event.entity.EntityDamageEvent` |
| `damager` | entity summary | `getDamager()` | `org.bukkit.entity.Entity` | `org.bukkit.event.entity.EntityDamageByEntityEvent` |
| `entity` | entity summary | `getEntity()` | `org.bukkit.entity.Entity` | `org.bukkit.event.entity.EntityEvent` |
| `entityType` | string | `getEntityType()` | `org.bukkit.entity.EntityType` | `org.bukkit.event.entity.EntityEvent` |
| `finalDamage` | number | `getFinalDamage()` | `double` | `org.bukkit.event.entity.EntityDamageEvent` |

[[Data-Format-en|Wire format and limits]] · [[Event-org-bukkit-event-entity-entitydamagebyentityevent|中文]]

If this event is not enabled, add its Java class or simple name to `events.include` in the Paper plugin configuration.
