# LingeringPotionSplashEvent

[[Home|首页]] / [[Category-entity|实体]]

- Java 类: `org.bukkit.event.entity.LingeringPotionSplashEvent`
- 父类: `org.bukkit.event.entity.ProjectileHitEvent`
- Python 订阅名: `LingeringPotionSplashEvent`
- Python 常量: `Events.LINGERING_POTION_SPLASH`
- 可取消: 是
- 可能关联玩家: 取决于实际对象
- 处理器列表定义于: `org.bukkit.event.entity.LingeringPotionSplashEvent`
- [Paper 官方 Javadoc](https://jd.papermc.io/paper/1.16.5/org/bukkit/event/entity/LingeringPotionSplashEvent.html)

## Python 示例

```python
from paperpybridge import Events

@bridge.on(Events.LINGERING_POTION_SPLASH)
def on_event(event):
    print(event.event, event.data)
```

## `data` 字段

| 字段 | JSON 类型 | Java getter | Java 返回类型 | 定义于 |
| --- | --- | --- | --- | --- |
| `areaEffectCloud` | 实体摘要 | `getAreaEffectCloud()` | `org.bukkit.entity.AreaEffectCloud` | `org.bukkit.event.entity.LingeringPotionSplashEvent` |
| `entity` | 实体摘要 | `getEntity()` | `org.bukkit.entity.Entity` | `org.bukkit.event.entity.LingeringPotionSplashEvent` |
| `entityType` | 字符串 | `getEntityType()` | `org.bukkit.entity.EntityType` | `org.bukkit.event.entity.EntityEvent` |
| `hitBlock` | 方块摘要 | `getHitBlock()` | `org.bukkit.block.Block` | `org.bukkit.event.entity.ProjectileHitEvent` |
| `hitBlockFace` | 字符串 | `getHitBlockFace()` | `org.bukkit.block.BlockFace` | `org.bukkit.event.entity.ProjectileHitEvent` |
| `hitEntity` | 实体摘要 | `getHitEntity()` | `org.bukkit.entity.Entity` | `org.bukkit.event.entity.ProjectileHitEvent` |

[[Data-Format|通用字段、数据格式和限制]] · [[Event-org-bukkit-event-entity-lingeringpotionsplashevent-en|English]]

若此事件尚未启用，请将其 Java 完整类名或简单类名加入 Paper 插件配置的 `events.include`。
