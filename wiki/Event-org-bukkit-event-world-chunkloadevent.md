# ChunkLoadEvent

[[Home|首页]] / [[Category-world|世界]]

- Java 类: `org.bukkit.event.world.ChunkLoadEvent`
- 父类: `org.bukkit.event.world.ChunkEvent`
- Python 订阅名: `ChunkLoadEvent`
- Python 常量: `Events.CHUNK_LOAD`
- 可取消: 否
- 可能关联玩家: 没有已知玩家 getter
- 处理器列表定义于: `org.bukkit.event.world.ChunkLoadEvent`
- [Paper 官方 Javadoc](https://jd.papermc.io/paper/1.16.5/org/bukkit/event/world/ChunkLoadEvent.html)

## Python 示例

```python
from paperpybridge import Events

@bridge.on(Events.CHUNK_LOAD)
def on_event(event):
    print(event.event, event.data)
```

## `data` 字段

| 字段 | JSON 类型 | Java getter | Java 返回类型 | 定义于 |
| --- | --- | --- | --- | --- |
| `world` | 世界摘要 | `getWorld()` | `org.bukkit.World` | `org.bukkit.event.world.WorldEvent` |
| `newChunk` | 布尔值 | `isNewChunk()` | `boolean` | `org.bukkit.event.world.ChunkLoadEvent` |

[[Data-Format|通用字段、数据格式和限制]] · [[Event-org-bukkit-event-world-chunkloadevent-en|English]]

若此事件尚未启用，请将其 Java 完整类名或简单类名加入 Paper 插件配置的 `events.include`。
