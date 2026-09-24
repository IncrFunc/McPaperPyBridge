# PlayerElytraBoostEvent

[[Home|首页]] / [[Category-player|玩家]]

- Java 类: `com.destroystokyo.paper.event.player.PlayerElytraBoostEvent`
- 父类: `org.bukkit.event.player.PlayerEvent`
- Python 订阅名: `PlayerElytraBoostEvent`
- Python 常量: `Events.PLAYER_ELYTRA_BOOST`
- 可取消: 是
- 可能关联玩家: 取决于实际对象
- 处理器列表定义于: `com.destroystokyo.paper.event.player.PlayerElytraBoostEvent`
- [Paper 官方 Javadoc](https://jd.papermc.io/paper/1.16.5/com/destroystokyo/paper/event/player/PlayerElytraBoostEvent.html)

## Python 示例

```python
from paperpybridge import Events

@bridge.on(Events.PLAYER_ELYTRA_BOOST)
def on_event(event):
    print(event.event, event.data)
```

## `data` 字段

| 字段 | JSON 类型 | Java getter | Java 返回类型 | 定义于 |
| --- | --- | --- | --- | --- |
| `firework` | 实体摘要 | `getFirework()` | `org.bukkit.entity.Firework` | `com.destroystokyo.paper.event.player.PlayerElytraBoostEvent` |
| `itemStack` | 物品摘要 | `getItemStack()` | `org.bukkit.inventory.ItemStack` | `com.destroystokyo.paper.event.player.PlayerElytraBoostEvent` |

[[Data-Format|通用字段、数据格式和限制]] · [[Event-com-destroystokyo-paper-event-player-playerelytraboostevent-en|English]]

若此事件尚未启用，请将其 Java 完整类名或简单类名加入 Paper 插件配置的 `events.include`。
