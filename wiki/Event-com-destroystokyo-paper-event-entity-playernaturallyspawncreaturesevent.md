# PlayerNaturallySpawnCreaturesEvent

[[Home|首页]] / [[Category-entity|实体]]

- Java 类: `com.destroystokyo.paper.event.entity.PlayerNaturallySpawnCreaturesEvent`
- 父类: `org.bukkit.event.player.PlayerEvent`
- Python 订阅名: `PlayerNaturallySpawnCreaturesEvent`
- Python 常量: `Events.PLAYER_NATURALLY_SPAWN_CREATURES`
- 可取消: 是
- 可能关联玩家: 取决于实际对象
- 处理器列表定义于: `com.destroystokyo.paper.event.entity.PlayerNaturallySpawnCreaturesEvent`
- [Paper 官方 Javadoc](https://jd.papermc.io/paper/1.16.5/com/destroystokyo/paper/event/entity/PlayerNaturallySpawnCreaturesEvent.html)

## Python 示例

```python
from paperpybridge import Events

@bridge.on(Events.PLAYER_NATURALLY_SPAWN_CREATURES)
def on_event(event):
    print(event.event, event.data)
```

## `data` 字段

| 字段 | JSON 类型 | Java getter | Java 返回类型 | 定义于 |
| --- | --- | --- | --- | --- |
| `spawnRadius` | 数字 | `getSpawnRadius()` | `byte` | `com.destroystokyo.paper.event.entity.PlayerNaturallySpawnCreaturesEvent` |

[[Data-Format|通用字段、数据格式和限制]] · [[Event-com-destroystokyo-paper-event-entity-playernaturallyspawncreaturesevent-en|English]]

若此事件尚未启用，请将其 Java 完整类名或简单类名加入 Paper 插件配置的 `events.include`。
