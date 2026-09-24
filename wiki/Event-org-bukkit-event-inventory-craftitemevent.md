# CraftItemEvent

[[Home|首页]] / [[Category-inventory|物品栏]]

- Java 类: `org.bukkit.event.inventory.CraftItemEvent`
- 父类: `org.bukkit.event.inventory.InventoryClickEvent`
- Python 订阅名: `CraftItemEvent`
- Python 常量: `Events.CRAFT_ITEM`
- 可取消: 是
- 可能关联玩家: 取决于实际对象
- 处理器列表定义于: `org.bukkit.event.inventory.InventoryClickEvent`
- [Paper 官方 Javadoc](https://jd.papermc.io/paper/1.16.5/org/bukkit/event/inventory/CraftItemEvent.html)

## Python 示例

```python
from paperpybridge import Events

@bridge.on(Events.CRAFT_ITEM)
def on_event(event):
    print(event.event, event.data)
```

## `data` 字段

| 字段 | JSON 类型 | Java getter | Java 返回类型 | 定义于 |
| --- | --- | --- | --- | --- |
| `action` | 字符串 | `getAction()` | `org.bukkit.event.inventory.InventoryAction` | `org.bukkit.event.inventory.InventoryClickEvent` |
| `click` | 字符串 | `getClick()` | `org.bukkit.event.inventory.ClickType` | `org.bukkit.event.inventory.InventoryClickEvent` |
| `currentItem` | 物品摘要 | `getCurrentItem()` | `org.bukkit.inventory.ItemStack` | `org.bukkit.event.inventory.InventoryClickEvent` |
| `cursor` | 物品摘要 | `getCursor()` | `org.bukkit.inventory.ItemStack` | `org.bukkit.event.inventory.InventoryClickEvent` |
| `hotbarButton` | 数字 | `getHotbarButton()` | `int` | `org.bukkit.event.inventory.InventoryClickEvent` |
| `rawSlot` | 数字 | `getRawSlot()` | `int` | `org.bukkit.event.inventory.InventoryClickEvent` |
| `result` | 字符串 | `getResult()` | `org.bukkit.event.Event$Result` | `org.bukkit.event.inventory.InventoryInteractEvent` |
| `slot` | 数字 | `getSlot()` | `int` | `org.bukkit.event.inventory.InventoryClickEvent` |
| `slotType` | 字符串 | `getSlotType()` | `org.bukkit.event.inventory.InventoryType$SlotType` | `org.bukkit.event.inventory.InventoryClickEvent` |
| `whoClicked` | 实体摘要 | `getWhoClicked()` | `org.bukkit.entity.HumanEntity` | `org.bukkit.event.inventory.InventoryInteractEvent` |
| `leftClick` | 布尔值 | `isLeftClick()` | `boolean` | `org.bukkit.event.inventory.InventoryClickEvent` |
| `rightClick` | 布尔值 | `isRightClick()` | `boolean` | `org.bukkit.event.inventory.InventoryClickEvent` |
| `shiftClick` | 布尔值 | `isShiftClick()` | `boolean` | `org.bukkit.event.inventory.InventoryClickEvent` |

[[Data-Format|通用字段、数据格式和限制]] · [[Event-org-bukkit-event-inventory-craftitemevent-en|English]]

若此事件尚未启用，请将其 Java 完整类名或简单类名加入 Paper 插件配置的 `events.include`。
