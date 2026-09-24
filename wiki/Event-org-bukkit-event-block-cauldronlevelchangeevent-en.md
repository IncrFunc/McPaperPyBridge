# CauldronLevelChangeEvent

[[Home-en|Home]] / [[Category-block-en|block]]

- Java class: `org.bukkit.event.block.CauldronLevelChangeEvent`
- Parent class: `org.bukkit.event.block.BlockEvent`
- Python subscription: `CauldronLevelChangeEvent`
- Python constant: `Events.CAULDRON_LEVEL_CHANGE`
- Cancellable: Yes
- Player available: Possible at runtime
- HandlerList owner: `org.bukkit.event.block.CauldronLevelChangeEvent`
- [Official Paper Javadoc](https://jd.papermc.io/paper/1.16.5/org/bukkit/event/block/CauldronLevelChangeEvent.html)

## Python example

```python
from paperpybridge import Events

@bridge.on(Events.CAULDRON_LEVEL_CHANGE)
def on_event(event):
    print(event.event, event.data)
```

## `data` fields

| Field | JSON type | Java getter | Java return type | Declared in |
| --- | --- | --- | --- | --- |
| `block` | block summary | `getBlock()` | `org.bukkit.block.Block` | `org.bukkit.event.block.BlockEvent` |
| `entity` | entity summary | `getEntity()` | `org.bukkit.entity.Entity` | `org.bukkit.event.block.CauldronLevelChangeEvent` |
| `newLevel` | number | `getNewLevel()` | `int` | `org.bukkit.event.block.CauldronLevelChangeEvent` |
| `oldLevel` | number | `getOldLevel()` | `int` | `org.bukkit.event.block.CauldronLevelChangeEvent` |
| `reason` | string | `getReason()` | `org.bukkit.event.block.CauldronLevelChangeEvent$ChangeReason` | `org.bukkit.event.block.CauldronLevelChangeEvent` |

[[Data-Format-en|Wire format and limits]] · [[Event-org-bukkit-event-block-cauldronlevelchangeevent|中文]]

If this event is not enabled, add its Java class or simple name to `events.include` in the Paper plugin configuration.
