# InventoryDragEvent

[[Home|首页]] / [[Category-inventory|物品栏]]

- Java 类: `org.bukkit.event.inventory.InventoryDragEvent`
- 父类: `org.bukkit.event.inventory.InventoryInteractEvent`
- Python 订阅名: `InventoryDragEvent`
- Python 常量: `Events.INVENTORY_DRAG`
- 可取消: 是
- 可能关联玩家: 取决于实际对象
- 处理器列表定义于: `org.bukkit.event.inventory.InventoryDragEvent`
- [Paper 官方 Javadoc](https://jd.papermc.io/paper/1.16.5/org/bukkit/event/inventory/InventoryDragEvent.html)

## Python 示例

```python
from paperpybridge import Events

@bridge.on(Events.INVENTORY_DRAG)
def on_event(event):
    print(event.event, event.data)
```

## `data` 字段

| 字段 | JSON 类型 | Java getter | Java 返回类型 | 定义于 |
| --- | --- | --- | --- | --- |
| `cursor` | 物品摘要 | `getCursor()` | `org.bukkit.inventory.ItemStack` | `org.bukkit.event.inventory.InventoryDragEvent` |
| `oldCursor` | 物品摘要 | `getOldCursor()` | `org.bukkit.inventory.ItemStack` | `org.bukkit.event.inventory.InventoryDragEvent` |
| `result` | 字符串 | `getResult()` | `org.bukkit.event.Event$Result` | `org.bukkit.event.inventory.InventoryInteractEvent` |
| `type` | 字符串 | `getType()` | `org.bukkit.event.inventory.DragType` | `org.bukkit.event.inventory.InventoryDragEvent` |
| `whoClicked` | 实体摘要 | `getWhoClicked()` | `org.bukkit.entity.HumanEntity` | `org.bukkit.event.inventory.InventoryInteractEvent` |

[[Data-Format|通用字段、数据格式和限制]] · [[Event-org-bukkit-event-inventory-inventorydragevent-en|English]]

若此事件尚未启用，请将其 Java 完整类名或简单类名加入 Paper 插件配置的 `events.include`。
