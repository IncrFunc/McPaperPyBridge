# PlayerLecternPageChangeEvent

[[Home|首页]] / [[Category-player|玩家]]

- Java 类: `io.papermc.paper.event.player.PlayerLecternPageChangeEvent`
- 父类: `org.bukkit.event.player.PlayerEvent`
- Python 订阅名: `PlayerLecternPageChangeEvent`
- Python 常量: `Events.PLAYER_LECTERN_PAGE_CHANGE`
- 可取消: 是
- 可能关联玩家: 取决于实际对象
- 处理器列表定义于: `io.papermc.paper.event.player.PlayerLecternPageChangeEvent`
- [Paper 官方 Javadoc](https://jd.papermc.io/paper/1.16.5/io/papermc/paper/event/player/PlayerLecternPageChangeEvent.html)

## Python 示例

```python
from paperpybridge import Events

@bridge.on(Events.PLAYER_LECTERN_PAGE_CHANGE)
def on_event(event):
    print(event.event, event.data)
```

## `data` 字段

| 字段 | JSON 类型 | Java getter | Java 返回类型 | 定义于 |
| --- | --- | --- | --- | --- |
| `book` | 物品摘要 | `getBook()` | `org.bukkit.inventory.ItemStack` | `io.papermc.paper.event.player.PlayerLecternPageChangeEvent` |
| `newPage` | 数字 | `getNewPage()` | `int` | `io.papermc.paper.event.player.PlayerLecternPageChangeEvent` |
| `oldPage` | 数字 | `getOldPage()` | `int` | `io.papermc.paper.event.player.PlayerLecternPageChangeEvent` |
| `pageChangeDirection` | 字符串 | `getPageChangeDirection()` | `io.papermc.paper.event.player.PlayerLecternPageChangeEvent$PageChangeDirection` | `io.papermc.paper.event.player.PlayerLecternPageChangeEvent` |

[[Data-Format|通用字段、数据格式和限制]] · [[Event-io-papermc-paper-event-player-playerlecternpagechangeevent-en|English]]

若此事件尚未启用，请将其 Java 完整类名或简单类名加入 Paper 插件配置的 `events.include`。
