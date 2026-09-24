# EntityEnterLoveModeEvent

[[Home-en|Home]] / [[Category-entity-en|entity]]

- Java class: `org.bukkit.event.entity.EntityEnterLoveModeEvent`
- Parent class: `org.bukkit.event.entity.EntityEvent`
- Python subscription: `EntityEnterLoveModeEvent`
- Python constant: `Events.ENTITY_ENTER_LOVE_MODE`
- Cancellable: Yes
- Player available: Possible at runtime
- HandlerList owner: `org.bukkit.event.entity.EntityEnterLoveModeEvent`
- [Official Paper Javadoc](https://jd.papermc.io/paper/1.16.5/org/bukkit/event/entity/EntityEnterLoveModeEvent.html)

## Python example

```python
from paperpybridge import Events

@bridge.on(Events.ENTITY_ENTER_LOVE_MODE)
def on_event(event):
    print(event.event, event.data)
```

## `data` fields

| Field | JSON type | Java getter | Java return type | Declared in |
| --- | --- | --- | --- | --- |
| `entity` | entity summary | `getEntity()` | `org.bukkit.entity.Animals` | `org.bukkit.event.entity.EntityEnterLoveModeEvent` |
| `entityType` | string | `getEntityType()` | `org.bukkit.entity.EntityType` | `org.bukkit.event.entity.EntityEvent` |
| `humanEntity` | entity summary | `getHumanEntity()` | `org.bukkit.entity.HumanEntity` | `org.bukkit.event.entity.EntityEnterLoveModeEvent` |
| `ticksInLove` | number | `getTicksInLove()` | `int` | `org.bukkit.event.entity.EntityEnterLoveModeEvent` |

[[Data-Format-en|Wire format and limits]] · [[Event-org-bukkit-event-entity-entityenterlovemodeevent|中文]]

If this event is not enabled, add its Java class or simple name to `events.include` in the Paper plugin configuration.
