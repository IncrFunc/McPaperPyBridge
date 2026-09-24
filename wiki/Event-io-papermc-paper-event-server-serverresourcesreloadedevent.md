# ServerResourcesReloadedEvent

[[Home|首页]] / [[Category-server|服务端]]

- Java 类: `io.papermc.paper.event.server.ServerResourcesReloadedEvent`
- 父类: `org.bukkit.event.server.ServerEvent`
- Python 订阅名: `ServerResourcesReloadedEvent`
- Python 常量: `Events.SERVER_RESOURCES_RELOADED`
- 可取消: 否
- 可能关联玩家: 没有已知玩家 getter
- 处理器列表定义于: `io.papermc.paper.event.server.ServerResourcesReloadedEvent`
- [Paper 官方 Javadoc](https://jd.papermc.io/paper/1.16.5/io/papermc/paper/event/server/ServerResourcesReloadedEvent.html)

## Python 示例

```python
from paperpybridge import Events

@bridge.on(Events.SERVER_RESOURCES_RELOADED)
def on_event(event):
    print(event.event, event.data)
```

## `data` 字段

| 字段 | JSON 类型 | Java getter | Java 返回类型 | 定义于 |
| --- | --- | --- | --- | --- |
| `cause` | 字符串 | `getCause()` | `io.papermc.paper.event.server.ServerResourcesReloadedEvent$Cause` | `io.papermc.paper.event.server.ServerResourcesReloadedEvent` |

[[Data-Format|通用字段、数据格式和限制]] · [[Event-io-papermc-paper-event-server-serverresourcesreloadedevent-en|English]]

若此事件尚未启用，请将其 Java 完整类名或简单类名加入 Paper 插件配置的 `events.include`。
