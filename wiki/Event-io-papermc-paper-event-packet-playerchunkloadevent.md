# PlayerChunkLoadEvent

[[Home|首页]] / [[Category-packet|网络包]]

- Java 类: `io.papermc.paper.event.packet.PlayerChunkLoadEvent`
- 父类: `org.bukkit.event.world.ChunkEvent`
- Python 订阅名: `PlayerChunkLoadEvent`
- Python 常量: `Events.PLAYER_CHUNK_LOAD`
- 可取消: 否
- 可能关联玩家: 取决于实际对象
- 处理器列表定义于: `io.papermc.paper.event.packet.PlayerChunkLoadEvent`
- [Paper 官方 Javadoc](https://jd.papermc.io/paper/1.16.5/io/papermc/paper/event/packet/PlayerChunkLoadEvent.html)

## Python 示例

```python
from paperpybridge import Events

@bridge.on(Events.PLAYER_CHUNK_LOAD)
def on_event(event):
    print(event.event, event.data)
```

## `data` 字段

| 字段 | JSON 类型 | Java getter | Java 返回类型 | 定义于 |
| --- | --- | --- | --- | --- |
| `world` | 世界摘要 | `getWorld()` | `org.bukkit.World` | `org.bukkit.event.world.WorldEvent` |

[[Data-Format|通用字段、数据格式和限制]] · [[Event-io-papermc-paper-event-packet-playerchunkloadevent-en|English]]

若此事件尚未启用，请将其 Java 完整类名或简单类名加入 Paper 插件配置的 `events.include`。
