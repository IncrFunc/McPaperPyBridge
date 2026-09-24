# ThrownEggHatchEvent

[[Home|首页]] / [[Category-entity|实体]]

- Java 类: `com.destroystokyo.paper.event.entity.ThrownEggHatchEvent`
- 父类: `org.bukkit.event.Event`
- Python 订阅名: `ThrownEggHatchEvent`
- Python 常量: `Events.THROWN_EGG_HATCH`
- 可取消: 否
- 可能关联玩家: 没有已知玩家 getter
- 处理器列表定义于: `com.destroystokyo.paper.event.entity.ThrownEggHatchEvent`
- [Paper 官方 Javadoc](https://jd.papermc.io/paper/1.16.5/com/destroystokyo/paper/event/entity/ThrownEggHatchEvent.html)

## Python 示例

```python
from paperpybridge import Events

@bridge.on(Events.THROWN_EGG_HATCH)
def on_event(event):
    print(event.event, event.data)
```

## `data` 字段

| 字段 | JSON 类型 | Java getter | Java 返回类型 | 定义于 |
| --- | --- | --- | --- | --- |
| `egg` | 实体摘要 | `getEgg()` | `org.bukkit.entity.Egg` | `com.destroystokyo.paper.event.entity.ThrownEggHatchEvent` |
| `hatchingType` | 字符串 | `getHatchingType()` | `org.bukkit.entity.EntityType` | `com.destroystokyo.paper.event.entity.ThrownEggHatchEvent` |
| `numHatches` | 数字 | `getNumHatches()` | `byte` | `com.destroystokyo.paper.event.entity.ThrownEggHatchEvent` |
| `hatching` | 布尔值 | `isHatching()` | `boolean` | `com.destroystokyo.paper.event.entity.ThrownEggHatchEvent` |

[[Data-Format|通用字段、数据格式和限制]] · [[Event-com-destroystokyo-paper-event-entity-thrownegghatchevent-en|English]]

若此事件尚未启用，请将其 Java 完整类名或简单类名加入 Paper 插件配置的 `events.include`。
