# PlayerBedFailEnterEvent

[[Home|首页]] / [[Category-player|玩家]]

- Java 类: `io.papermc.paper.event.player.PlayerBedFailEnterEvent`
- 父类: `org.bukkit.event.player.PlayerEvent`
- Python 订阅名: `PlayerBedFailEnterEvent`
- Python 常量: `Events.PLAYER_BED_FAIL_ENTER`
- 可取消: 是
- 可能关联玩家: 取决于实际对象
- 处理器列表定义于: `io.papermc.paper.event.player.PlayerBedFailEnterEvent`
- [Paper 官方 Javadoc](https://jd.papermc.io/paper/1.16.5/io/papermc/paper/event/player/PlayerBedFailEnterEvent.html)

## Python 示例

```python
from paperpybridge import Events

@bridge.on(Events.PLAYER_BED_FAIL_ENTER)
def on_event(event):
    print(event.event, event.data)
```

## `data` 字段

| 字段 | JSON 类型 | Java getter | Java 返回类型 | 定义于 |
| --- | --- | --- | --- | --- |
| `bed` | 方块摘要 | `getBed()` | `org.bukkit.block.Block` | `io.papermc.paper.event.player.PlayerBedFailEnterEvent` |
| `failReason` | 字符串 | `getFailReason()` | `io.papermc.paper.event.player.PlayerBedFailEnterEvent$FailReason` | `io.papermc.paper.event.player.PlayerBedFailEnterEvent` |
| `willExplode` | 布尔值 | `getWillExplode()` | `boolean` | `io.papermc.paper.event.player.PlayerBedFailEnterEvent` |

[[Data-Format|通用字段、数据格式和限制]] · [[Event-io-papermc-paper-event-player-playerbedfailenterevent-en|English]]

若此事件尚未启用，请将其 Java 完整类名或简单类名加入 Paper 插件配置的 `events.include`。
