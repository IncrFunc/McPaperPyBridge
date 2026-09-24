# ElderGuardianAppearanceEvent

[[Home-en|Home]] / [[Category-entity-en|entity]]

- Java class: `io.papermc.paper.event.entity.ElderGuardianAppearanceEvent`
- Parent class: `org.bukkit.event.entity.EntityEvent`
- Python subscription: `ElderGuardianAppearanceEvent`
- Python constant: `Events.ELDER_GUARDIAN_APPEARANCE`
- Cancellable: Yes
- Player available: Possible at runtime
- HandlerList owner: `io.papermc.paper.event.entity.ElderGuardianAppearanceEvent`
- [Official Paper Javadoc](https://jd.papermc.io/paper/1.16.5/io/papermc/paper/event/entity/ElderGuardianAppearanceEvent.html)

## Python example

```python
from paperpybridge import Events

@bridge.on(Events.ELDER_GUARDIAN_APPEARANCE)
def on_event(event):
    print(event.event, event.data)
```

## `data` fields

| Field | JSON type | Java getter | Java return type | Declared in |
| --- | --- | --- | --- | --- |
| `affectedPlayer` | entity summary | `getAffectedPlayer()` | `org.bukkit.entity.Player` | `io.papermc.paper.event.entity.ElderGuardianAppearanceEvent` |
| `entity` | entity summary | `getEntity()` | `org.bukkit.entity.Entity` | `io.papermc.paper.event.entity.ElderGuardianAppearanceEvent` |
| `entityType` | string | `getEntityType()` | `org.bukkit.entity.EntityType` | `org.bukkit.event.entity.EntityEvent` |

[[Data-Format-en|Wire format and limits]] · [[Event-io-papermc-paper-event-entity-elderguardianappearanceevent|中文]]

If this event is not enabled, add its Java class or simple name to `events.include` in the Paper plugin configuration.
