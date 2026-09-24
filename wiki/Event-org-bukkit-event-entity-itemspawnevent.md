# ItemSpawnEvent

[[Home|首页]] / [[Category-entity|实体]]

- Java 类: `org.bukkit.event.entity.ItemSpawnEvent`
- 父类: `org.bukkit.event.entity.EntitySpawnEvent`
- Python 订阅名: `ItemSpawnEvent`
- Python 常量: `Events.ITEM_SPAWN`
- 可取消: 是
- 可能关联玩家: 取决于实际对象
- 处理器列表定义于: `org.bukkit.event.entity.EntitySpawnEvent`
- [Paper 官方 Javadoc](https://jd.papermc.io/paper/1.16.5/org/bukkit/event/entity/ItemSpawnEvent.html)

## Python 示例

```python
from paperpybridge import Events

@bridge.on(Events.ITEM_SPAWN)
def on_event(event):
    print(event.event, event.data)
```

## `data` 字段

| 字段 | JSON 类型 | Java getter | Java 返回类型 | 定义于 |
| --- | --- | --- | --- | --- |
| `entity` | 实体摘要 | `getEntity()` | `org.bukkit.entity.Item` | `org.bukkit.event.entity.ItemSpawnEvent` |
| `entityType` | 字符串 | `getEntityType()` | `org.bukkit.entity.EntityType` | `org.bukkit.event.entity.EntityEvent` |
| `location` | 位置摘要 | `getLocation()` | `org.bukkit.Location` | `org.bukkit.event.entity.EntitySpawnEvent` |

[[Data-Format|通用字段、数据格式和限制]] · [[Event-org-bukkit-event-entity-itemspawnevent-en|English]]

若此事件尚未启用，请将其 Java 完整类名或简单类名加入 Paper 插件配置的 `events.include`。
