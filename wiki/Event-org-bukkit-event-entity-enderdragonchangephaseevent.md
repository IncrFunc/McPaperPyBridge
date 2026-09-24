# EnderDragonChangePhaseEvent

[[Home|首页]] / [[Category-entity|实体]]

- Java 类: `org.bukkit.event.entity.EnderDragonChangePhaseEvent`
- 父类: `org.bukkit.event.entity.EntityEvent`
- Python 订阅名: `EnderDragonChangePhaseEvent`
- Python 常量: `Events.ENDER_DRAGON_CHANGE_PHASE`
- 可取消: 是
- 可能关联玩家: 取决于实际对象
- 处理器列表定义于: `org.bukkit.event.entity.EnderDragonChangePhaseEvent`
- [Paper 官方 Javadoc](https://jd.papermc.io/paper/1.16.5/org/bukkit/event/entity/EnderDragonChangePhaseEvent.html)

## Python 示例

```python
from paperpybridge import Events

@bridge.on(Events.ENDER_DRAGON_CHANGE_PHASE)
def on_event(event):
    print(event.event, event.data)
```

## `data` 字段

| 字段 | JSON 类型 | Java getter | Java 返回类型 | 定义于 |
| --- | --- | --- | --- | --- |
| `currentPhase` | 字符串 | `getCurrentPhase()` | `org.bukkit.entity.EnderDragon$Phase` | `org.bukkit.event.entity.EnderDragonChangePhaseEvent` |
| `entity` | 实体摘要 | `getEntity()` | `org.bukkit.entity.EnderDragon` | `org.bukkit.event.entity.EnderDragonChangePhaseEvent` |
| `entityType` | 字符串 | `getEntityType()` | `org.bukkit.entity.EntityType` | `org.bukkit.event.entity.EntityEvent` |
| `newPhase` | 字符串 | `getNewPhase()` | `org.bukkit.entity.EnderDragon$Phase` | `org.bukkit.event.entity.EnderDragonChangePhaseEvent` |

[[Data-Format|通用字段、数据格式和限制]] · [[Event-org-bukkit-event-entity-enderdragonchangephaseevent-en|English]]

若此事件尚未启用，请将其 Java 完整类名或简单类名加入 Paper 插件配置的 `events.include`。
