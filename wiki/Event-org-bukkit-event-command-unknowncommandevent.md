# UnknownCommandEvent

[[Home|首页]] / [[Category-command|命令]]

- Java 类: `org.bukkit.event.command.UnknownCommandEvent`
- 父类: `org.bukkit.event.Event`
- Python 订阅名: `UnknownCommandEvent`
- Python 常量: `Events.UNKNOWN_COMMAND`
- 可取消: 否
- 可能关联玩家: 没有已知玩家 getter
- 处理器列表定义于: `org.bukkit.event.command.UnknownCommandEvent`
- [Paper 官方 Javadoc](https://jd.papermc.io/paper/1.16.5/org/bukkit/event/command/UnknownCommandEvent.html)

## Python 示例

```python
from paperpybridge import Events

@bridge.on(Events.UNKNOWN_COMMAND)
def on_event(event):
    print(event.event, event.data)
```

## `data` 字段

| 字段 | JSON 类型 | Java getter | Java 返回类型 | 定义于 |
| --- | --- | --- | --- | --- |
| `commandLine` | 字符串 | `getCommandLine()` | `java.lang.String` | `org.bukkit.event.command.UnknownCommandEvent` |
| `message` | 字符串 | `getMessage()` | `java.lang.String` | `org.bukkit.event.command.UnknownCommandEvent` |

[[Data-Format|通用字段、数据格式和限制]] · [[Event-org-bukkit-event-command-unknowncommandevent-en|English]]

若此事件尚未启用，请将其 Java 完整类名或简单类名加入 Paper 插件配置的 `events.include`。
