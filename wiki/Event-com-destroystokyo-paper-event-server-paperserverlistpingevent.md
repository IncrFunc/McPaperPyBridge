# PaperServerListPingEvent

[[Home|首页]] / [[Category-server|服务端]]

- Java 类: `com.destroystokyo.paper.event.server.PaperServerListPingEvent`
- 父类: `org.bukkit.event.server.ServerListPingEvent`
- Python 订阅名: `PaperServerListPingEvent`
- Python 常量: `Events.PAPER_SERVER_LIST_PING`
- 可取消: 是
- 可能关联玩家: 没有已知玩家 getter
- 处理器列表定义于: `org.bukkit.event.server.ServerListPingEvent`
- [Paper 官方 Javadoc](https://jd.papermc.io/paper/1.16.5/com/destroystokyo/paper/event/server/PaperServerListPingEvent.html)

## Python 示例

```python
from paperpybridge import Events

@bridge.on(Events.PAPER_SERVER_LIST_PING)
def on_event(event):
    print(event.event, event.data)
```

## `data` 字段

| 字段 | JSON 类型 | Java getter | Java 返回类型 | 定义于 |
| --- | --- | --- | --- | --- |
| `maxPlayers` | 数字 | `getMaxPlayers()` | `int` | `com.destroystokyo.paper.event.server.PaperServerListPingEvent` |
| `motd` | 字符串 | `getMotd()` | `java.lang.String` | `org.bukkit.event.server.ServerListPingEvent` |
| `numPlayers` | 数字 | `getNumPlayers()` | `int` | `com.destroystokyo.paper.event.server.PaperServerListPingEvent` |
| `protocolVersion` | 数字 | `getProtocolVersion()` | `int` | `com.destroystokyo.paper.event.server.PaperServerListPingEvent` |
| `version` | 字符串 | `getVersion()` | `java.lang.String` | `com.destroystokyo.paper.event.server.PaperServerListPingEvent` |

[[Data-Format|通用字段、数据格式和限制]] · [[Event-com-destroystokyo-paper-event-server-paperserverlistpingevent-en|English]]

若此事件尚未启用，请将其 Java 完整类名或简单类名加入 Paper 插件配置的 `events.include`。
