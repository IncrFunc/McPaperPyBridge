# EntityBreedEvent

[[Home-en|Home]] / [[Category-entity-en|entity]]

- Java class: `org.bukkit.event.entity.EntityBreedEvent`
- Parent class: `org.bukkit.event.entity.EntityEvent`
- Python subscription: `EntityBreedEvent`
- Python constant: `Events.ENTITY_BREED`
- Cancellable: Yes
- Player available: Possible at runtime
- HandlerList owner: `org.bukkit.event.entity.EntityBreedEvent`
- [Official Paper Javadoc](https://jd.papermc.io/paper/1.16.5/org/bukkit/event/entity/EntityBreedEvent.html)

## Python example

```python
from paperpybridge import Events

@bridge.on(Events.ENTITY_BREED)
def on_event(event):
    print(event.event, event.data)
```

## `data` fields

| Field | JSON type | Java getter | Java return type | Declared in |
| --- | --- | --- | --- | --- |
| `bredWith` | item summary | `getBredWith()` | `org.bukkit.inventory.ItemStack` | `org.bukkit.event.entity.EntityBreedEvent` |
| `breeder` | entity summary | `getBreeder()` | `org.bukkit.entity.LivingEntity` | `org.bukkit.event.entity.EntityBreedEvent` |
| `entity` | entity summary | `getEntity()` | `org.bukkit.entity.LivingEntity` | `org.bukkit.event.entity.EntityBreedEvent` |
| `entityType` | string | `getEntityType()` | `org.bukkit.entity.EntityType` | `org.bukkit.event.entity.EntityEvent` |
| `experience` | number | `getExperience()` | `int` | `org.bukkit.event.entity.EntityBreedEvent` |
| `father` | entity summary | `getFather()` | `org.bukkit.entity.LivingEntity` | `org.bukkit.event.entity.EntityBreedEvent` |
| `mother` | entity summary | `getMother()` | `org.bukkit.entity.LivingEntity` | `org.bukkit.event.entity.EntityBreedEvent` |

[[Data-Format-en|Wire format and limits]] · [[Event-org-bukkit-event-entity-entitybreedevent|中文]]

If this event is not enabled, add its Java class or simple name to `events.include` in the Paper plugin configuration.
