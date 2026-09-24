# EntityToggleGlideEvent

[[Home-en|Home]] / [[Category-entity-en|entity]]

- Java class: `org.bukkit.event.entity.EntityToggleGlideEvent`
- Parent class: `org.bukkit.event.entity.EntityEvent`
- Python subscription: `EntityToggleGlideEvent`
- Python constant: `Events.ENTITY_TOGGLE_GLIDE`
- Cancellable: Yes
- Player available: Possible at runtime
- HandlerList owner: `org.bukkit.event.entity.EntityToggleGlideEvent`
- [Official Paper Javadoc](https://jd.papermc.io/paper/1.16.5/org/bukkit/event/entity/EntityToggleGlideEvent.html)

## Python example

```python
from paperpybridge import Events

@bridge.on(Events.ENTITY_TOGGLE_GLIDE)
def on_event(event):
    print(event.event, event.data)
```

## `data` fields

| Field | JSON type | Java getter | Java return type | Declared in |
| --- | --- | --- | --- | --- |
| `entity` | entity summary | `getEntity()` | `org.bukkit.entity.Entity` | `org.bukkit.event.entity.EntityEvent` |
| `entityType` | string | `getEntityType()` | `org.bukkit.entity.EntityType` | `org.bukkit.event.entity.EntityEvent` |
| `gliding` | boolean | `isGliding()` | `boolean` | `org.bukkit.event.entity.EntityToggleGlideEvent` |

[[Data-Format-en|Wire format and limits]] · [[Event-org-bukkit-event-entity-entitytoggleglideevent|中文]]

If this event is not enabled, add its Java class or simple name to `events.include` in the Paper plugin configuration.
