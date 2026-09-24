# AnvilDamagedEvent

[[Home-en|Home]] / [[Category-block-en|block]]

- Java class: `com.destroystokyo.paper.event.block.AnvilDamagedEvent`
- Parent class: `org.bukkit.event.inventory.InventoryEvent`
- Python subscription: `AnvilDamagedEvent`
- Python constant: `Events.ANVIL_DAMAGED`
- Cancellable: Yes
- Player available: No known player getter
- HandlerList owner: `com.destroystokyo.paper.event.block.AnvilDamagedEvent`
- [Official Paper Javadoc](https://jd.papermc.io/paper/1.16.5/com/destroystokyo/paper/event/block/AnvilDamagedEvent.html)

## Python example

```python
from paperpybridge import Events

@bridge.on(Events.ANVIL_DAMAGED)
def on_event(event):
    print(event.event, event.data)
```

## `data` fields

| Field | JSON type | Java getter | Java return type | Declared in |
| --- | --- | --- | --- | --- |
| `damageState` | string | `getDamageState()` | `com.destroystokyo.paper.event.block.AnvilDamagedEvent$DamageState` | `com.destroystokyo.paper.event.block.AnvilDamagedEvent` |
| `breaking` | boolean | `isBreaking()` | `boolean` | `com.destroystokyo.paper.event.block.AnvilDamagedEvent` |

[[Data-Format-en|Wire format and limits]] · [[Event-com-destroystokyo-paper-event-block-anvildamagedevent|中文]]

If this event is not enabled, add its Java class or simple name to `events.include` in the Paper plugin configuration.
