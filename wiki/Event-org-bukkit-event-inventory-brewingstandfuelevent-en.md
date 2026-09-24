# BrewingStandFuelEvent

[[Home-en|Home]] / [[Category-inventory-en|inventory]]

- Java class: `org.bukkit.event.inventory.BrewingStandFuelEvent`
- Parent class: `org.bukkit.event.block.BlockEvent`
- Python subscription: `BrewingStandFuelEvent`
- Python constant: `Events.BREWING_STAND_FUEL`
- Cancellable: Yes
- Player available: No known player getter
- HandlerList owner: `org.bukkit.event.inventory.BrewingStandFuelEvent`
- [Official Paper Javadoc](https://jd.papermc.io/paper/1.16.5/org/bukkit/event/inventory/BrewingStandFuelEvent.html)

## Python example

```python
from paperpybridge import Events

@bridge.on(Events.BREWING_STAND_FUEL)
def on_event(event):
    print(event.event, event.data)
```

## `data` fields

| Field | JSON type | Java getter | Java return type | Declared in |
| --- | --- | --- | --- | --- |
| `block` | block summary | `getBlock()` | `org.bukkit.block.Block` | `org.bukkit.event.block.BlockEvent` |
| `fuel` | item summary | `getFuel()` | `org.bukkit.inventory.ItemStack` | `org.bukkit.event.inventory.BrewingStandFuelEvent` |
| `fuelPower` | number | `getFuelPower()` | `int` | `org.bukkit.event.inventory.BrewingStandFuelEvent` |
| `consuming` | boolean | `isConsuming()` | `boolean` | `org.bukkit.event.inventory.BrewingStandFuelEvent` |

[[Data-Format-en|Wire format and limits]] · [[Event-org-bukkit-event-inventory-brewingstandfuelevent|中文]]

If this event is not enabled, add its Java class or simple name to `events.include` in the Paper plugin configuration.
