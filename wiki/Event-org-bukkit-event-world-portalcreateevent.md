# PortalCreateEvent

[[Home|首页]] / [[Category-world|世界]]

- Java 类: `org.bukkit.event.world.PortalCreateEvent`
- 父类: `org.bukkit.event.world.WorldEvent`
- Python 订阅名: `PortalCreateEvent`
- Python 常量: `Events.PORTAL_CREATE`
- 可取消: 是
- 可能关联玩家: 取决于实际对象
- 处理器列表定义于: `org.bukkit.event.world.PortalCreateEvent`
- [Paper 官方 Javadoc](https://jd.papermc.io/paper/1.16.5/org/bukkit/event/world/PortalCreateEvent.html)

## Python 示例

```python
from paperpybridge import Events

@bridge.on(Events.PORTAL_CREATE)
def on_event(event):
    print(event.event, event.data)
```

## `data` 字段

| 字段 | JSON 类型 | Java getter | Java 返回类型 | 定义于 |
| --- | --- | --- | --- | --- |
| `entity` | 实体摘要 | `getEntity()` | `org.bukkit.entity.Entity` | `org.bukkit.event.world.PortalCreateEvent` |
| `reason` | 字符串 | `getReason()` | `org.bukkit.event.world.PortalCreateEvent$CreateReason` | `org.bukkit.event.world.PortalCreateEvent` |
| `world` | 世界摘要 | `getWorld()` | `org.bukkit.World` | `org.bukkit.event.world.WorldEvent` |

[[Data-Format|通用字段、数据格式和限制]] · [[Event-org-bukkit-event-world-portalcreateevent-en|English]]

若此事件尚未启用，请将其 Java 完整类名或简单类名加入 Paper 插件配置的 `events.include`。
