# PlayerQuitEvent

[[Home|首页]] / [[Category-player|玩家]]

- Java 类: `org.bukkit.event.player.PlayerQuitEvent`
- 父类: `org.bukkit.event.player.PlayerEvent`
- Python 订阅名: `quit`
- Python 常量: `Events.PLAYER_QUIT`
- 可取消: 否
- 可能关联玩家: 取决于实际对象
- 处理器列表定义于: `org.bukkit.event.player.PlayerQuitEvent`
- [Paper 官方 Javadoc](https://jd.papermc.io/paper/1.16.5/org/bukkit/event/player/PlayerQuitEvent.html)

## Python 示例

```python
from paperpybridge import Events

@bridge.on(Events.PLAYER_QUIT)
def on_event(event):
    print(event.event, event.data)
```

## `data` 字段

| 字段 | JSON 类型 | Java getter | Java 返回类型 | 定义于 |
| --- | --- | --- | --- | --- |
| `quitMessage` | 字符串 | `getQuitMessage()` | `java.lang.String` | `org.bukkit.event.player.PlayerQuitEvent` |
| `reason` | 字符串 | `getReason()` | `org.bukkit.event.player.PlayerQuitEvent$QuitReason` | `org.bukkit.event.player.PlayerQuitEvent` |

[[Data-Format|通用字段、数据格式和限制]] · [[Event-org-bukkit-event-player-playerquitevent-en|English]]

若此事件尚未启用，请将其 Java 完整类名或简单类名加入 Paper 插件配置的 `events.include`。
