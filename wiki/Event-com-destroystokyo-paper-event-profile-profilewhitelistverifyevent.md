# ProfileWhitelistVerifyEvent

[[Home|首页]] / [[Category-profile|玩家资料]]

- Java 类: `com.destroystokyo.paper.event.profile.ProfileWhitelistVerifyEvent`
- 父类: `org.bukkit.event.Event`
- Python 订阅名: `ProfileWhitelistVerifyEvent`
- Python 常量: `Events.PROFILE_WHITELIST_VERIFY`
- 可取消: 否
- 可能关联玩家: 没有已知玩家 getter
- 处理器列表定义于: `com.destroystokyo.paper.event.profile.ProfileWhitelistVerifyEvent`
- [Paper 官方 Javadoc](https://jd.papermc.io/paper/1.16.5/com/destroystokyo/paper/event/profile/ProfileWhitelistVerifyEvent.html)

## Python 示例

```python
from paperpybridge import Events

@bridge.on(Events.PROFILE_WHITELIST_VERIFY)
def on_event(event):
    print(event.event, event.data)
```

## `data` 字段

| 字段 | JSON 类型 | Java getter | Java 返回类型 | 定义于 |
| --- | --- | --- | --- | --- |
| `kickMessage` | 字符串 | `getKickMessage()` | `java.lang.String` | `com.destroystokyo.paper.event.profile.ProfileWhitelistVerifyEvent` |
| `op` | 布尔值 | `isOp()` | `boolean` | `com.destroystokyo.paper.event.profile.ProfileWhitelistVerifyEvent` |
| `whitelistEnabled` | 布尔值 | `isWhitelistEnabled()` | `boolean` | `com.destroystokyo.paper.event.profile.ProfileWhitelistVerifyEvent` |
| `whitelisted` | 布尔值 | `isWhitelisted()` | `boolean` | `com.destroystokyo.paper.event.profile.ProfileWhitelistVerifyEvent` |

[[Data-Format|通用字段、数据格式和限制]] · [[Event-com-destroystokyo-paper-event-profile-profilewhitelistverifyevent-en|English]]

若此事件尚未启用，请将其 Java 完整类名或简单类名加入 Paper 插件配置的 `events.include`。
