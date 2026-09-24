# GS4QueryEvent

[[Home|首页]] / [[Category-server|服务端]]

- Java 类: `com.destroystokyo.paper.event.server.GS4QueryEvent`
- 父类: `org.bukkit.event.Event`
- Python 订阅名: `GS4QueryEvent`
- Python 常量: `Events.GS4_QUERY`
- 可取消: 否
- 可能关联玩家: 没有已知玩家 getter
- 处理器列表定义于: `com.destroystokyo.paper.event.server.GS4QueryEvent`
- [Paper 官方 Javadoc](https://jd.papermc.io/paper/1.16.5/com/destroystokyo/paper/event/server/GS4QueryEvent.html)

## Python 示例

```python
from paperpybridge import Events

@bridge.on(Events.GS4_QUERY)
def on_event(event):
    print(event.event, event.data)
```

## `data` 字段

| 字段 | JSON 类型 | Java getter | Java 返回类型 | 定义于 |
| --- | --- | --- | --- | --- |
| `queryType` | 字符串 | `getQueryType()` | `com.destroystokyo.paper.event.server.GS4QueryEvent$QueryType` | `com.destroystokyo.paper.event.server.GS4QueryEvent` |

[[Data-Format|通用字段、数据格式和限制]] · [[Event-com-destroystokyo-paper-event-server-gs4queryevent-en|English]]

若此事件尚未启用，请将其 Java 完整类名或简单类名加入 Paper 插件配置的 `events.include`。
