# VillagerCareerChangeEvent

[[Home-en|Home]] / [[Category-entity-en|entity]]

- Java class: `org.bukkit.event.entity.VillagerCareerChangeEvent`
- Parent class: `org.bukkit.event.entity.EntityEvent`
- Python subscription: `VillagerCareerChangeEvent`
- Python constant: `Events.VILLAGER_CAREER_CHANGE`
- Cancellable: Yes
- Player available: Possible at runtime
- HandlerList owner: `org.bukkit.event.entity.VillagerCareerChangeEvent`
- [Official Paper Javadoc](https://jd.papermc.io/paper/1.16.5/org/bukkit/event/entity/VillagerCareerChangeEvent.html)

## Python example

```python
from paperpybridge import Events

@bridge.on(Events.VILLAGER_CAREER_CHANGE)
def on_event(event):
    print(event.event, event.data)
```

## `data` fields

| Field | JSON type | Java getter | Java return type | Declared in |
| --- | --- | --- | --- | --- |
| `entity` | entity summary | `getEntity()` | `org.bukkit.entity.Villager` | `org.bukkit.event.entity.VillagerCareerChangeEvent` |
| `entityType` | string | `getEntityType()` | `org.bukkit.entity.EntityType` | `org.bukkit.event.entity.EntityEvent` |
| `profession` | string | `getProfession()` | `org.bukkit.entity.Villager$Profession` | `org.bukkit.event.entity.VillagerCareerChangeEvent` |
| `reason` | string | `getReason()` | `org.bukkit.event.entity.VillagerCareerChangeEvent$ChangeReason` | `org.bukkit.event.entity.VillagerCareerChangeEvent` |

[[Data-Format-en|Wire format and limits]] · [[Event-org-bukkit-event-entity-villagercareerchangeevent|中文]]

If this event is not enabled, add its Java class or simple name to `events.include` in the Paper plugin configuration.
