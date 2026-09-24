# VehicleExitEvent

[[Home|首页]] / [[Category-vehicle|载具]]

- Java 类: `org.bukkit.event.vehicle.VehicleExitEvent`
- 父类: `org.bukkit.event.vehicle.VehicleEvent`
- Python 订阅名: `VehicleExitEvent`
- Python 常量: `Events.VEHICLE_EXIT`
- 可取消: 是
- 可能关联玩家: 没有已知玩家 getter
- 处理器列表定义于: `org.bukkit.event.vehicle.VehicleExitEvent`
- [Paper 官方 Javadoc](https://jd.papermc.io/paper/1.16.5/org/bukkit/event/vehicle/VehicleExitEvent.html)

## Python 示例

```python
from paperpybridge import Events

@bridge.on(Events.VEHICLE_EXIT)
def on_event(event):
    print(event.event, event.data)
```

## `data` 字段

| 字段 | JSON 类型 | Java getter | Java 返回类型 | 定义于 |
| --- | --- | --- | --- | --- |
| `exited` | 实体摘要 | `getExited()` | `org.bukkit.entity.LivingEntity` | `org.bukkit.event.vehicle.VehicleExitEvent` |
| `vehicle` | 实体摘要 | `getVehicle()` | `org.bukkit.entity.Vehicle` | `org.bukkit.event.vehicle.VehicleEvent` |
| `cancellable` | 布尔值 | `isCancellable()` | `boolean` | `org.bukkit.event.vehicle.VehicleExitEvent` |

[[Data-Format|通用字段、数据格式和限制]] · [[Event-org-bukkit-event-vehicle-vehicleexitevent-en|English]]

若此事件尚未启用，请将其 Java 完整类名或简单类名加入 Paper 插件配置的 `events.include`。
