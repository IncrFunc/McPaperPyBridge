# BeaconEffectEvent

[[Home|首页]] / [[Category-block|方块]]

- Java 类: `com.destroystokyo.paper.event.block.BeaconEffectEvent`
- 父类: `org.bukkit.event.block.BlockEvent`
- Python 订阅名: `BeaconEffectEvent`
- Python 常量: `Events.BEACON_EFFECT`
- 可取消: 是
- 可能关联玩家: 取决于实际对象
- 处理器列表定义于: `com.destroystokyo.paper.event.block.BeaconEffectEvent`
- [Paper 官方 Javadoc](https://jd.papermc.io/paper/1.16.5/com/destroystokyo/paper/event/block/BeaconEffectEvent.html)

## Python 示例

```python
from paperpybridge import Events

@bridge.on(Events.BEACON_EFFECT)
def on_event(event):
    print(event.event, event.data)
```

## `data` 字段

| 字段 | JSON 类型 | Java getter | Java 返回类型 | 定义于 |
| --- | --- | --- | --- | --- |
| `block` | 方块摘要 | `getBlock()` | `org.bukkit.block.Block` | `org.bukkit.event.block.BlockEvent` |
| `primary` | 布尔值 | `isPrimary()` | `boolean` | `com.destroystokyo.paper.event.block.BeaconEffectEvent` |

[[Data-Format|通用字段、数据格式和限制]] · [[Event-com-destroystokyo-paper-event-block-beaconeffectevent-en|English]]

若此事件尚未启用，请将其 Java 完整类名或简单类名加入 Paper 插件配置的 `events.include`。
