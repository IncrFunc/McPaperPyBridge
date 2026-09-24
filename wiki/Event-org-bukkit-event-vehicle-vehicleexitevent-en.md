# VehicleExitEvent

[[Home-en|Home]] / [[Category-vehicle-en|vehicle]]

- Java class: `org.bukkit.event.vehicle.VehicleExitEvent`
- Parent class: `org.bukkit.event.vehicle.VehicleEvent`
- Python subscription: `VehicleExitEvent`
- Python constant: `Events.VEHICLE_EXIT`
- Cancellable: Yes
- Player available: No known player getter
- HandlerList owner: `org.bukkit.event.vehicle.VehicleExitEvent`
- [Official Paper Javadoc](https://jd.papermc.io/paper/1.16.5/org/bukkit/event/vehicle/VehicleExitEvent.html)

## Python example

```python
from paperpybridge import Events

@bridge.on(Events.VEHICLE_EXIT)
def on_event(event):
    print(event.event, event.data)
```

## `data` fields

| Field | JSON type | Java getter | Java return type | Declared in |
| --- | --- | --- | --- | --- |
| `exited` | entity summary | `getExited()` | `org.bukkit.entity.LivingEntity` | `org.bukkit.event.vehicle.VehicleExitEvent` |
| `vehicle` | entity summary | `getVehicle()` | `org.bukkit.entity.Vehicle` | `org.bukkit.event.vehicle.VehicleEvent` |
| `cancellable` | boolean | `isCancellable()` | `boolean` | `org.bukkit.event.vehicle.VehicleExitEvent` |

[[Data-Format-en|Wire format and limits]] · [[Event-org-bukkit-event-vehicle-vehicleexitevent|中文]]

If this event is not enabled, add its Java class or simple name to `events.include` in the Paper plugin configuration.
