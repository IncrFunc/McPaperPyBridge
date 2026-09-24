# VehicleMoveEvent

[[Home-en|Home]] / [[Category-vehicle-en|vehicle]]

- Java class: `org.bukkit.event.vehicle.VehicleMoveEvent`
- Parent class: `org.bukkit.event.vehicle.VehicleEvent`
- Python subscription: `VehicleMoveEvent`
- Python constant: `Events.VEHICLE_MOVE`
- Cancellable: No
- Player available: No known player getter
- HandlerList owner: `org.bukkit.event.vehicle.VehicleMoveEvent`
- [Official Paper Javadoc](https://jd.papermc.io/paper/1.16.5/org/bukkit/event/vehicle/VehicleMoveEvent.html)

## Python example

```python
from paperpybridge import Events

@bridge.on(Events.VEHICLE_MOVE)
def on_event(event):
    print(event.event, event.data)
```

## `data` fields

| Field | JSON type | Java getter | Java return type | Declared in |
| --- | --- | --- | --- | --- |
| `from` | location summary | `getFrom()` | `org.bukkit.Location` | `org.bukkit.event.vehicle.VehicleMoveEvent` |
| `to` | location summary | `getTo()` | `org.bukkit.Location` | `org.bukkit.event.vehicle.VehicleMoveEvent` |
| `vehicle` | entity summary | `getVehicle()` | `org.bukkit.entity.Vehicle` | `org.bukkit.event.vehicle.VehicleEvent` |

[[Data-Format-en|Wire format and limits]] · [[Event-org-bukkit-event-vehicle-vehiclemoveevent|中文]]

If this event is not enabled, add its Java class or simple name to `events.include` in the Paper plugin configuration.
