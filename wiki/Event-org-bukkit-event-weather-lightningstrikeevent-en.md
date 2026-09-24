# LightningStrikeEvent

[[Home-en|Home]] / [[Category-weather-en|weather]]

- Java class: `org.bukkit.event.weather.LightningStrikeEvent`
- Parent class: `org.bukkit.event.weather.WeatherEvent`
- Python subscription: `LightningStrikeEvent`
- Python constant: `Events.LIGHTNING_STRIKE`
- Cancellable: Yes
- Player available: No known player getter
- HandlerList owner: `org.bukkit.event.weather.LightningStrikeEvent`
- [Official Paper Javadoc](https://jd.papermc.io/paper/1.16.5/org/bukkit/event/weather/LightningStrikeEvent.html)

## Python example

```python
from paperpybridge import Events

@bridge.on(Events.LIGHTNING_STRIKE)
def on_event(event):
    print(event.event, event.data)
```

## `data` fields

| Field | JSON type | Java getter | Java return type | Declared in |
| --- | --- | --- | --- | --- |
| `cause` | string | `getCause()` | `org.bukkit.event.weather.LightningStrikeEvent$Cause` | `org.bukkit.event.weather.LightningStrikeEvent` |
| `lightning` | entity summary | `getLightning()` | `org.bukkit.entity.LightningStrike` | `org.bukkit.event.weather.LightningStrikeEvent` |
| `world` | world summary | `getWorld()` | `org.bukkit.World` | `org.bukkit.event.weather.WeatherEvent` |

[[Data-Format-en|Wire format and limits]] · [[Event-org-bukkit-event-weather-lightningstrikeevent|中文]]

If this event is not enabled, add its Java class or simple name to `events.include` in the Paper plugin configuration.
