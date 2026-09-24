# ServerTickEndEvent

[[Home|首页]] / [[Category-server|服务端]]

- Java 类: `com.destroystokyo.paper.event.server.ServerTickEndEvent`
- 父类: `org.bukkit.event.Event`
- Python 订阅名: `ServerTickEndEvent`
- Python 常量: `Events.SERVER_TICK_END`
- 可取消: 否
- 可能关联玩家: 没有已知玩家 getter
- 处理器列表定义于: `com.destroystokyo.paper.event.server.ServerTickEndEvent`
- [Paper 官方 Javadoc](https://jd.papermc.io/paper/1.16.5/com/destroystokyo/paper/event/server/ServerTickEndEvent.html)

## Python 示例

```python
from paperpybridge import Events

@bridge.on(Events.SERVER_TICK_END)
def on_event(event):
    print(event.event, event.data)
```

## `data` 字段

| 字段 | JSON 类型 | Java getter | Java 返回类型 | 定义于 |
| --- | --- | --- | --- | --- |
| `tickDuration` | 数字 | `getTickDuration()` | `double` | `com.destroystokyo.paper.event.server.ServerTickEndEvent` |
| `tickNumber` | 数字 | `getTickNumber()` | `int` | `com.destroystokyo.paper.event.server.ServerTickEndEvent` |
| `timeRemaining` | 数字 | `getTimeRemaining()` | `long` | `com.destroystokyo.paper.event.server.ServerTickEndEvent` |

[[Data-Format|通用字段、数据格式和限制]] · [[Event-com-destroystokyo-paper-event-server-servertickendevent-en|English]]

若此事件尚未启用，请将其 Java 完整类名或简单类名加入 Paper 插件配置的 `events.include`。
