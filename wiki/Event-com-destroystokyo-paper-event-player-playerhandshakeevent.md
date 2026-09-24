# PlayerHandshakeEvent

[[Home|首页]] / [[Category-player|玩家]]

- Java 类: `com.destroystokyo.paper.event.player.PlayerHandshakeEvent`
- 父类: `org.bukkit.event.Event`
- Python 订阅名: `PlayerHandshakeEvent`
- Python 常量: `Events.PLAYER_HANDSHAKE`
- 可取消: 是
- 可能关联玩家: 没有已知玩家 getter
- 处理器列表定义于: `com.destroystokyo.paper.event.player.PlayerHandshakeEvent`
- [Paper 官方 Javadoc](https://jd.papermc.io/paper/1.16.5/com/destroystokyo/paper/event/player/PlayerHandshakeEvent.html)

## Python 示例

```python
from paperpybridge import Events

@bridge.on(Events.PLAYER_HANDSHAKE)
def on_event(event):
    print(event.event, event.data)
```

## `data` 字段

| 字段 | JSON 类型 | Java getter | Java 返回类型 | 定义于 |
| --- | --- | --- | --- | --- |
| `failMessage` | 字符串 | `getFailMessage()` | `java.lang.String` | `com.destroystokyo.paper.event.player.PlayerHandshakeEvent` |
| `originalHandshake` | 字符串 | `getOriginalHandshake()` | `java.lang.String` | `com.destroystokyo.paper.event.player.PlayerHandshakeEvent` |
| `originalSocketAddressHostname` | 字符串 | `getOriginalSocketAddressHostname()` | `java.lang.String` | `com.destroystokyo.paper.event.player.PlayerHandshakeEvent` |
| `propertiesJson` | 字符串 | `getPropertiesJson()` | `java.lang.String` | `com.destroystokyo.paper.event.player.PlayerHandshakeEvent` |
| `serverHostname` | 字符串 | `getServerHostname()` | `java.lang.String` | `com.destroystokyo.paper.event.player.PlayerHandshakeEvent` |
| `socketAddressHostname` | 字符串 | `getSocketAddressHostname()` | `java.lang.String` | `com.destroystokyo.paper.event.player.PlayerHandshakeEvent` |
| `uniqueId` | 字符串 | `getUniqueId()` | `java.util.UUID` | `com.destroystokyo.paper.event.player.PlayerHandshakeEvent` |
| `failed` | 布尔值 | `isFailed()` | `boolean` | `com.destroystokyo.paper.event.player.PlayerHandshakeEvent` |

[[Data-Format|通用字段、数据格式和限制]] · [[Event-com-destroystokyo-paper-event-player-playerhandshakeevent-en|English]]

若此事件尚未启用，请将其 Java 完整类名或简单类名加入 Paper 插件配置的 `events.include`。
