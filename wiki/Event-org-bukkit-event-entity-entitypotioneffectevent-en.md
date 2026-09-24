# EntityPotionEffectEvent

[[Home-en|Home]] / [[Category-entity-en|entity]]

- Java class: `org.bukkit.event.entity.EntityPotionEffectEvent`
- Parent class: `org.bukkit.event.entity.EntityEvent`
- Python subscription: `EntityPotionEffectEvent`
- Python constant: `Events.ENTITY_POTION_EFFECT`
- Cancellable: Yes
- Player available: Possible at runtime
- HandlerList owner: `org.bukkit.event.entity.EntityPotionEffectEvent`
- [Official Paper Javadoc](https://jd.papermc.io/paper/1.16.5/org/bukkit/event/entity/EntityPotionEffectEvent.html)

## Python example

```python
from paperpybridge import Events

@bridge.on(Events.ENTITY_POTION_EFFECT)
def on_event(event):
    print(event.event, event.data)
```

## `data` fields

| Field | JSON type | Java getter | Java return type | Declared in |
| --- | --- | --- | --- | --- |
| `action` | string | `getAction()` | `org.bukkit.event.entity.EntityPotionEffectEvent$Action` | `org.bukkit.event.entity.EntityPotionEffectEvent` |
| `cause` | string | `getCause()` | `org.bukkit.event.entity.EntityPotionEffectEvent$Cause` | `org.bukkit.event.entity.EntityPotionEffectEvent` |
| `entity` | entity summary | `getEntity()` | `org.bukkit.entity.Entity` | `org.bukkit.event.entity.EntityEvent` |
| `entityType` | string | `getEntityType()` | `org.bukkit.entity.EntityType` | `org.bukkit.event.entity.EntityEvent` |
| `override` | boolean | `isOverride()` | `boolean` | `org.bukkit.event.entity.EntityPotionEffectEvent` |

[[Data-Format-en|Wire format and limits]] · [[Event-org-bukkit-event-entity-entitypotioneffectevent|中文]]

If this event is not enabled, add its Java class or simple name to `events.include` in the Paper plugin configuration.
