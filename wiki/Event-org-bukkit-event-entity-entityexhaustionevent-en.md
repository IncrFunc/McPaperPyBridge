# EntityExhaustionEvent

[[Home-en|Home]] / [[Category-entity-en|entity]]

- Java class: `org.bukkit.event.entity.EntityExhaustionEvent`
- Parent class: `org.bukkit.event.entity.EntityEvent`
- Python subscription: `EntityExhaustionEvent`
- Python constant: `Events.ENTITY_EXHAUSTION`
- Cancellable: Yes
- Player available: Possible at runtime
- HandlerList owner: `org.bukkit.event.entity.EntityExhaustionEvent`
- [Official Paper Javadoc](https://jd.papermc.io/paper/1.16.5/org/bukkit/event/entity/EntityExhaustionEvent.html)

## Python example

```python
from paperpybridge import Events

@bridge.on(Events.ENTITY_EXHAUSTION)
def on_event(event):
    print(event.event, event.data)
```

## `data` fields

| Field | JSON type | Java getter | Java return type | Declared in |
| --- | --- | --- | --- | --- |
| `entity` | entity summary | `getEntity()` | `org.bukkit.entity.HumanEntity` | `org.bukkit.event.entity.EntityExhaustionEvent` |
| `entityType` | string | `getEntityType()` | `org.bukkit.entity.EntityType` | `org.bukkit.event.entity.EntityEvent` |
| `exhaustion` | number | `getExhaustion()` | `float` | `org.bukkit.event.entity.EntityExhaustionEvent` |
| `exhaustionReason` | string | `getExhaustionReason()` | `org.bukkit.event.entity.EntityExhaustionEvent$ExhaustionReason` | `org.bukkit.event.entity.EntityExhaustionEvent` |

[[Data-Format-en|Wire format and limits]] · [[Event-org-bukkit-event-entity-entityexhaustionevent|中文]]

If this event is not enabled, add its Java class or simple name to `events.include` in the Paper plugin configuration.
