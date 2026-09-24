# VehicleBlockCollisionEvent

[[Home-en|Home]] / [[Category-vehicle-en|vehicle]]

- Java class: `org.bukkit.event.vehicle.VehicleBlockCollisionEvent`
- Parent class: `org.bukkit.event.vehicle.VehicleCollisionEvent`
- Python subscription: `VehicleBlockCollisionEvent`
- Python constant: `Events.VEHICLE_BLOCK_COLLISION`
- Cancellable: No
- Player available: No known player getter
- HandlerList owner: `org.bukkit.event.vehicle.VehicleBlockCollisionEvent`
- [Official Paper Javadoc](https://jd.papermc.io/paper/1.16.5/org/bukkit/event/vehicle/VehicleBlockCollisionEvent.html)

## Python example

```python
from paperpybridge import Events

@bridge.on(Events.VEHICLE_BLOCK_COLLISION)
def on_event(event):
    print(event.event, event.data)
```

## `data` fields

| Field | JSON type | Java getter | Java return type | Declared in |
| --- | --- | --- | --- | --- |
| `block` | block summary | `getBlock()` | `org.bukkit.block.Block` | `org.bukkit.event.vehicle.VehicleBlockCollisionEvent` |
| `vehicle` | entity summary | `getVehicle()` | `org.bukkit.entity.Vehicle` | `org.bukkit.event.vehicle.VehicleEvent` |

[[Data-Format-en|Wire format and limits]] · [[Event-org-bukkit-event-vehicle-vehicleblockcollisionevent|中文]]

If this event is not enabled, add its Java class or simple name to `events.include` in the Paper plugin configuration.
