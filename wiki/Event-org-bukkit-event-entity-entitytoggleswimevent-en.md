# EntityToggleSwimEvent

[[Home-en|Home]] / [[Category-entity-en|entity]]

- Java class: `org.bukkit.event.entity.EntityToggleSwimEvent`
- Parent class: `org.bukkit.event.entity.EntityEvent`
- Python subscription: `EntityToggleSwimEvent`
- Python constant: `Events.ENTITY_TOGGLE_SWIM`
- Cancellable: Yes
- Player available: Possible at runtime
- HandlerList owner: `org.bukkit.event.entity.EntityToggleSwimEvent`
- [Official Paper Javadoc](https://jd.papermc.io/paper/1.16.5/org/bukkit/event/entity/EntityToggleSwimEvent.html)

## Python example

```python
from paperpybridge import Events

@bridge.on(Events.ENTITY_TOGGLE_SWIM)
def on_event(event):
    print(event.event, event.data)
```

## `data` fields

| Field | JSON type | Java getter | Java return type | Declared in |
| --- | --- | --- | --- | --- |
| `entity` | entity summary | `getEntity()` | `org.bukkit.entity.Entity` | `org.bukkit.event.entity.EntityEvent` |
| `entityType` | string | `getEntityType()` | `org.bukkit.entity.EntityType` | `org.bukkit.event.entity.EntityEvent` |
| `swimming` | boolean | `isSwimming()` | `boolean` | `org.bukkit.event.entity.EntityToggleSwimEvent` |

[[Data-Format-en|Wire format and limits]] · [[Event-org-bukkit-event-entity-entitytoggleswimevent|中文]]

If this event is not enabled, add its Java class or simple name to `events.include` in the Paper plugin configuration.
