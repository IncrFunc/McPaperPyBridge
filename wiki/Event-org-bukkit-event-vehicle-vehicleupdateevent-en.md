# VehicleUpdateEvent

[[Home-en|Home]] / [[Category-vehicle-en|vehicle]]

- Java class: `org.bukkit.event.vehicle.VehicleUpdateEvent`
- Parent class: `org.bukkit.event.vehicle.VehicleEvent`
- Python subscription: `VehicleUpdateEvent`
- Python constant: `Events.VEHICLE_UPDATE`
- Cancellable: No
- Player available: No known player getter
- HandlerList owner: `org.bukkit.event.vehicle.VehicleUpdateEvent`
- [Official Paper Javadoc](https://jd.papermc.io/paper/1.16.5/org/bukkit/event/vehicle/VehicleUpdateEvent.html)

## Python example

```python
from paperpybridge import Events

@bridge.on(Events.VEHICLE_UPDATE)
def on_event(event):
    print(event.event, event.data)
```

## `data` fields

| Field | JSON type | Java getter | Java return type | Declared in |
| --- | --- | --- | --- | --- |
| `vehicle` | entity summary | `getVehicle()` | `org.bukkit.entity.Vehicle` | `org.bukkit.event.vehicle.VehicleEvent` |

[[Data-Format-en|Wire format and limits]] · [[Event-org-bukkit-event-vehicle-vehicleupdateevent|中文]]

If this event is not enabled, add its Java class or simple name to `events.include` in the Paper plugin configuration.
