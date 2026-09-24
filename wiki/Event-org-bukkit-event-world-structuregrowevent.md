# StructureGrowEvent

[[Home|首页]] / [[Category-world|世界]]

- Java 类: `org.bukkit.event.world.StructureGrowEvent`
- 父类: `org.bukkit.event.world.WorldEvent`
- Python 订阅名: `StructureGrowEvent`
- Python 常量: `Events.STRUCTURE_GROW`
- 可取消: 是
- 可能关联玩家: 取决于实际对象
- 处理器列表定义于: `org.bukkit.event.world.StructureGrowEvent`
- [Paper 官方 Javadoc](https://jd.papermc.io/paper/1.16.5/org/bukkit/event/world/StructureGrowEvent.html)

## Python 示例

```python
from paperpybridge import Events

@bridge.on(Events.STRUCTURE_GROW)
def on_event(event):
    print(event.event, event.data)
```

## `data` 字段

| 字段 | JSON 类型 | Java getter | Java 返回类型 | 定义于 |
| --- | --- | --- | --- | --- |
| `location` | 位置摘要 | `getLocation()` | `org.bukkit.Location` | `org.bukkit.event.world.StructureGrowEvent` |
| `species` | 字符串 | `getSpecies()` | `org.bukkit.TreeType` | `org.bukkit.event.world.StructureGrowEvent` |
| `world` | 世界摘要 | `getWorld()` | `org.bukkit.World` | `org.bukkit.event.world.WorldEvent` |
| `fromBonemeal` | 布尔值 | `isFromBonemeal()` | `boolean` | `org.bukkit.event.world.StructureGrowEvent` |

[[Data-Format|通用字段、数据格式和限制]] · [[Event-org-bukkit-event-world-structuregrowevent-en|English]]

若此事件尚未启用，请将其 Java 完整类名或简单类名加入 Paper 插件配置的 `events.include`。
