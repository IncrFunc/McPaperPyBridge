# EntityDropItemEvent

[[Home|首页]] / [[Category-entity|实体]]

- Java 类: `org.bukkit.event.entity.EntityDropItemEvent`
- 父类: `org.bukkit.event.entity.EntityEvent`
- Python 订阅名: `EntityDropItemEvent`
- Python 常量: `Events.ENTITY_DROP_ITEM`
- 可取消: 是
- 可能关联玩家: 取决于实际对象
- 处理器列表定义于: `org.bukkit.event.entity.EntityDropItemEvent`
- [Paper 官方 Javadoc](https://jd.papermc.io/paper/1.16.5/org/bukkit/event/entity/EntityDropItemEvent.html)

## Python 示例

```python
from paperpybridge import Events

@bridge.on(Events.ENTITY_DROP_ITEM)
def on_event(event):
    print(event.event, event.data)
```

## `data` 字段

| 字段 | JSON 类型 | Java getter | Java 返回类型 | 定义于 |
| --- | --- | --- | --- | --- |
| `entity` | 实体摘要 | `getEntity()` | `org.bukkit.entity.Entity` | `org.bukkit.event.entity.EntityEvent` |
| `entityType` | 字符串 | `getEntityType()` | `org.bukkit.entity.EntityType` | `org.bukkit.event.entity.EntityEvent` |
| `itemDrop` | 实体摘要 | `getItemDrop()` | `org.bukkit.entity.Item` | `org.bukkit.event.entity.EntityDropItemEvent` |

[[Data-Format|通用字段、数据格式和限制]] · [[Event-org-bukkit-event-entity-entitydropitemevent-en|English]]

若此事件尚未启用，请将其 Java 完整类名或简单类名加入 Paper 插件配置的 `events.include`。
