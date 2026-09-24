# PlayerInitialSpawnEvent

[[Home|首页]] / [[Category-player|玩家]]

- Java 类: `com.destroystokyo.paper.event.player.PlayerInitialSpawnEvent`
- 父类: `org.spigotmc.event.player.PlayerSpawnLocationEvent`
- Python 订阅名: `PlayerInitialSpawnEvent`
- Python 常量: `Events.PLAYER_INITIAL_SPAWN`
- 可取消: 否
- 可能关联玩家: 取决于实际对象
- 处理器列表定义于: `org.spigotmc.event.player.PlayerSpawnLocationEvent`
- [Paper 官方 Javadoc](https://jd.papermc.io/paper/1.16.5/com/destroystokyo/paper/event/player/PlayerInitialSpawnEvent.html)

## Python 示例

```python
from paperpybridge import Events

@bridge.on(Events.PLAYER_INITIAL_SPAWN)
def on_event(event):
    print(event.event, event.data)
```

## `data` 字段

| 字段 | JSON 类型 | Java getter | Java 返回类型 | 定义于 |
| --- | --- | --- | --- | --- |
| `spawnLocation` | 位置摘要 | `getSpawnLocation()` | `org.bukkit.Location` | `org.spigotmc.event.player.PlayerSpawnLocationEvent` |

[[Data-Format|通用字段、数据格式和限制]] · [[Event-com-destroystokyo-paper-event-player-playerinitialspawnevent-en|English]]

若此事件尚未启用，请将其 Java 完整类名或简单类名加入 Paper 插件配置的 `events.include`。
