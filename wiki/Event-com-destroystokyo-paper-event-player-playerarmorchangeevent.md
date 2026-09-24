# PlayerArmorChangeEvent

[[Home|首页]] / [[Category-player|玩家]]

- Java 类: `com.destroystokyo.paper.event.player.PlayerArmorChangeEvent`
- 父类: `org.bukkit.event.player.PlayerEvent`
- Python 订阅名: `PlayerArmorChangeEvent`
- Python 常量: `Events.PLAYER_ARMOR_CHANGE`
- 可取消: 否
- 可能关联玩家: 取决于实际对象
- 处理器列表定义于: `com.destroystokyo.paper.event.player.PlayerArmorChangeEvent`
- [Paper 官方 Javadoc](https://jd.papermc.io/paper/1.16.5/com/destroystokyo/paper/event/player/PlayerArmorChangeEvent.html)

## Python 示例

```python
from paperpybridge import Events

@bridge.on(Events.PLAYER_ARMOR_CHANGE)
def on_event(event):
    print(event.event, event.data)
```

## `data` 字段

| 字段 | JSON 类型 | Java getter | Java 返回类型 | 定义于 |
| --- | --- | --- | --- | --- |
| `newItem` | 物品摘要 | `getNewItem()` | `org.bukkit.inventory.ItemStack` | `com.destroystokyo.paper.event.player.PlayerArmorChangeEvent` |
| `oldItem` | 物品摘要 | `getOldItem()` | `org.bukkit.inventory.ItemStack` | `com.destroystokyo.paper.event.player.PlayerArmorChangeEvent` |
| `slotType` | 字符串 | `getSlotType()` | `com.destroystokyo.paper.event.player.PlayerArmorChangeEvent$SlotType` | `com.destroystokyo.paper.event.player.PlayerArmorChangeEvent` |

[[Data-Format|通用字段、数据格式和限制]] · [[Event-com-destroystokyo-paper-event-player-playerarmorchangeevent-en|English]]

若此事件尚未启用，请将其 Java 完整类名或简单类名加入 Paper 插件配置的 `events.include`。
