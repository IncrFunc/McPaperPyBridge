# RaidSpawnWaveEvent

[[Home|首页]] / [[Category-raid|袭击]]

- Java 类: `org.bukkit.event.raid.RaidSpawnWaveEvent`
- 父类: `org.bukkit.event.raid.RaidEvent`
- Python 订阅名: `RaidSpawnWaveEvent`
- Python 常量: `Events.RAID_SPAWN_WAVE`
- 可取消: 否
- 可能关联玩家: 没有已知玩家 getter
- 处理器列表定义于: `org.bukkit.event.raid.RaidSpawnWaveEvent`
- [Paper 官方 Javadoc](https://jd.papermc.io/paper/1.16.5/org/bukkit/event/raid/RaidSpawnWaveEvent.html)

## Python 示例

```python
from paperpybridge import Events

@bridge.on(Events.RAID_SPAWN_WAVE)
def on_event(event):
    print(event.event, event.data)
```

## `data` 字段

| 字段 | JSON 类型 | Java getter | Java 返回类型 | 定义于 |
| --- | --- | --- | --- | --- |
| `patrolLeader` | 实体摘要 | `getPatrolLeader()` | `org.bukkit.entity.Raider` | `org.bukkit.event.raid.RaidSpawnWaveEvent` |
| `world` | 世界摘要 | `getWorld()` | `org.bukkit.World` | `org.bukkit.event.world.WorldEvent` |

[[Data-Format|通用字段、数据格式和限制]] · [[Event-org-bukkit-event-raid-raidspawnwaveevent-en|English]]

若此事件尚未启用，请将其 Java 完整类名或简单类名加入 Paper 插件配置的 `events.include`。
