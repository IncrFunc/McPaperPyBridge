# WitchThrowPotionEvent

[[Home|首页]] / [[Category-entity|实体]]

- Java 类: `com.destroystokyo.paper.event.entity.WitchThrowPotionEvent`
- 父类: `org.bukkit.event.entity.EntityEvent`
- Python 订阅名: `WitchThrowPotionEvent`
- Python 常量: `Events.WITCH_THROW_POTION`
- 可取消: 是
- 可能关联玩家: 取决于实际对象
- 处理器列表定义于: `com.destroystokyo.paper.event.entity.WitchThrowPotionEvent`
- [Paper 官方 Javadoc](https://jd.papermc.io/paper/1.16.5/com/destroystokyo/paper/event/entity/WitchThrowPotionEvent.html)

## Python 示例

```python
from paperpybridge import Events

@bridge.on(Events.WITCH_THROW_POTION)
def on_event(event):
    print(event.event, event.data)
```

## `data` 字段

| 字段 | JSON 类型 | Java getter | Java 返回类型 | 定义于 |
| --- | --- | --- | --- | --- |
| `entity` | 实体摘要 | `getEntity()` | `org.bukkit.entity.Witch` | `com.destroystokyo.paper.event.entity.WitchThrowPotionEvent` |
| `entityType` | 字符串 | `getEntityType()` | `org.bukkit.entity.EntityType` | `org.bukkit.event.entity.EntityEvent` |
| `potion` | 物品摘要 | `getPotion()` | `org.bukkit.inventory.ItemStack` | `com.destroystokyo.paper.event.entity.WitchThrowPotionEvent` |
| `target` | 实体摘要 | `getTarget()` | `org.bukkit.entity.LivingEntity` | `com.destroystokyo.paper.event.entity.WitchThrowPotionEvent` |

[[Data-Format|通用字段、数据格式和限制]] · [[Event-com-destroystokyo-paper-event-entity-witchthrowpotionevent-en|English]]

若此事件尚未启用，请将其 Java 完整类名或简单类名加入 Paper 插件配置的 `events.include`。
