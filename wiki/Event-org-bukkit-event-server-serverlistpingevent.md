# ServerListPingEvent

[[Home|首页]] / [[Category-server|服务端]]

- Java 类: `org.bukkit.event.server.ServerListPingEvent`
- 父类: `org.bukkit.event.server.ServerEvent`
- Python 订阅名: `ServerListPingEvent`
- Python 常量: `Events.SERVER_LIST_PING`
- 可取消: 否
- 可能关联玩家: 没有已知玩家 getter
- 处理器列表定义于: `org.bukkit.event.server.ServerListPingEvent`
- [Paper 官方 Javadoc](https://jd.papermc.io/paper/1.16.5/org/bukkit/event/server/ServerListPingEvent.html)

## Python 示例

```python
from paperpybridge import Events

@bridge.on(Events.SERVER_LIST_PING)
def on_event(event):
    print(event.event, event.data)
```

## `data` 字段

| 字段 | JSON 类型 | Java getter | Java 返回类型 | 定义于 |
| --- | --- | --- | --- | --- |
| `maxPlayers` | 数字 | `getMaxPlayers()` | `int` | `org.bukkit.event.server.ServerListPingEvent` |
| `motd` | 字符串 | `getMotd()` | `java.lang.String` | `org.bukkit.event.server.ServerListPingEvent` |
| `numPlayers` | 数字 | `getNumPlayers()` | `int` | `org.bukkit.event.server.ServerListPingEvent` |

[[Data-Format|通用字段、数据格式和限制]] · [[Event-org-bukkit-event-server-serverlistpingevent-en|English]]

若此事件尚未启用，请将其 Java 完整类名或简单类名加入 Paper 插件配置的 `events.include`。
