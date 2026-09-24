# ItemMergeEvent

[[Home|首页]] / [[Category-entity|实体]]

- Java 类: `org.bukkit.event.entity.ItemMergeEvent`
- 父类: `org.bukkit.event.entity.EntityEvent`
- Python 订阅名: `ItemMergeEvent`
- Python 常量: `Events.ITEM_MERGE`
- 可取消: 是
- 可能关联玩家: 取决于实际对象
- 处理器列表定义于: `org.bukkit.event.entity.ItemMergeEvent`
- [Paper 官方 Javadoc](https://jd.papermc.io/paper/1.16.5/org/bukkit/event/entity/ItemMergeEvent.html)

## Python 示例

```python
from paperpybridge import Events

@bridge.on(Events.ITEM_MERGE)
def on_event(event):
    print(event.event, event.data)
```

## `data` 字段

| 字段 | JSON 类型 | Java getter | Java 返回类型 | 定义于 |
| --- | --- | --- | --- | --- |
| `entity` | 实体摘要 | `getEntity()` | `org.bukkit.entity.Entity` | `org.bukkit.event.entity.ItemMergeEvent` |
| `entityType` | 字符串 | `getEntityType()` | `org.bukkit.entity.EntityType` | `org.bukkit.event.entity.EntityEvent` |
| `target` | 实体摘要 | `getTarget()` | `org.bukkit.entity.Item` | `org.bukkit.event.entity.ItemMergeEvent` |

[[Data-Format|通用字段、数据格式和限制]] · [[Event-org-bukkit-event-entity-itemmergeevent-en|English]]

若此事件尚未启用，请将其 Java 完整类名或简单类名加入 Paper 插件配置的 `events.include`。
