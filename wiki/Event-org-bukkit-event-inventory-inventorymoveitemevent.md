# InventoryMoveItemEvent

[[Home|首页]] / [[Category-inventory|物品栏]]

- Java 类: `org.bukkit.event.inventory.InventoryMoveItemEvent`
- 父类: `org.bukkit.event.Event`
- Python 订阅名: `InventoryMoveItemEvent`
- Python 常量: `Events.INVENTORY_MOVE_ITEM`
- 可取消: 是
- 可能关联玩家: 没有已知玩家 getter
- 处理器列表定义于: `org.bukkit.event.inventory.InventoryMoveItemEvent`
- [Paper 官方 Javadoc](https://jd.papermc.io/paper/1.16.5/org/bukkit/event/inventory/InventoryMoveItemEvent.html)

## Python 示例

```python
from paperpybridge import Events

@bridge.on(Events.INVENTORY_MOVE_ITEM)
def on_event(event):
    print(event.event, event.data)
```

## `data` 字段

| 字段 | JSON 类型 | Java getter | Java 返回类型 | 定义于 |
| --- | --- | --- | --- | --- |
| `item` | 物品摘要 | `getItem()` | `org.bukkit.inventory.ItemStack` | `org.bukkit.event.inventory.InventoryMoveItemEvent` |

[[Data-Format|通用字段、数据格式和限制]] · [[Event-org-bukkit-event-inventory-inventorymoveitemevent-en|English]]

若此事件尚未启用，请将其 Java 完整类名或简单类名加入 Paper 插件配置的 `events.include`。
