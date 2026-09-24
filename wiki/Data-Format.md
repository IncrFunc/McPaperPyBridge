# 通用字段、数据格式和限制

[[Home|首页]] · [[Data-Format-en|English]]

## 示例

```json
{"protocol_version":1,"type":"PlayerMoveEvent","event":"org.bukkit.event.player.PlayerMoveEvent","name":"PlayerMoveEvent","server":"survival","asynchronous":false,"timestamp_ms":1234567890000,"cancelled":false,"player":{"uuid":"...","name":"Steve"},"data":{"from":{"world":"world","x":1,"y":64,"z":2,"yaw":0,"pitch":0}}}
```

- 总会出现：`protocol_version`、`type`、`event`、`name`、`server`、`asynchronous`、`timestamp_ms`、`data`。
- `cancelled` 仅在可取消事件中出现；`player` 仅在识别到玩家时出现。
- 字符串 `data.message` 还会复制到顶层 `message`。
- `data` 来自受支持的公开无参数 getter；返回空值或调用失败时，该字段缺失。
- `data` 最多 24 个字段、4096 字节；字符串最多 512 字符，超限时删减末尾字段。
- 世界、位置、方块、实体和物品会转成摘要，不是完整 Bukkit 对象。
- 插件将事件排队，每批最多发送 32 条；Python 跟不上时可能丢弃事件。
- Python 不能同步取消或修改原事件。

## 摘要对象

| 类型 | JSON 属性 |
| --- | --- |
| `world` | `name`, `uuid` |
| `location` | `world`（可选）, `x`, `y`, `z`, `yaw`, `pitch` |
| `block` | `world`, `x`, `y`, `z`, `type` |
| `entity` | `uuid`, `type`, `name`（玩家时） |
| `item` | `type`, `amount` |
