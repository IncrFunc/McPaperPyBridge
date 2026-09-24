# TabCompleteEvent

[[Home|首页]] / [[Category-server|服务端]]

- Java 类: `org.bukkit.event.server.TabCompleteEvent`
- 父类: `org.bukkit.event.Event`
- Python 订阅名: `TabCompleteEvent`
- Python 常量: `Events.TAB_COMPLETE`
- 可取消: 是
- 可能关联玩家: 没有已知玩家 getter
- 处理器列表定义于: `org.bukkit.event.server.TabCompleteEvent`
- [Paper 官方 Javadoc](https://jd.papermc.io/paper/1.16.5/org/bukkit/event/server/TabCompleteEvent.html)

## Python 示例

```python
from paperpybridge import Events

@bridge.on(Events.TAB_COMPLETE)
def on_event(event):
    print(event.event, event.data)
```

## `data` 字段

| 字段 | JSON 类型 | Java getter | Java 返回类型 | 定义于 |
| --- | --- | --- | --- | --- |
| `buffer` | 字符串 | `getBuffer()` | `java.lang.String` | `org.bukkit.event.server.TabCompleteEvent` |
| `location` | 位置摘要 | `getLocation()` | `org.bukkit.Location` | `org.bukkit.event.server.TabCompleteEvent` |
| `command` | 布尔值 | `isCommand()` | `boolean` | `org.bukkit.event.server.TabCompleteEvent` |

[[Data-Format|通用字段、数据格式和限制]] · [[Event-org-bukkit-event-server-tabcompleteevent-en|English]]

若此事件尚未启用，请将其 Java 完整类名或简单类名加入 Paper 插件配置的 `events.include`。
