# ServerExceptionEvent

[[Home|首页]] / [[Category-server|服务端]]

- Java 类: `com.destroystokyo.paper.event.server.ServerExceptionEvent`
- 父类: `org.bukkit.event.Event`
- Python 订阅名: `ServerExceptionEvent`
- Python 常量: `Events.SERVER_EXCEPTION`
- 可取消: 否
- 可能关联玩家: 没有已知玩家 getter
- 处理器列表定义于: `com.destroystokyo.paper.event.server.ServerExceptionEvent`
- [Paper 官方 Javadoc](https://jd.papermc.io/paper/1.16.5/com/destroystokyo/paper/event/server/ServerExceptionEvent.html)

## Python 示例

```python
from paperpybridge import Events

@bridge.on(Events.SERVER_EXCEPTION)
def on_event(event):
    print(event.event, event.data)
```

## `data` 字段

没有可序列化的字段，仍会收到通用事件字段。

[[Data-Format|通用字段、数据格式和限制]] · [[Event-com-destroystokyo-paper-event-server-serverexceptionevent-en|English]]

若此事件尚未启用，请将其 Java 完整类名或简单类名加入 Paper 插件配置的 `events.include`。
