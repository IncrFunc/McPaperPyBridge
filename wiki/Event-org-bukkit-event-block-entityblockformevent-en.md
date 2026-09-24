# EntityBlockFormEvent

[[Home-en|Home]] / [[Category-block-en|block]]

- Java class: `org.bukkit.event.block.EntityBlockFormEvent`
- Parent class: `org.bukkit.event.block.BlockFormEvent`
- Python subscription: `EntityBlockFormEvent`
- Python constant: `Events.ENTITY_BLOCK_FORM`
- Cancellable: Yes
- Player available: Possible at runtime
- HandlerList owner: `org.bukkit.event.block.BlockFormEvent`
- [Official Paper Javadoc](https://jd.papermc.io/paper/1.16.5/org/bukkit/event/block/EntityBlockFormEvent.html)

## Python example

```python
from paperpybridge import Events

@bridge.on(Events.ENTITY_BLOCK_FORM)
def on_event(event):
    print(event.event, event.data)
```

## `data` fields

| Field | JSON type | Java getter | Java return type | Declared in |
| --- | --- | --- | --- | --- |
| `block` | block summary | `getBlock()` | `org.bukkit.block.Block` | `org.bukkit.event.block.BlockEvent` |
| `entity` | entity summary | `getEntity()` | `org.bukkit.entity.Entity` | `org.bukkit.event.block.EntityBlockFormEvent` |

[[Data-Format-en|Wire format and limits]] · [[Event-org-bukkit-event-block-entityblockformevent|中文]]

If this event is not enabled, add its Java class or simple name to `events.include` in the Paper plugin configuration.
