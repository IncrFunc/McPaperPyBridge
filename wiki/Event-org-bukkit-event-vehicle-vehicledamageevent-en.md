# VehicleDamageEvent

[[Home-en|Home]] / [[Category-vehicle-en|vehicle]]

- Java class: `org.bukkit.event.vehicle.VehicleDamageEvent`
- Parent class: `org.bukkit.event.vehicle.VehicleEvent`
- Python subscription: `VehicleDamageEvent`
- Python constant: `Events.VEHICLE_DAMAGE`
- Cancellable: Yes
- Player available: No known player getter
- HandlerList owner: `org.bukkit.event.vehicle.VehicleDamageEvent`
- [Official Paper Javadoc](https://jd.papermc.io/paper/1.16.5/org/bukkit/event/vehicle/VehicleDamageEvent.html)

## Python example

```python
from paperpybridge import Events

@bridge.on(Events.VEHICLE_DAMAGE)
def on_event(event):
    print(event.event, event.data)
```

## `data` fields

| Field | JSON type | Java getter | Java return type | Declared in |
| --- | --- | --- | --- | --- |
| `attacker` | entity summary | `getAttacker()` | `org.bukkit.entity.Entity` | `org.bukkit.event.vehicle.VehicleDamageEvent` |
| `damage` | number | `getDamage()` | `double` | `org.bukkit.event.vehicle.VehicleDamageEvent` |
| `vehicle` | entity summary | `getVehicle()` | `org.bukkit.entity.Vehicle` | `org.bukkit.event.vehicle.VehicleEvent` |

[[Data-Format-en|Wire format and limits]] · [[Event-org-bukkit-event-vehicle-vehicledamageevent|中文]]

If this event is not enabled, add its Java class or simple name to `events.include` in the Paper plugin configuration.
