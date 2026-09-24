# PlayerCommandPreprocessEvent

[[Home|首页]] / [[Category-player|玩家]]

- Java 类: `org.bukkit.event.player.PlayerCommandPreprocessEvent`
- 父类: `org.bukkit.event.player.PlayerEvent`
- Python 订阅名: `PlayerCommandPreprocessEvent`
- Python 常量: `Events.PLAYER_COMMAND_PREPROCESS`
- 可取消: 是
- 可能关联玩家: 取决于实际对象
- 处理器列表定义于: `org.bukkit.event.player.PlayerCommandPreprocessEvent`
- [Paper 官方 Javadoc](https://jd.papermc.io/paper/1.16.5/org/bukkit/event/player/PlayerCommandPreprocessEvent.html)

## Python 示例

```python
from paperpybridge import Events

@bridge.on(Events.PLAYER_COMMAND_PREPROCESS)
def on_event(event):
    print(event.event, event.data)
```

## `data` 字段

| 字段 | JSON 类型 | Java getter | Java 返回类型 | 定义于 |
| --- | --- | --- | --- | --- |
| `message` | 字符串 | `getMessage()` | `java.lang.String` | `org.bukkit.event.player.PlayerCommandPreprocessEvent` |

[[Data-Format|通用字段、数据格式和限制]] · [[Event-org-bukkit-event-player-playercommandpreprocessevent-en|English]]

若此事件尚未启用，请将其 Java 完整类名或简单类名加入 Paper 插件配置的 `events.include`。
