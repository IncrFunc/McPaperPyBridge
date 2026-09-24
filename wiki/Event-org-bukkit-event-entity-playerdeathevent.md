# PlayerDeathEvent

[[Home|首页]] / [[Category-entity|实体]]

- Java 类: `org.bukkit.event.entity.PlayerDeathEvent`
- 父类: `org.bukkit.event.entity.EntityDeathEvent`
- Python 订阅名: `PlayerDeathEvent`
- Python 常量: `Events.PLAYER_DEATH`
- 可取消: 是
- 可能关联玩家: 取决于实际对象
- 处理器列表定义于: `org.bukkit.event.entity.EntityDeathEvent`
- [Paper 官方 Javadoc](https://jd.papermc.io/paper/1.16.5/org/bukkit/event/entity/PlayerDeathEvent.html)

## Python 示例

```python
from paperpybridge import Events

@bridge.on(Events.PLAYER_DEATH)
def on_event(event):
    print(event.event, event.data)
```

## `data` 字段

| 字段 | JSON 类型 | Java getter | Java 返回类型 | 定义于 |
| --- | --- | --- | --- | --- |
| `deathMessage` | 字符串 | `getDeathMessage()` | `java.lang.String` | `org.bukkit.event.entity.PlayerDeathEvent` |
| `deathSound` | 字符串 | `getDeathSound()` | `org.bukkit.Sound` | `org.bukkit.event.entity.EntityDeathEvent` |
| `deathSoundCategory` | 字符串 | `getDeathSoundCategory()` | `org.bukkit.SoundCategory` | `org.bukkit.event.entity.EntityDeathEvent` |
| `deathSoundPitch` | 数字 | `getDeathSoundPitch()` | `float` | `org.bukkit.event.entity.EntityDeathEvent` |
| `deathSoundVolume` | 数字 | `getDeathSoundVolume()` | `float` | `org.bukkit.event.entity.EntityDeathEvent` |
| `droppedExp` | 数字 | `getDroppedExp()` | `int` | `org.bukkit.event.entity.EntityDeathEvent` |
| `entity` | 实体摘要 | `getEntity()` | `org.bukkit.entity.LivingEntity` | `org.bukkit.event.entity.PlayerDeathEvent` |
| `entityType` | 字符串 | `getEntityType()` | `org.bukkit.entity.EntityType` | `org.bukkit.event.entity.EntityEvent` |
| `keepInventory` | 布尔值 | `getKeepInventory()` | `boolean` | `org.bukkit.event.entity.PlayerDeathEvent` |
| `keepLevel` | 布尔值 | `getKeepLevel()` | `boolean` | `org.bukkit.event.entity.PlayerDeathEvent` |
| `newExp` | 数字 | `getNewExp()` | `int` | `org.bukkit.event.entity.PlayerDeathEvent` |
| `newLevel` | 数字 | `getNewLevel()` | `int` | `org.bukkit.event.entity.PlayerDeathEvent` |
| `newTotalExp` | 数字 | `getNewTotalExp()` | `int` | `org.bukkit.event.entity.PlayerDeathEvent` |
| `reviveHealth` | 数字 | `getReviveHealth()` | `double` | `org.bukkit.event.entity.EntityDeathEvent` |

[[Data-Format|通用字段、数据格式和限制]] · [[Event-org-bukkit-event-entity-playerdeathevent-en|English]]

若此事件尚未启用，请将其 Java 完整类名或简单类名加入 Paper 插件配置的 `events.include`。
