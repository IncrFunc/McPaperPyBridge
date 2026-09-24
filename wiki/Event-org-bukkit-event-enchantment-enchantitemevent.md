# EnchantItemEvent

[[Home|首页]] / [[Category-enchantment|附魔]]

- Java 类: `org.bukkit.event.enchantment.EnchantItemEvent`
- 父类: `org.bukkit.event.inventory.InventoryEvent`
- Python 订阅名: `EnchantItemEvent`
- Python 常量: `Events.ENCHANT_ITEM`
- 可取消: 是
- 可能关联玩家: 没有已知玩家 getter
- 处理器列表定义于: `org.bukkit.event.enchantment.EnchantItemEvent`
- [Paper 官方 Javadoc](https://jd.papermc.io/paper/1.16.5/org/bukkit/event/enchantment/EnchantItemEvent.html)

## Python 示例

```python
from paperpybridge import Events

@bridge.on(Events.ENCHANT_ITEM)
def on_event(event):
    print(event.event, event.data)
```

## `data` 字段

| 字段 | JSON 类型 | Java getter | Java 返回类型 | 定义于 |
| --- | --- | --- | --- | --- |
| `enchantBlock` | 方块摘要 | `getEnchantBlock()` | `org.bukkit.block.Block` | `org.bukkit.event.enchantment.EnchantItemEvent` |
| `enchanter` | 实体摘要 | `getEnchanter()` | `org.bukkit.entity.Player` | `org.bukkit.event.enchantment.EnchantItemEvent` |
| `expLevelCost` | 数字 | `getExpLevelCost()` | `int` | `org.bukkit.event.enchantment.EnchantItemEvent` |
| `item` | 物品摘要 | `getItem()` | `org.bukkit.inventory.ItemStack` | `org.bukkit.event.enchantment.EnchantItemEvent` |

[[Data-Format|通用字段、数据格式和限制]] · [[Event-org-bukkit-event-enchantment-enchantitemevent-en|English]]

若此事件尚未启用，请将其 Java 完整类名或简单类名加入 Paper 插件配置的 `events.include`。
