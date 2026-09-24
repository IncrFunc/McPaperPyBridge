# EnderDragonChangePhaseEvent

[[Home-en|Home]] / [[Category-entity-en|entity]]

- Java class: `org.bukkit.event.entity.EnderDragonChangePhaseEvent`
- Parent class: `org.bukkit.event.entity.EntityEvent`
- Python subscription: `EnderDragonChangePhaseEvent`
- Python constant: `Events.ENDER_DRAGON_CHANGE_PHASE`
- Cancellable: Yes
- Player available: Possible at runtime
- HandlerList owner: `org.bukkit.event.entity.EnderDragonChangePhaseEvent`
- [Official Paper Javadoc](https://jd.papermc.io/paper/1.16.5/org/bukkit/event/entity/EnderDragonChangePhaseEvent.html)

## Python example

```python
from paperpybridge import Events

@bridge.on(Events.ENDER_DRAGON_CHANGE_PHASE)
def on_event(event):
    print(event.event, event.data)
```

## `data` fields

| Field | JSON type | Java getter | Java return type | Declared in |
| --- | --- | --- | --- | --- |
| `currentPhase` | string | `getCurrentPhase()` | `org.bukkit.entity.EnderDragon$Phase` | `org.bukkit.event.entity.EnderDragonChangePhaseEvent` |
| `entity` | entity summary | `getEntity()` | `org.bukkit.entity.EnderDragon` | `org.bukkit.event.entity.EnderDragonChangePhaseEvent` |
| `entityType` | string | `getEntityType()` | `org.bukkit.entity.EntityType` | `org.bukkit.event.entity.EntityEvent` |
| `newPhase` | string | `getNewPhase()` | `org.bukkit.entity.EnderDragon$Phase` | `org.bukkit.event.entity.EnderDragonChangePhaseEvent` |

[[Data-Format-en|Wire format and limits]] · [[Event-org-bukkit-event-entity-enderdragonchangephaseevent|中文]]

If this event is not enabled, add its Java class or simple name to `events.include` in the Paper plugin configuration.
