# ExperienceOrbMergeEvent

[[Home|首页]] / [[Category-entity|实体]]

- Java 类: `com.destroystokyo.paper.event.entity.ExperienceOrbMergeEvent`
- 父类: `org.bukkit.event.entity.EntityEvent`
- Python 订阅名: `ExperienceOrbMergeEvent`
- Python 常量: `Events.EXPERIENCE_ORB_MERGE`
- 可取消: 是
- 可能关联玩家: 取决于实际对象
- 处理器列表定义于: `com.destroystokyo.paper.event.entity.ExperienceOrbMergeEvent`
- [Paper 官方 Javadoc](https://jd.papermc.io/paper/1.16.5/com/destroystokyo/paper/event/entity/ExperienceOrbMergeEvent.html)

## Python 示例

```python
from paperpybridge import Events

@bridge.on(Events.EXPERIENCE_ORB_MERGE)
def on_event(event):
    print(event.event, event.data)
```

## `data` 字段

| 字段 | JSON 类型 | Java getter | Java 返回类型 | 定义于 |
| --- | --- | --- | --- | --- |
| `entity` | 实体摘要 | `getEntity()` | `org.bukkit.entity.Entity` | `org.bukkit.event.entity.EntityEvent` |
| `entityType` | 字符串 | `getEntityType()` | `org.bukkit.entity.EntityType` | `org.bukkit.event.entity.EntityEvent` |
| `mergeSource` | 实体摘要 | `getMergeSource()` | `org.bukkit.entity.ExperienceOrb` | `com.destroystokyo.paper.event.entity.ExperienceOrbMergeEvent` |
| `mergeTarget` | 实体摘要 | `getMergeTarget()` | `org.bukkit.entity.ExperienceOrb` | `com.destroystokyo.paper.event.entity.ExperienceOrbMergeEvent` |

[[Data-Format|通用字段、数据格式和限制]] · [[Event-com-destroystokyo-paper-event-entity-experienceorbmergeevent-en|English]]

若此事件尚未启用，请将其 Java 完整类名或简单类名加入 Paper 插件配置的 `events.include`。
