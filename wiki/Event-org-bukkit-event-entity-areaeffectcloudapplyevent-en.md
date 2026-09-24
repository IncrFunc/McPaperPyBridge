# AreaEffectCloudApplyEvent

[[Home-en|Home]] / [[Category-entity-en|entity]]

- Java class: `org.bukkit.event.entity.AreaEffectCloudApplyEvent`
- Parent class: `org.bukkit.event.entity.EntityEvent`
- Python subscription: `AreaEffectCloudApplyEvent`
- Python constant: `Events.AREA_EFFECT_CLOUD_APPLY`
- Cancellable: Yes
- Player available: Possible at runtime
- HandlerList owner: `org.bukkit.event.entity.AreaEffectCloudApplyEvent`
- [Official Paper Javadoc](https://jd.papermc.io/paper/1.16.5/org/bukkit/event/entity/AreaEffectCloudApplyEvent.html)

## Python example

```python
from paperpybridge import Events

@bridge.on(Events.AREA_EFFECT_CLOUD_APPLY)
def on_event(event):
    print(event.event, event.data)
```

## `data` fields

| Field | JSON type | Java getter | Java return type | Declared in |
| --- | --- | --- | --- | --- |
| `entity` | entity summary | `getEntity()` | `org.bukkit.entity.Entity` | `org.bukkit.event.entity.AreaEffectCloudApplyEvent` |
| `entityType` | string | `getEntityType()` | `org.bukkit.entity.EntityType` | `org.bukkit.event.entity.EntityEvent` |

[[Data-Format-en|Wire format and limits]] · [[Event-org-bukkit-event-entity-areaeffectcloudapplyevent|中文]]

If this event is not enabled, add its Java class or simple name to `events.include` in the Paper plugin configuration.
