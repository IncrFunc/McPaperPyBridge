# AsyncTabCompleteEvent

[[Home|首页]] / [[Category-server|服务端]]

- Java 类: `com.destroystokyo.paper.event.server.AsyncTabCompleteEvent`
- 父类: `org.bukkit.event.Event`
- Python 订阅名: `AsyncTabCompleteEvent`
- Python 常量: `Events.ASYNC_TAB_COMPLETE`
- 可取消: 是
- 可能关联玩家: 没有已知玩家 getter
- 处理器列表定义于: `com.destroystokyo.paper.event.server.AsyncTabCompleteEvent`
- [Paper 官方 Javadoc](https://jd.papermc.io/paper/1.16.5/com/destroystokyo/paper/event/server/AsyncTabCompleteEvent.html)

## Python 示例

```python
from paperpybridge import Events

@bridge.on(Events.ASYNC_TAB_COMPLETE)
def on_event(event):
    print(event.event, event.data)
```

## `data` 字段

| 字段 | JSON 类型 | Java getter | Java 返回类型 | 定义于 |
| --- | --- | --- | --- | --- |
| `buffer` | 字符串 | `getBuffer()` | `java.lang.String` | `com.destroystokyo.paper.event.server.AsyncTabCompleteEvent` |
| `location` | 位置摘要 | `getLocation()` | `org.bukkit.Location` | `com.destroystokyo.paper.event.server.AsyncTabCompleteEvent` |
| `command` | 布尔值 | `isCommand()` | `boolean` | `com.destroystokyo.paper.event.server.AsyncTabCompleteEvent` |
| `handled` | 布尔值 | `isHandled()` | `boolean` | `com.destroystokyo.paper.event.server.AsyncTabCompleteEvent` |

[[Data-Format|通用字段、数据格式和限制]] · [[Event-com-destroystokyo-paper-event-server-asynctabcompleteevent-en|English]]

若此事件尚未启用，请将其 Java 完整类名或简单类名加入 Paper 插件配置的 `events.include`。
