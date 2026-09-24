# VehicleCreateEvent

[[Home|首页]] / [[Category-vehicle|载具]]

- Java 类: `org.bukkit.event.vehicle.VehicleCreateEvent`
- 父类: `org.bukkit.event.vehicle.VehicleEvent`
- Python 订阅名: `VehicleCreateEvent`
- Python 常量: `Events.VEHICLE_CREATE`
- 可取消: 是
- 可能关联玩家: 没有已知玩家 getter
- 处理器列表定义于: `org.bukkit.event.vehicle.VehicleCreateEvent`
- [Paper 官方 Javadoc](https://jd.papermc.io/paper/1.16.5/org/bukkit/event/vehicle/VehicleCreateEvent.html)

## Python 示例

```python
from paperpybridge import Events

@bridge.on(Events.VEHICLE_CREATE)
def on_event(event):
    print(event.event, event.data)
```

## `data` 字段

| 字段 | JSON 类型 | Java getter | Java 返回类型 | 定义于 |
| --- | --- | --- | --- | --- |
| `vehicle` | 实体摘要 | `getVehicle()` | `org.bukkit.entity.Vehicle` | `org.bukkit.event.vehicle.VehicleEvent` |

[[Data-Format|通用字段、数据格式和限制]] · [[Event-org-bukkit-event-vehicle-vehiclecreateevent-en|English]]

若此事件尚未启用，请将其 Java 完整类名或简单类名加入 Paper 插件配置的 `events.include`。
