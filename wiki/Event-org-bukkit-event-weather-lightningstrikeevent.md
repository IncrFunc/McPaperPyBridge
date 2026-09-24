# LightningStrikeEvent

[[Home|首页]] / [[Category-weather|天气]]

- Java 类: `org.bukkit.event.weather.LightningStrikeEvent`
- 父类: `org.bukkit.event.weather.WeatherEvent`
- Python 订阅名: `LightningStrikeEvent`
- Python 常量: `Events.LIGHTNING_STRIKE`
- 可取消: 是
- 可能关联玩家: 没有已知玩家 getter
- 处理器列表定义于: `org.bukkit.event.weather.LightningStrikeEvent`
- [Paper 官方 Javadoc](https://jd.papermc.io/paper/1.16.5/org/bukkit/event/weather/LightningStrikeEvent.html)

## Python 示例

```python
from paperpybridge import Events

@bridge.on(Events.LIGHTNING_STRIKE)
def on_event(event):
    print(event.event, event.data)
```

## `data` 字段

| 字段 | JSON 类型 | Java getter | Java 返回类型 | 定义于 |
| --- | --- | --- | --- | --- |
| `cause` | 字符串 | `getCause()` | `org.bukkit.event.weather.LightningStrikeEvent$Cause` | `org.bukkit.event.weather.LightningStrikeEvent` |
| `lightning` | 实体摘要 | `getLightning()` | `org.bukkit.entity.LightningStrike` | `org.bukkit.event.weather.LightningStrikeEvent` |
| `world` | 世界摘要 | `getWorld()` | `org.bukkit.World` | `org.bukkit.event.weather.WeatherEvent` |

[[Data-Format|通用字段、数据格式和限制]] · [[Event-org-bukkit-event-weather-lightningstrikeevent-en|English]]

若此事件尚未启用，请将其 Java 完整类名或简单类名加入 Paper 插件配置的 `events.include`。
