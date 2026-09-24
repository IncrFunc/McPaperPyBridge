# EntityPoseChangeEvent

[[Home-en|Home]] / [[Category-entity-en|entity]]

- Java class: `org.bukkit.event.entity.EntityPoseChangeEvent`
- Parent class: `org.bukkit.event.entity.EntityEvent`
- Python subscription: `EntityPoseChangeEvent`
- Python constant: `Events.ENTITY_POSE_CHANGE`
- Cancellable: No
- Player available: Possible at runtime
- HandlerList owner: `org.bukkit.event.entity.EntityPoseChangeEvent`
- [Official Paper Javadoc](https://jd.papermc.io/paper/1.16.5/org/bukkit/event/entity/EntityPoseChangeEvent.html)

## Python example

```python
from paperpybridge import Events

@bridge.on(Events.ENTITY_POSE_CHANGE)
def on_event(event):
    print(event.event, event.data)
```

## `data` fields

| Field | JSON type | Java getter | Java return type | Declared in |
| --- | --- | --- | --- | --- |
| `entity` | entity summary | `getEntity()` | `org.bukkit.entity.Entity` | `org.bukkit.event.entity.EntityEvent` |
| `entityType` | string | `getEntityType()` | `org.bukkit.entity.EntityType` | `org.bukkit.event.entity.EntityEvent` |
| `pose` | string | `getPose()` | `org.bukkit.entity.Pose` | `org.bukkit.event.entity.EntityPoseChangeEvent` |

[[Data-Format-en|Wire format and limits]] · [[Event-org-bukkit-event-entity-entityposechangeevent|中文]]

If this event is not enabled, add its Java class or simple name to `events.include` in the Paper plugin configuration.
