# PlayerItemConsumeEvent

[[Home|首页]] / [[Category-player|玩家]]

- Java 类: `org.bukkit.event.player.PlayerItemConsumeEvent`
- 父类: `org.bukkit.event.player.PlayerEvent`
- Python 订阅名: `PlayerItemConsumeEvent`
- Python 常量: `Events.PLAYER_ITEM_CONSUME`
- 可取消: 是
- 可能关联玩家: 取决于实际对象
- 处理器列表定义于: `org.bukkit.event.player.PlayerItemConsumeEvent`
- [Paper 官方 Javadoc](https://jd.papermc.io/paper/1.16.5/org/bukkit/event/player/PlayerItemConsumeEvent.html)

## Python 示例

```python
from paperpybridge import Events

@bridge.on(Events.PLAYER_ITEM_CONSUME)
def on_event(event):
    print(event.event, event.data)
```

## `data` 字段

| 字段 | JSON 类型 | Java getter | Java 返回类型 | 定义于 |
| --- | --- | --- | --- | --- |
| `item` | 物品摘要 | `getItem()` | `org.bukkit.inventory.ItemStack` | `org.bukkit.event.player.PlayerItemConsumeEvent` |
| `replacement` | 物品摘要 | `getReplacement()` | `org.bukkit.inventory.ItemStack` | `org.bukkit.event.player.PlayerItemConsumeEvent` |

[[Data-Format|通用字段、数据格式和限制]] · [[Event-org-bukkit-event-player-playeritemconsumeevent-en|English]]

若此事件尚未启用，请将其 Java 完整类名或简单类名加入 Paper 插件配置的 `events.include`。
