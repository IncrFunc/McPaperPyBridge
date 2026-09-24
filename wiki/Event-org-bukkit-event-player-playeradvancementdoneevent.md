# PlayerAdvancementDoneEvent

[[Home|首页]] / [[Category-player|玩家]]

- Java 类: `org.bukkit.event.player.PlayerAdvancementDoneEvent`
- 父类: `org.bukkit.event.player.PlayerEvent`
- Python 订阅名: `PlayerAdvancementDoneEvent`
- Python 常量: `Events.PLAYER_ADVANCEMENT_DONE`
- 可取消: 否
- 可能关联玩家: 取决于实际对象
- 处理器列表定义于: `org.bukkit.event.player.PlayerAdvancementDoneEvent`
- [Paper 官方 Javadoc](https://jd.papermc.io/paper/1.16.5/org/bukkit/event/player/PlayerAdvancementDoneEvent.html)

## Python 示例

```python
from paperpybridge import Events

@bridge.on(Events.PLAYER_ADVANCEMENT_DONE)
def on_event(event):
    print(event.event, event.data)
```

## `data` 字段

没有可序列化的字段，仍会收到通用事件字段。

[[Data-Format|通用字段、数据格式和限制]] · [[Event-org-bukkit-event-player-playeradvancementdoneevent-en|English]]

若此事件尚未启用，请将其 Java 完整类名或简单类名加入 Paper 插件配置的 `events.include`。
