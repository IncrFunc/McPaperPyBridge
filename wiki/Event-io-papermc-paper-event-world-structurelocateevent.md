# StructureLocateEvent

[[Home|首页]] / [[Category-world|世界]]

- Java 类: `io.papermc.paper.event.world.StructureLocateEvent`
- 父类: `org.bukkit.event.world.WorldEvent`
- Python 订阅名: `StructureLocateEvent`
- Python 常量: `Events.STRUCTURE_LOCATE`
- 可取消: 是
- 可能关联玩家: 没有已知玩家 getter
- 处理器列表定义于: `io.papermc.paper.event.world.StructureLocateEvent`
- [Paper 官方 Javadoc](https://jd.papermc.io/paper/1.16.5/io/papermc/paper/event/world/StructureLocateEvent.html)

## Python 示例

```python
from paperpybridge import Events

@bridge.on(Events.STRUCTURE_LOCATE)
def on_event(event):
    print(event.event, event.data)
```

## `data` 字段

| 字段 | JSON 类型 | Java getter | Java 返回类型 | 定义于 |
| --- | --- | --- | --- | --- |
| `origin` | 位置摘要 | `getOrigin()` | `org.bukkit.Location` | `io.papermc.paper.event.world.StructureLocateEvent` |
| `radius` | 数字 | `getRadius()` | `int` | `io.papermc.paper.event.world.StructureLocateEvent` |
| `result` | 位置摘要 | `getResult()` | `org.bukkit.Location` | `io.papermc.paper.event.world.StructureLocateEvent` |
| `world` | 世界摘要 | `getWorld()` | `org.bukkit.World` | `org.bukkit.event.world.WorldEvent` |

[[Data-Format|通用字段、数据格式和限制]] · [[Event-io-papermc-paper-event-world-structurelocateevent-en|English]]

若此事件尚未启用，请将其 Java 完整类名或简单类名加入 Paper 插件配置的 `events.include`。
