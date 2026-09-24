# VehicleEntityCollisionEvent

[[Home-en|Home]] / [[Category-vehicle-en|vehicle]]

- Java class: `org.bukkit.event.vehicle.VehicleEntityCollisionEvent`
- Parent class: `org.bukkit.event.vehicle.VehicleCollisionEvent`
- Python subscription: `VehicleEntityCollisionEvent`
- Python constant: `Events.VEHICLE_ENTITY_COLLISION`
- Cancellable: Yes
- Player available: Possible at runtime
- HandlerList owner: `org.bukkit.event.vehicle.VehicleEntityCollisionEvent`
- [Official Paper Javadoc](https://jd.papermc.io/paper/1.16.5/org/bukkit/event/vehicle/VehicleEntityCollisionEvent.html)

## Python example

```python
from paperpybridge import Events

@bridge.on(Events.VEHICLE_ENTITY_COLLISION)
def on_event(event):
    print(event.event, event.data)
```

## `data` fields

| Field | JSON type | Java getter | Java return type | Declared in |
| --- | --- | --- | --- | --- |
| `entity` | entity summary | `getEntity()` | `org.bukkit.entity.Entity` | `org.bukkit.event.vehicle.VehicleEntityCollisionEvent` |
| `vehicle` | entity summary | `getVehicle()` | `org.bukkit.entity.Vehicle` | `org.bukkit.event.vehicle.VehicleEvent` |
| `collisionCancelled` | boolean | `isCollisionCancelled()` | `boolean` | `org.bukkit.event.vehicle.VehicleEntityCollisionEvent` |
| `pickupCancelled` | boolean | `isPickupCancelled()` | `boolean` | `org.bukkit.event.vehicle.VehicleEntityCollisionEvent` |

[[Data-Format-en|Wire format and limits]] · [[Event-org-bukkit-event-vehicle-vehicleentitycollisionevent|中文]]

If this event is not enabled, add its Java class or simple name to `events.include` in the Paper plugin configuration.
