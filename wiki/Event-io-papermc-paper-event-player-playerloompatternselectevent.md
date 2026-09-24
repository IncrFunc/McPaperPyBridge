# PlayerLoomPatternSelectEvent

[[Home|首页]] / [[Category-player|玩家]]

- Java 类: `io.papermc.paper.event.player.PlayerLoomPatternSelectEvent`
- 父类: `org.bukkit.event.player.PlayerEvent`
- Python 订阅名: `PlayerLoomPatternSelectEvent`
- Python 常量: `Events.PLAYER_LOOM_PATTERN_SELECT`
- 可取消: 是
- 可能关联玩家: 取决于实际对象
- 处理器列表定义于: `io.papermc.paper.event.player.PlayerLoomPatternSelectEvent`
- [Paper 官方 Javadoc](https://jd.papermc.io/paper/1.16.5/io/papermc/paper/event/player/PlayerLoomPatternSelectEvent.html)

## Python 示例

```python
from paperpybridge import Events

@bridge.on(Events.PLAYER_LOOM_PATTERN_SELECT)
def on_event(event):
    print(event.event, event.data)
```

## `data` 字段

| 字段 | JSON 类型 | Java getter | Java 返回类型 | 定义于 |
| --- | --- | --- | --- | --- |
| `patternType` | 字符串 | `getPatternType()` | `org.bukkit.block.banner.PatternType` | `io.papermc.paper.event.player.PlayerLoomPatternSelectEvent` |

[[Data-Format|通用字段、数据格式和限制]] · [[Event-io-papermc-paper-event-player-playerloompatternselectevent-en|English]]

若此事件尚未启用，请将其 Java 完整类名或简单类名加入 Paper 插件配置的 `events.include`。
