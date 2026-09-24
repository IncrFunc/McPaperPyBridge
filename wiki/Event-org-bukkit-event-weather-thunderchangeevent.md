# ThunderChangeEvent

[[Home|首页]] / [[Category-weather|天气]]

- Java 类: `org.bukkit.event.weather.ThunderChangeEvent`
- 父类: `org.bukkit.event.weather.WeatherEvent`
- Python 订阅名: `ThunderChangeEvent`
- Python 常量: `Events.THUNDER_CHANGE`
- 可取消: 是
- 可能关联玩家: 没有已知玩家 getter
- 处理器列表定义于: `org.bukkit.event.weather.ThunderChangeEvent`
- [Paper 官方 Javadoc](https://jd.papermc.io/paper/1.16.5/org/bukkit/event/weather/ThunderChangeEvent.html)

## Python 示例

```python
from paperpybridge import Events

@bridge.on(Events.THUNDER_CHANGE)
def on_event(event):
    print(event.event, event.data)
```

## `data` 字段

| 字段 | JSON 类型 | Java getter | Java 返回类型 | 定义于 |
| --- | --- | --- | --- | --- |
| `cause` | 字符串 | `getCause()` | `org.bukkit.event.weather.ThunderChangeEvent$Cause` | `org.bukkit.event.weather.ThunderChangeEvent` |
| `world` | 世界摘要 | `getWorld()` | `org.bukkit.World` | `org.bukkit.event.weather.WeatherEvent` |

[[Data-Format|通用字段、数据格式和限制]] · [[Event-org-bukkit-event-weather-thunderchangeevent-en|English]]

若此事件尚未启用，请将其 Java 完整类名或简单类名加入 Paper 插件配置的 `events.include`。
