# PreLookupProfileEvent

[[Home|首页]] / [[Category-profile|玩家资料]]

- Java 类: `com.destroystokyo.paper.event.profile.PreLookupProfileEvent`
- 父类: `org.bukkit.event.Event`
- Python 订阅名: `PreLookupProfileEvent`
- Python 常量: `Events.PRE_LOOKUP_PROFILE`
- 可取消: 否
- 可能关联玩家: 没有已知玩家 getter
- 处理器列表定义于: `com.destroystokyo.paper.event.profile.PreLookupProfileEvent`
- [Paper 官方 Javadoc](https://jd.papermc.io/paper/1.16.5/com/destroystokyo/paper/event/profile/PreLookupProfileEvent.html)

## Python 示例

```python
from paperpybridge import Events

@bridge.on(Events.PRE_LOOKUP_PROFILE)
def on_event(event):
    print(event.event, event.data)
```

## `data` 字段

| 字段 | JSON 类型 | Java getter | Java 返回类型 | 定义于 |
| --- | --- | --- | --- | --- |
| `name` | 字符串 | `getName()` | `java.lang.String` | `com.destroystokyo.paper.event.profile.PreLookupProfileEvent` |
| `uUID` | 字符串 | `getUUID()` | `java.util.UUID` | `com.destroystokyo.paper.event.profile.PreLookupProfileEvent` |

[[Data-Format|通用字段、数据格式和限制]] · [[Event-com-destroystokyo-paper-event-profile-prelookupprofileevent-en|English]]

若此事件尚未启用，请将其 Java 完整类名或简单类名加入 Paper 插件配置的 `events.include`。
