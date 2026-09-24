# CreeperPowerEvent

[[Home-en|Home]] / [[Category-entity-en|entity]]

- Java class: `org.bukkit.event.entity.CreeperPowerEvent`
- Parent class: `org.bukkit.event.entity.EntityEvent`
- Python subscription: `CreeperPowerEvent`
- Python constant: `Events.CREEPER_POWER`
- Cancellable: Yes
- Player available: Possible at runtime
- HandlerList owner: `org.bukkit.event.entity.CreeperPowerEvent`
- [Official Paper Javadoc](https://jd.papermc.io/paper/1.16.5/org/bukkit/event/entity/CreeperPowerEvent.html)

## Python example

```python
from paperpybridge import Events

@bridge.on(Events.CREEPER_POWER)
def on_event(event):
    print(event.event, event.data)
```

## `data` fields

| Field | JSON type | Java getter | Java return type | Declared in |
| --- | --- | --- | --- | --- |
| `cause` | string | `getCause()` | `org.bukkit.event.entity.CreeperPowerEvent$PowerCause` | `org.bukkit.event.entity.CreeperPowerEvent` |
| `entity` | entity summary | `getEntity()` | `org.bukkit.entity.Creeper` | `org.bukkit.event.entity.CreeperPowerEvent` |
| `entityType` | string | `getEntityType()` | `org.bukkit.entity.EntityType` | `org.bukkit.event.entity.EntityEvent` |
| `lightning` | entity summary | `getLightning()` | `org.bukkit.entity.LightningStrike` | `org.bukkit.event.entity.CreeperPowerEvent` |

[[Data-Format-en|Wire format and limits]] · [[Event-org-bukkit-event-entity-creeperpowerevent|中文]]

If this event is not enabled, add its Java class or simple name to `events.include` in the Paper plugin configuration.
