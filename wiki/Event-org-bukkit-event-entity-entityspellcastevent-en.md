# EntitySpellCastEvent

[[Home-en|Home]] / [[Category-entity-en|entity]]

- Java class: `org.bukkit.event.entity.EntitySpellCastEvent`
- Parent class: `org.bukkit.event.entity.EntityEvent`
- Python subscription: `EntitySpellCastEvent`
- Python constant: `Events.ENTITY_SPELL_CAST`
- Cancellable: Yes
- Player available: Possible at runtime
- HandlerList owner: `org.bukkit.event.entity.EntitySpellCastEvent`
- [Official Paper Javadoc](https://jd.papermc.io/paper/1.16.5/org/bukkit/event/entity/EntitySpellCastEvent.html)

## Python example

```python
from paperpybridge import Events

@bridge.on(Events.ENTITY_SPELL_CAST)
def on_event(event):
    print(event.event, event.data)
```

## `data` fields

| Field | JSON type | Java getter | Java return type | Declared in |
| --- | --- | --- | --- | --- |
| `entity` | entity summary | `getEntity()` | `org.bukkit.entity.Entity` | `org.bukkit.event.entity.EntitySpellCastEvent` |
| `entityType` | string | `getEntityType()` | `org.bukkit.entity.EntityType` | `org.bukkit.event.entity.EntityEvent` |
| `spell` | string | `getSpell()` | `org.bukkit.entity.Spellcaster$Spell` | `org.bukkit.event.entity.EntitySpellCastEvent` |

[[Data-Format-en|Wire format and limits]] · [[Event-org-bukkit-event-entity-entityspellcastevent|中文]]

If this event is not enabled, add its Java class or simple name to `events.include` in the Paper plugin configuration.
