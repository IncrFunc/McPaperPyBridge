# StriderTemperatureChangeEvent

[[Home-en|Home]] / [[Category-entity-en|entity]]

- Java class: `org.bukkit.event.entity.StriderTemperatureChangeEvent`
- Parent class: `org.bukkit.event.entity.EntityEvent`
- Python subscription: `StriderTemperatureChangeEvent`
- Python constant: `Events.STRIDER_TEMPERATURE_CHANGE`
- Cancellable: No
- Player available: Possible at runtime
- HandlerList owner: `org.bukkit.event.entity.StriderTemperatureChangeEvent`
- [Official Paper Javadoc](https://jd.papermc.io/paper/1.16.5/org/bukkit/event/entity/StriderTemperatureChangeEvent.html)

## Python example

```python
from paperpybridge import Events

@bridge.on(Events.STRIDER_TEMPERATURE_CHANGE)
def on_event(event):
    print(event.event, event.data)
```

## `data` fields

| Field | JSON type | Java getter | Java return type | Declared in |
| --- | --- | --- | --- | --- |
| `entity` | entity summary | `getEntity()` | `org.bukkit.entity.Entity` | `org.bukkit.event.entity.StriderTemperatureChangeEvent` |
| `entityType` | string | `getEntityType()` | `org.bukkit.entity.EntityType` | `org.bukkit.event.entity.EntityEvent` |
| `shivering` | boolean | `isShivering()` | `boolean` | `org.bukkit.event.entity.StriderTemperatureChangeEvent` |

[[Data-Format-en|Wire format and limits]] · [[Event-org-bukkit-event-entity-stridertemperaturechangeevent|中文]]

If this event is not enabled, add its Java class or simple name to `events.include` in the Paper plugin configuration.
