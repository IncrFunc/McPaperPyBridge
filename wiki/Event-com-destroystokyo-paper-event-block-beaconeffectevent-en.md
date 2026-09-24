# BeaconEffectEvent

[[Home-en|Home]] / [[Category-block-en|block]]

- Java class: `com.destroystokyo.paper.event.block.BeaconEffectEvent`
- Parent class: `org.bukkit.event.block.BlockEvent`
- Python subscription: `BeaconEffectEvent`
- Python constant: `Events.BEACON_EFFECT`
- Cancellable: Yes
- Player available: Possible at runtime
- HandlerList owner: `com.destroystokyo.paper.event.block.BeaconEffectEvent`
- [Official Paper Javadoc](https://jd.papermc.io/paper/1.16.5/com/destroystokyo/paper/event/block/BeaconEffectEvent.html)

## Python example

```python
from paperpybridge import Events

@bridge.on(Events.BEACON_EFFECT)
def on_event(event):
    print(event.event, event.data)
```

## `data` fields

| Field | JSON type | Java getter | Java return type | Declared in |
| --- | --- | --- | --- | --- |
| `block` | block summary | `getBlock()` | `org.bukkit.block.Block` | `org.bukkit.event.block.BlockEvent` |
| `primary` | boolean | `isPrimary()` | `boolean` | `com.destroystokyo.paper.event.block.BeaconEffectEvent` |

[[Data-Format-en|Wire format and limits]] · [[Event-com-destroystokyo-paper-event-block-beaconeffectevent|中文]]

If this event is not enabled, add its Java class or simple name to `events.include` in the Paper plugin configuration.
