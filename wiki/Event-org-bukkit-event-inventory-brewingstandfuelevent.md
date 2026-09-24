# BrewingStandFuelEvent

[[Home|首页]] / [[Category-inventory|物品栏]]

- Java 类: `org.bukkit.event.inventory.BrewingStandFuelEvent`
- 父类: `org.bukkit.event.block.BlockEvent`
- Python 订阅名: `BrewingStandFuelEvent`
- Python 常量: `Events.BREWING_STAND_FUEL`
- 可取消: 是
- 可能关联玩家: 没有已知玩家 getter
- 处理器列表定义于: `org.bukkit.event.inventory.BrewingStandFuelEvent`
- [Paper 官方 Javadoc](https://jd.papermc.io/paper/1.16.5/org/bukkit/event/inventory/BrewingStandFuelEvent.html)

## Python 示例

```python
from paperpybridge import Events

@bridge.on(Events.BREWING_STAND_FUEL)
def on_event(event):
    print(event.event, event.data)
```

## `data` 字段

| 字段 | JSON 类型 | Java getter | Java 返回类型 | 定义于 |
| --- | --- | --- | --- | --- |
| `block` | 方块摘要 | `getBlock()` | `org.bukkit.block.Block` | `org.bukkit.event.block.BlockEvent` |
| `fuel` | 物品摘要 | `getFuel()` | `org.bukkit.inventory.ItemStack` | `org.bukkit.event.inventory.BrewingStandFuelEvent` |
| `fuelPower` | 数字 | `getFuelPower()` | `int` | `org.bukkit.event.inventory.BrewingStandFuelEvent` |
| `consuming` | 布尔值 | `isConsuming()` | `boolean` | `org.bukkit.event.inventory.BrewingStandFuelEvent` |

[[Data-Format|通用字段、数据格式和限制]] · [[Event-org-bukkit-event-inventory-brewingstandfuelevent-en|English]]

若此事件尚未启用，请将其 Java 完整类名或简单类名加入 Paper 插件配置的 `events.include`。
