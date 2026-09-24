# ElderGuardianAppearanceEvent

[[Home|首页]] / [[Category-entity|实体]]

- Java 类: `io.papermc.paper.event.entity.ElderGuardianAppearanceEvent`
- 父类: `org.bukkit.event.entity.EntityEvent`
- Python 订阅名: `ElderGuardianAppearanceEvent`
- Python 常量: `Events.ELDER_GUARDIAN_APPEARANCE`
- 可取消: 是
- 可能关联玩家: 取决于实际对象
- 处理器列表定义于: `io.papermc.paper.event.entity.ElderGuardianAppearanceEvent`
- [Paper 官方 Javadoc](https://jd.papermc.io/paper/1.16.5/io/papermc/paper/event/entity/ElderGuardianAppearanceEvent.html)

## Python 示例

```python
from paperpybridge import Events

@bridge.on(Events.ELDER_GUARDIAN_APPEARANCE)
def on_event(event):
    print(event.event, event.data)
```

## `data` 字段

| 字段 | JSON 类型 | Java getter | Java 返回类型 | 定义于 |
| --- | --- | --- | --- | --- |
| `affectedPlayer` | 实体摘要 | `getAffectedPlayer()` | `org.bukkit.entity.Player` | `io.papermc.paper.event.entity.ElderGuardianAppearanceEvent` |
| `entity` | 实体摘要 | `getEntity()` | `org.bukkit.entity.Entity` | `io.papermc.paper.event.entity.ElderGuardianAppearanceEvent` |
| `entityType` | 字符串 | `getEntityType()` | `org.bukkit.entity.EntityType` | `org.bukkit.event.entity.EntityEvent` |

[[Data-Format|通用字段、数据格式和限制]] · [[Event-io-papermc-paper-event-entity-elderguardianappearanceevent-en|English]]

若此事件尚未启用，请将其 Java 完整类名或简单类名加入 Paper 插件配置的 `events.include`。
