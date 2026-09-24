# PiglinBarterEvent

[[Home-en|Home]] / [[Category-entity-en|entity]]

- Java class: `org.bukkit.event.entity.PiglinBarterEvent`
- Parent class: `org.bukkit.event.entity.EntityEvent`
- Python subscription: `PiglinBarterEvent`
- Python constant: `Events.PIGLIN_BARTER`
- Cancellable: Yes
- Player available: Possible at runtime
- HandlerList owner: `org.bukkit.event.entity.PiglinBarterEvent`
- [Official Paper Javadoc](https://jd.papermc.io/paper/1.16.5/org/bukkit/event/entity/PiglinBarterEvent.html)

## Python example

```python
from paperpybridge import Events

@bridge.on(Events.PIGLIN_BARTER)
def on_event(event):
    print(event.event, event.data)
```

## `data` fields

| Field | JSON type | Java getter | Java return type | Declared in |
| --- | --- | --- | --- | --- |
| `entity` | entity summary | `getEntity()` | `org.bukkit.entity.Piglin` | `org.bukkit.event.entity.PiglinBarterEvent` |
| `entityType` | string | `getEntityType()` | `org.bukkit.entity.EntityType` | `org.bukkit.event.entity.EntityEvent` |
| `input` | item summary | `getInput()` | `org.bukkit.inventory.ItemStack` | `org.bukkit.event.entity.PiglinBarterEvent` |

[[Data-Format-en|Wire format and limits]] · [[Event-org-bukkit-event-entity-piglinbarterevent|中文]]

If this event is not enabled, add its Java class or simple name to `events.include` in the Paper plugin configuration.
