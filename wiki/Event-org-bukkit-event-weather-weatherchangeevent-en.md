# WeatherChangeEvent

[[Home-en|Home]] / [[Category-weather-en|weather]]

- Java class: `org.bukkit.event.weather.WeatherChangeEvent`
- Parent class: `org.bukkit.event.weather.WeatherEvent`
- Python subscription: `WeatherChangeEvent`
- Python constant: `Events.WEATHER_CHANGE`
- Cancellable: Yes
- Player available: No known player getter
- HandlerList owner: `org.bukkit.event.weather.WeatherChangeEvent`
- [Official Paper Javadoc](https://jd.papermc.io/paper/1.16.5/org/bukkit/event/weather/WeatherChangeEvent.html)

## Python example

```python
from paperpybridge import Events

@bridge.on(Events.WEATHER_CHANGE)
def on_event(event):
    print(event.event, event.data)
```

## `data` fields

| Field | JSON type | Java getter | Java return type | Declared in |
| --- | --- | --- | --- | --- |
| `cause` | string | `getCause()` | `org.bukkit.event.weather.WeatherChangeEvent$Cause` | `org.bukkit.event.weather.WeatherChangeEvent` |
| `world` | world summary | `getWorld()` | `org.bukkit.World` | `org.bukkit.event.weather.WeatherEvent` |

[[Data-Format-en|Wire format and limits]] · [[Event-org-bukkit-event-weather-weatherchangeevent|中文]]

If this event is not enabled, add its Java class or simple name to `events.include` in the Paper plugin configuration.
