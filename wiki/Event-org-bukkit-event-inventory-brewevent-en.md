# BrewEvent

[[Home-en|Home]] / [[Category-inventory-en|inventory]]

- Java class: `org.bukkit.event.inventory.BrewEvent`
- Parent class: `org.bukkit.event.block.BlockEvent`
- Python subscription: `BrewEvent`
- Python constant: `Events.BREW`
- Cancellable: Yes
- Player available: No known player getter
- HandlerList owner: `org.bukkit.event.inventory.BrewEvent`
- [Official Paper Javadoc](https://jd.papermc.io/paper/1.16.5/org/bukkit/event/inventory/BrewEvent.html)

## Python example

```python
from paperpybridge import Events

@bridge.on(Events.BREW)
def on_event(event):
    print(event.event, event.data)
```

## `data` fields

| Field | JSON type | Java getter | Java return type | Declared in |
| --- | --- | --- | --- | --- |
| `block` | block summary | `getBlock()` | `org.bukkit.block.Block` | `org.bukkit.event.block.BlockEvent` |
| `fuelLevel` | number | `getFuelLevel()` | `int` | `org.bukkit.event.inventory.BrewEvent` |

[[Data-Format-en|Wire format and limits]] · [[Event-org-bukkit-event-inventory-brewevent|中文]]

If this event is not enabled, add its Java class or simple name to `events.include` in the Paper plugin configuration.
