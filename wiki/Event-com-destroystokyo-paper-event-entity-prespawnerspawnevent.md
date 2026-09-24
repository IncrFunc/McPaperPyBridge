# PreSpawnerSpawnEvent

[[Home|首页]] / [[Category-entity|实体]]

- Java 类: `com.destroystokyo.paper.event.entity.PreSpawnerSpawnEvent`
- 父类: `com.destroystokyo.paper.event.entity.PreCreatureSpawnEvent`
- Python 订阅名: `PreSpawnerSpawnEvent`
- Python 常量: `Events.PRE_SPAWNER_SPAWN`
- 可取消: 是
- 可能关联玩家: 没有已知玩家 getter
- 处理器列表定义于: `com.destroystokyo.paper.event.entity.PreCreatureSpawnEvent`
- [Paper 官方 Javadoc](https://jd.papermc.io/paper/1.16.5/com/destroystokyo/paper/event/entity/PreSpawnerSpawnEvent.html)

## Python 示例

```python
from paperpybridge import Events

@bridge.on(Events.PRE_SPAWNER_SPAWN)
def on_event(event):
    print(event.event, event.data)
```

## `data` 字段

| 字段 | JSON 类型 | Java getter | Java 返回类型 | 定义于 |
| --- | --- | --- | --- | --- |
| `reason` | 字符串 | `getReason()` | `org.bukkit.event.entity.CreatureSpawnEvent$SpawnReason` | `com.destroystokyo.paper.event.entity.PreCreatureSpawnEvent` |
| `spawnLocation` | 位置摘要 | `getSpawnLocation()` | `org.bukkit.Location` | `com.destroystokyo.paper.event.entity.PreCreatureSpawnEvent` |
| `spawnerLocation` | 位置摘要 | `getSpawnerLocation()` | `org.bukkit.Location` | `com.destroystokyo.paper.event.entity.PreSpawnerSpawnEvent` |
| `type` | 字符串 | `getType()` | `org.bukkit.entity.EntityType` | `com.destroystokyo.paper.event.entity.PreCreatureSpawnEvent` |

[[Data-Format|通用字段、数据格式和限制]] · [[Event-com-destroystokyo-paper-event-entity-prespawnerspawnevent-en|English]]

若此事件尚未启用，请将其 Java 完整类名或简单类名加入 Paper 插件配置的 `events.include`。
