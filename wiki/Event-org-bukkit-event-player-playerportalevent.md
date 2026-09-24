# PlayerPortalEvent

[[Home|首页]] / [[Category-player|玩家]]

- Java 类: `org.bukkit.event.player.PlayerPortalEvent`
- 父类: `org.bukkit.event.player.PlayerTeleportEvent`
- Python 订阅名: `PlayerPortalEvent`
- Python 常量: `Events.PLAYER_PORTAL`
- 可取消: 是
- 可能关联玩家: 取决于实际对象
- 处理器列表定义于: `org.bukkit.event.player.PlayerPortalEvent`
- [Paper 官方 Javadoc](https://jd.papermc.io/paper/1.16.5/org/bukkit/event/player/PlayerPortalEvent.html)

## Python 示例

```python
from paperpybridge import Events

@bridge.on(Events.PLAYER_PORTAL)
def on_event(event):
    print(event.event, event.data)
```

## `data` 字段

| 字段 | JSON 类型 | Java getter | Java 返回类型 | 定义于 |
| --- | --- | --- | --- | --- |
| `canCreatePortal` | 布尔值 | `getCanCreatePortal()` | `boolean` | `org.bukkit.event.player.PlayerPortalEvent` |
| `cause` | 字符串 | `getCause()` | `org.bukkit.event.player.PlayerTeleportEvent$TeleportCause` | `org.bukkit.event.player.PlayerTeleportEvent` |
| `creationRadius` | 数字 | `getCreationRadius()` | `int` | `org.bukkit.event.player.PlayerPortalEvent` |
| `from` | 位置摘要 | `getFrom()` | `org.bukkit.Location` | `org.bukkit.event.player.PlayerMoveEvent` |
| `searchRadius` | 数字 | `getSearchRadius()` | `int` | `org.bukkit.event.player.PlayerPortalEvent` |
| `to` | 位置摘要 | `getTo()` | `org.bukkit.Location` | `org.bukkit.event.player.PlayerMoveEvent` |

[[Data-Format|通用字段、数据格式和限制]] · [[Event-org-bukkit-event-player-playerportalevent-en|English]]

若此事件尚未启用，请将其 Java 完整类名或简单类名加入 Paper 插件配置的 `events.include`。
