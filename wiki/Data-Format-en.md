# Wire format and limits

[[Home-en|Home]] · [[Data-Format|中文]]

## Example

```json
{"protocol_version":1,"type":"PlayerMoveEvent","event":"org.bukkit.event.player.PlayerMoveEvent","name":"PlayerMoveEvent","server":"survival","asynchronous":false,"timestamp_ms":1234567890000,"cancelled":false,"player":{"uuid":"...","name":"Steve"},"data":{"from":{"world":"world","x":1,"y":64,"z":2,"yaw":0,"pitch":0}}}
```

- Always present: `protocol_version`, `type`, `event`, `name`, `server`, `asynchronous`, `timestamp_ms`, `data`.
- `cancelled` appears for cancellable events; `player` appears only when a player is identified.
- A string `data.message` is also copied to top-level `message`.
- `data` comes from supported public no-argument getters. Null or failed getters are omitted.
- At most 24 `data` fields and 4096 bytes; strings are at most 512 characters. Excess tail fields are omitted.
- World, location, block, entity, and item values are summaries, not Bukkit objects.
- The bridge queues events and sends batches of up to 32. Events may be dropped if Python falls behind.
- Python cannot synchronously cancel or modify an event.

## Summary shapes

| Type | JSON properties |
| --- | --- |
| `world` | `name`, `uuid` |
| `location` | `world` (optional), `x`, `y`, `z`, `yaw`, `pitch` |
| `block` | `world`, `x`, `y`, `z`, `type` |
| `entity` | `uuid`, `type`, `name` (for players) |
| `item` | `type`, `amount` |
