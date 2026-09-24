# PaperPyBridge 事件参考：Paper 1.16.5

本页列出 **333 个可转发的具体事件类**，来自插件内的 `paper-events.txt` 和当前 `EventSnapshot` 序列化规则。
它们共使用 **292 组 HandlerList**；共享 HandlerList 的事件类只注册一次监听器，因此这个数字小于事件类数量。
默认仅转发聊天、玩家加入和退出事件；其他事件需要加入 Paper 插件配置的 `events.include`。Wiki 中列出某事件不代表已启用。
事件含义和触发时机请查看每项的 Paper 官方 Javadoc；本页重点说明 Python 实际接收的字段。

## 通用事件格式

```json
{"protocol_version":1,"type":"PlayerMoveEvent","event":"org.bukkit.event.player.PlayerMoveEvent","name":"PlayerMoveEvent","server":"survival","asynchronous":false,"timestamp_ms":1234567890000,"cancelled":false,"player":{"uuid":"...","name":"Steve"},"data":{"from":{"world":"world","x":1,"y":64,"z":2,"yaw":0,"pitch":0},"to":{"world":"world","x":2,"y":64,"z":2,"yaw":0,"pitch":0}}}
```

- `protocol_version`、`type`、`event`、`name`、`server`、`asynchronous`、`timestamp_ms` 和 `data` 总会生成。
- `cancelled` 仅对实现 `Cancellable` 的事件生成；`player` 只有实际关联到玩家时生成；字符串 `data.message` 还会复制到顶层 `message`。
- `type` 是 Python 订阅名。聊天、加入、退出仍使用 `chat`、`join`、`quit`；其他事件使用简单类名。也可用完整类名或 `*` 订阅。
- `data` 字段来自公开、无参数、返回受支持类型的 `get...()`/`is...()` 方法。getter 返回 `null` 或抛错时字段缺失。每条最多 24 个字段、4096 字节；字符串最多 512 字符，超限时删减末尾字段。
- 世界、位置、方块、实体和物品是**摘要对象**，不是完整 Bukkit 对象。Python 不能同步取消或修改已经转发的事件。

| 摘要类型 | JSON 属性 |
| --- | --- |
| `world` | `name`, `uuid` |
| `location` | `world`（可选）, `x`, `y`, `z`, `yaw`, `pitch` |
| `block` | `world`, `x`, `y`, `z`, `type` |
| `entity` | `uuid`, `type`, `name`（玩家时） |
| `item` | `type`, `amount` |

## 分类索引

| 分类 | 事件数 |
| --- | ---: |
| [方块 (`block`)](#category-block) | 45 |
| [命令 (`command`)](#category-command) | 1 |
| [附魔 (`enchantment`)](#category-enchantment) | 2 |
| [实体 (`entity`)](#category-entity) | 107 |
| [悬挂实体 (`hanging`)](#category-hanging) | 3 |
| [物品栏 (`inventory`)](#category-inventory) | 21 |
| [网络包 (`packet`)](#category-packet) | 2 |
| [玩家 (`player`)](#category-player) | 95 |
| [玩家资料 (`profile`)](#category-profile) | 5 |
| [袭击 (`raid`)](#category-raid) | 4 |
| [服务端 (`server`)](#category-server) | 19 |
| [载具 (`vehicle`)](#category-vehicle) | 9 |
| [天气 (`weather`)](#category-weather) | 3 |
| [世界 (`world`)](#category-world) | 17 |

<a id="category-block"></a>
## 方块 / block

| 事件 | Python `type` | `data` 候选字段数 | 可取消 |
| --- | --- | ---: | --- |
| [AnvilDamagedEvent](#event-com-destroystokyo-paper-event-block-anvildamagedevent) | `AnvilDamagedEvent` | 2 | 是 |
| [BeaconActivatedEvent](#event-io-papermc-paper-event-block-beaconactivatedevent) | `BeaconActivatedEvent` | 1 | 否 |
| [BeaconDeactivatedEvent](#event-io-papermc-paper-event-block-beacondeactivatedevent) | `BeaconDeactivatedEvent` | 1 | 否 |
| [BeaconEffectEvent](#event-com-destroystokyo-paper-event-block-beaconeffectevent) | `BeaconEffectEvent` | 2 | 是 |
| [BellRevealRaiderEvent](#event-io-papermc-paper-event-block-bellrevealraiderevent) | `BellRevealRaiderEvent` | 2 | 是 |
| [BellRingEvent](#event-io-papermc-paper-event-block-bellringevent) | `BellRingEvent` | 2 | 是 |
| [BlockBreakEvent](#event-org-bukkit-event-block-blockbreakevent) | `BlockBreakEvent` | 3 | 是 |
| [BlockBurnEvent](#event-org-bukkit-event-block-blockburnevent) | `BlockBurnEvent` | 2 | 是 |
| [BlockCanBuildEvent](#event-org-bukkit-event-block-blockcanbuildevent) | `BlockCanBuildEvent` | 3 | 否 |
| [BlockCookEvent](#event-org-bukkit-event-block-blockcookevent) | `BlockCookEvent` | 3 | 是 |
| [BlockDamageEvent](#event-org-bukkit-event-block-blockdamageevent) | `BlockDamageEvent` | 3 | 是 |
| [BlockDestroyEvent](#event-com-destroystokyo-paper-event-block-blockdestroyevent) | `BlockDestroyEvent` | 1 | 是 |
| [BlockDispenseArmorEvent](#event-org-bukkit-event-block-blockdispensearmorevent) | `BlockDispenseArmorEvent` | 3 | 是 |
| [BlockDispenseEvent](#event-org-bukkit-event-block-blockdispenseevent) | `BlockDispenseEvent` | 2 | 是 |
| [BlockDropItemEvent](#event-org-bukkit-event-block-blockdropitemevent) | `BlockDropItemEvent` | 1 | 是 |
| [BlockExpEvent](#event-org-bukkit-event-block-blockexpevent) | `BlockExpEvent` | 2 | 否 |
| [BlockExplodeEvent](#event-org-bukkit-event-block-blockexplodeevent) | `BlockExplodeEvent` | 2 | 是 |
| [BlockFadeEvent](#event-org-bukkit-event-block-blockfadeevent) | `BlockFadeEvent` | 1 | 是 |
| [BlockFailedDispenseEvent](#event-io-papermc-paper-event-block-blockfaileddispenseevent) | `BlockFailedDispenseEvent` | 1 | 否 |
| [BlockFertilizeEvent](#event-org-bukkit-event-block-blockfertilizeevent) | `BlockFertilizeEvent` | 1 | 是 |
| [BlockFormEvent](#event-org-bukkit-event-block-blockformevent) | `BlockFormEvent` | 1 | 是 |
| [BlockFromToEvent](#event-org-bukkit-event-block-blockfromtoevent) | `BlockFromToEvent` | 3 | 是 |
| [BlockGrowEvent](#event-org-bukkit-event-block-blockgrowevent) | `BlockGrowEvent` | 1 | 是 |
| [BlockIgniteEvent](#event-org-bukkit-event-block-blockigniteevent) | `BlockIgniteEvent` | 4 | 是 |
| [BlockMultiPlaceEvent](#event-org-bukkit-event-block-blockmultiplaceevent) | `BlockMultiPlaceEvent` | 5 | 是 |
| [BlockPhysicsEvent](#event-org-bukkit-event-block-blockphysicsevent) | `BlockPhysicsEvent` | 3 | 是 |
| [BlockPistonExtendEvent](#event-org-bukkit-event-block-blockpistonextendevent) | `BlockPistonExtendEvent` | 4 | 是 |
| [BlockPistonRetractEvent](#event-org-bukkit-event-block-blockpistonretractevent) | `BlockPistonRetractEvent` | 4 | 是 |
| [BlockPlaceEvent](#event-org-bukkit-event-block-blockplaceevent) | `BlockPlaceEvent` | 5 | 是 |
| [BlockPreDispenseEvent](#event-io-papermc-paper-event-block-blockpredispenseevent) | `BlockPreDispenseEvent` | 3 | 是 |
| [BlockRedstoneEvent](#event-org-bukkit-event-block-blockredstoneevent) | `BlockRedstoneEvent` | 3 | 否 |
| [BlockShearEntityEvent](#event-org-bukkit-event-block-blockshearentityevent) | `BlockShearEntityEvent` | 3 | 是 |
| [BlockSpreadEvent](#event-org-bukkit-event-block-blockspreadevent) | `BlockSpreadEvent` | 2 | 是 |
| [CauldronLevelChangeEvent](#event-org-bukkit-event-block-cauldronlevelchangeevent) | `CauldronLevelChangeEvent` | 5 | 是 |
| [DragonEggFormEvent](#event-io-papermc-paper-event-block-dragoneggformevent) | `DragonEggFormEvent` | 1 | 是 |
| [EntityBlockFormEvent](#event-org-bukkit-event-block-entityblockformevent) | `EntityBlockFormEvent` | 2 | 是 |
| [FluidLevelChangeEvent](#event-org-bukkit-event-block-fluidlevelchangeevent) | `FluidLevelChangeEvent` | 1 | 是 |
| [LeavesDecayEvent](#event-org-bukkit-event-block-leavesdecayevent) | `LeavesDecayEvent` | 1 | 是 |
| [MoistureChangeEvent](#event-org-bukkit-event-block-moisturechangeevent) | `MoistureChangeEvent` | 1 | 是 |
| [NotePlayEvent](#event-org-bukkit-event-block-noteplayevent) | `NotePlayEvent` | 2 | 是 |
| [PlayerShearBlockEvent](#event-io-papermc-paper-event-block-playershearblockevent) | `PlayerShearBlockEvent` | 3 | 是 |
| [SignChangeEvent](#event-org-bukkit-event-block-signchangeevent) | `SignChangeEvent` | 1 | 是 |
| [SpongeAbsorbEvent](#event-org-bukkit-event-block-spongeabsorbevent) | `SpongeAbsorbEvent` | 1 | 是 |
| [TargetHitEvent](#event-io-papermc-paper-event-block-targethitevent) | `TargetHitEvent` | 6 | 是 |
| [TNTPrimeEvent](#event-com-destroystokyo-paper-event-block-tntprimeevent) | `TNTPrimeEvent` | 3 | 是 |

<a id="event-com-destroystokyo-paper-event-block-anvildamagedevent"></a>
### AnvilDamagedEvent

- Java 类：`com.destroystokyo.paper.event.block.AnvilDamagedEvent`；父类：`org.bukkit.event.inventory.InventoryEvent`。
- Python 订阅：`@bridge.on("AnvilDamagedEvent")`；也可使用 `Events.ANVIL_DAMAGED`。
- 可取消：是；关联玩家：无已知玩家 getter。
- [Paper 官方 Javadoc](https://jd.papermc.io/paper/1.16.5/com/destroystokyo/paper/event/block/AnvilDamagedEvent.html)：事件含义、触发条件和 Java API。

| `data` 字段 | JSON 类型 | Java getter | Java 返回类型 |
| --- | --- | --- | --- |
| `damageState` | 字符串 | `getDamageState()` | `com.destroystokyo.paper.event.block.AnvilDamagedEvent$DamageState` |
| `breaking` | 布尔值 | `isBreaking()` | `boolean` |

<a id="event-io-papermc-paper-event-block-beaconactivatedevent"></a>
### BeaconActivatedEvent

- Java 类：`io.papermc.paper.event.block.BeaconActivatedEvent`；父类：`org.bukkit.event.block.BlockEvent`。
- Python 订阅：`@bridge.on("BeaconActivatedEvent")`；也可使用 `Events.BEACON_ACTIVATED`。
- 可取消：否；关联玩家：无已知玩家 getter。
- [Paper 官方 Javadoc](https://jd.papermc.io/paper/1.16.5/io/papermc/paper/event/block/BeaconActivatedEvent.html)：事件含义、触发条件和 Java API。

| `data` 字段 | JSON 类型 | Java getter | Java 返回类型 |
| --- | --- | --- | --- |
| `block` | 方块摘要 | `getBlock()` | `org.bukkit.block.Block` |

<a id="event-io-papermc-paper-event-block-beacondeactivatedevent"></a>
### BeaconDeactivatedEvent

- Java 类：`io.papermc.paper.event.block.BeaconDeactivatedEvent`；父类：`org.bukkit.event.block.BlockEvent`。
- Python 订阅：`@bridge.on("BeaconDeactivatedEvent")`；也可使用 `Events.BEACON_DEACTIVATED`。
- 可取消：否；关联玩家：无已知玩家 getter。
- [Paper 官方 Javadoc](https://jd.papermc.io/paper/1.16.5/io/papermc/paper/event/block/BeaconDeactivatedEvent.html)：事件含义、触发条件和 Java API。

| `data` 字段 | JSON 类型 | Java getter | Java 返回类型 |
| --- | --- | --- | --- |
| `block` | 方块摘要 | `getBlock()` | `org.bukkit.block.Block` |

<a id="event-com-destroystokyo-paper-event-block-beaconeffectevent"></a>
### BeaconEffectEvent

- Java 类：`com.destroystokyo.paper.event.block.BeaconEffectEvent`；父类：`org.bukkit.event.block.BlockEvent`。
- Python 订阅：`@bridge.on("BeaconEffectEvent")`；也可使用 `Events.BEACON_EFFECT`。
- 可取消：是；关联玩家：可能有，取决于实际对象。
- [Paper 官方 Javadoc](https://jd.papermc.io/paper/1.16.5/com/destroystokyo/paper/event/block/BeaconEffectEvent.html)：事件含义、触发条件和 Java API。

| `data` 字段 | JSON 类型 | Java getter | Java 返回类型 |
| --- | --- | --- | --- |
| `block` | 方块摘要 | `getBlock()` | `org.bukkit.block.Block` |
| `primary` | 布尔值 | `isPrimary()` | `boolean` |

<a id="event-io-papermc-paper-event-block-bellrevealraiderevent"></a>
### BellRevealRaiderEvent

- Java 类：`io.papermc.paper.event.block.BellRevealRaiderEvent`；父类：`org.bukkit.event.block.BlockEvent`。
- Python 订阅：`@bridge.on("BellRevealRaiderEvent")`；也可使用 `Events.BELL_REVEAL_RAIDER`。
- 可取消：是；关联玩家：可能有，取决于实际对象。
- [Paper 官方 Javadoc](https://jd.papermc.io/paper/1.16.5/io/papermc/paper/event/block/BellRevealRaiderEvent.html)：事件含义、触发条件和 Java API。

| `data` 字段 | JSON 类型 | Java getter | Java 返回类型 |
| --- | --- | --- | --- |
| `block` | 方块摘要 | `getBlock()` | `org.bukkit.block.Block` |
| `entity` | 实体摘要 | `getEntity()` | `org.bukkit.entity.Raider` |

<a id="event-io-papermc-paper-event-block-bellringevent"></a>
### BellRingEvent

- Java 类：`io.papermc.paper.event.block.BellRingEvent`；父类：`org.bukkit.event.block.BlockEvent`。
- Python 订阅：`@bridge.on("BellRingEvent")`；也可使用 `Events.BELL_RING`。
- 可取消：是；关联玩家：可能有，取决于实际对象。
- [Paper 官方 Javadoc](https://jd.papermc.io/paper/1.16.5/io/papermc/paper/event/block/BellRingEvent.html)：事件含义、触发条件和 Java API。

| `data` 字段 | JSON 类型 | Java getter | Java 返回类型 |
| --- | --- | --- | --- |
| `block` | 方块摘要 | `getBlock()` | `org.bukkit.block.Block` |
| `entity` | 实体摘要 | `getEntity()` | `org.bukkit.entity.Entity` |

<a id="event-org-bukkit-event-block-blockbreakevent"></a>
### BlockBreakEvent

- Java 类：`org.bukkit.event.block.BlockBreakEvent`；父类：`org.bukkit.event.block.BlockExpEvent`。
- Python 订阅：`@bridge.on("BlockBreakEvent")`；也可使用 `Events.BLOCK_BREAK`。
- 可取消：是；关联玩家：可能有，取决于实际对象。
- [Paper 官方 Javadoc](https://jd.papermc.io/paper/1.16.5/org/bukkit/event/block/BlockBreakEvent.html)：事件含义、触发条件和 Java API。

| `data` 字段 | JSON 类型 | Java getter | Java 返回类型 |
| --- | --- | --- | --- |
| `block` | 方块摘要 | `getBlock()` | `org.bukkit.block.Block` |
| `expToDrop` | 数字 | `getExpToDrop()` | `int` |
| `dropItems` | 布尔值 | `isDropItems()` | `boolean` |

<a id="event-org-bukkit-event-block-blockburnevent"></a>
### BlockBurnEvent

- Java 类：`org.bukkit.event.block.BlockBurnEvent`；父类：`org.bukkit.event.block.BlockEvent`。
- Python 订阅：`@bridge.on("BlockBurnEvent")`；也可使用 `Events.BLOCK_BURN`。
- 可取消：是；关联玩家：无已知玩家 getter。
- [Paper 官方 Javadoc](https://jd.papermc.io/paper/1.16.5/org/bukkit/event/block/BlockBurnEvent.html)：事件含义、触发条件和 Java API。

| `data` 字段 | JSON 类型 | Java getter | Java 返回类型 |
| --- | --- | --- | --- |
| `block` | 方块摘要 | `getBlock()` | `org.bukkit.block.Block` |
| `ignitingBlock` | 方块摘要 | `getIgnitingBlock()` | `org.bukkit.block.Block` |

<a id="event-org-bukkit-event-block-blockcanbuildevent"></a>
### BlockCanBuildEvent

- Java 类：`org.bukkit.event.block.BlockCanBuildEvent`；父类：`org.bukkit.event.block.BlockEvent`。
- Python 订阅：`@bridge.on("BlockCanBuildEvent")`；也可使用 `Events.BLOCK_CAN_BUILD`。
- 可取消：否；关联玩家：可能有，取决于实际对象。
- [Paper 官方 Javadoc](https://jd.papermc.io/paper/1.16.5/org/bukkit/event/block/BlockCanBuildEvent.html)：事件含义、触发条件和 Java API。

| `data` 字段 | JSON 类型 | Java getter | Java 返回类型 |
| --- | --- | --- | --- |
| `block` | 方块摘要 | `getBlock()` | `org.bukkit.block.Block` |
| `material` | 字符串 | `getMaterial()` | `org.bukkit.Material` |
| `buildable` | 布尔值 | `isBuildable()` | `boolean` |

<a id="event-org-bukkit-event-block-blockcookevent"></a>
### BlockCookEvent

- Java 类：`org.bukkit.event.block.BlockCookEvent`；父类：`org.bukkit.event.block.BlockEvent`。
- Python 订阅：`@bridge.on("BlockCookEvent")`；也可使用 `Events.BLOCK_COOK`。
- 可取消：是；关联玩家：无已知玩家 getter。
- [Paper 官方 Javadoc](https://jd.papermc.io/paper/1.16.5/org/bukkit/event/block/BlockCookEvent.html)：事件含义、触发条件和 Java API。

| `data` 字段 | JSON 类型 | Java getter | Java 返回类型 |
| --- | --- | --- | --- |
| `block` | 方块摘要 | `getBlock()` | `org.bukkit.block.Block` |
| `result` | 物品摘要 | `getResult()` | `org.bukkit.inventory.ItemStack` |
| `source` | 物品摘要 | `getSource()` | `org.bukkit.inventory.ItemStack` |

<a id="event-org-bukkit-event-block-blockdamageevent"></a>
### BlockDamageEvent

- Java 类：`org.bukkit.event.block.BlockDamageEvent`；父类：`org.bukkit.event.block.BlockEvent`。
- Python 订阅：`@bridge.on("BlockDamageEvent")`；也可使用 `Events.BLOCK_DAMAGE`。
- 可取消：是；关联玩家：可能有，取决于实际对象。
- [Paper 官方 Javadoc](https://jd.papermc.io/paper/1.16.5/org/bukkit/event/block/BlockDamageEvent.html)：事件含义、触发条件和 Java API。

| `data` 字段 | JSON 类型 | Java getter | Java 返回类型 |
| --- | --- | --- | --- |
| `block` | 方块摘要 | `getBlock()` | `org.bukkit.block.Block` |
| `instaBreak` | 布尔值 | `getInstaBreak()` | `boolean` |
| `itemInHand` | 物品摘要 | `getItemInHand()` | `org.bukkit.inventory.ItemStack` |

<a id="event-com-destroystokyo-paper-event-block-blockdestroyevent"></a>
### BlockDestroyEvent

- Java 类：`com.destroystokyo.paper.event.block.BlockDestroyEvent`；父类：`org.bukkit.event.block.BlockEvent`。
- Python 订阅：`@bridge.on("BlockDestroyEvent")`；也可使用 `Events.BLOCK_DESTROY`。
- 可取消：是；关联玩家：无已知玩家 getter。
- [Paper 官方 Javadoc](https://jd.papermc.io/paper/1.16.5/com/destroystokyo/paper/event/block/BlockDestroyEvent.html)：事件含义、触发条件和 Java API。

| `data` 字段 | JSON 类型 | Java getter | Java 返回类型 |
| --- | --- | --- | --- |
| `block` | 方块摘要 | `getBlock()` | `org.bukkit.block.Block` |

<a id="event-org-bukkit-event-block-blockdispensearmorevent"></a>
### BlockDispenseArmorEvent

- Java 类：`org.bukkit.event.block.BlockDispenseArmorEvent`；父类：`org.bukkit.event.block.BlockDispenseEvent`。
- Python 订阅：`@bridge.on("BlockDispenseArmorEvent")`；也可使用 `Events.BLOCK_DISPENSE_ARMOR`。
- 可取消：是；关联玩家：无已知玩家 getter。
- [Paper 官方 Javadoc](https://jd.papermc.io/paper/1.16.5/org/bukkit/event/block/BlockDispenseArmorEvent.html)：事件含义、触发条件和 Java API。

| `data` 字段 | JSON 类型 | Java getter | Java 返回类型 |
| --- | --- | --- | --- |
| `block` | 方块摘要 | `getBlock()` | `org.bukkit.block.Block` |
| `item` | 物品摘要 | `getItem()` | `org.bukkit.inventory.ItemStack` |
| `targetEntity` | 实体摘要 | `getTargetEntity()` | `org.bukkit.entity.LivingEntity` |

<a id="event-org-bukkit-event-block-blockdispenseevent"></a>
### BlockDispenseEvent

- Java 类：`org.bukkit.event.block.BlockDispenseEvent`；父类：`org.bukkit.event.block.BlockEvent`。
- Python 订阅：`@bridge.on("BlockDispenseEvent")`；也可使用 `Events.BLOCK_DISPENSE`。
- 可取消：是；关联玩家：无已知玩家 getter。
- [Paper 官方 Javadoc](https://jd.papermc.io/paper/1.16.5/org/bukkit/event/block/BlockDispenseEvent.html)：事件含义、触发条件和 Java API。

| `data` 字段 | JSON 类型 | Java getter | Java 返回类型 |
| --- | --- | --- | --- |
| `block` | 方块摘要 | `getBlock()` | `org.bukkit.block.Block` |
| `item` | 物品摘要 | `getItem()` | `org.bukkit.inventory.ItemStack` |

<a id="event-org-bukkit-event-block-blockdropitemevent"></a>
### BlockDropItemEvent

- Java 类：`org.bukkit.event.block.BlockDropItemEvent`；父类：`org.bukkit.event.block.BlockEvent`。
- Python 订阅：`@bridge.on("BlockDropItemEvent")`；也可使用 `Events.BLOCK_DROP_ITEM`。
- 可取消：是；关联玩家：可能有，取决于实际对象。
- [Paper 官方 Javadoc](https://jd.papermc.io/paper/1.16.5/org/bukkit/event/block/BlockDropItemEvent.html)：事件含义、触发条件和 Java API。

| `data` 字段 | JSON 类型 | Java getter | Java 返回类型 |
| --- | --- | --- | --- |
| `block` | 方块摘要 | `getBlock()` | `org.bukkit.block.Block` |

<a id="event-org-bukkit-event-block-blockexpevent"></a>
### BlockExpEvent

- Java 类：`org.bukkit.event.block.BlockExpEvent`；父类：`org.bukkit.event.block.BlockEvent`。
- Python 订阅：`@bridge.on("BlockExpEvent")`；也可使用 `Events.BLOCK_EXP`。
- 可取消：否；关联玩家：无已知玩家 getter。
- [Paper 官方 Javadoc](https://jd.papermc.io/paper/1.16.5/org/bukkit/event/block/BlockExpEvent.html)：事件含义、触发条件和 Java API。

| `data` 字段 | JSON 类型 | Java getter | Java 返回类型 |
| --- | --- | --- | --- |
| `block` | 方块摘要 | `getBlock()` | `org.bukkit.block.Block` |
| `expToDrop` | 数字 | `getExpToDrop()` | `int` |

<a id="event-org-bukkit-event-block-blockexplodeevent"></a>
### BlockExplodeEvent

- Java 类：`org.bukkit.event.block.BlockExplodeEvent`；父类：`org.bukkit.event.block.BlockEvent`。
- Python 订阅：`@bridge.on("BlockExplodeEvent")`；也可使用 `Events.BLOCK_EXPLODE`。
- 可取消：是；关联玩家：无已知玩家 getter。
- [Paper 官方 Javadoc](https://jd.papermc.io/paper/1.16.5/org/bukkit/event/block/BlockExplodeEvent.html)：事件含义、触发条件和 Java API。

| `data` 字段 | JSON 类型 | Java getter | Java 返回类型 |
| --- | --- | --- | --- |
| `block` | 方块摘要 | `getBlock()` | `org.bukkit.block.Block` |
| `yield` | 数字 | `getYield()` | `float` |

<a id="event-org-bukkit-event-block-blockfadeevent"></a>
### BlockFadeEvent

- Java 类：`org.bukkit.event.block.BlockFadeEvent`；父类：`org.bukkit.event.block.BlockEvent`。
- Python 订阅：`@bridge.on("BlockFadeEvent")`；也可使用 `Events.BLOCK_FADE`。
- 可取消：是；关联玩家：无已知玩家 getter。
- [Paper 官方 Javadoc](https://jd.papermc.io/paper/1.16.5/org/bukkit/event/block/BlockFadeEvent.html)：事件含义、触发条件和 Java API。

| `data` 字段 | JSON 类型 | Java getter | Java 返回类型 |
| --- | --- | --- | --- |
| `block` | 方块摘要 | `getBlock()` | `org.bukkit.block.Block` |

<a id="event-io-papermc-paper-event-block-blockfaileddispenseevent"></a>
### BlockFailedDispenseEvent

- Java 类：`io.papermc.paper.event.block.BlockFailedDispenseEvent`；父类：`org.bukkit.event.block.BlockEvent`。
- Python 订阅：`@bridge.on("BlockFailedDispenseEvent")`；也可使用 `Events.BLOCK_FAILED_DISPENSE`。
- 可取消：否；关联玩家：无已知玩家 getter。
- [Paper 官方 Javadoc](https://jd.papermc.io/paper/1.16.5/io/papermc/paper/event/block/BlockFailedDispenseEvent.html)：事件含义、触发条件和 Java API。

| `data` 字段 | JSON 类型 | Java getter | Java 返回类型 |
| --- | --- | --- | --- |
| `block` | 方块摘要 | `getBlock()` | `org.bukkit.block.Block` |

<a id="event-org-bukkit-event-block-blockfertilizeevent"></a>
### BlockFertilizeEvent

- Java 类：`org.bukkit.event.block.BlockFertilizeEvent`；父类：`org.bukkit.event.block.BlockEvent`。
- Python 订阅：`@bridge.on("BlockFertilizeEvent")`；也可使用 `Events.BLOCK_FERTILIZE`。
- 可取消：是；关联玩家：可能有，取决于实际对象。
- [Paper 官方 Javadoc](https://jd.papermc.io/paper/1.16.5/org/bukkit/event/block/BlockFertilizeEvent.html)：事件含义、触发条件和 Java API。

| `data` 字段 | JSON 类型 | Java getter | Java 返回类型 |
| --- | --- | --- | --- |
| `block` | 方块摘要 | `getBlock()` | `org.bukkit.block.Block` |

<a id="event-org-bukkit-event-block-blockformevent"></a>
### BlockFormEvent

- Java 类：`org.bukkit.event.block.BlockFormEvent`；父类：`org.bukkit.event.block.BlockGrowEvent`。
- Python 订阅：`@bridge.on("BlockFormEvent")`；也可使用 `Events.BLOCK_FORM`。
- 可取消：是；关联玩家：无已知玩家 getter。
- [Paper 官方 Javadoc](https://jd.papermc.io/paper/1.16.5/org/bukkit/event/block/BlockFormEvent.html)：事件含义、触发条件和 Java API。

| `data` 字段 | JSON 类型 | Java getter | Java 返回类型 |
| --- | --- | --- | --- |
| `block` | 方块摘要 | `getBlock()` | `org.bukkit.block.Block` |

<a id="event-org-bukkit-event-block-blockfromtoevent"></a>
### BlockFromToEvent

- Java 类：`org.bukkit.event.block.BlockFromToEvent`；父类：`org.bukkit.event.block.BlockEvent`。
- Python 订阅：`@bridge.on("BlockFromToEvent")`；也可使用 `Events.BLOCK_FROM_TO`。
- 可取消：是；关联玩家：无已知玩家 getter。
- [Paper 官方 Javadoc](https://jd.papermc.io/paper/1.16.5/org/bukkit/event/block/BlockFromToEvent.html)：事件含义、触发条件和 Java API。

| `data` 字段 | JSON 类型 | Java getter | Java 返回类型 |
| --- | --- | --- | --- |
| `block` | 方块摘要 | `getBlock()` | `org.bukkit.block.Block` |
| `face` | 字符串 | `getFace()` | `org.bukkit.block.BlockFace` |
| `toBlock` | 方块摘要 | `getToBlock()` | `org.bukkit.block.Block` |

<a id="event-org-bukkit-event-block-blockgrowevent"></a>
### BlockGrowEvent

- Java 类：`org.bukkit.event.block.BlockGrowEvent`；父类：`org.bukkit.event.block.BlockEvent`。
- Python 订阅：`@bridge.on("BlockGrowEvent")`；也可使用 `Events.BLOCK_GROW`。
- 可取消：是；关联玩家：无已知玩家 getter。
- [Paper 官方 Javadoc](https://jd.papermc.io/paper/1.16.5/org/bukkit/event/block/BlockGrowEvent.html)：事件含义、触发条件和 Java API。

| `data` 字段 | JSON 类型 | Java getter | Java 返回类型 |
| --- | --- | --- | --- |
| `block` | 方块摘要 | `getBlock()` | `org.bukkit.block.Block` |

<a id="event-org-bukkit-event-block-blockigniteevent"></a>
### BlockIgniteEvent

- Java 类：`org.bukkit.event.block.BlockIgniteEvent`；父类：`org.bukkit.event.block.BlockEvent`。
- Python 订阅：`@bridge.on("BlockIgniteEvent")`；也可使用 `Events.BLOCK_IGNITE`。
- 可取消：是；关联玩家：可能有，取决于实际对象。
- [Paper 官方 Javadoc](https://jd.papermc.io/paper/1.16.5/org/bukkit/event/block/BlockIgniteEvent.html)：事件含义、触发条件和 Java API。

| `data` 字段 | JSON 类型 | Java getter | Java 返回类型 |
| --- | --- | --- | --- |
| `block` | 方块摘要 | `getBlock()` | `org.bukkit.block.Block` |
| `cause` | 字符串 | `getCause()` | `org.bukkit.event.block.BlockIgniteEvent$IgniteCause` |
| `ignitingBlock` | 方块摘要 | `getIgnitingBlock()` | `org.bukkit.block.Block` |
| `ignitingEntity` | 实体摘要 | `getIgnitingEntity()` | `org.bukkit.entity.Entity` |

<a id="event-org-bukkit-event-block-blockmultiplaceevent"></a>
### BlockMultiPlaceEvent

- Java 类：`org.bukkit.event.block.BlockMultiPlaceEvent`；父类：`org.bukkit.event.block.BlockPlaceEvent`。
- Python 订阅：`@bridge.on("BlockMultiPlaceEvent")`；也可使用 `Events.BLOCK_MULTI_PLACE`。
- 可取消：是；关联玩家：可能有，取决于实际对象。
- [Paper 官方 Javadoc](https://jd.papermc.io/paper/1.16.5/org/bukkit/event/block/BlockMultiPlaceEvent.html)：事件含义、触发条件和 Java API。

| `data` 字段 | JSON 类型 | Java getter | Java 返回类型 |
| --- | --- | --- | --- |
| `block` | 方块摘要 | `getBlock()` | `org.bukkit.block.Block` |
| `blockAgainst` | 方块摘要 | `getBlockAgainst()` | `org.bukkit.block.Block` |
| `blockPlaced` | 方块摘要 | `getBlockPlaced()` | `org.bukkit.block.Block` |
| `hand` | 字符串 | `getHand()` | `org.bukkit.inventory.EquipmentSlot` |
| `itemInHand` | 物品摘要 | `getItemInHand()` | `org.bukkit.inventory.ItemStack` |

<a id="event-org-bukkit-event-block-blockphysicsevent"></a>
### BlockPhysicsEvent

- Java 类：`org.bukkit.event.block.BlockPhysicsEvent`；父类：`org.bukkit.event.block.BlockEvent`。
- Python 订阅：`@bridge.on("BlockPhysicsEvent")`；也可使用 `Events.BLOCK_PHYSICS`。
- 可取消：是；关联玩家：无已知玩家 getter。
- [Paper 官方 Javadoc](https://jd.papermc.io/paper/1.16.5/org/bukkit/event/block/BlockPhysicsEvent.html)：事件含义、触发条件和 Java API。

| `data` 字段 | JSON 类型 | Java getter | Java 返回类型 |
| --- | --- | --- | --- |
| `block` | 方块摘要 | `getBlock()` | `org.bukkit.block.Block` |
| `changedType` | 字符串 | `getChangedType()` | `org.bukkit.Material` |
| `sourceBlock` | 方块摘要 | `getSourceBlock()` | `org.bukkit.block.Block` |

<a id="event-org-bukkit-event-block-blockpistonextendevent"></a>
### BlockPistonExtendEvent

- Java 类：`org.bukkit.event.block.BlockPistonExtendEvent`；父类：`org.bukkit.event.block.BlockPistonEvent`。
- Python 订阅：`@bridge.on("BlockPistonExtendEvent")`；也可使用 `Events.BLOCK_PISTON_EXTEND`。
- 可取消：是；关联玩家：无已知玩家 getter。
- [Paper 官方 Javadoc](https://jd.papermc.io/paper/1.16.5/org/bukkit/event/block/BlockPistonExtendEvent.html)：事件含义、触发条件和 Java API。

| `data` 字段 | JSON 类型 | Java getter | Java 返回类型 |
| --- | --- | --- | --- |
| `block` | 方块摘要 | `getBlock()` | `org.bukkit.block.Block` |
| `direction` | 字符串 | `getDirection()` | `org.bukkit.block.BlockFace` |
| `length` | 数字 | `getLength()` | `int` |
| `sticky` | 布尔值 | `isSticky()` | `boolean` |

<a id="event-org-bukkit-event-block-blockpistonretractevent"></a>
### BlockPistonRetractEvent

- Java 类：`org.bukkit.event.block.BlockPistonRetractEvent`；父类：`org.bukkit.event.block.BlockPistonEvent`。
- Python 订阅：`@bridge.on("BlockPistonRetractEvent")`；也可使用 `Events.BLOCK_PISTON_RETRACT`。
- 可取消：是；关联玩家：无已知玩家 getter。
- [Paper 官方 Javadoc](https://jd.papermc.io/paper/1.16.5/org/bukkit/event/block/BlockPistonRetractEvent.html)：事件含义、触发条件和 Java API。

| `data` 字段 | JSON 类型 | Java getter | Java 返回类型 |
| --- | --- | --- | --- |
| `block` | 方块摘要 | `getBlock()` | `org.bukkit.block.Block` |
| `direction` | 字符串 | `getDirection()` | `org.bukkit.block.BlockFace` |
| `retractLocation` | 位置摘要 | `getRetractLocation()` | `org.bukkit.Location` |
| `sticky` | 布尔值 | `isSticky()` | `boolean` |

<a id="event-org-bukkit-event-block-blockplaceevent"></a>
### BlockPlaceEvent

- Java 类：`org.bukkit.event.block.BlockPlaceEvent`；父类：`org.bukkit.event.block.BlockEvent`。
- Python 订阅：`@bridge.on("BlockPlaceEvent")`；也可使用 `Events.BLOCK_PLACE`。
- 可取消：是；关联玩家：可能有，取决于实际对象。
- [Paper 官方 Javadoc](https://jd.papermc.io/paper/1.16.5/org/bukkit/event/block/BlockPlaceEvent.html)：事件含义、触发条件和 Java API。

| `data` 字段 | JSON 类型 | Java getter | Java 返回类型 |
| --- | --- | --- | --- |
| `block` | 方块摘要 | `getBlock()` | `org.bukkit.block.Block` |
| `blockAgainst` | 方块摘要 | `getBlockAgainst()` | `org.bukkit.block.Block` |
| `blockPlaced` | 方块摘要 | `getBlockPlaced()` | `org.bukkit.block.Block` |
| `hand` | 字符串 | `getHand()` | `org.bukkit.inventory.EquipmentSlot` |
| `itemInHand` | 物品摘要 | `getItemInHand()` | `org.bukkit.inventory.ItemStack` |

<a id="event-io-papermc-paper-event-block-blockpredispenseevent"></a>
### BlockPreDispenseEvent

- Java 类：`io.papermc.paper.event.block.BlockPreDispenseEvent`；父类：`org.bukkit.event.block.BlockEvent`。
- Python 订阅：`@bridge.on("BlockPreDispenseEvent")`；也可使用 `Events.BLOCK_PRE_DISPENSE`。
- 可取消：是；关联玩家：无已知玩家 getter。
- [Paper 官方 Javadoc](https://jd.papermc.io/paper/1.16.5/io/papermc/paper/event/block/BlockPreDispenseEvent.html)：事件含义、触发条件和 Java API。

| `data` 字段 | JSON 类型 | Java getter | Java 返回类型 |
| --- | --- | --- | --- |
| `block` | 方块摘要 | `getBlock()` | `org.bukkit.block.Block` |
| `itemStack` | 物品摘要 | `getItemStack()` | `org.bukkit.inventory.ItemStack` |
| `slot` | 数字 | `getSlot()` | `int` |

<a id="event-org-bukkit-event-block-blockredstoneevent"></a>
### BlockRedstoneEvent

- Java 类：`org.bukkit.event.block.BlockRedstoneEvent`；父类：`org.bukkit.event.block.BlockEvent`。
- Python 订阅：`@bridge.on("BlockRedstoneEvent")`；也可使用 `Events.BLOCK_REDSTONE`。
- 可取消：否；关联玩家：无已知玩家 getter。
- [Paper 官方 Javadoc](https://jd.papermc.io/paper/1.16.5/org/bukkit/event/block/BlockRedstoneEvent.html)：事件含义、触发条件和 Java API。

| `data` 字段 | JSON 类型 | Java getter | Java 返回类型 |
| --- | --- | --- | --- |
| `block` | 方块摘要 | `getBlock()` | `org.bukkit.block.Block` |
| `newCurrent` | 数字 | `getNewCurrent()` | `int` |
| `oldCurrent` | 数字 | `getOldCurrent()` | `int` |

<a id="event-org-bukkit-event-block-blockshearentityevent"></a>
### BlockShearEntityEvent

- Java 类：`org.bukkit.event.block.BlockShearEntityEvent`；父类：`org.bukkit.event.block.BlockEvent`。
- Python 订阅：`@bridge.on("BlockShearEntityEvent")`；也可使用 `Events.BLOCK_SHEAR_ENTITY`。
- 可取消：是；关联玩家：可能有，取决于实际对象。
- [Paper 官方 Javadoc](https://jd.papermc.io/paper/1.16.5/org/bukkit/event/block/BlockShearEntityEvent.html)：事件含义、触发条件和 Java API。

| `data` 字段 | JSON 类型 | Java getter | Java 返回类型 |
| --- | --- | --- | --- |
| `block` | 方块摘要 | `getBlock()` | `org.bukkit.block.Block` |
| `entity` | 实体摘要 | `getEntity()` | `org.bukkit.entity.Entity` |
| `tool` | 物品摘要 | `getTool()` | `org.bukkit.inventory.ItemStack` |

<a id="event-org-bukkit-event-block-blockspreadevent"></a>
### BlockSpreadEvent

- Java 类：`org.bukkit.event.block.BlockSpreadEvent`；父类：`org.bukkit.event.block.BlockFormEvent`。
- Python 订阅：`@bridge.on("BlockSpreadEvent")`；也可使用 `Events.BLOCK_SPREAD`。
- 可取消：是；关联玩家：无已知玩家 getter。
- [Paper 官方 Javadoc](https://jd.papermc.io/paper/1.16.5/org/bukkit/event/block/BlockSpreadEvent.html)：事件含义、触发条件和 Java API。

| `data` 字段 | JSON 类型 | Java getter | Java 返回类型 |
| --- | --- | --- | --- |
| `block` | 方块摘要 | `getBlock()` | `org.bukkit.block.Block` |
| `source` | 方块摘要 | `getSource()` | `org.bukkit.block.Block` |

<a id="event-org-bukkit-event-block-cauldronlevelchangeevent"></a>
### CauldronLevelChangeEvent

- Java 类：`org.bukkit.event.block.CauldronLevelChangeEvent`；父类：`org.bukkit.event.block.BlockEvent`。
- Python 订阅：`@bridge.on("CauldronLevelChangeEvent")`；也可使用 `Events.CAULDRON_LEVEL_CHANGE`。
- 可取消：是；关联玩家：可能有，取决于实际对象。
- [Paper 官方 Javadoc](https://jd.papermc.io/paper/1.16.5/org/bukkit/event/block/CauldronLevelChangeEvent.html)：事件含义、触发条件和 Java API。

| `data` 字段 | JSON 类型 | Java getter | Java 返回类型 |
| --- | --- | --- | --- |
| `block` | 方块摘要 | `getBlock()` | `org.bukkit.block.Block` |
| `entity` | 实体摘要 | `getEntity()` | `org.bukkit.entity.Entity` |
| `newLevel` | 数字 | `getNewLevel()` | `int` |
| `oldLevel` | 数字 | `getOldLevel()` | `int` |
| `reason` | 字符串 | `getReason()` | `org.bukkit.event.block.CauldronLevelChangeEvent$ChangeReason` |

<a id="event-io-papermc-paper-event-block-dragoneggformevent"></a>
### DragonEggFormEvent

- Java 类：`io.papermc.paper.event.block.DragonEggFormEvent`；父类：`org.bukkit.event.block.BlockFormEvent`。
- Python 订阅：`@bridge.on("DragonEggFormEvent")`；也可使用 `Events.DRAGON_EGG_FORM`。
- 可取消：是；关联玩家：无已知玩家 getter。
- [Paper 官方 Javadoc](https://jd.papermc.io/paper/1.16.5/io/papermc/paper/event/block/DragonEggFormEvent.html)：事件含义、触发条件和 Java API。

| `data` 字段 | JSON 类型 | Java getter | Java 返回类型 |
| --- | --- | --- | --- |
| `block` | 方块摘要 | `getBlock()` | `org.bukkit.block.Block` |

<a id="event-org-bukkit-event-block-entityblockformevent"></a>
### EntityBlockFormEvent

- Java 类：`org.bukkit.event.block.EntityBlockFormEvent`；父类：`org.bukkit.event.block.BlockFormEvent`。
- Python 订阅：`@bridge.on("EntityBlockFormEvent")`；也可使用 `Events.ENTITY_BLOCK_FORM`。
- 可取消：是；关联玩家：可能有，取决于实际对象。
- [Paper 官方 Javadoc](https://jd.papermc.io/paper/1.16.5/org/bukkit/event/block/EntityBlockFormEvent.html)：事件含义、触发条件和 Java API。

| `data` 字段 | JSON 类型 | Java getter | Java 返回类型 |
| --- | --- | --- | --- |
| `block` | 方块摘要 | `getBlock()` | `org.bukkit.block.Block` |
| `entity` | 实体摘要 | `getEntity()` | `org.bukkit.entity.Entity` |

<a id="event-org-bukkit-event-block-fluidlevelchangeevent"></a>
### FluidLevelChangeEvent

- Java 类：`org.bukkit.event.block.FluidLevelChangeEvent`；父类：`org.bukkit.event.block.BlockEvent`。
- Python 订阅：`@bridge.on("FluidLevelChangeEvent")`；也可使用 `Events.FLUID_LEVEL_CHANGE`。
- 可取消：是；关联玩家：无已知玩家 getter。
- [Paper 官方 Javadoc](https://jd.papermc.io/paper/1.16.5/org/bukkit/event/block/FluidLevelChangeEvent.html)：事件含义、触发条件和 Java API。

| `data` 字段 | JSON 类型 | Java getter | Java 返回类型 |
| --- | --- | --- | --- |
| `block` | 方块摘要 | `getBlock()` | `org.bukkit.block.Block` |

<a id="event-org-bukkit-event-block-leavesdecayevent"></a>
### LeavesDecayEvent

- Java 类：`org.bukkit.event.block.LeavesDecayEvent`；父类：`org.bukkit.event.block.BlockEvent`。
- Python 订阅：`@bridge.on("LeavesDecayEvent")`；也可使用 `Events.LEAVES_DECAY`。
- 可取消：是；关联玩家：无已知玩家 getter。
- [Paper 官方 Javadoc](https://jd.papermc.io/paper/1.16.5/org/bukkit/event/block/LeavesDecayEvent.html)：事件含义、触发条件和 Java API。

| `data` 字段 | JSON 类型 | Java getter | Java 返回类型 |
| --- | --- | --- | --- |
| `block` | 方块摘要 | `getBlock()` | `org.bukkit.block.Block` |

<a id="event-org-bukkit-event-block-moisturechangeevent"></a>
### MoistureChangeEvent

- Java 类：`org.bukkit.event.block.MoistureChangeEvent`；父类：`org.bukkit.event.block.BlockEvent`。
- Python 订阅：`@bridge.on("MoistureChangeEvent")`；也可使用 `Events.MOISTURE_CHANGE`。
- 可取消：是；关联玩家：无已知玩家 getter。
- [Paper 官方 Javadoc](https://jd.papermc.io/paper/1.16.5/org/bukkit/event/block/MoistureChangeEvent.html)：事件含义、触发条件和 Java API。

| `data` 字段 | JSON 类型 | Java getter | Java 返回类型 |
| --- | --- | --- | --- |
| `block` | 方块摘要 | `getBlock()` | `org.bukkit.block.Block` |

<a id="event-org-bukkit-event-block-noteplayevent"></a>
### NotePlayEvent

- Java 类：`org.bukkit.event.block.NotePlayEvent`；父类：`org.bukkit.event.block.BlockEvent`。
- Python 订阅：`@bridge.on("NotePlayEvent")`；也可使用 `Events.NOTE_PLAY`。
- 可取消：是；关联玩家：无已知玩家 getter。
- [Paper 官方 Javadoc](https://jd.papermc.io/paper/1.16.5/org/bukkit/event/block/NotePlayEvent.html)：事件含义、触发条件和 Java API。

| `data` 字段 | JSON 类型 | Java getter | Java 返回类型 |
| --- | --- | --- | --- |
| `block` | 方块摘要 | `getBlock()` | `org.bukkit.block.Block` |
| `instrument` | 字符串 | `getInstrument()` | `org.bukkit.Instrument` |

<a id="event-io-papermc-paper-event-block-playershearblockevent"></a>
### PlayerShearBlockEvent

- Java 类：`io.papermc.paper.event.block.PlayerShearBlockEvent`；父类：`org.bukkit.event.player.PlayerEvent`。
- Python 订阅：`@bridge.on("PlayerShearBlockEvent")`；也可使用 `Events.PLAYER_SHEAR_BLOCK`。
- 可取消：是；关联玩家：可能有，取决于实际对象。
- [Paper 官方 Javadoc](https://jd.papermc.io/paper/1.16.5/io/papermc/paper/event/block/PlayerShearBlockEvent.html)：事件含义、触发条件和 Java API。

| `data` 字段 | JSON 类型 | Java getter | Java 返回类型 |
| --- | --- | --- | --- |
| `block` | 方块摘要 | `getBlock()` | `org.bukkit.block.Block` |
| `hand` | 字符串 | `getHand()` | `org.bukkit.inventory.EquipmentSlot` |
| `item` | 物品摘要 | `getItem()` | `org.bukkit.inventory.ItemStack` |

<a id="event-org-bukkit-event-block-signchangeevent"></a>
### SignChangeEvent

- Java 类：`org.bukkit.event.block.SignChangeEvent`；父类：`org.bukkit.event.block.BlockEvent`。
- Python 订阅：`@bridge.on("SignChangeEvent")`；也可使用 `Events.SIGN_CHANGE`。
- 可取消：是；关联玩家：可能有，取决于实际对象。
- [Paper 官方 Javadoc](https://jd.papermc.io/paper/1.16.5/org/bukkit/event/block/SignChangeEvent.html)：事件含义、触发条件和 Java API。

| `data` 字段 | JSON 类型 | Java getter | Java 返回类型 |
| --- | --- | --- | --- |
| `block` | 方块摘要 | `getBlock()` | `org.bukkit.block.Block` |

<a id="event-org-bukkit-event-block-spongeabsorbevent"></a>
### SpongeAbsorbEvent

- Java 类：`org.bukkit.event.block.SpongeAbsorbEvent`；父类：`org.bukkit.event.block.BlockEvent`。
- Python 订阅：`@bridge.on("SpongeAbsorbEvent")`；也可使用 `Events.SPONGE_ABSORB`。
- 可取消：是；关联玩家：无已知玩家 getter。
- [Paper 官方 Javadoc](https://jd.papermc.io/paper/1.16.5/org/bukkit/event/block/SpongeAbsorbEvent.html)：事件含义、触发条件和 Java API。

| `data` 字段 | JSON 类型 | Java getter | Java 返回类型 |
| --- | --- | --- | --- |
| `block` | 方块摘要 | `getBlock()` | `org.bukkit.block.Block` |

<a id="event-io-papermc-paper-event-block-targethitevent"></a>
### TargetHitEvent

- Java 类：`io.papermc.paper.event.block.TargetHitEvent`；父类：`org.bukkit.event.entity.ProjectileHitEvent`。
- Python 订阅：`@bridge.on("TargetHitEvent")`；也可使用 `Events.TARGET_HIT`。
- 可取消：是；关联玩家：可能有，取决于实际对象。
- [Paper 官方 Javadoc](https://jd.papermc.io/paper/1.16.5/io/papermc/paper/event/block/TargetHitEvent.html)：事件含义、触发条件和 Java API。

| `data` 字段 | JSON 类型 | Java getter | Java 返回类型 |
| --- | --- | --- | --- |
| `entity` | 实体摘要 | `getEntity()` | `org.bukkit.entity.Projectile` |
| `entityType` | 字符串 | `getEntityType()` | `org.bukkit.entity.EntityType` |
| `hitBlock` | 方块摘要 | `getHitBlock()` | `org.bukkit.block.Block` |
| `hitBlockFace` | 字符串 | `getHitBlockFace()` | `org.bukkit.block.BlockFace` |
| `hitEntity` | 实体摘要 | `getHitEntity()` | `org.bukkit.entity.Entity` |
| `signalStrength` | 数字 | `getSignalStrength()` | `int` |

<a id="event-com-destroystokyo-paper-event-block-tntprimeevent"></a>
### TNTPrimeEvent

- Java 类：`com.destroystokyo.paper.event.block.TNTPrimeEvent`；父类：`org.bukkit.event.block.BlockEvent`。
- Python 订阅：`@bridge.on("TNTPrimeEvent")`；也可使用 `Events.TNT_PRIME`。
- 可取消：是；关联玩家：无已知玩家 getter。
- [Paper 官方 Javadoc](https://jd.papermc.io/paper/1.16.5/com/destroystokyo/paper/event/block/TNTPrimeEvent.html)：事件含义、触发条件和 Java API。

| `data` 字段 | JSON 类型 | Java getter | Java 返回类型 |
| --- | --- | --- | --- |
| `block` | 方块摘要 | `getBlock()` | `org.bukkit.block.Block` |
| `primerEntity` | 实体摘要 | `getPrimerEntity()` | `org.bukkit.entity.Entity` |
| `reason` | 字符串 | `getReason()` | `com.destroystokyo.paper.event.block.TNTPrimeEvent$PrimeReason` |

<a id="category-command"></a>
## 命令 / command

| 事件 | Python `type` | `data` 候选字段数 | 可取消 |
| --- | --- | ---: | --- |
| [UnknownCommandEvent](#event-org-bukkit-event-command-unknowncommandevent) | `UnknownCommandEvent` | 2 | 否 |

<a id="event-org-bukkit-event-command-unknowncommandevent"></a>
### UnknownCommandEvent

- Java 类：`org.bukkit.event.command.UnknownCommandEvent`；父类：`org.bukkit.event.Event`。
- Python 订阅：`@bridge.on("UnknownCommandEvent")`；也可使用 `Events.UNKNOWN_COMMAND`。
- 可取消：否；关联玩家：无已知玩家 getter。
- [Paper 官方 Javadoc](https://jd.papermc.io/paper/1.16.5/org/bukkit/event/command/UnknownCommandEvent.html)：事件含义、触发条件和 Java API。

| `data` 字段 | JSON 类型 | Java getter | Java 返回类型 |
| --- | --- | --- | --- |
| `commandLine` | 字符串 | `getCommandLine()` | `java.lang.String` |
| `message` | 字符串 | `getMessage()` | `java.lang.String` |

<a id="category-enchantment"></a>
## 附魔 / enchantment

| 事件 | Python `type` | `data` 候选字段数 | 可取消 |
| --- | --- | ---: | --- |
| [EnchantItemEvent](#event-org-bukkit-event-enchantment-enchantitemevent) | `EnchantItemEvent` | 4 | 是 |
| [PrepareItemEnchantEvent](#event-org-bukkit-event-enchantment-prepareitemenchantevent) | `PrepareItemEnchantEvent` | 4 | 是 |

<a id="event-org-bukkit-event-enchantment-enchantitemevent"></a>
### EnchantItemEvent

- Java 类：`org.bukkit.event.enchantment.EnchantItemEvent`；父类：`org.bukkit.event.inventory.InventoryEvent`。
- Python 订阅：`@bridge.on("EnchantItemEvent")`；也可使用 `Events.ENCHANT_ITEM`。
- 可取消：是；关联玩家：无已知玩家 getter。
- [Paper 官方 Javadoc](https://jd.papermc.io/paper/1.16.5/org/bukkit/event/enchantment/EnchantItemEvent.html)：事件含义、触发条件和 Java API。

| `data` 字段 | JSON 类型 | Java getter | Java 返回类型 |
| --- | --- | --- | --- |
| `enchantBlock` | 方块摘要 | `getEnchantBlock()` | `org.bukkit.block.Block` |
| `enchanter` | 实体摘要 | `getEnchanter()` | `org.bukkit.entity.Player` |
| `expLevelCost` | 数字 | `getExpLevelCost()` | `int` |
| `item` | 物品摘要 | `getItem()` | `org.bukkit.inventory.ItemStack` |

<a id="event-org-bukkit-event-enchantment-prepareitemenchantevent"></a>
### PrepareItemEnchantEvent

- Java 类：`org.bukkit.event.enchantment.PrepareItemEnchantEvent`；父类：`org.bukkit.event.inventory.InventoryEvent`。
- Python 订阅：`@bridge.on("PrepareItemEnchantEvent")`；也可使用 `Events.PREPARE_ITEM_ENCHANT`。
- 可取消：是；关联玩家：无已知玩家 getter。
- [Paper 官方 Javadoc](https://jd.papermc.io/paper/1.16.5/org/bukkit/event/enchantment/PrepareItemEnchantEvent.html)：事件含义、触发条件和 Java API。

| `data` 字段 | JSON 类型 | Java getter | Java 返回类型 |
| --- | --- | --- | --- |
| `enchantBlock` | 方块摘要 | `getEnchantBlock()` | `org.bukkit.block.Block` |
| `enchanter` | 实体摘要 | `getEnchanter()` | `org.bukkit.entity.Player` |
| `enchantmentBonus` | 数字 | `getEnchantmentBonus()` | `int` |
| `item` | 物品摘要 | `getItem()` | `org.bukkit.inventory.ItemStack` |

<a id="category-entity"></a>
## 实体 / entity

| 事件 | Python `type` | `data` 候选字段数 | 可取消 |
| --- | --- | ---: | --- |
| [AreaEffectCloudApplyEvent](#event-org-bukkit-event-entity-areaeffectcloudapplyevent) | `AreaEffectCloudApplyEvent` | 2 | 是 |
| [ArrowBodyCountChangeEvent](#event-org-bukkit-event-entity-arrowbodycountchangeevent) | `ArrowBodyCountChangeEvent` | 5 | 是 |
| [BatToggleSleepEvent](#event-org-bukkit-event-entity-battogglesleepevent) | `BatToggleSleepEvent` | 3 | 是 |
| [CreatureSpawnEvent](#event-org-bukkit-event-entity-creaturespawnevent) | `CreatureSpawnEvent` | 4 | 是 |
| [CreeperIgniteEvent](#event-com-destroystokyo-paper-event-entity-creeperigniteevent) | `CreeperIgniteEvent` | 3 | 是 |
| [CreeperPowerEvent](#event-org-bukkit-event-entity-creeperpowerevent) | `CreeperPowerEvent` | 4 | 是 |
| [ElderGuardianAppearanceEvent](#event-io-papermc-paper-event-entity-elderguardianappearanceevent) | `ElderGuardianAppearanceEvent` | 3 | 是 |
| [EnderDragonChangePhaseEvent](#event-org-bukkit-event-entity-enderdragonchangephaseevent) | `EnderDragonChangePhaseEvent` | 4 | 是 |
| [EnderDragonFireballHitEvent](#event-com-destroystokyo-paper-event-entity-enderdragonfireballhitevent) | `EnderDragonFireballHitEvent` | 3 | 是 |
| [EnderDragonFlameEvent](#event-com-destroystokyo-paper-event-entity-enderdragonflameevent) | `EnderDragonFlameEvent` | 3 | 是 |
| [EnderDragonShootFireballEvent](#event-com-destroystokyo-paper-event-entity-enderdragonshootfireballevent) | `EnderDragonShootFireballEvent` | 3 | 是 |
| [EndermanAttackPlayerEvent](#event-com-destroystokyo-paper-event-entity-endermanattackplayerevent) | `EndermanAttackPlayerEvent` | 2 | 是 |
| [EndermanEscapeEvent](#event-com-destroystokyo-paper-event-entity-endermanescapeevent) | `EndermanEscapeEvent` | 3 | 是 |
| [EntityAddToWorldEvent](#event-com-destroystokyo-paper-event-entity-entityaddtoworldevent) | `EntityAddToWorldEvent` | 2 | 否 |
| [EntityAirChangeEvent](#event-org-bukkit-event-entity-entityairchangeevent) | `EntityAirChangeEvent` | 3 | 是 |
| [EntityBreakDoorEvent](#event-org-bukkit-event-entity-entitybreakdoorevent) | `EntityBreakDoorEvent` | 4 | 是 |
| [EntityBreedEvent](#event-org-bukkit-event-entity-entitybreedevent) | `EntityBreedEvent` | 7 | 是 |
| [EntityChangeBlockEvent](#event-org-bukkit-event-entity-entitychangeblockevent) | `EntityChangeBlockEvent` | 4 | 是 |
| [EntityCombustByBlockEvent](#event-org-bukkit-event-entity-entitycombustbyblockevent) | `EntityCombustByBlockEvent` | 4 | 是 |
| [EntityCombustByEntityEvent](#event-org-bukkit-event-entity-entitycombustbyentityevent) | `EntityCombustByEntityEvent` | 4 | 是 |
| [EntityCombustEvent](#event-org-bukkit-event-entity-entitycombustevent) | `EntityCombustEvent` | 3 | 是 |
| [EntityCreatePortalEvent](#event-org-bukkit-event-entity-entitycreateportalevent) | `EntityCreatePortalEvent` | 3 | 是 |
| [EntityDamageByBlockEvent](#event-org-bukkit-event-entity-entitydamagebyblockevent) | `EntityDamageByBlockEvent` | 6 | 是 |
| [EntityDamageByEntityEvent](#event-org-bukkit-event-entity-entitydamagebyentityevent) | `EntityDamageByEntityEvent` | 6 | 是 |
| [EntityDamageEvent](#event-org-bukkit-event-entity-entitydamageevent) | `EntityDamageEvent` | 5 | 是 |
| [EntityDeathEvent](#event-org-bukkit-event-entity-entitydeathevent) | `EntityDeathEvent` | 8 | 是 |
| [EntityDropItemEvent](#event-org-bukkit-event-entity-entitydropitemevent) | `EntityDropItemEvent` | 3 | 是 |
| [EntityEnterBlockEvent](#event-org-bukkit-event-entity-entityenterblockevent) | `EntityEnterBlockEvent` | 3 | 是 |
| [EntityEnterLoveModeEvent](#event-org-bukkit-event-entity-entityenterlovemodeevent) | `EntityEnterLoveModeEvent` | 4 | 是 |
| [EntityExhaustionEvent](#event-org-bukkit-event-entity-entityexhaustionevent) | `EntityExhaustionEvent` | 4 | 是 |
| [EntityExplodeEvent](#event-org-bukkit-event-entity-entityexplodeevent) | `EntityExplodeEvent` | 4 | 是 |
| [EntityInsideBlockEvent](#event-io-papermc-paper-event-entity-entityinsideblockevent) | `EntityInsideBlockEvent` | 3 | 是 |
| [EntityInteractEvent](#event-org-bukkit-event-entity-entityinteractevent) | `EntityInteractEvent` | 3 | 是 |
| [EntityJumpEvent](#event-com-destroystokyo-paper-event-entity-entityjumpevent) | `EntityJumpEvent` | 2 | 是 |
| [EntityKnockbackByEntityEvent](#event-com-destroystokyo-paper-event-entity-entityknockbackbyentityevent) | `EntityKnockbackByEntityEvent` | 4 | 是 |
| [EntityLoadCrossbowEvent](#event-io-papermc-paper-event-entity-entityloadcrossbowevent) | `EntityLoadCrossbowEvent` | 4 | 是 |
| [EntityMoveEvent](#event-io-papermc-paper-event-entity-entitymoveevent) | `EntityMoveEvent` | 4 | 是 |
| [EntityPathfindEvent](#event-com-destroystokyo-paper-event-entity-entitypathfindevent) | `EntityPathfindEvent` | 4 | 是 |
| [EntityPickupItemEvent](#event-org-bukkit-event-entity-entitypickupitemevent) | `EntityPickupItemEvent` | 4 | 是 |
| [EntityPlaceEvent](#event-org-bukkit-event-entity-entityplaceevent) | `EntityPlaceEvent` | 4 | 是 |
| [EntityPortalEnterEvent](#event-org-bukkit-event-entity-entityportalenterevent) | `EntityPortalEnterEvent` | 3 | 否 |
| [EntityPortalEvent](#event-org-bukkit-event-entity-entityportalevent) | `EntityPortalEvent` | 5 | 是 |
| [EntityPortalExitEvent](#event-org-bukkit-event-entity-entityportalexitevent) | `EntityPortalExitEvent` | 4 | 是 |
| [EntityPoseChangeEvent](#event-org-bukkit-event-entity-entityposechangeevent) | `EntityPoseChangeEvent` | 3 | 否 |
| [EntityPotionEffectEvent](#event-org-bukkit-event-entity-entitypotioneffectevent) | `EntityPotionEffectEvent` | 5 | 是 |
| [EntityRegainHealthEvent](#event-org-bukkit-event-entity-entityregainhealthevent) | `EntityRegainHealthEvent` | 5 | 是 |
| [EntityRemoveFromWorldEvent](#event-com-destroystokyo-paper-event-entity-entityremovefromworldevent) | `EntityRemoveFromWorldEvent` | 2 | 否 |
| [EntityResurrectEvent](#event-org-bukkit-event-entity-entityresurrectevent) | `EntityResurrectEvent` | 2 | 是 |
| [EntityShootBowEvent](#event-org-bukkit-event-entity-entityshootbowevent) | `EntityShootBowEvent` | 9 | 是 |
| [EntitySpawnEvent](#event-org-bukkit-event-entity-entityspawnevent) | `EntitySpawnEvent` | 3 | 是 |
| [EntitySpellCastEvent](#event-org-bukkit-event-entity-entityspellcastevent) | `EntitySpellCastEvent` | 3 | 是 |
| [EntityTameEvent](#event-org-bukkit-event-entity-entitytameevent) | `EntityTameEvent` | 2 | 是 |
| [EntityTargetEvent](#event-org-bukkit-event-entity-entitytargetevent) | `EntityTargetEvent` | 4 | 是 |
| [EntityTargetLivingEntityEvent](#event-org-bukkit-event-entity-entitytargetlivingentityevent) | `EntityTargetLivingEntityEvent` | 4 | 是 |
| [EntityTeleportEndGatewayEvent](#event-com-destroystokyo-paper-event-entity-entityteleportendgatewayevent) | `EntityTeleportEndGatewayEvent` | 4 | 是 |
| [EntityTeleportEvent](#event-org-bukkit-event-entity-entityteleportevent) | `EntityTeleportEvent` | 4 | 是 |
| [EntityToggleGlideEvent](#event-org-bukkit-event-entity-entitytoggleglideevent) | `EntityToggleGlideEvent` | 3 | 是 |
| [EntityToggleSwimEvent](#event-org-bukkit-event-entity-entitytoggleswimevent) | `EntityToggleSwimEvent` | 3 | 是 |
| [EntityTransformedEvent](#event-com-destroystokyo-paper-event-entity-entitytransformedevent) | `EntityTransformedEvent` | 4 | 是 |
| [EntityTransformEvent](#event-org-bukkit-event-entity-entitytransformevent) | `EntityTransformEvent` | 4 | 是 |
| [EntityUnleashEvent](#event-org-bukkit-event-entity-entityunleashevent) | `EntityUnleashEvent` | 4 | 否 |
| [EntityZapEvent](#event-com-destroystokyo-paper-event-entity-entityzapevent) | `EntityZapEvent` | 6 | 是 |
| [ExpBottleEvent](#event-org-bukkit-event-entity-expbottleevent) | `ExpBottleEvent` | 7 | 是 |
| [ExperienceOrbMergeEvent](#event-com-destroystokyo-paper-event-entity-experienceorbmergeevent) | `ExperienceOrbMergeEvent` | 4 | 是 |
| [ExplosionPrimeEvent](#event-org-bukkit-event-entity-explosionprimeevent) | `ExplosionPrimeEvent` | 4 | 是 |
| [FireworkExplodeEvent](#event-org-bukkit-event-entity-fireworkexplodeevent) | `FireworkExplodeEvent` | 2 | 是 |
| [FoodLevelChangeEvent](#event-org-bukkit-event-entity-foodlevelchangeevent) | `FoodLevelChangeEvent` | 4 | 是 |
| [HorseJumpEvent](#event-org-bukkit-event-entity-horsejumpevent) | `HorseJumpEvent` | 3 | 是 |
| [ItemDespawnEvent](#event-org-bukkit-event-entity-itemdespawnevent) | `ItemDespawnEvent` | 3 | 是 |
| [ItemMergeEvent](#event-org-bukkit-event-entity-itemmergeevent) | `ItemMergeEvent` | 3 | 是 |
| [ItemSpawnEvent](#event-org-bukkit-event-entity-itemspawnevent) | `ItemSpawnEvent` | 3 | 是 |
| [LingeringPotionSplashEvent](#event-org-bukkit-event-entity-lingeringpotionsplashevent) | `LingeringPotionSplashEvent` | 6 | 是 |
| [PhantomPreSpawnEvent](#event-com-destroystokyo-paper-event-entity-phantomprespawnevent) | `PhantomPreSpawnEvent` | 4 | 是 |
| [PiglinBarterEvent](#event-org-bukkit-event-entity-piglinbarterevent) | `PiglinBarterEvent` | 3 | 是 |
| [PigZapEvent](#event-org-bukkit-event-entity-pigzapevent) | `PigZapEvent` | 8 | 是 |
| [PigZombieAngerEvent](#event-org-bukkit-event-entity-pigzombieangerevent) | `PigZombieAngerEvent` | 4 | 是 |
| [PlayerDeathEvent](#event-org-bukkit-event-entity-playerdeathevent) | `PlayerDeathEvent` | 14 | 是 |
| [PlayerLeashEntityEvent](#event-org-bukkit-event-entity-playerleashentityevent) | `PlayerLeashEntityEvent` | 2 | 是 |
| [PlayerNaturallySpawnCreaturesEvent](#event-com-destroystokyo-paper-event-entity-playernaturallyspawncreaturesevent) | `PlayerNaturallySpawnCreaturesEvent` | 1 | 是 |
| [PotionSplashEvent](#event-org-bukkit-event-entity-potionsplashevent) | `PotionSplashEvent` | 6 | 是 |
| [PreCreatureSpawnEvent](#event-com-destroystokyo-paper-event-entity-precreaturespawnevent) | `PreCreatureSpawnEvent` | 3 | 是 |
| [PreSpawnerSpawnEvent](#event-com-destroystokyo-paper-event-entity-prespawnerspawnevent) | `PreSpawnerSpawnEvent` | 4 | 是 |
| [ProjectileCollideEvent](#event-com-destroystokyo-paper-event-entity-projectilecollideevent) | `ProjectileCollideEvent` | 3 | 是 |
| [ProjectileHitEvent](#event-org-bukkit-event-entity-projectilehitevent) | `ProjectileHitEvent` | 5 | 是 |
| [ProjectileLaunchEvent](#event-org-bukkit-event-entity-projectilelaunchevent) | `ProjectileLaunchEvent` | 3 | 是 |
| [PufferFishStateChangeEvent](#event-io-papermc-paper-event-entity-pufferfishstatechangeevent) | `PufferFishStateChangeEvent` | 5 | 是 |
| [SheepDyeWoolEvent](#event-org-bukkit-event-entity-sheepdyewoolevent) | `SheepDyeWoolEvent` | 3 | 是 |
| [SheepRegrowWoolEvent](#event-org-bukkit-event-entity-sheepregrowwoolevent) | `SheepRegrowWoolEvent` | 2 | 是 |
| [SkeletonHorseTrapEvent](#event-com-destroystokyo-paper-event-entity-skeletonhorsetrapevent) | `SkeletonHorseTrapEvent` | 2 | 是 |
| [SlimeChangeDirectionEvent](#event-com-destroystokyo-paper-event-entity-slimechangedirectionevent) | `SlimeChangeDirectionEvent` | 3 | 是 |
| [SlimePathfindEvent](#event-com-destroystokyo-paper-event-entity-slimepathfindevent) | `SlimePathfindEvent` | 2 | 是 |
| [SlimeSplitEvent](#event-org-bukkit-event-entity-slimesplitevent) | `SlimeSplitEvent` | 3 | 是 |
| [SlimeSwimEvent](#event-com-destroystokyo-paper-event-entity-slimeswimevent) | `SlimeSwimEvent` | 2 | 是 |
| [SlimeTargetLivingEntityEvent](#event-com-destroystokyo-paper-event-entity-slimetargetlivingentityevent) | `SlimeTargetLivingEntityEvent` | 3 | 是 |
| [SlimeWanderEvent](#event-com-destroystokyo-paper-event-entity-slimewanderevent) | `SlimeWanderEvent` | 2 | 是 |
| [SpawnerSpawnEvent](#event-org-bukkit-event-entity-spawnerspawnevent) | `SpawnerSpawnEvent` | 3 | 是 |
| [StriderTemperatureChangeEvent](#event-org-bukkit-event-entity-stridertemperaturechangeevent) | `StriderTemperatureChangeEvent` | 3 | 否 |
| [ThrownEggHatchEvent](#event-com-destroystokyo-paper-event-entity-thrownegghatchevent) | `ThrownEggHatchEvent` | 4 | 否 |
| [TurtleGoHomeEvent](#event-com-destroystokyo-paper-event-entity-turtlegohomeevent) | `TurtleGoHomeEvent` | 2 | 是 |
| [TurtleLayEggEvent](#event-com-destroystokyo-paper-event-entity-turtlelayeggevent) | `TurtleLayEggEvent` | 4 | 是 |
| [TurtleStartDiggingEvent](#event-com-destroystokyo-paper-event-entity-turtlestartdiggingevent) | `TurtleStartDiggingEvent` | 3 | 是 |
| [VillagerAcquireTradeEvent](#event-org-bukkit-event-entity-villageracquiretradeevent) | `VillagerAcquireTradeEvent` | 2 | 是 |
| [VillagerCareerChangeEvent](#event-org-bukkit-event-entity-villagercareerchangeevent) | `VillagerCareerChangeEvent` | 4 | 是 |
| [VillagerReplenishTradeEvent](#event-org-bukkit-event-entity-villagerreplenishtradeevent) | `VillagerReplenishTradeEvent` | 3 | 是 |
| [WitchConsumePotionEvent](#event-com-destroystokyo-paper-event-entity-witchconsumepotionevent) | `WitchConsumePotionEvent` | 3 | 是 |
| [WitchReadyPotionEvent](#event-com-destroystokyo-paper-event-entity-witchreadypotionevent) | `WitchReadyPotionEvent` | 3 | 是 |
| [WitchThrowPotionEvent](#event-com-destroystokyo-paper-event-entity-witchthrowpotionevent) | `WitchThrowPotionEvent` | 4 | 是 |

<a id="event-org-bukkit-event-entity-areaeffectcloudapplyevent"></a>
### AreaEffectCloudApplyEvent

- Java 类：`org.bukkit.event.entity.AreaEffectCloudApplyEvent`；父类：`org.bukkit.event.entity.EntityEvent`。
- Python 订阅：`@bridge.on("AreaEffectCloudApplyEvent")`；也可使用 `Events.AREA_EFFECT_CLOUD_APPLY`。
- 可取消：是；关联玩家：可能有，取决于实际对象。
- [Paper 官方 Javadoc](https://jd.papermc.io/paper/1.16.5/org/bukkit/event/entity/AreaEffectCloudApplyEvent.html)：事件含义、触发条件和 Java API。

| `data` 字段 | JSON 类型 | Java getter | Java 返回类型 |
| --- | --- | --- | --- |
| `entity` | 实体摘要 | `getEntity()` | `org.bukkit.entity.AreaEffectCloud` |
| `entityType` | 字符串 | `getEntityType()` | `org.bukkit.entity.EntityType` |

<a id="event-org-bukkit-event-entity-arrowbodycountchangeevent"></a>
### ArrowBodyCountChangeEvent

- Java 类：`org.bukkit.event.entity.ArrowBodyCountChangeEvent`；父类：`org.bukkit.event.entity.EntityEvent`。
- Python 订阅：`@bridge.on("ArrowBodyCountChangeEvent")`；也可使用 `Events.ARROW_BODY_COUNT_CHANGE`。
- 可取消：是；关联玩家：可能有，取决于实际对象。
- [Paper 官方 Javadoc](https://jd.papermc.io/paper/1.16.5/org/bukkit/event/entity/ArrowBodyCountChangeEvent.html)：事件含义、触发条件和 Java API。

| `data` 字段 | JSON 类型 | Java getter | Java 返回类型 |
| --- | --- | --- | --- |
| `entity` | 实体摘要 | `getEntity()` | `org.bukkit.entity.Entity` |
| `entityType` | 字符串 | `getEntityType()` | `org.bukkit.entity.EntityType` |
| `newAmount` | 数字 | `getNewAmount()` | `int` |
| `oldAmount` | 数字 | `getOldAmount()` | `int` |
| `reset` | 布尔值 | `isReset()` | `boolean` |

<a id="event-org-bukkit-event-entity-battogglesleepevent"></a>
### BatToggleSleepEvent

- Java 类：`org.bukkit.event.entity.BatToggleSleepEvent`；父类：`org.bukkit.event.entity.EntityEvent`。
- Python 订阅：`@bridge.on("BatToggleSleepEvent")`；也可使用 `Events.BAT_TOGGLE_SLEEP`。
- 可取消：是；关联玩家：可能有，取决于实际对象。
- [Paper 官方 Javadoc](https://jd.papermc.io/paper/1.16.5/org/bukkit/event/entity/BatToggleSleepEvent.html)：事件含义、触发条件和 Java API。

| `data` 字段 | JSON 类型 | Java getter | Java 返回类型 |
| --- | --- | --- | --- |
| `entity` | 实体摘要 | `getEntity()` | `org.bukkit.entity.Entity` |
| `entityType` | 字符串 | `getEntityType()` | `org.bukkit.entity.EntityType` |
| `awake` | 布尔值 | `isAwake()` | `boolean` |

<a id="event-org-bukkit-event-entity-creaturespawnevent"></a>
### CreatureSpawnEvent

- Java 类：`org.bukkit.event.entity.CreatureSpawnEvent`；父类：`org.bukkit.event.entity.EntitySpawnEvent`。
- Python 订阅：`@bridge.on("CreatureSpawnEvent")`；也可使用 `Events.CREATURE_SPAWN`。
- 可取消：是；关联玩家：可能有，取决于实际对象。
- [Paper 官方 Javadoc](https://jd.papermc.io/paper/1.16.5/org/bukkit/event/entity/CreatureSpawnEvent.html)：事件含义、触发条件和 Java API。

| `data` 字段 | JSON 类型 | Java getter | Java 返回类型 |
| --- | --- | --- | --- |
| `entity` | 实体摘要 | `getEntity()` | `org.bukkit.entity.LivingEntity` |
| `entityType` | 字符串 | `getEntityType()` | `org.bukkit.entity.EntityType` |
| `location` | 位置摘要 | `getLocation()` | `org.bukkit.Location` |
| `spawnReason` | 字符串 | `getSpawnReason()` | `org.bukkit.event.entity.CreatureSpawnEvent$SpawnReason` |

<a id="event-com-destroystokyo-paper-event-entity-creeperigniteevent"></a>
### CreeperIgniteEvent

- Java 类：`com.destroystokyo.paper.event.entity.CreeperIgniteEvent`；父类：`org.bukkit.event.entity.EntityEvent`。
- Python 订阅：`@bridge.on("CreeperIgniteEvent")`；也可使用 `Events.CREEPER_IGNITE`。
- 可取消：是；关联玩家：可能有，取决于实际对象。
- [Paper 官方 Javadoc](https://jd.papermc.io/paper/1.16.5/com/destroystokyo/paper/event/entity/CreeperIgniteEvent.html)：事件含义、触发条件和 Java API。

| `data` 字段 | JSON 类型 | Java getter | Java 返回类型 |
| --- | --- | --- | --- |
| `entity` | 实体摘要 | `getEntity()` | `org.bukkit.entity.Entity` |
| `entityType` | 字符串 | `getEntityType()` | `org.bukkit.entity.EntityType` |
| `ignited` | 布尔值 | `isIgnited()` | `boolean` |

<a id="event-org-bukkit-event-entity-creeperpowerevent"></a>
### CreeperPowerEvent

- Java 类：`org.bukkit.event.entity.CreeperPowerEvent`；父类：`org.bukkit.event.entity.EntityEvent`。
- Python 订阅：`@bridge.on("CreeperPowerEvent")`；也可使用 `Events.CREEPER_POWER`。
- 可取消：是；关联玩家：可能有，取决于实际对象。
- [Paper 官方 Javadoc](https://jd.papermc.io/paper/1.16.5/org/bukkit/event/entity/CreeperPowerEvent.html)：事件含义、触发条件和 Java API。

| `data` 字段 | JSON 类型 | Java getter | Java 返回类型 |
| --- | --- | --- | --- |
| `cause` | 字符串 | `getCause()` | `org.bukkit.event.entity.CreeperPowerEvent$PowerCause` |
| `entity` | 实体摘要 | `getEntity()` | `org.bukkit.entity.Entity` |
| `entityType` | 字符串 | `getEntityType()` | `org.bukkit.entity.EntityType` |
| `lightning` | 实体摘要 | `getLightning()` | `org.bukkit.entity.LightningStrike` |

<a id="event-io-papermc-paper-event-entity-elderguardianappearanceevent"></a>
### ElderGuardianAppearanceEvent

- Java 类：`io.papermc.paper.event.entity.ElderGuardianAppearanceEvent`；父类：`org.bukkit.event.entity.EntityEvent`。
- Python 订阅：`@bridge.on("ElderGuardianAppearanceEvent")`；也可使用 `Events.ELDER_GUARDIAN_APPEARANCE`。
- 可取消：是；关联玩家：可能有，取决于实际对象。
- [Paper 官方 Javadoc](https://jd.papermc.io/paper/1.16.5/io/papermc/paper/event/entity/ElderGuardianAppearanceEvent.html)：事件含义、触发条件和 Java API。

| `data` 字段 | JSON 类型 | Java getter | Java 返回类型 |
| --- | --- | --- | --- |
| `affectedPlayer` | 实体摘要 | `getAffectedPlayer()` | `org.bukkit.entity.Player` |
| `entity` | 实体摘要 | `getEntity()` | `org.bukkit.entity.ElderGuardian` |
| `entityType` | 字符串 | `getEntityType()` | `org.bukkit.entity.EntityType` |

<a id="event-org-bukkit-event-entity-enderdragonchangephaseevent"></a>
### EnderDragonChangePhaseEvent

- Java 类：`org.bukkit.event.entity.EnderDragonChangePhaseEvent`；父类：`org.bukkit.event.entity.EntityEvent`。
- Python 订阅：`@bridge.on("EnderDragonChangePhaseEvent")`；也可使用 `Events.ENDER_DRAGON_CHANGE_PHASE`。
- 可取消：是；关联玩家：可能有，取决于实际对象。
- [Paper 官方 Javadoc](https://jd.papermc.io/paper/1.16.5/org/bukkit/event/entity/EnderDragonChangePhaseEvent.html)：事件含义、触发条件和 Java API。

| `data` 字段 | JSON 类型 | Java getter | Java 返回类型 |
| --- | --- | --- | --- |
| `currentPhase` | 字符串 | `getCurrentPhase()` | `org.bukkit.entity.EnderDragon$Phase` |
| `entity` | 实体摘要 | `getEntity()` | `org.bukkit.entity.Entity` |
| `entityType` | 字符串 | `getEntityType()` | `org.bukkit.entity.EntityType` |
| `newPhase` | 字符串 | `getNewPhase()` | `org.bukkit.entity.EnderDragon$Phase` |

<a id="event-com-destroystokyo-paper-event-entity-enderdragonfireballhitevent"></a>
### EnderDragonFireballHitEvent

- Java 类：`com.destroystokyo.paper.event.entity.EnderDragonFireballHitEvent`；父类：`org.bukkit.event.entity.EntityEvent`。
- Python 订阅：`@bridge.on("EnderDragonFireballHitEvent")`；也可使用 `Events.ENDER_DRAGON_FIREBALL_HIT`。
- 可取消：是；关联玩家：可能有，取决于实际对象。
- [Paper 官方 Javadoc](https://jd.papermc.io/paper/1.16.5/com/destroystokyo/paper/event/entity/EnderDragonFireballHitEvent.html)：事件含义、触发条件和 Java API。

| `data` 字段 | JSON 类型 | Java getter | Java 返回类型 |
| --- | --- | --- | --- |
| `areaEffectCloud` | 实体摘要 | `getAreaEffectCloud()` | `org.bukkit.entity.AreaEffectCloud` |
| `entity` | 实体摘要 | `getEntity()` | `org.bukkit.entity.Entity` |
| `entityType` | 字符串 | `getEntityType()` | `org.bukkit.entity.EntityType` |

<a id="event-com-destroystokyo-paper-event-entity-enderdragonflameevent"></a>
### EnderDragonFlameEvent

- Java 类：`com.destroystokyo.paper.event.entity.EnderDragonFlameEvent`；父类：`org.bukkit.event.entity.EntityEvent`。
- Python 订阅：`@bridge.on("EnderDragonFlameEvent")`；也可使用 `Events.ENDER_DRAGON_FLAME`。
- 可取消：是；关联玩家：可能有，取决于实际对象。
- [Paper 官方 Javadoc](https://jd.papermc.io/paper/1.16.5/com/destroystokyo/paper/event/entity/EnderDragonFlameEvent.html)：事件含义、触发条件和 Java API。

| `data` 字段 | JSON 类型 | Java getter | Java 返回类型 |
| --- | --- | --- | --- |
| `areaEffectCloud` | 实体摘要 | `getAreaEffectCloud()` | `org.bukkit.entity.AreaEffectCloud` |
| `entity` | 实体摘要 | `getEntity()` | `org.bukkit.entity.EnderDragon` |
| `entityType` | 字符串 | `getEntityType()` | `org.bukkit.entity.EntityType` |

<a id="event-com-destroystokyo-paper-event-entity-enderdragonshootfireballevent"></a>
### EnderDragonShootFireballEvent

- Java 类：`com.destroystokyo.paper.event.entity.EnderDragonShootFireballEvent`；父类：`org.bukkit.event.entity.EntityEvent`。
- Python 订阅：`@bridge.on("EnderDragonShootFireballEvent")`；也可使用 `Events.ENDER_DRAGON_SHOOT_FIREBALL`。
- 可取消：是；关联玩家：可能有，取决于实际对象。
- [Paper 官方 Javadoc](https://jd.papermc.io/paper/1.16.5/com/destroystokyo/paper/event/entity/EnderDragonShootFireballEvent.html)：事件含义、触发条件和 Java API。

| `data` 字段 | JSON 类型 | Java getter | Java 返回类型 |
| --- | --- | --- | --- |
| `entity` | 实体摘要 | `getEntity()` | `org.bukkit.entity.EnderDragon` |
| `entityType` | 字符串 | `getEntityType()` | `org.bukkit.entity.EntityType` |
| `fireball` | 实体摘要 | `getFireball()` | `org.bukkit.entity.DragonFireball` |

<a id="event-com-destroystokyo-paper-event-entity-endermanattackplayerevent"></a>
### EndermanAttackPlayerEvent

- Java 类：`com.destroystokyo.paper.event.entity.EndermanAttackPlayerEvent`；父类：`org.bukkit.event.entity.EntityEvent`。
- Python 订阅：`@bridge.on("EndermanAttackPlayerEvent")`；也可使用 `Events.ENDERMAN_ATTACK_PLAYER`。
- 可取消：是；关联玩家：可能有，取决于实际对象。
- [Paper 官方 Javadoc](https://jd.papermc.io/paper/1.16.5/com/destroystokyo/paper/event/entity/EndermanAttackPlayerEvent.html)：事件含义、触发条件和 Java API。

| `data` 字段 | JSON 类型 | Java getter | Java 返回类型 |
| --- | --- | --- | --- |
| `entity` | 实体摘要 | `getEntity()` | `org.bukkit.entity.Enderman` |
| `entityType` | 字符串 | `getEntityType()` | `org.bukkit.entity.EntityType` |

<a id="event-com-destroystokyo-paper-event-entity-endermanescapeevent"></a>
### EndermanEscapeEvent

- Java 类：`com.destroystokyo.paper.event.entity.EndermanEscapeEvent`；父类：`org.bukkit.event.entity.EntityEvent`。
- Python 订阅：`@bridge.on("EndermanEscapeEvent")`；也可使用 `Events.ENDERMAN_ESCAPE`。
- 可取消：是；关联玩家：可能有，取决于实际对象。
- [Paper 官方 Javadoc](https://jd.papermc.io/paper/1.16.5/com/destroystokyo/paper/event/entity/EndermanEscapeEvent.html)：事件含义、触发条件和 Java API。

| `data` 字段 | JSON 类型 | Java getter | Java 返回类型 |
| --- | --- | --- | --- |
| `entity` | 实体摘要 | `getEntity()` | `org.bukkit.entity.Enderman` |
| `entityType` | 字符串 | `getEntityType()` | `org.bukkit.entity.EntityType` |
| `reason` | 字符串 | `getReason()` | `com.destroystokyo.paper.event.entity.EndermanEscapeEvent$Reason` |

<a id="event-com-destroystokyo-paper-event-entity-entityaddtoworldevent"></a>
### EntityAddToWorldEvent

- Java 类：`com.destroystokyo.paper.event.entity.EntityAddToWorldEvent`；父类：`org.bukkit.event.entity.EntityEvent`。
- Python 订阅：`@bridge.on("EntityAddToWorldEvent")`；也可使用 `Events.ENTITY_ADD_TO_WORLD`。
- 可取消：否；关联玩家：可能有，取决于实际对象。
- [Paper 官方 Javadoc](https://jd.papermc.io/paper/1.16.5/com/destroystokyo/paper/event/entity/EntityAddToWorldEvent.html)：事件含义、触发条件和 Java API。

| `data` 字段 | JSON 类型 | Java getter | Java 返回类型 |
| --- | --- | --- | --- |
| `entity` | 实体摘要 | `getEntity()` | `org.bukkit.entity.Entity` |
| `entityType` | 字符串 | `getEntityType()` | `org.bukkit.entity.EntityType` |

<a id="event-org-bukkit-event-entity-entityairchangeevent"></a>
### EntityAirChangeEvent

- Java 类：`org.bukkit.event.entity.EntityAirChangeEvent`；父类：`org.bukkit.event.entity.EntityEvent`。
- Python 订阅：`@bridge.on("EntityAirChangeEvent")`；也可使用 `Events.ENTITY_AIR_CHANGE`。
- 可取消：是；关联玩家：可能有，取决于实际对象。
- [Paper 官方 Javadoc](https://jd.papermc.io/paper/1.16.5/org/bukkit/event/entity/EntityAirChangeEvent.html)：事件含义、触发条件和 Java API。

| `data` 字段 | JSON 类型 | Java getter | Java 返回类型 |
| --- | --- | --- | --- |
| `amount` | 数字 | `getAmount()` | `int` |
| `entity` | 实体摘要 | `getEntity()` | `org.bukkit.entity.Entity` |
| `entityType` | 字符串 | `getEntityType()` | `org.bukkit.entity.EntityType` |

<a id="event-org-bukkit-event-entity-entitybreakdoorevent"></a>
### EntityBreakDoorEvent

- Java 类：`org.bukkit.event.entity.EntityBreakDoorEvent`；父类：`org.bukkit.event.entity.EntityChangeBlockEvent`。
- Python 订阅：`@bridge.on("EntityBreakDoorEvent")`；也可使用 `Events.ENTITY_BREAK_DOOR`。
- 可取消：是；关联玩家：可能有，取决于实际对象。
- [Paper 官方 Javadoc](https://jd.papermc.io/paper/1.16.5/org/bukkit/event/entity/EntityBreakDoorEvent.html)：事件含义、触发条件和 Java API。

| `data` 字段 | JSON 类型 | Java getter | Java 返回类型 |
| --- | --- | --- | --- |
| `block` | 方块摘要 | `getBlock()` | `org.bukkit.block.Block` |
| `entity` | 实体摘要 | `getEntity()` | `org.bukkit.entity.Entity` |
| `entityType` | 字符串 | `getEntityType()` | `org.bukkit.entity.EntityType` |
| `to` | 字符串 | `getTo()` | `org.bukkit.Material` |

<a id="event-org-bukkit-event-entity-entitybreedevent"></a>
### EntityBreedEvent

- Java 类：`org.bukkit.event.entity.EntityBreedEvent`；父类：`org.bukkit.event.entity.EntityEvent`。
- Python 订阅：`@bridge.on("EntityBreedEvent")`；也可使用 `Events.ENTITY_BREED`。
- 可取消：是；关联玩家：可能有，取决于实际对象。
- [Paper 官方 Javadoc](https://jd.papermc.io/paper/1.16.5/org/bukkit/event/entity/EntityBreedEvent.html)：事件含义、触发条件和 Java API。

| `data` 字段 | JSON 类型 | Java getter | Java 返回类型 |
| --- | --- | --- | --- |
| `bredWith` | 物品摘要 | `getBredWith()` | `org.bukkit.inventory.ItemStack` |
| `breeder` | 实体摘要 | `getBreeder()` | `org.bukkit.entity.LivingEntity` |
| `entity` | 实体摘要 | `getEntity()` | `org.bukkit.entity.LivingEntity` |
| `entityType` | 字符串 | `getEntityType()` | `org.bukkit.entity.EntityType` |
| `experience` | 数字 | `getExperience()` | `int` |
| `father` | 实体摘要 | `getFather()` | `org.bukkit.entity.LivingEntity` |
| `mother` | 实体摘要 | `getMother()` | `org.bukkit.entity.LivingEntity` |

<a id="event-org-bukkit-event-entity-entitychangeblockevent"></a>
### EntityChangeBlockEvent

- Java 类：`org.bukkit.event.entity.EntityChangeBlockEvent`；父类：`org.bukkit.event.entity.EntityEvent`。
- Python 订阅：`@bridge.on("EntityChangeBlockEvent")`；也可使用 `Events.ENTITY_CHANGE_BLOCK`。
- 可取消：是；关联玩家：可能有，取决于实际对象。
- [Paper 官方 Javadoc](https://jd.papermc.io/paper/1.16.5/org/bukkit/event/entity/EntityChangeBlockEvent.html)：事件含义、触发条件和 Java API。

| `data` 字段 | JSON 类型 | Java getter | Java 返回类型 |
| --- | --- | --- | --- |
| `block` | 方块摘要 | `getBlock()` | `org.bukkit.block.Block` |
| `entity` | 实体摘要 | `getEntity()` | `org.bukkit.entity.Entity` |
| `entityType` | 字符串 | `getEntityType()` | `org.bukkit.entity.EntityType` |
| `to` | 字符串 | `getTo()` | `org.bukkit.Material` |

<a id="event-org-bukkit-event-entity-entitycombustbyblockevent"></a>
### EntityCombustByBlockEvent

- Java 类：`org.bukkit.event.entity.EntityCombustByBlockEvent`；父类：`org.bukkit.event.entity.EntityCombustEvent`。
- Python 订阅：`@bridge.on("EntityCombustByBlockEvent")`；也可使用 `Events.ENTITY_COMBUST_BY_BLOCK`。
- 可取消：是；关联玩家：可能有，取决于实际对象。
- [Paper 官方 Javadoc](https://jd.papermc.io/paper/1.16.5/org/bukkit/event/entity/EntityCombustByBlockEvent.html)：事件含义、触发条件和 Java API。

| `data` 字段 | JSON 类型 | Java getter | Java 返回类型 |
| --- | --- | --- | --- |
| `combuster` | 方块摘要 | `getCombuster()` | `org.bukkit.block.Block` |
| `duration` | 数字 | `getDuration()` | `int` |
| `entity` | 实体摘要 | `getEntity()` | `org.bukkit.entity.Entity` |
| `entityType` | 字符串 | `getEntityType()` | `org.bukkit.entity.EntityType` |

<a id="event-org-bukkit-event-entity-entitycombustbyentityevent"></a>
### EntityCombustByEntityEvent

- Java 类：`org.bukkit.event.entity.EntityCombustByEntityEvent`；父类：`org.bukkit.event.entity.EntityCombustEvent`。
- Python 订阅：`@bridge.on("EntityCombustByEntityEvent")`；也可使用 `Events.ENTITY_COMBUST_BY_ENTITY`。
- 可取消：是；关联玩家：可能有，取决于实际对象。
- [Paper 官方 Javadoc](https://jd.papermc.io/paper/1.16.5/org/bukkit/event/entity/EntityCombustByEntityEvent.html)：事件含义、触发条件和 Java API。

| `data` 字段 | JSON 类型 | Java getter | Java 返回类型 |
| --- | --- | --- | --- |
| `combuster` | 实体摘要 | `getCombuster()` | `org.bukkit.entity.Entity` |
| `duration` | 数字 | `getDuration()` | `int` |
| `entity` | 实体摘要 | `getEntity()` | `org.bukkit.entity.Entity` |
| `entityType` | 字符串 | `getEntityType()` | `org.bukkit.entity.EntityType` |

<a id="event-org-bukkit-event-entity-entitycombustevent"></a>
### EntityCombustEvent

- Java 类：`org.bukkit.event.entity.EntityCombustEvent`；父类：`org.bukkit.event.entity.EntityEvent`。
- Python 订阅：`@bridge.on("EntityCombustEvent")`；也可使用 `Events.ENTITY_COMBUST`。
- 可取消：是；关联玩家：可能有，取决于实际对象。
- [Paper 官方 Javadoc](https://jd.papermc.io/paper/1.16.5/org/bukkit/event/entity/EntityCombustEvent.html)：事件含义、触发条件和 Java API。

| `data` 字段 | JSON 类型 | Java getter | Java 返回类型 |
| --- | --- | --- | --- |
| `duration` | 数字 | `getDuration()` | `int` |
| `entity` | 实体摘要 | `getEntity()` | `org.bukkit.entity.Entity` |
| `entityType` | 字符串 | `getEntityType()` | `org.bukkit.entity.EntityType` |

<a id="event-org-bukkit-event-entity-entitycreateportalevent"></a>
### EntityCreatePortalEvent

- Java 类：`org.bukkit.event.entity.EntityCreatePortalEvent`；父类：`org.bukkit.event.entity.EntityEvent`。
- Python 订阅：`@bridge.on("EntityCreatePortalEvent")`；也可使用 `Events.ENTITY_CREATE_PORTAL`。
- 可取消：是；关联玩家：可能有，取决于实际对象。
- [Paper 官方 Javadoc](https://jd.papermc.io/paper/1.16.5/org/bukkit/event/entity/EntityCreatePortalEvent.html)：事件含义、触发条件和 Java API。

| `data` 字段 | JSON 类型 | Java getter | Java 返回类型 |
| --- | --- | --- | --- |
| `entity` | 实体摘要 | `getEntity()` | `org.bukkit.entity.LivingEntity` |
| `entityType` | 字符串 | `getEntityType()` | `org.bukkit.entity.EntityType` |
| `portalType` | 字符串 | `getPortalType()` | `org.bukkit.PortalType` |

<a id="event-org-bukkit-event-entity-entitydamagebyblockevent"></a>
### EntityDamageByBlockEvent

- Java 类：`org.bukkit.event.entity.EntityDamageByBlockEvent`；父类：`org.bukkit.event.entity.EntityDamageEvent`。
- Python 订阅：`@bridge.on("EntityDamageByBlockEvent")`；也可使用 `Events.ENTITY_DAMAGE_BY_BLOCK`。
- 可取消：是；关联玩家：可能有，取决于实际对象。
- [Paper 官方 Javadoc](https://jd.papermc.io/paper/1.16.5/org/bukkit/event/entity/EntityDamageByBlockEvent.html)：事件含义、触发条件和 Java API。

| `data` 字段 | JSON 类型 | Java getter | Java 返回类型 |
| --- | --- | --- | --- |
| `cause` | 字符串 | `getCause()` | `org.bukkit.event.entity.EntityDamageEvent$DamageCause` |
| `damage` | 数字 | `getDamage()` | `double` |
| `damager` | 方块摘要 | `getDamager()` | `org.bukkit.block.Block` |
| `entity` | 实体摘要 | `getEntity()` | `org.bukkit.entity.Entity` |
| `entityType` | 字符串 | `getEntityType()` | `org.bukkit.entity.EntityType` |
| `finalDamage` | 数字 | `getFinalDamage()` | `double` |

<a id="event-org-bukkit-event-entity-entitydamagebyentityevent"></a>
### EntityDamageByEntityEvent

- Java 类：`org.bukkit.event.entity.EntityDamageByEntityEvent`；父类：`org.bukkit.event.entity.EntityDamageEvent`。
- Python 订阅：`@bridge.on("EntityDamageByEntityEvent")`；也可使用 `Events.ENTITY_DAMAGE_BY_ENTITY`。
- 可取消：是；关联玩家：可能有，取决于实际对象。
- [Paper 官方 Javadoc](https://jd.papermc.io/paper/1.16.5/org/bukkit/event/entity/EntityDamageByEntityEvent.html)：事件含义、触发条件和 Java API。

| `data` 字段 | JSON 类型 | Java getter | Java 返回类型 |
| --- | --- | --- | --- |
| `cause` | 字符串 | `getCause()` | `org.bukkit.event.entity.EntityDamageEvent$DamageCause` |
| `damage` | 数字 | `getDamage()` | `double` |
| `damager` | 实体摘要 | `getDamager()` | `org.bukkit.entity.Entity` |
| `entity` | 实体摘要 | `getEntity()` | `org.bukkit.entity.Entity` |
| `entityType` | 字符串 | `getEntityType()` | `org.bukkit.entity.EntityType` |
| `finalDamage` | 数字 | `getFinalDamage()` | `double` |

<a id="event-org-bukkit-event-entity-entitydamageevent"></a>
### EntityDamageEvent

- Java 类：`org.bukkit.event.entity.EntityDamageEvent`；父类：`org.bukkit.event.entity.EntityEvent`。
- Python 订阅：`@bridge.on("EntityDamageEvent")`；也可使用 `Events.ENTITY_DAMAGE`。
- 可取消：是；关联玩家：可能有，取决于实际对象。
- [Paper 官方 Javadoc](https://jd.papermc.io/paper/1.16.5/org/bukkit/event/entity/EntityDamageEvent.html)：事件含义、触发条件和 Java API。

| `data` 字段 | JSON 类型 | Java getter | Java 返回类型 |
| --- | --- | --- | --- |
| `cause` | 字符串 | `getCause()` | `org.bukkit.event.entity.EntityDamageEvent$DamageCause` |
| `damage` | 数字 | `getDamage()` | `double` |
| `entity` | 实体摘要 | `getEntity()` | `org.bukkit.entity.Entity` |
| `entityType` | 字符串 | `getEntityType()` | `org.bukkit.entity.EntityType` |
| `finalDamage` | 数字 | `getFinalDamage()` | `double` |

<a id="event-org-bukkit-event-entity-entitydeathevent"></a>
### EntityDeathEvent

- Java 类：`org.bukkit.event.entity.EntityDeathEvent`；父类：`org.bukkit.event.entity.EntityEvent`。
- Python 订阅：`@bridge.on("EntityDeathEvent")`；也可使用 `Events.ENTITY_DEATH`。
- 可取消：是；关联玩家：可能有，取决于实际对象。
- [Paper 官方 Javadoc](https://jd.papermc.io/paper/1.16.5/org/bukkit/event/entity/EntityDeathEvent.html)：事件含义、触发条件和 Java API。

| `data` 字段 | JSON 类型 | Java getter | Java 返回类型 |
| --- | --- | --- | --- |
| `deathSound` | 字符串 | `getDeathSound()` | `org.bukkit.Sound` |
| `deathSoundCategory` | 字符串 | `getDeathSoundCategory()` | `org.bukkit.SoundCategory` |
| `deathSoundPitch` | 数字 | `getDeathSoundPitch()` | `float` |
| `deathSoundVolume` | 数字 | `getDeathSoundVolume()` | `float` |
| `droppedExp` | 数字 | `getDroppedExp()` | `int` |
| `entity` | 实体摘要 | `getEntity()` | `org.bukkit.entity.LivingEntity` |
| `entityType` | 字符串 | `getEntityType()` | `org.bukkit.entity.EntityType` |
| `reviveHealth` | 数字 | `getReviveHealth()` | `double` |

<a id="event-org-bukkit-event-entity-entitydropitemevent"></a>
### EntityDropItemEvent

- Java 类：`org.bukkit.event.entity.EntityDropItemEvent`；父类：`org.bukkit.event.entity.EntityEvent`。
- Python 订阅：`@bridge.on("EntityDropItemEvent")`；也可使用 `Events.ENTITY_DROP_ITEM`。
- 可取消：是；关联玩家：可能有，取决于实际对象。
- [Paper 官方 Javadoc](https://jd.papermc.io/paper/1.16.5/org/bukkit/event/entity/EntityDropItemEvent.html)：事件含义、触发条件和 Java API。

| `data` 字段 | JSON 类型 | Java getter | Java 返回类型 |
| --- | --- | --- | --- |
| `entity` | 实体摘要 | `getEntity()` | `org.bukkit.entity.Entity` |
| `entityType` | 字符串 | `getEntityType()` | `org.bukkit.entity.EntityType` |
| `itemDrop` | 实体摘要 | `getItemDrop()` | `org.bukkit.entity.Item` |

<a id="event-org-bukkit-event-entity-entityenterblockevent"></a>
### EntityEnterBlockEvent

- Java 类：`org.bukkit.event.entity.EntityEnterBlockEvent`；父类：`org.bukkit.event.entity.EntityEvent`。
- Python 订阅：`@bridge.on("EntityEnterBlockEvent")`；也可使用 `Events.ENTITY_ENTER_BLOCK`。
- 可取消：是；关联玩家：可能有，取决于实际对象。
- [Paper 官方 Javadoc](https://jd.papermc.io/paper/1.16.5/org/bukkit/event/entity/EntityEnterBlockEvent.html)：事件含义、触发条件和 Java API。

| `data` 字段 | JSON 类型 | Java getter | Java 返回类型 |
| --- | --- | --- | --- |
| `block` | 方块摘要 | `getBlock()` | `org.bukkit.block.Block` |
| `entity` | 实体摘要 | `getEntity()` | `org.bukkit.entity.Entity` |
| `entityType` | 字符串 | `getEntityType()` | `org.bukkit.entity.EntityType` |

<a id="event-org-bukkit-event-entity-entityenterlovemodeevent"></a>
### EntityEnterLoveModeEvent

- Java 类：`org.bukkit.event.entity.EntityEnterLoveModeEvent`；父类：`org.bukkit.event.entity.EntityEvent`。
- Python 订阅：`@bridge.on("EntityEnterLoveModeEvent")`；也可使用 `Events.ENTITY_ENTER_LOVE_MODE`。
- 可取消：是；关联玩家：可能有，取决于实际对象。
- [Paper 官方 Javadoc](https://jd.papermc.io/paper/1.16.5/org/bukkit/event/entity/EntityEnterLoveModeEvent.html)：事件含义、触发条件和 Java API。

| `data` 字段 | JSON 类型 | Java getter | Java 返回类型 |
| --- | --- | --- | --- |
| `entity` | 实体摘要 | `getEntity()` | `org.bukkit.entity.Entity` |
| `entityType` | 字符串 | `getEntityType()` | `org.bukkit.entity.EntityType` |
| `humanEntity` | 实体摘要 | `getHumanEntity()` | `org.bukkit.entity.HumanEntity` |
| `ticksInLove` | 数字 | `getTicksInLove()` | `int` |

<a id="event-org-bukkit-event-entity-entityexhaustionevent"></a>
### EntityExhaustionEvent

- Java 类：`org.bukkit.event.entity.EntityExhaustionEvent`；父类：`org.bukkit.event.entity.EntityEvent`。
- Python 订阅：`@bridge.on("EntityExhaustionEvent")`；也可使用 `Events.ENTITY_EXHAUSTION`。
- 可取消：是；关联玩家：可能有，取决于实际对象。
- [Paper 官方 Javadoc](https://jd.papermc.io/paper/1.16.5/org/bukkit/event/entity/EntityExhaustionEvent.html)：事件含义、触发条件和 Java API。

| `data` 字段 | JSON 类型 | Java getter | Java 返回类型 |
| --- | --- | --- | --- |
| `entity` | 实体摘要 | `getEntity()` | `org.bukkit.entity.HumanEntity` |
| `entityType` | 字符串 | `getEntityType()` | `org.bukkit.entity.EntityType` |
| `exhaustion` | 数字 | `getExhaustion()` | `float` |
| `exhaustionReason` | 字符串 | `getExhaustionReason()` | `org.bukkit.event.entity.EntityExhaustionEvent$ExhaustionReason` |

<a id="event-org-bukkit-event-entity-entityexplodeevent"></a>
### EntityExplodeEvent

- Java 类：`org.bukkit.event.entity.EntityExplodeEvent`；父类：`org.bukkit.event.entity.EntityEvent`。
- Python 订阅：`@bridge.on("EntityExplodeEvent")`；也可使用 `Events.ENTITY_EXPLODE`。
- 可取消：是；关联玩家：可能有，取决于实际对象。
- [Paper 官方 Javadoc](https://jd.papermc.io/paper/1.16.5/org/bukkit/event/entity/EntityExplodeEvent.html)：事件含义、触发条件和 Java API。

| `data` 字段 | JSON 类型 | Java getter | Java 返回类型 |
| --- | --- | --- | --- |
| `entity` | 实体摘要 | `getEntity()` | `org.bukkit.entity.Entity` |
| `entityType` | 字符串 | `getEntityType()` | `org.bukkit.entity.EntityType` |
| `location` | 位置摘要 | `getLocation()` | `org.bukkit.Location` |
| `yield` | 数字 | `getYield()` | `float` |

<a id="event-io-papermc-paper-event-entity-entityinsideblockevent"></a>
### EntityInsideBlockEvent

- Java 类：`io.papermc.paper.event.entity.EntityInsideBlockEvent`；父类：`org.bukkit.event.entity.EntityEvent`。
- Python 订阅：`@bridge.on("EntityInsideBlockEvent")`；也可使用 `Events.ENTITY_INSIDE_BLOCK`。
- 可取消：是；关联玩家：可能有，取决于实际对象。
- [Paper 官方 Javadoc](https://jd.papermc.io/paper/1.16.5/io/papermc/paper/event/entity/EntityInsideBlockEvent.html)：事件含义、触发条件和 Java API。

| `data` 字段 | JSON 类型 | Java getter | Java 返回类型 |
| --- | --- | --- | --- |
| `block` | 方块摘要 | `getBlock()` | `org.bukkit.block.Block` |
| `entity` | 实体摘要 | `getEntity()` | `org.bukkit.entity.Entity` |
| `entityType` | 字符串 | `getEntityType()` | `org.bukkit.entity.EntityType` |

<a id="event-org-bukkit-event-entity-entityinteractevent"></a>
### EntityInteractEvent

- Java 类：`org.bukkit.event.entity.EntityInteractEvent`；父类：`org.bukkit.event.entity.EntityEvent`。
- Python 订阅：`@bridge.on("EntityInteractEvent")`；也可使用 `Events.ENTITY_INTERACT`。
- 可取消：是；关联玩家：可能有，取决于实际对象。
- [Paper 官方 Javadoc](https://jd.papermc.io/paper/1.16.5/org/bukkit/event/entity/EntityInteractEvent.html)：事件含义、触发条件和 Java API。

| `data` 字段 | JSON 类型 | Java getter | Java 返回类型 |
| --- | --- | --- | --- |
| `block` | 方块摘要 | `getBlock()` | `org.bukkit.block.Block` |
| `entity` | 实体摘要 | `getEntity()` | `org.bukkit.entity.Entity` |
| `entityType` | 字符串 | `getEntityType()` | `org.bukkit.entity.EntityType` |

<a id="event-com-destroystokyo-paper-event-entity-entityjumpevent"></a>
### EntityJumpEvent

- Java 类：`com.destroystokyo.paper.event.entity.EntityJumpEvent`；父类：`org.bukkit.event.entity.EntityEvent`。
- Python 订阅：`@bridge.on("EntityJumpEvent")`；也可使用 `Events.ENTITY_JUMP`。
- 可取消：是；关联玩家：可能有，取决于实际对象。
- [Paper 官方 Javadoc](https://jd.papermc.io/paper/1.16.5/com/destroystokyo/paper/event/entity/EntityJumpEvent.html)：事件含义、触发条件和 Java API。

| `data` 字段 | JSON 类型 | Java getter | Java 返回类型 |
| --- | --- | --- | --- |
| `entity` | 实体摘要 | `getEntity()` | `org.bukkit.entity.Entity` |
| `entityType` | 字符串 | `getEntityType()` | `org.bukkit.entity.EntityType` |

<a id="event-com-destroystokyo-paper-event-entity-entityknockbackbyentityevent"></a>
### EntityKnockbackByEntityEvent

- Java 类：`com.destroystokyo.paper.event.entity.EntityKnockbackByEntityEvent`；父类：`org.bukkit.event.entity.EntityEvent`。
- Python 订阅：`@bridge.on("EntityKnockbackByEntityEvent")`；也可使用 `Events.ENTITY_KNOCKBACK_BY_ENTITY`。
- 可取消：是；关联玩家：可能有，取决于实际对象。
- [Paper 官方 Javadoc](https://jd.papermc.io/paper/1.16.5/com/destroystokyo/paper/event/entity/EntityKnockbackByEntityEvent.html)：事件含义、触发条件和 Java API。

| `data` 字段 | JSON 类型 | Java getter | Java 返回类型 |
| --- | --- | --- | --- |
| `entity` | 实体摘要 | `getEntity()` | `org.bukkit.entity.Entity` |
| `entityType` | 字符串 | `getEntityType()` | `org.bukkit.entity.EntityType` |
| `hitBy` | 实体摘要 | `getHitBy()` | `org.bukkit.entity.Entity` |
| `knockbackStrength` | 数字 | `getKnockbackStrength()` | `float` |

<a id="event-io-papermc-paper-event-entity-entityloadcrossbowevent"></a>
### EntityLoadCrossbowEvent

- Java 类：`io.papermc.paper.event.entity.EntityLoadCrossbowEvent`；父类：`org.bukkit.event.entity.EntityEvent`。
- Python 订阅：`@bridge.on("EntityLoadCrossbowEvent")`；也可使用 `Events.ENTITY_LOAD_CROSSBOW`。
- 可取消：是；关联玩家：可能有，取决于实际对象。
- [Paper 官方 Javadoc](https://jd.papermc.io/paper/1.16.5/io/papermc/paper/event/entity/EntityLoadCrossbowEvent.html)：事件含义、触发条件和 Java API。

| `data` 字段 | JSON 类型 | Java getter | Java 返回类型 |
| --- | --- | --- | --- |
| `crossbow` | 物品摘要 | `getCrossbow()` | `org.bukkit.inventory.ItemStack` |
| `entity` | 实体摘要 | `getEntity()` | `org.bukkit.entity.Entity` |
| `entityType` | 字符串 | `getEntityType()` | `org.bukkit.entity.EntityType` |
| `hand` | 字符串 | `getHand()` | `org.bukkit.inventory.EquipmentSlot` |

<a id="event-io-papermc-paper-event-entity-entitymoveevent"></a>
### EntityMoveEvent

- Java 类：`io.papermc.paper.event.entity.EntityMoveEvent`；父类：`org.bukkit.event.entity.EntityEvent`。
- Python 订阅：`@bridge.on("EntityMoveEvent")`；也可使用 `Events.ENTITY_MOVE`。
- 可取消：是；关联玩家：可能有，取决于实际对象。
- [Paper 官方 Javadoc](https://jd.papermc.io/paper/1.16.5/io/papermc/paper/event/entity/EntityMoveEvent.html)：事件含义、触发条件和 Java API。

| `data` 字段 | JSON 类型 | Java getter | Java 返回类型 |
| --- | --- | --- | --- |
| `entity` | 实体摘要 | `getEntity()` | `org.bukkit.entity.LivingEntity` |
| `entityType` | 字符串 | `getEntityType()` | `org.bukkit.entity.EntityType` |
| `from` | 位置摘要 | `getFrom()` | `org.bukkit.Location` |
| `to` | 位置摘要 | `getTo()` | `org.bukkit.Location` |

<a id="event-com-destroystokyo-paper-event-entity-entitypathfindevent"></a>
### EntityPathfindEvent

- Java 类：`com.destroystokyo.paper.event.entity.EntityPathfindEvent`；父类：`org.bukkit.event.entity.EntityEvent`。
- Python 订阅：`@bridge.on("EntityPathfindEvent")`；也可使用 `Events.ENTITY_PATHFIND`。
- 可取消：是；关联玩家：可能有，取决于实际对象。
- [Paper 官方 Javadoc](https://jd.papermc.io/paper/1.16.5/com/destroystokyo/paper/event/entity/EntityPathfindEvent.html)：事件含义、触发条件和 Java API。

| `data` 字段 | JSON 类型 | Java getter | Java 返回类型 |
| --- | --- | --- | --- |
| `entity` | 实体摘要 | `getEntity()` | `org.bukkit.entity.Entity` |
| `entityType` | 字符串 | `getEntityType()` | `org.bukkit.entity.EntityType` |
| `loc` | 位置摘要 | `getLoc()` | `org.bukkit.Location` |
| `targetEntity` | 实体摘要 | `getTargetEntity()` | `org.bukkit.entity.Entity` |

<a id="event-org-bukkit-event-entity-entitypickupitemevent"></a>
### EntityPickupItemEvent

- Java 类：`org.bukkit.event.entity.EntityPickupItemEvent`；父类：`org.bukkit.event.entity.EntityEvent`。
- Python 订阅：`@bridge.on("EntityPickupItemEvent")`；也可使用 `Events.ENTITY_PICKUP_ITEM`。
- 可取消：是；关联玩家：可能有，取决于实际对象。
- [Paper 官方 Javadoc](https://jd.papermc.io/paper/1.16.5/org/bukkit/event/entity/EntityPickupItemEvent.html)：事件含义、触发条件和 Java API。

| `data` 字段 | JSON 类型 | Java getter | Java 返回类型 |
| --- | --- | --- | --- |
| `entity` | 实体摘要 | `getEntity()` | `org.bukkit.entity.LivingEntity` |
| `entityType` | 字符串 | `getEntityType()` | `org.bukkit.entity.EntityType` |
| `item` | 实体摘要 | `getItem()` | `org.bukkit.entity.Item` |
| `remaining` | 数字 | `getRemaining()` | `int` |

<a id="event-org-bukkit-event-entity-entityplaceevent"></a>
### EntityPlaceEvent

- Java 类：`org.bukkit.event.entity.EntityPlaceEvent`；父类：`org.bukkit.event.entity.EntityEvent`。
- Python 订阅：`@bridge.on("EntityPlaceEvent")`；也可使用 `Events.ENTITY_PLACE`。
- 可取消：是；关联玩家：可能有，取决于实际对象。
- [Paper 官方 Javadoc](https://jd.papermc.io/paper/1.16.5/org/bukkit/event/entity/EntityPlaceEvent.html)：事件含义、触发条件和 Java API。

| `data` 字段 | JSON 类型 | Java getter | Java 返回类型 |
| --- | --- | --- | --- |
| `block` | 方块摘要 | `getBlock()` | `org.bukkit.block.Block` |
| `blockFace` | 字符串 | `getBlockFace()` | `org.bukkit.block.BlockFace` |
| `entity` | 实体摘要 | `getEntity()` | `org.bukkit.entity.Entity` |
| `entityType` | 字符串 | `getEntityType()` | `org.bukkit.entity.EntityType` |

<a id="event-org-bukkit-event-entity-entityportalenterevent"></a>
### EntityPortalEnterEvent

- Java 类：`org.bukkit.event.entity.EntityPortalEnterEvent`；父类：`org.bukkit.event.entity.EntityEvent`。
- Python 订阅：`@bridge.on("EntityPortalEnterEvent")`；也可使用 `Events.ENTITY_PORTAL_ENTER`。
- 可取消：否；关联玩家：可能有，取决于实际对象。
- [Paper 官方 Javadoc](https://jd.papermc.io/paper/1.16.5/org/bukkit/event/entity/EntityPortalEnterEvent.html)：事件含义、触发条件和 Java API。

| `data` 字段 | JSON 类型 | Java getter | Java 返回类型 |
| --- | --- | --- | --- |
| `entity` | 实体摘要 | `getEntity()` | `org.bukkit.entity.Entity` |
| `entityType` | 字符串 | `getEntityType()` | `org.bukkit.entity.EntityType` |
| `location` | 位置摘要 | `getLocation()` | `org.bukkit.Location` |

<a id="event-org-bukkit-event-entity-entityportalevent"></a>
### EntityPortalEvent

- Java 类：`org.bukkit.event.entity.EntityPortalEvent`；父类：`org.bukkit.event.entity.EntityTeleportEvent`。
- Python 订阅：`@bridge.on("EntityPortalEvent")`；也可使用 `Events.ENTITY_PORTAL`。
- 可取消：是；关联玩家：可能有，取决于实际对象。
- [Paper 官方 Javadoc](https://jd.papermc.io/paper/1.16.5/org/bukkit/event/entity/EntityPortalEvent.html)：事件含义、触发条件和 Java API。

| `data` 字段 | JSON 类型 | Java getter | Java 返回类型 |
| --- | --- | --- | --- |
| `entity` | 实体摘要 | `getEntity()` | `org.bukkit.entity.Entity` |
| `entityType` | 字符串 | `getEntityType()` | `org.bukkit.entity.EntityType` |
| `from` | 位置摘要 | `getFrom()` | `org.bukkit.Location` |
| `searchRadius` | 数字 | `getSearchRadius()` | `int` |
| `to` | 位置摘要 | `getTo()` | `org.bukkit.Location` |

<a id="event-org-bukkit-event-entity-entityportalexitevent"></a>
### EntityPortalExitEvent

- Java 类：`org.bukkit.event.entity.EntityPortalExitEvent`；父类：`org.bukkit.event.entity.EntityTeleportEvent`。
- Python 订阅：`@bridge.on("EntityPortalExitEvent")`；也可使用 `Events.ENTITY_PORTAL_EXIT`。
- 可取消：是；关联玩家：可能有，取决于实际对象。
- [Paper 官方 Javadoc](https://jd.papermc.io/paper/1.16.5/org/bukkit/event/entity/EntityPortalExitEvent.html)：事件含义、触发条件和 Java API。

| `data` 字段 | JSON 类型 | Java getter | Java 返回类型 |
| --- | --- | --- | --- |
| `entity` | 实体摘要 | `getEntity()` | `org.bukkit.entity.Entity` |
| `entityType` | 字符串 | `getEntityType()` | `org.bukkit.entity.EntityType` |
| `from` | 位置摘要 | `getFrom()` | `org.bukkit.Location` |
| `to` | 位置摘要 | `getTo()` | `org.bukkit.Location` |

<a id="event-org-bukkit-event-entity-entityposechangeevent"></a>
### EntityPoseChangeEvent

- Java 类：`org.bukkit.event.entity.EntityPoseChangeEvent`；父类：`org.bukkit.event.entity.EntityEvent`。
- Python 订阅：`@bridge.on("EntityPoseChangeEvent")`；也可使用 `Events.ENTITY_POSE_CHANGE`。
- 可取消：否；关联玩家：可能有，取决于实际对象。
- [Paper 官方 Javadoc](https://jd.papermc.io/paper/1.16.5/org/bukkit/event/entity/EntityPoseChangeEvent.html)：事件含义、触发条件和 Java API。

| `data` 字段 | JSON 类型 | Java getter | Java 返回类型 |
| --- | --- | --- | --- |
| `entity` | 实体摘要 | `getEntity()` | `org.bukkit.entity.Entity` |
| `entityType` | 字符串 | `getEntityType()` | `org.bukkit.entity.EntityType` |
| `pose` | 字符串 | `getPose()` | `org.bukkit.entity.Pose` |

<a id="event-org-bukkit-event-entity-entitypotioneffectevent"></a>
### EntityPotionEffectEvent

- Java 类：`org.bukkit.event.entity.EntityPotionEffectEvent`；父类：`org.bukkit.event.entity.EntityEvent`。
- Python 订阅：`@bridge.on("EntityPotionEffectEvent")`；也可使用 `Events.ENTITY_POTION_EFFECT`。
- 可取消：是；关联玩家：可能有，取决于实际对象。
- [Paper 官方 Javadoc](https://jd.papermc.io/paper/1.16.5/org/bukkit/event/entity/EntityPotionEffectEvent.html)：事件含义、触发条件和 Java API。

| `data` 字段 | JSON 类型 | Java getter | Java 返回类型 |
| --- | --- | --- | --- |
| `action` | 字符串 | `getAction()` | `org.bukkit.event.entity.EntityPotionEffectEvent$Action` |
| `cause` | 字符串 | `getCause()` | `org.bukkit.event.entity.EntityPotionEffectEvent$Cause` |
| `entity` | 实体摘要 | `getEntity()` | `org.bukkit.entity.Entity` |
| `entityType` | 字符串 | `getEntityType()` | `org.bukkit.entity.EntityType` |
| `override` | 布尔值 | `isOverride()` | `boolean` |

<a id="event-org-bukkit-event-entity-entityregainhealthevent"></a>
### EntityRegainHealthEvent

- Java 类：`org.bukkit.event.entity.EntityRegainHealthEvent`；父类：`org.bukkit.event.entity.EntityEvent`。
- Python 订阅：`@bridge.on("EntityRegainHealthEvent")`；也可使用 `Events.ENTITY_REGAIN_HEALTH`。
- 可取消：是；关联玩家：可能有，取决于实际对象。
- [Paper 官方 Javadoc](https://jd.papermc.io/paper/1.16.5/org/bukkit/event/entity/EntityRegainHealthEvent.html)：事件含义、触发条件和 Java API。

| `data` 字段 | JSON 类型 | Java getter | Java 返回类型 |
| --- | --- | --- | --- |
| `amount` | 数字 | `getAmount()` | `double` |
| `entity` | 实体摘要 | `getEntity()` | `org.bukkit.entity.Entity` |
| `entityType` | 字符串 | `getEntityType()` | `org.bukkit.entity.EntityType` |
| `regainReason` | 字符串 | `getRegainReason()` | `org.bukkit.event.entity.EntityRegainHealthEvent$RegainReason` |
| `fastRegen` | 布尔值 | `isFastRegen()` | `boolean` |

<a id="event-com-destroystokyo-paper-event-entity-entityremovefromworldevent"></a>
### EntityRemoveFromWorldEvent

- Java 类：`com.destroystokyo.paper.event.entity.EntityRemoveFromWorldEvent`；父类：`org.bukkit.event.entity.EntityEvent`。
- Python 订阅：`@bridge.on("EntityRemoveFromWorldEvent")`；也可使用 `Events.ENTITY_REMOVE_FROM_WORLD`。
- 可取消：否；关联玩家：可能有，取决于实际对象。
- [Paper 官方 Javadoc](https://jd.papermc.io/paper/1.16.5/com/destroystokyo/paper/event/entity/EntityRemoveFromWorldEvent.html)：事件含义、触发条件和 Java API。

| `data` 字段 | JSON 类型 | Java getter | Java 返回类型 |
| --- | --- | --- | --- |
| `entity` | 实体摘要 | `getEntity()` | `org.bukkit.entity.Entity` |
| `entityType` | 字符串 | `getEntityType()` | `org.bukkit.entity.EntityType` |

<a id="event-org-bukkit-event-entity-entityresurrectevent"></a>
### EntityResurrectEvent

- Java 类：`org.bukkit.event.entity.EntityResurrectEvent`；父类：`org.bukkit.event.entity.EntityEvent`。
- Python 订阅：`@bridge.on("EntityResurrectEvent")`；也可使用 `Events.ENTITY_RESURRECT`。
- 可取消：是；关联玩家：可能有，取决于实际对象。
- [Paper 官方 Javadoc](https://jd.papermc.io/paper/1.16.5/org/bukkit/event/entity/EntityResurrectEvent.html)：事件含义、触发条件和 Java API。

| `data` 字段 | JSON 类型 | Java getter | Java 返回类型 |
| --- | --- | --- | --- |
| `entity` | 实体摘要 | `getEntity()` | `org.bukkit.entity.Entity` |
| `entityType` | 字符串 | `getEntityType()` | `org.bukkit.entity.EntityType` |

<a id="event-org-bukkit-event-entity-entityshootbowevent"></a>
### EntityShootBowEvent

- Java 类：`org.bukkit.event.entity.EntityShootBowEvent`；父类：`org.bukkit.event.entity.EntityEvent`。
- Python 订阅：`@bridge.on("EntityShootBowEvent")`；也可使用 `Events.ENTITY_SHOOT_BOW`。
- 可取消：是；关联玩家：可能有，取决于实际对象。
- [Paper 官方 Javadoc](https://jd.papermc.io/paper/1.16.5/org/bukkit/event/entity/EntityShootBowEvent.html)：事件含义、触发条件和 Java API。

| `data` 字段 | JSON 类型 | Java getter | Java 返回类型 |
| --- | --- | --- | --- |
| `arrowItem` | 物品摘要 | `getArrowItem()` | `org.bukkit.inventory.ItemStack` |
| `bow` | 物品摘要 | `getBow()` | `org.bukkit.inventory.ItemStack` |
| `consumable` | 物品摘要 | `getConsumable()` | `org.bukkit.inventory.ItemStack` |
| `consumeArrow` | 布尔值 | `getConsumeArrow()` | `boolean` |
| `entity` | 实体摘要 | `getEntity()` | `org.bukkit.entity.LivingEntity` |
| `entityType` | 字符串 | `getEntityType()` | `org.bukkit.entity.EntityType` |
| `force` | 数字 | `getForce()` | `float` |
| `hand` | 字符串 | `getHand()` | `org.bukkit.inventory.EquipmentSlot` |
| `projectile` | 实体摘要 | `getProjectile()` | `org.bukkit.entity.Entity` |

<a id="event-org-bukkit-event-entity-entityspawnevent"></a>
### EntitySpawnEvent

- Java 类：`org.bukkit.event.entity.EntitySpawnEvent`；父类：`org.bukkit.event.entity.EntityEvent`。
- Python 订阅：`@bridge.on("EntitySpawnEvent")`；也可使用 `Events.ENTITY_SPAWN`。
- 可取消：是；关联玩家：可能有，取决于实际对象。
- [Paper 官方 Javadoc](https://jd.papermc.io/paper/1.16.5/org/bukkit/event/entity/EntitySpawnEvent.html)：事件含义、触发条件和 Java API。

| `data` 字段 | JSON 类型 | Java getter | Java 返回类型 |
| --- | --- | --- | --- |
| `entity` | 实体摘要 | `getEntity()` | `org.bukkit.entity.Entity` |
| `entityType` | 字符串 | `getEntityType()` | `org.bukkit.entity.EntityType` |
| `location` | 位置摘要 | `getLocation()` | `org.bukkit.Location` |

<a id="event-org-bukkit-event-entity-entityspellcastevent"></a>
### EntitySpellCastEvent

- Java 类：`org.bukkit.event.entity.EntitySpellCastEvent`；父类：`org.bukkit.event.entity.EntityEvent`。
- Python 订阅：`@bridge.on("EntitySpellCastEvent")`；也可使用 `Events.ENTITY_SPELL_CAST`。
- 可取消：是；关联玩家：可能有，取决于实际对象。
- [Paper 官方 Javadoc](https://jd.papermc.io/paper/1.16.5/org/bukkit/event/entity/EntitySpellCastEvent.html)：事件含义、触发条件和 Java API。

| `data` 字段 | JSON 类型 | Java getter | Java 返回类型 |
| --- | --- | --- | --- |
| `entity` | 实体摘要 | `getEntity()` | `org.bukkit.entity.Spellcaster` |
| `entityType` | 字符串 | `getEntityType()` | `org.bukkit.entity.EntityType` |
| `spell` | 字符串 | `getSpell()` | `org.bukkit.entity.Spellcaster$Spell` |

<a id="event-org-bukkit-event-entity-entitytameevent"></a>
### EntityTameEvent

- Java 类：`org.bukkit.event.entity.EntityTameEvent`；父类：`org.bukkit.event.entity.EntityEvent`。
- Python 订阅：`@bridge.on("EntityTameEvent")`；也可使用 `Events.ENTITY_TAME`。
- 可取消：是；关联玩家：可能有，取决于实际对象。
- [Paper 官方 Javadoc](https://jd.papermc.io/paper/1.16.5/org/bukkit/event/entity/EntityTameEvent.html)：事件含义、触发条件和 Java API。

| `data` 字段 | JSON 类型 | Java getter | Java 返回类型 |
| --- | --- | --- | --- |
| `entity` | 实体摘要 | `getEntity()` | `org.bukkit.entity.LivingEntity` |
| `entityType` | 字符串 | `getEntityType()` | `org.bukkit.entity.EntityType` |

<a id="event-org-bukkit-event-entity-entitytargetevent"></a>
### EntityTargetEvent

- Java 类：`org.bukkit.event.entity.EntityTargetEvent`；父类：`org.bukkit.event.entity.EntityEvent`。
- Python 订阅：`@bridge.on("EntityTargetEvent")`；也可使用 `Events.ENTITY_TARGET`。
- 可取消：是；关联玩家：可能有，取决于实际对象。
- [Paper 官方 Javadoc](https://jd.papermc.io/paper/1.16.5/org/bukkit/event/entity/EntityTargetEvent.html)：事件含义、触发条件和 Java API。

| `data` 字段 | JSON 类型 | Java getter | Java 返回类型 |
| --- | --- | --- | --- |
| `entity` | 实体摘要 | `getEntity()` | `org.bukkit.entity.Entity` |
| `entityType` | 字符串 | `getEntityType()` | `org.bukkit.entity.EntityType` |
| `reason` | 字符串 | `getReason()` | `org.bukkit.event.entity.EntityTargetEvent$TargetReason` |
| `target` | 实体摘要 | `getTarget()` | `org.bukkit.entity.Entity` |

<a id="event-org-bukkit-event-entity-entitytargetlivingentityevent"></a>
### EntityTargetLivingEntityEvent

- Java 类：`org.bukkit.event.entity.EntityTargetLivingEntityEvent`；父类：`org.bukkit.event.entity.EntityTargetEvent`。
- Python 订阅：`@bridge.on("EntityTargetLivingEntityEvent")`；也可使用 `Events.ENTITY_TARGET_LIVING_ENTITY`。
- 可取消：是；关联玩家：可能有，取决于实际对象。
- [Paper 官方 Javadoc](https://jd.papermc.io/paper/1.16.5/org/bukkit/event/entity/EntityTargetLivingEntityEvent.html)：事件含义、触发条件和 Java API。

| `data` 字段 | JSON 类型 | Java getter | Java 返回类型 |
| --- | --- | --- | --- |
| `entity` | 实体摘要 | `getEntity()` | `org.bukkit.entity.Entity` |
| `entityType` | 字符串 | `getEntityType()` | `org.bukkit.entity.EntityType` |
| `reason` | 字符串 | `getReason()` | `org.bukkit.event.entity.EntityTargetEvent$TargetReason` |
| `target` | 实体摘要 | `getTarget()` | `org.bukkit.entity.LivingEntity` |

<a id="event-com-destroystokyo-paper-event-entity-entityteleportendgatewayevent"></a>
### EntityTeleportEndGatewayEvent

- Java 类：`com.destroystokyo.paper.event.entity.EntityTeleportEndGatewayEvent`；父类：`org.bukkit.event.entity.EntityTeleportEvent`。
- Python 订阅：`@bridge.on("EntityTeleportEndGatewayEvent")`；也可使用 `Events.ENTITY_TELEPORT_END_GATEWAY`。
- 可取消：是；关联玩家：可能有，取决于实际对象。
- [Paper 官方 Javadoc](https://jd.papermc.io/paper/1.16.5/com/destroystokyo/paper/event/entity/EntityTeleportEndGatewayEvent.html)：事件含义、触发条件和 Java API。

| `data` 字段 | JSON 类型 | Java getter | Java 返回类型 |
| --- | --- | --- | --- |
| `entity` | 实体摘要 | `getEntity()` | `org.bukkit.entity.Entity` |
| `entityType` | 字符串 | `getEntityType()` | `org.bukkit.entity.EntityType` |
| `from` | 位置摘要 | `getFrom()` | `org.bukkit.Location` |
| `to` | 位置摘要 | `getTo()` | `org.bukkit.Location` |

<a id="event-org-bukkit-event-entity-entityteleportevent"></a>
### EntityTeleportEvent

- Java 类：`org.bukkit.event.entity.EntityTeleportEvent`；父类：`org.bukkit.event.entity.EntityEvent`。
- Python 订阅：`@bridge.on("EntityTeleportEvent")`；也可使用 `Events.ENTITY_TELEPORT`。
- 可取消：是；关联玩家：可能有，取决于实际对象。
- [Paper 官方 Javadoc](https://jd.papermc.io/paper/1.16.5/org/bukkit/event/entity/EntityTeleportEvent.html)：事件含义、触发条件和 Java API。

| `data` 字段 | JSON 类型 | Java getter | Java 返回类型 |
| --- | --- | --- | --- |
| `entity` | 实体摘要 | `getEntity()` | `org.bukkit.entity.Entity` |
| `entityType` | 字符串 | `getEntityType()` | `org.bukkit.entity.EntityType` |
| `from` | 位置摘要 | `getFrom()` | `org.bukkit.Location` |
| `to` | 位置摘要 | `getTo()` | `org.bukkit.Location` |

<a id="event-org-bukkit-event-entity-entitytoggleglideevent"></a>
### EntityToggleGlideEvent

- Java 类：`org.bukkit.event.entity.EntityToggleGlideEvent`；父类：`org.bukkit.event.entity.EntityEvent`。
- Python 订阅：`@bridge.on("EntityToggleGlideEvent")`；也可使用 `Events.ENTITY_TOGGLE_GLIDE`。
- 可取消：是；关联玩家：可能有，取决于实际对象。
- [Paper 官方 Javadoc](https://jd.papermc.io/paper/1.16.5/org/bukkit/event/entity/EntityToggleGlideEvent.html)：事件含义、触发条件和 Java API。

| `data` 字段 | JSON 类型 | Java getter | Java 返回类型 |
| --- | --- | --- | --- |
| `entity` | 实体摘要 | `getEntity()` | `org.bukkit.entity.Entity` |
| `entityType` | 字符串 | `getEntityType()` | `org.bukkit.entity.EntityType` |
| `gliding` | 布尔值 | `isGliding()` | `boolean` |

<a id="event-org-bukkit-event-entity-entitytoggleswimevent"></a>
### EntityToggleSwimEvent

- Java 类：`org.bukkit.event.entity.EntityToggleSwimEvent`；父类：`org.bukkit.event.entity.EntityEvent`。
- Python 订阅：`@bridge.on("EntityToggleSwimEvent")`；也可使用 `Events.ENTITY_TOGGLE_SWIM`。
- 可取消：是；关联玩家：可能有，取决于实际对象。
- [Paper 官方 Javadoc](https://jd.papermc.io/paper/1.16.5/org/bukkit/event/entity/EntityToggleSwimEvent.html)：事件含义、触发条件和 Java API。

| `data` 字段 | JSON 类型 | Java getter | Java 返回类型 |
| --- | --- | --- | --- |
| `entity` | 实体摘要 | `getEntity()` | `org.bukkit.entity.Entity` |
| `entityType` | 字符串 | `getEntityType()` | `org.bukkit.entity.EntityType` |
| `swimming` | 布尔值 | `isSwimming()` | `boolean` |

<a id="event-com-destroystokyo-paper-event-entity-entitytransformedevent"></a>
### EntityTransformedEvent

- Java 类：`com.destroystokyo.paper.event.entity.EntityTransformedEvent`；父类：`org.bukkit.event.entity.EntityEvent`。
- Python 订阅：`@bridge.on("EntityTransformedEvent")`；也可使用 `Events.ENTITY_TRANSFORMED`。
- 可取消：是；关联玩家：可能有，取决于实际对象。
- [Paper 官方 Javadoc](https://jd.papermc.io/paper/1.16.5/com/destroystokyo/paper/event/entity/EntityTransformedEvent.html)：事件含义、触发条件和 Java API。

| `data` 字段 | JSON 类型 | Java getter | Java 返回类型 |
| --- | --- | --- | --- |
| `entity` | 实体摘要 | `getEntity()` | `org.bukkit.entity.Entity` |
| `entityType` | 字符串 | `getEntityType()` | `org.bukkit.entity.EntityType` |
| `reason` | 字符串 | `getReason()` | `com.destroystokyo.paper.event.entity.EntityTransformedEvent$TransformedReason` |
| `transformed` | 实体摘要 | `getTransformed()` | `org.bukkit.entity.Entity` |

<a id="event-org-bukkit-event-entity-entitytransformevent"></a>
### EntityTransformEvent

- Java 类：`org.bukkit.event.entity.EntityTransformEvent`；父类：`org.bukkit.event.entity.EntityEvent`。
- Python 订阅：`@bridge.on("EntityTransformEvent")`；也可使用 `Events.ENTITY_TRANSFORM`。
- 可取消：是；关联玩家：可能有，取决于实际对象。
- [Paper 官方 Javadoc](https://jd.papermc.io/paper/1.16.5/org/bukkit/event/entity/EntityTransformEvent.html)：事件含义、触发条件和 Java API。

| `data` 字段 | JSON 类型 | Java getter | Java 返回类型 |
| --- | --- | --- | --- |
| `entity` | 实体摘要 | `getEntity()` | `org.bukkit.entity.Entity` |
| `entityType` | 字符串 | `getEntityType()` | `org.bukkit.entity.EntityType` |
| `transformReason` | 字符串 | `getTransformReason()` | `org.bukkit.event.entity.EntityTransformEvent$TransformReason` |
| `transformedEntity` | 实体摘要 | `getTransformedEntity()` | `org.bukkit.entity.Entity` |

<a id="event-org-bukkit-event-entity-entityunleashevent"></a>
### EntityUnleashEvent

- Java 类：`org.bukkit.event.entity.EntityUnleashEvent`；父类：`org.bukkit.event.entity.EntityEvent`。
- Python 订阅：`@bridge.on("EntityUnleashEvent")`；也可使用 `Events.ENTITY_UNLEASH`。
- 可取消：否；关联玩家：可能有，取决于实际对象。
- [Paper 官方 Javadoc](https://jd.papermc.io/paper/1.16.5/org/bukkit/event/entity/EntityUnleashEvent.html)：事件含义、触发条件和 Java API。

| `data` 字段 | JSON 类型 | Java getter | Java 返回类型 |
| --- | --- | --- | --- |
| `entity` | 实体摘要 | `getEntity()` | `org.bukkit.entity.Entity` |
| `entityType` | 字符串 | `getEntityType()` | `org.bukkit.entity.EntityType` |
| `reason` | 字符串 | `getReason()` | `org.bukkit.event.entity.EntityUnleashEvent$UnleashReason` |
| `dropLeash` | 布尔值 | `isDropLeash()` | `boolean` |

<a id="event-com-destroystokyo-paper-event-entity-entityzapevent"></a>
### EntityZapEvent

- Java 类：`com.destroystokyo.paper.event.entity.EntityZapEvent`；父类：`org.bukkit.event.entity.EntityTransformEvent`。
- Python 订阅：`@bridge.on("EntityZapEvent")`；也可使用 `Events.ENTITY_ZAP`。
- 可取消：是；关联玩家：可能有，取决于实际对象。
- [Paper 官方 Javadoc](https://jd.papermc.io/paper/1.16.5/com/destroystokyo/paper/event/entity/EntityZapEvent.html)：事件含义、触发条件和 Java API。

| `data` 字段 | JSON 类型 | Java getter | Java 返回类型 |
| --- | --- | --- | --- |
| `bolt` | 实体摘要 | `getBolt()` | `org.bukkit.entity.LightningStrike` |
| `entity` | 实体摘要 | `getEntity()` | `org.bukkit.entity.Entity` |
| `entityType` | 字符串 | `getEntityType()` | `org.bukkit.entity.EntityType` |
| `replacementEntity` | 实体摘要 | `getReplacementEntity()` | `org.bukkit.entity.Entity` |
| `transformReason` | 字符串 | `getTransformReason()` | `org.bukkit.event.entity.EntityTransformEvent$TransformReason` |
| `transformedEntity` | 实体摘要 | `getTransformedEntity()` | `org.bukkit.entity.Entity` |

<a id="event-org-bukkit-event-entity-expbottleevent"></a>
### ExpBottleEvent

- Java 类：`org.bukkit.event.entity.ExpBottleEvent`；父类：`org.bukkit.event.entity.ProjectileHitEvent`。
- Python 订阅：`@bridge.on("ExpBottleEvent")`；也可使用 `Events.EXP_BOTTLE`。
- 可取消：是；关联玩家：可能有，取决于实际对象。
- [Paper 官方 Javadoc](https://jd.papermc.io/paper/1.16.5/org/bukkit/event/entity/ExpBottleEvent.html)：事件含义、触发条件和 Java API。

| `data` 字段 | JSON 类型 | Java getter | Java 返回类型 |
| --- | --- | --- | --- |
| `entity` | 实体摘要 | `getEntity()` | `org.bukkit.entity.Projectile` |
| `entityType` | 字符串 | `getEntityType()` | `org.bukkit.entity.EntityType` |
| `experience` | 数字 | `getExperience()` | `int` |
| `hitBlock` | 方块摘要 | `getHitBlock()` | `org.bukkit.block.Block` |
| `hitBlockFace` | 字符串 | `getHitBlockFace()` | `org.bukkit.block.BlockFace` |
| `hitEntity` | 实体摘要 | `getHitEntity()` | `org.bukkit.entity.Entity` |
| `showEffect` | 布尔值 | `getShowEffect()` | `boolean` |

<a id="event-com-destroystokyo-paper-event-entity-experienceorbmergeevent"></a>
### ExperienceOrbMergeEvent

- Java 类：`com.destroystokyo.paper.event.entity.ExperienceOrbMergeEvent`；父类：`org.bukkit.event.entity.EntityEvent`。
- Python 订阅：`@bridge.on("ExperienceOrbMergeEvent")`；也可使用 `Events.EXPERIENCE_ORB_MERGE`。
- 可取消：是；关联玩家：可能有，取决于实际对象。
- [Paper 官方 Javadoc](https://jd.papermc.io/paper/1.16.5/com/destroystokyo/paper/event/entity/ExperienceOrbMergeEvent.html)：事件含义、触发条件和 Java API。

| `data` 字段 | JSON 类型 | Java getter | Java 返回类型 |
| --- | --- | --- | --- |
| `entity` | 实体摘要 | `getEntity()` | `org.bukkit.entity.Entity` |
| `entityType` | 字符串 | `getEntityType()` | `org.bukkit.entity.EntityType` |
| `mergeSource` | 实体摘要 | `getMergeSource()` | `org.bukkit.entity.ExperienceOrb` |
| `mergeTarget` | 实体摘要 | `getMergeTarget()` | `org.bukkit.entity.ExperienceOrb` |

<a id="event-org-bukkit-event-entity-explosionprimeevent"></a>
### ExplosionPrimeEvent

- Java 类：`org.bukkit.event.entity.ExplosionPrimeEvent`；父类：`org.bukkit.event.entity.EntityEvent`。
- Python 订阅：`@bridge.on("ExplosionPrimeEvent")`；也可使用 `Events.EXPLOSION_PRIME`。
- 可取消：是；关联玩家：可能有，取决于实际对象。
- [Paper 官方 Javadoc](https://jd.papermc.io/paper/1.16.5/org/bukkit/event/entity/ExplosionPrimeEvent.html)：事件含义、触发条件和 Java API。

| `data` 字段 | JSON 类型 | Java getter | Java 返回类型 |
| --- | --- | --- | --- |
| `entity` | 实体摘要 | `getEntity()` | `org.bukkit.entity.Entity` |
| `entityType` | 字符串 | `getEntityType()` | `org.bukkit.entity.EntityType` |
| `fire` | 布尔值 | `getFire()` | `boolean` |
| `radius` | 数字 | `getRadius()` | `float` |

<a id="event-org-bukkit-event-entity-fireworkexplodeevent"></a>
### FireworkExplodeEvent

- Java 类：`org.bukkit.event.entity.FireworkExplodeEvent`；父类：`org.bukkit.event.entity.EntityEvent`。
- Python 订阅：`@bridge.on("FireworkExplodeEvent")`；也可使用 `Events.FIREWORK_EXPLODE`。
- 可取消：是；关联玩家：可能有，取决于实际对象。
- [Paper 官方 Javadoc](https://jd.papermc.io/paper/1.16.5/org/bukkit/event/entity/FireworkExplodeEvent.html)：事件含义、触发条件和 Java API。

| `data` 字段 | JSON 类型 | Java getter | Java 返回类型 |
| --- | --- | --- | --- |
| `entity` | 实体摘要 | `getEntity()` | `org.bukkit.entity.Entity` |
| `entityType` | 字符串 | `getEntityType()` | `org.bukkit.entity.EntityType` |

<a id="event-org-bukkit-event-entity-foodlevelchangeevent"></a>
### FoodLevelChangeEvent

- Java 类：`org.bukkit.event.entity.FoodLevelChangeEvent`；父类：`org.bukkit.event.entity.EntityEvent`。
- Python 订阅：`@bridge.on("FoodLevelChangeEvent")`；也可使用 `Events.FOOD_LEVEL_CHANGE`。
- 可取消：是；关联玩家：可能有，取决于实际对象。
- [Paper 官方 Javadoc](https://jd.papermc.io/paper/1.16.5/org/bukkit/event/entity/FoodLevelChangeEvent.html)：事件含义、触发条件和 Java API。

| `data` 字段 | JSON 类型 | Java getter | Java 返回类型 |
| --- | --- | --- | --- |
| `entity` | 实体摘要 | `getEntity()` | `org.bukkit.entity.HumanEntity` |
| `entityType` | 字符串 | `getEntityType()` | `org.bukkit.entity.EntityType` |
| `foodLevel` | 数字 | `getFoodLevel()` | `int` |
| `item` | 物品摘要 | `getItem()` | `org.bukkit.inventory.ItemStack` |

<a id="event-org-bukkit-event-entity-horsejumpevent"></a>
### HorseJumpEvent

- Java 类：`org.bukkit.event.entity.HorseJumpEvent`；父类：`org.bukkit.event.entity.EntityEvent`。
- Python 订阅：`@bridge.on("HorseJumpEvent")`；也可使用 `Events.HORSE_JUMP`。
- 可取消：是；关联玩家：可能有，取决于实际对象。
- [Paper 官方 Javadoc](https://jd.papermc.io/paper/1.16.5/org/bukkit/event/entity/HorseJumpEvent.html)：事件含义、触发条件和 Java API。

| `data` 字段 | JSON 类型 | Java getter | Java 返回类型 |
| --- | --- | --- | --- |
| `entity` | 实体摘要 | `getEntity()` | `org.bukkit.entity.Entity` |
| `entityType` | 字符串 | `getEntityType()` | `org.bukkit.entity.EntityType` |
| `power` | 数字 | `getPower()` | `float` |

<a id="event-org-bukkit-event-entity-itemdespawnevent"></a>
### ItemDespawnEvent

- Java 类：`org.bukkit.event.entity.ItemDespawnEvent`；父类：`org.bukkit.event.entity.EntityEvent`。
- Python 订阅：`@bridge.on("ItemDespawnEvent")`；也可使用 `Events.ITEM_DESPAWN`。
- 可取消：是；关联玩家：可能有，取决于实际对象。
- [Paper 官方 Javadoc](https://jd.papermc.io/paper/1.16.5/org/bukkit/event/entity/ItemDespawnEvent.html)：事件含义、触发条件和 Java API。

| `data` 字段 | JSON 类型 | Java getter | Java 返回类型 |
| --- | --- | --- | --- |
| `entity` | 实体摘要 | `getEntity()` | `org.bukkit.entity.Entity` |
| `entityType` | 字符串 | `getEntityType()` | `org.bukkit.entity.EntityType` |
| `location` | 位置摘要 | `getLocation()` | `org.bukkit.Location` |

<a id="event-org-bukkit-event-entity-itemmergeevent"></a>
### ItemMergeEvent

- Java 类：`org.bukkit.event.entity.ItemMergeEvent`；父类：`org.bukkit.event.entity.EntityEvent`。
- Python 订阅：`@bridge.on("ItemMergeEvent")`；也可使用 `Events.ITEM_MERGE`。
- 可取消：是；关联玩家：可能有，取决于实际对象。
- [Paper 官方 Javadoc](https://jd.papermc.io/paper/1.16.5/org/bukkit/event/entity/ItemMergeEvent.html)：事件含义、触发条件和 Java API。

| `data` 字段 | JSON 类型 | Java getter | Java 返回类型 |
| --- | --- | --- | --- |
| `entity` | 实体摘要 | `getEntity()` | `org.bukkit.entity.Entity` |
| `entityType` | 字符串 | `getEntityType()` | `org.bukkit.entity.EntityType` |
| `target` | 实体摘要 | `getTarget()` | `org.bukkit.entity.Item` |

<a id="event-org-bukkit-event-entity-itemspawnevent"></a>
### ItemSpawnEvent

- Java 类：`org.bukkit.event.entity.ItemSpawnEvent`；父类：`org.bukkit.event.entity.EntitySpawnEvent`。
- Python 订阅：`@bridge.on("ItemSpawnEvent")`；也可使用 `Events.ITEM_SPAWN`。
- 可取消：是；关联玩家：可能有，取决于实际对象。
- [Paper 官方 Javadoc](https://jd.papermc.io/paper/1.16.5/org/bukkit/event/entity/ItemSpawnEvent.html)：事件含义、触发条件和 Java API。

| `data` 字段 | JSON 类型 | Java getter | Java 返回类型 |
| --- | --- | --- | --- |
| `entity` | 实体摘要 | `getEntity()` | `org.bukkit.entity.Item` |
| `entityType` | 字符串 | `getEntityType()` | `org.bukkit.entity.EntityType` |
| `location` | 位置摘要 | `getLocation()` | `org.bukkit.Location` |

<a id="event-org-bukkit-event-entity-lingeringpotionsplashevent"></a>
### LingeringPotionSplashEvent

- Java 类：`org.bukkit.event.entity.LingeringPotionSplashEvent`；父类：`org.bukkit.event.entity.ProjectileHitEvent`。
- Python 订阅：`@bridge.on("LingeringPotionSplashEvent")`；也可使用 `Events.LINGERING_POTION_SPLASH`。
- 可取消：是；关联玩家：可能有，取决于实际对象。
- [Paper 官方 Javadoc](https://jd.papermc.io/paper/1.16.5/org/bukkit/event/entity/LingeringPotionSplashEvent.html)：事件含义、触发条件和 Java API。

| `data` 字段 | JSON 类型 | Java getter | Java 返回类型 |
| --- | --- | --- | --- |
| `areaEffectCloud` | 实体摘要 | `getAreaEffectCloud()` | `org.bukkit.entity.AreaEffectCloud` |
| `entity` | 实体摘要 | `getEntity()` | `org.bukkit.entity.ThrownPotion` |
| `entityType` | 字符串 | `getEntityType()` | `org.bukkit.entity.EntityType` |
| `hitBlock` | 方块摘要 | `getHitBlock()` | `org.bukkit.block.Block` |
| `hitBlockFace` | 字符串 | `getHitBlockFace()` | `org.bukkit.block.BlockFace` |
| `hitEntity` | 实体摘要 | `getHitEntity()` | `org.bukkit.entity.Entity` |

<a id="event-com-destroystokyo-paper-event-entity-phantomprespawnevent"></a>
### PhantomPreSpawnEvent

- Java 类：`com.destroystokyo.paper.event.entity.PhantomPreSpawnEvent`；父类：`com.destroystokyo.paper.event.entity.PreCreatureSpawnEvent`。
- Python 订阅：`@bridge.on("PhantomPreSpawnEvent")`；也可使用 `Events.PHANTOM_PRE_SPAWN`。
- 可取消：是；关联玩家：无已知玩家 getter。
- [Paper 官方 Javadoc](https://jd.papermc.io/paper/1.16.5/com/destroystokyo/paper/event/entity/PhantomPreSpawnEvent.html)：事件含义、触发条件和 Java API。

| `data` 字段 | JSON 类型 | Java getter | Java 返回类型 |
| --- | --- | --- | --- |
| `reason` | 字符串 | `getReason()` | `org.bukkit.event.entity.CreatureSpawnEvent$SpawnReason` |
| `spawnLocation` | 位置摘要 | `getSpawnLocation()` | `org.bukkit.Location` |
| `spawningEntity` | 实体摘要 | `getSpawningEntity()` | `org.bukkit.entity.Entity` |
| `type` | 字符串 | `getType()` | `org.bukkit.entity.EntityType` |

<a id="event-org-bukkit-event-entity-piglinbarterevent"></a>
### PiglinBarterEvent

- Java 类：`org.bukkit.event.entity.PiglinBarterEvent`；父类：`org.bukkit.event.entity.EntityEvent`。
- Python 订阅：`@bridge.on("PiglinBarterEvent")`；也可使用 `Events.PIGLIN_BARTER`。
- 可取消：是；关联玩家：可能有，取决于实际对象。
- [Paper 官方 Javadoc](https://jd.papermc.io/paper/1.16.5/org/bukkit/event/entity/PiglinBarterEvent.html)：事件含义、触发条件和 Java API。

| `data` 字段 | JSON 类型 | Java getter | Java 返回类型 |
| --- | --- | --- | --- |
| `entity` | 实体摘要 | `getEntity()` | `org.bukkit.entity.Entity` |
| `entityType` | 字符串 | `getEntityType()` | `org.bukkit.entity.EntityType` |
| `input` | 物品摘要 | `getInput()` | `org.bukkit.inventory.ItemStack` |

<a id="event-org-bukkit-event-entity-pigzapevent"></a>
### PigZapEvent

- Java 类：`org.bukkit.event.entity.PigZapEvent`；父类：`com.destroystokyo.paper.event.entity.EntityZapEvent`。
- Python 订阅：`@bridge.on("PigZapEvent")`；也可使用 `Events.PIG_ZAP`。
- 可取消：是；关联玩家：可能有，取决于实际对象。
- [Paper 官方 Javadoc](https://jd.papermc.io/paper/1.16.5/org/bukkit/event/entity/PigZapEvent.html)：事件含义、触发条件和 Java API。

| `data` 字段 | JSON 类型 | Java getter | Java 返回类型 |
| --- | --- | --- | --- |
| `bolt` | 实体摘要 | `getBolt()` | `org.bukkit.entity.LightningStrike` |
| `entity` | 实体摘要 | `getEntity()` | `org.bukkit.entity.Entity` |
| `entityType` | 字符串 | `getEntityType()` | `org.bukkit.entity.EntityType` |
| `lightning` | 实体摘要 | `getLightning()` | `org.bukkit.entity.LightningStrike` |
| `pigZombie` | 实体摘要 | `getPigZombie()` | `org.bukkit.entity.PigZombie` |
| `replacementEntity` | 实体摘要 | `getReplacementEntity()` | `org.bukkit.entity.Entity` |
| `transformReason` | 字符串 | `getTransformReason()` | `org.bukkit.event.entity.EntityTransformEvent$TransformReason` |
| `transformedEntity` | 实体摘要 | `getTransformedEntity()` | `org.bukkit.entity.Entity` |

<a id="event-org-bukkit-event-entity-pigzombieangerevent"></a>
### PigZombieAngerEvent

- Java 类：`org.bukkit.event.entity.PigZombieAngerEvent`；父类：`org.bukkit.event.entity.EntityEvent`。
- Python 订阅：`@bridge.on("PigZombieAngerEvent")`；也可使用 `Events.PIG_ZOMBIE_ANGER`。
- 可取消：是；关联玩家：可能有，取决于实际对象。
- [Paper 官方 Javadoc](https://jd.papermc.io/paper/1.16.5/org/bukkit/event/entity/PigZombieAngerEvent.html)：事件含义、触发条件和 Java API。

| `data` 字段 | JSON 类型 | Java getter | Java 返回类型 |
| --- | --- | --- | --- |
| `entity` | 实体摘要 | `getEntity()` | `org.bukkit.entity.PigZombie` |
| `entityType` | 字符串 | `getEntityType()` | `org.bukkit.entity.EntityType` |
| `newAnger` | 数字 | `getNewAnger()` | `int` |
| `target` | 实体摘要 | `getTarget()` | `org.bukkit.entity.Entity` |

<a id="event-org-bukkit-event-entity-playerdeathevent"></a>
### PlayerDeathEvent

- Java 类：`org.bukkit.event.entity.PlayerDeathEvent`；父类：`org.bukkit.event.entity.EntityDeathEvent`。
- Python 订阅：`@bridge.on("PlayerDeathEvent")`；也可使用 `Events.PLAYER_DEATH`。
- 可取消：是；关联玩家：可能有，取决于实际对象。
- [Paper 官方 Javadoc](https://jd.papermc.io/paper/1.16.5/org/bukkit/event/entity/PlayerDeathEvent.html)：事件含义、触发条件和 Java API。

| `data` 字段 | JSON 类型 | Java getter | Java 返回类型 |
| --- | --- | --- | --- |
| `deathMessage` | 字符串 | `getDeathMessage()` | `java.lang.String` |
| `deathSound` | 字符串 | `getDeathSound()` | `org.bukkit.Sound` |
| `deathSoundCategory` | 字符串 | `getDeathSoundCategory()` | `org.bukkit.SoundCategory` |
| `deathSoundPitch` | 数字 | `getDeathSoundPitch()` | `float` |
| `deathSoundVolume` | 数字 | `getDeathSoundVolume()` | `float` |
| `droppedExp` | 数字 | `getDroppedExp()` | `int` |
| `entity` | 实体摘要 | `getEntity()` | `org.bukkit.entity.LivingEntity` |
| `entityType` | 字符串 | `getEntityType()` | `org.bukkit.entity.EntityType` |
| `keepInventory` | 布尔值 | `getKeepInventory()` | `boolean` |
| `keepLevel` | 布尔值 | `getKeepLevel()` | `boolean` |
| `newExp` | 数字 | `getNewExp()` | `int` |
| `newLevel` | 数字 | `getNewLevel()` | `int` |
| `newTotalExp` | 数字 | `getNewTotalExp()` | `int` |
| `reviveHealth` | 数字 | `getReviveHealth()` | `double` |

<a id="event-org-bukkit-event-entity-playerleashentityevent"></a>
### PlayerLeashEntityEvent

- Java 类：`org.bukkit.event.entity.PlayerLeashEntityEvent`；父类：`org.bukkit.event.Event`。
- Python 订阅：`@bridge.on("PlayerLeashEntityEvent")`；也可使用 `Events.PLAYER_LEASH_ENTITY`。
- 可取消：是；关联玩家：可能有，取决于实际对象。
- [Paper 官方 Javadoc](https://jd.papermc.io/paper/1.16.5/org/bukkit/event/entity/PlayerLeashEntityEvent.html)：事件含义、触发条件和 Java API。

| `data` 字段 | JSON 类型 | Java getter | Java 返回类型 |
| --- | --- | --- | --- |
| `entity` | 实体摘要 | `getEntity()` | `org.bukkit.entity.Entity` |
| `leashHolder` | 实体摘要 | `getLeashHolder()` | `org.bukkit.entity.Entity` |

<a id="event-com-destroystokyo-paper-event-entity-playernaturallyspawncreaturesevent"></a>
### PlayerNaturallySpawnCreaturesEvent

- Java 类：`com.destroystokyo.paper.event.entity.PlayerNaturallySpawnCreaturesEvent`；父类：`org.bukkit.event.player.PlayerEvent`。
- Python 订阅：`@bridge.on("PlayerNaturallySpawnCreaturesEvent")`；也可使用 `Events.PLAYER_NATURALLY_SPAWN_CREATURES`。
- 可取消：是；关联玩家：可能有，取决于实际对象。
- [Paper 官方 Javadoc](https://jd.papermc.io/paper/1.16.5/com/destroystokyo/paper/event/entity/PlayerNaturallySpawnCreaturesEvent.html)：事件含义、触发条件和 Java API。

| `data` 字段 | JSON 类型 | Java getter | Java 返回类型 |
| --- | --- | --- | --- |
| `spawnRadius` | 数字 | `getSpawnRadius()` | `byte` |

<a id="event-org-bukkit-event-entity-potionsplashevent"></a>
### PotionSplashEvent

- Java 类：`org.bukkit.event.entity.PotionSplashEvent`；父类：`org.bukkit.event.entity.ProjectileHitEvent`。
- Python 订阅：`@bridge.on("PotionSplashEvent")`；也可使用 `Events.POTION_SPLASH`。
- 可取消：是；关联玩家：可能有，取决于实际对象。
- [Paper 官方 Javadoc](https://jd.papermc.io/paper/1.16.5/org/bukkit/event/entity/PotionSplashEvent.html)：事件含义、触发条件和 Java API。

| `data` 字段 | JSON 类型 | Java getter | Java 返回类型 |
| --- | --- | --- | --- |
| `entity` | 实体摘要 | `getEntity()` | `org.bukkit.entity.Entity` |
| `entityType` | 字符串 | `getEntityType()` | `org.bukkit.entity.EntityType` |
| `hitBlock` | 方块摘要 | `getHitBlock()` | `org.bukkit.block.Block` |
| `hitBlockFace` | 字符串 | `getHitBlockFace()` | `org.bukkit.block.BlockFace` |
| `hitEntity` | 实体摘要 | `getHitEntity()` | `org.bukkit.entity.Entity` |
| `potion` | 实体摘要 | `getPotion()` | `org.bukkit.entity.ThrownPotion` |

<a id="event-com-destroystokyo-paper-event-entity-precreaturespawnevent"></a>
### PreCreatureSpawnEvent

- Java 类：`com.destroystokyo.paper.event.entity.PreCreatureSpawnEvent`；父类：`org.bukkit.event.Event`。
- Python 订阅：`@bridge.on("PreCreatureSpawnEvent")`；也可使用 `Events.PRE_CREATURE_SPAWN`。
- 可取消：是；关联玩家：无已知玩家 getter。
- [Paper 官方 Javadoc](https://jd.papermc.io/paper/1.16.5/com/destroystokyo/paper/event/entity/PreCreatureSpawnEvent.html)：事件含义、触发条件和 Java API。

| `data` 字段 | JSON 类型 | Java getter | Java 返回类型 |
| --- | --- | --- | --- |
| `reason` | 字符串 | `getReason()` | `org.bukkit.event.entity.CreatureSpawnEvent$SpawnReason` |
| `spawnLocation` | 位置摘要 | `getSpawnLocation()` | `org.bukkit.Location` |
| `type` | 字符串 | `getType()` | `org.bukkit.entity.EntityType` |

<a id="event-com-destroystokyo-paper-event-entity-prespawnerspawnevent"></a>
### PreSpawnerSpawnEvent

- Java 类：`com.destroystokyo.paper.event.entity.PreSpawnerSpawnEvent`；父类：`com.destroystokyo.paper.event.entity.PreCreatureSpawnEvent`。
- Python 订阅：`@bridge.on("PreSpawnerSpawnEvent")`；也可使用 `Events.PRE_SPAWNER_SPAWN`。
- 可取消：是；关联玩家：无已知玩家 getter。
- [Paper 官方 Javadoc](https://jd.papermc.io/paper/1.16.5/com/destroystokyo/paper/event/entity/PreSpawnerSpawnEvent.html)：事件含义、触发条件和 Java API。

| `data` 字段 | JSON 类型 | Java getter | Java 返回类型 |
| --- | --- | --- | --- |
| `reason` | 字符串 | `getReason()` | `org.bukkit.event.entity.CreatureSpawnEvent$SpawnReason` |
| `spawnLocation` | 位置摘要 | `getSpawnLocation()` | `org.bukkit.Location` |
| `spawnerLocation` | 位置摘要 | `getSpawnerLocation()` | `org.bukkit.Location` |
| `type` | 字符串 | `getType()` | `org.bukkit.entity.EntityType` |

<a id="event-com-destroystokyo-paper-event-entity-projectilecollideevent"></a>
### ProjectileCollideEvent

- Java 类：`com.destroystokyo.paper.event.entity.ProjectileCollideEvent`；父类：`org.bukkit.event.entity.EntityEvent`。
- Python 订阅：`@bridge.on("ProjectileCollideEvent")`；也可使用 `Events.PROJECTILE_COLLIDE`。
- 可取消：是；关联玩家：可能有，取决于实际对象。
- [Paper 官方 Javadoc](https://jd.papermc.io/paper/1.16.5/com/destroystokyo/paper/event/entity/ProjectileCollideEvent.html)：事件含义、触发条件和 Java API。

| `data` 字段 | JSON 类型 | Java getter | Java 返回类型 |
| --- | --- | --- | --- |
| `collidedWith` | 实体摘要 | `getCollidedWith()` | `org.bukkit.entity.Entity` |
| `entity` | 实体摘要 | `getEntity()` | `org.bukkit.entity.Entity` |
| `entityType` | 字符串 | `getEntityType()` | `org.bukkit.entity.EntityType` |

<a id="event-org-bukkit-event-entity-projectilehitevent"></a>
### ProjectileHitEvent

- Java 类：`org.bukkit.event.entity.ProjectileHitEvent`；父类：`org.bukkit.event.entity.EntityEvent`。
- Python 订阅：`@bridge.on("ProjectileHitEvent")`；也可使用 `Events.PROJECTILE_HIT`。
- 可取消：是；关联玩家：可能有，取决于实际对象。
- [Paper 官方 Javadoc](https://jd.papermc.io/paper/1.16.5/org/bukkit/event/entity/ProjectileHitEvent.html)：事件含义、触发条件和 Java API。

| `data` 字段 | JSON 类型 | Java getter | Java 返回类型 |
| --- | --- | --- | --- |
| `entity` | 实体摘要 | `getEntity()` | `org.bukkit.entity.Projectile` |
| `entityType` | 字符串 | `getEntityType()` | `org.bukkit.entity.EntityType` |
| `hitBlock` | 方块摘要 | `getHitBlock()` | `org.bukkit.block.Block` |
| `hitBlockFace` | 字符串 | `getHitBlockFace()` | `org.bukkit.block.BlockFace` |
| `hitEntity` | 实体摘要 | `getHitEntity()` | `org.bukkit.entity.Entity` |

<a id="event-org-bukkit-event-entity-projectilelaunchevent"></a>
### ProjectileLaunchEvent

- Java 类：`org.bukkit.event.entity.ProjectileLaunchEvent`；父类：`org.bukkit.event.entity.EntitySpawnEvent`。
- Python 订阅：`@bridge.on("ProjectileLaunchEvent")`；也可使用 `Events.PROJECTILE_LAUNCH`。
- 可取消：是；关联玩家：可能有，取决于实际对象。
- [Paper 官方 Javadoc](https://jd.papermc.io/paper/1.16.5/org/bukkit/event/entity/ProjectileLaunchEvent.html)：事件含义、触发条件和 Java API。

| `data` 字段 | JSON 类型 | Java getter | Java 返回类型 |
| --- | --- | --- | --- |
| `entity` | 实体摘要 | `getEntity()` | `org.bukkit.entity.Entity` |
| `entityType` | 字符串 | `getEntityType()` | `org.bukkit.entity.EntityType` |
| `location` | 位置摘要 | `getLocation()` | `org.bukkit.Location` |

<a id="event-io-papermc-paper-event-entity-pufferfishstatechangeevent"></a>
### PufferFishStateChangeEvent

- Java 类：`io.papermc.paper.event.entity.PufferFishStateChangeEvent`；父类：`org.bukkit.event.entity.EntityEvent`。
- Python 订阅：`@bridge.on("PufferFishStateChangeEvent")`；也可使用 `Events.PUFFER_FISH_STATE_CHANGE`。
- 可取消：是；关联玩家：可能有，取决于实际对象。
- [Paper 官方 Javadoc](https://jd.papermc.io/paper/1.16.5/io/papermc/paper/event/entity/PufferFishStateChangeEvent.html)：事件含义、触发条件和 Java API。

| `data` 字段 | JSON 类型 | Java getter | Java 返回类型 |
| --- | --- | --- | --- |
| `entity` | 实体摘要 | `getEntity()` | `org.bukkit.entity.Entity` |
| `entityType` | 字符串 | `getEntityType()` | `org.bukkit.entity.EntityType` |
| `newPuffState` | 数字 | `getNewPuffState()` | `int` |
| `deflating` | 布尔值 | `isDeflating()` | `boolean` |
| `inflating` | 布尔值 | `isInflating()` | `boolean` |

<a id="event-org-bukkit-event-entity-sheepdyewoolevent"></a>
### SheepDyeWoolEvent

- Java 类：`org.bukkit.event.entity.SheepDyeWoolEvent`；父类：`org.bukkit.event.entity.EntityEvent`。
- Python 订阅：`@bridge.on("SheepDyeWoolEvent")`；也可使用 `Events.SHEEP_DYE_WOOL`。
- 可取消：是；关联玩家：可能有，取决于实际对象。
- [Paper 官方 Javadoc](https://jd.papermc.io/paper/1.16.5/org/bukkit/event/entity/SheepDyeWoolEvent.html)：事件含义、触发条件和 Java API。

| `data` 字段 | JSON 类型 | Java getter | Java 返回类型 |
| --- | --- | --- | --- |
| `color` | 字符串 | `getColor()` | `org.bukkit.DyeColor` |
| `entity` | 实体摘要 | `getEntity()` | `org.bukkit.entity.Entity` |
| `entityType` | 字符串 | `getEntityType()` | `org.bukkit.entity.EntityType` |

<a id="event-org-bukkit-event-entity-sheepregrowwoolevent"></a>
### SheepRegrowWoolEvent

- Java 类：`org.bukkit.event.entity.SheepRegrowWoolEvent`；父类：`org.bukkit.event.entity.EntityEvent`。
- Python 订阅：`@bridge.on("SheepRegrowWoolEvent")`；也可使用 `Events.SHEEP_REGROW_WOOL`。
- 可取消：是；关联玩家：可能有，取决于实际对象。
- [Paper 官方 Javadoc](https://jd.papermc.io/paper/1.16.5/org/bukkit/event/entity/SheepRegrowWoolEvent.html)：事件含义、触发条件和 Java API。

| `data` 字段 | JSON 类型 | Java getter | Java 返回类型 |
| --- | --- | --- | --- |
| `entity` | 实体摘要 | `getEntity()` | `org.bukkit.entity.Entity` |
| `entityType` | 字符串 | `getEntityType()` | `org.bukkit.entity.EntityType` |

<a id="event-com-destroystokyo-paper-event-entity-skeletonhorsetrapevent"></a>
### SkeletonHorseTrapEvent

- Java 类：`com.destroystokyo.paper.event.entity.SkeletonHorseTrapEvent`；父类：`org.bukkit.event.entity.EntityEvent`。
- Python 订阅：`@bridge.on("SkeletonHorseTrapEvent")`；也可使用 `Events.SKELETON_HORSE_TRAP`。
- 可取消：是；关联玩家：可能有，取决于实际对象。
- [Paper 官方 Javadoc](https://jd.papermc.io/paper/1.16.5/com/destroystokyo/paper/event/entity/SkeletonHorseTrapEvent.html)：事件含义、触发条件和 Java API。

| `data` 字段 | JSON 类型 | Java getter | Java 返回类型 |
| --- | --- | --- | --- |
| `entity` | 实体摘要 | `getEntity()` | `org.bukkit.entity.SkeletonHorse` |
| `entityType` | 字符串 | `getEntityType()` | `org.bukkit.entity.EntityType` |

<a id="event-com-destroystokyo-paper-event-entity-slimechangedirectionevent"></a>
### SlimeChangeDirectionEvent

- Java 类：`com.destroystokyo.paper.event.entity.SlimeChangeDirectionEvent`；父类：`com.destroystokyo.paper.event.entity.SlimePathfindEvent`。
- Python 订阅：`@bridge.on("SlimeChangeDirectionEvent")`；也可使用 `Events.SLIME_CHANGE_DIRECTION`。
- 可取消：是；关联玩家：可能有，取决于实际对象。
- [Paper 官方 Javadoc](https://jd.papermc.io/paper/1.16.5/com/destroystokyo/paper/event/entity/SlimeChangeDirectionEvent.html)：事件含义、触发条件和 Java API。

| `data` 字段 | JSON 类型 | Java getter | Java 返回类型 |
| --- | --- | --- | --- |
| `entity` | 实体摘要 | `getEntity()` | `org.bukkit.entity.Slime` |
| `entityType` | 字符串 | `getEntityType()` | `org.bukkit.entity.EntityType` |
| `newYaw` | 数字 | `getNewYaw()` | `float` |

<a id="event-com-destroystokyo-paper-event-entity-slimepathfindevent"></a>
### SlimePathfindEvent

- Java 类：`com.destroystokyo.paper.event.entity.SlimePathfindEvent`；父类：`org.bukkit.event.entity.EntityEvent`。
- Python 订阅：`@bridge.on("SlimePathfindEvent")`；也可使用 `Events.SLIME_PATHFIND`。
- 可取消：是；关联玩家：可能有，取决于实际对象。
- [Paper 官方 Javadoc](https://jd.papermc.io/paper/1.16.5/com/destroystokyo/paper/event/entity/SlimePathfindEvent.html)：事件含义、触发条件和 Java API。

| `data` 字段 | JSON 类型 | Java getter | Java 返回类型 |
| --- | --- | --- | --- |
| `entity` | 实体摘要 | `getEntity()` | `org.bukkit.entity.Slime` |
| `entityType` | 字符串 | `getEntityType()` | `org.bukkit.entity.EntityType` |

<a id="event-org-bukkit-event-entity-slimesplitevent"></a>
### SlimeSplitEvent

- Java 类：`org.bukkit.event.entity.SlimeSplitEvent`；父类：`org.bukkit.event.entity.EntityEvent`。
- Python 订阅：`@bridge.on("SlimeSplitEvent")`；也可使用 `Events.SLIME_SPLIT`。
- 可取消：是；关联玩家：可能有，取决于实际对象。
- [Paper 官方 Javadoc](https://jd.papermc.io/paper/1.16.5/org/bukkit/event/entity/SlimeSplitEvent.html)：事件含义、触发条件和 Java API。

| `data` 字段 | JSON 类型 | Java getter | Java 返回类型 |
| --- | --- | --- | --- |
| `count` | 数字 | `getCount()` | `int` |
| `entity` | 实体摘要 | `getEntity()` | `org.bukkit.entity.Slime` |
| `entityType` | 字符串 | `getEntityType()` | `org.bukkit.entity.EntityType` |

<a id="event-com-destroystokyo-paper-event-entity-slimeswimevent"></a>
### SlimeSwimEvent

- Java 类：`com.destroystokyo.paper.event.entity.SlimeSwimEvent`；父类：`com.destroystokyo.paper.event.entity.SlimeWanderEvent`。
- Python 订阅：`@bridge.on("SlimeSwimEvent")`；也可使用 `Events.SLIME_SWIM`。
- 可取消：是；关联玩家：可能有，取决于实际对象。
- [Paper 官方 Javadoc](https://jd.papermc.io/paper/1.16.5/com/destroystokyo/paper/event/entity/SlimeSwimEvent.html)：事件含义、触发条件和 Java API。

| `data` 字段 | JSON 类型 | Java getter | Java 返回类型 |
| --- | --- | --- | --- |
| `entity` | 实体摘要 | `getEntity()` | `org.bukkit.entity.Slime` |
| `entityType` | 字符串 | `getEntityType()` | `org.bukkit.entity.EntityType` |

<a id="event-com-destroystokyo-paper-event-entity-slimetargetlivingentityevent"></a>
### SlimeTargetLivingEntityEvent

- Java 类：`com.destroystokyo.paper.event.entity.SlimeTargetLivingEntityEvent`；父类：`com.destroystokyo.paper.event.entity.SlimePathfindEvent`。
- Python 订阅：`@bridge.on("SlimeTargetLivingEntityEvent")`；也可使用 `Events.SLIME_TARGET_LIVING_ENTITY`。
- 可取消：是；关联玩家：可能有，取决于实际对象。
- [Paper 官方 Javadoc](https://jd.papermc.io/paper/1.16.5/com/destroystokyo/paper/event/entity/SlimeTargetLivingEntityEvent.html)：事件含义、触发条件和 Java API。

| `data` 字段 | JSON 类型 | Java getter | Java 返回类型 |
| --- | --- | --- | --- |
| `entity` | 实体摘要 | `getEntity()` | `org.bukkit.entity.Slime` |
| `entityType` | 字符串 | `getEntityType()` | `org.bukkit.entity.EntityType` |
| `target` | 实体摘要 | `getTarget()` | `org.bukkit.entity.LivingEntity` |

<a id="event-com-destroystokyo-paper-event-entity-slimewanderevent"></a>
### SlimeWanderEvent

- Java 类：`com.destroystokyo.paper.event.entity.SlimeWanderEvent`；父类：`com.destroystokyo.paper.event.entity.SlimePathfindEvent`。
- Python 订阅：`@bridge.on("SlimeWanderEvent")`；也可使用 `Events.SLIME_WANDER`。
- 可取消：是；关联玩家：可能有，取决于实际对象。
- [Paper 官方 Javadoc](https://jd.papermc.io/paper/1.16.5/com/destroystokyo/paper/event/entity/SlimeWanderEvent.html)：事件含义、触发条件和 Java API。

| `data` 字段 | JSON 类型 | Java getter | Java 返回类型 |
| --- | --- | --- | --- |
| `entity` | 实体摘要 | `getEntity()` | `org.bukkit.entity.Slime` |
| `entityType` | 字符串 | `getEntityType()` | `org.bukkit.entity.EntityType` |

<a id="event-org-bukkit-event-entity-spawnerspawnevent"></a>
### SpawnerSpawnEvent

- Java 类：`org.bukkit.event.entity.SpawnerSpawnEvent`；父类：`org.bukkit.event.entity.EntitySpawnEvent`。
- Python 订阅：`@bridge.on("SpawnerSpawnEvent")`；也可使用 `Events.SPAWNER_SPAWN`。
- 可取消：是；关联玩家：可能有，取决于实际对象。
- [Paper 官方 Javadoc](https://jd.papermc.io/paper/1.16.5/org/bukkit/event/entity/SpawnerSpawnEvent.html)：事件含义、触发条件和 Java API。

| `data` 字段 | JSON 类型 | Java getter | Java 返回类型 |
| --- | --- | --- | --- |
| `entity` | 实体摘要 | `getEntity()` | `org.bukkit.entity.Entity` |
| `entityType` | 字符串 | `getEntityType()` | `org.bukkit.entity.EntityType` |
| `location` | 位置摘要 | `getLocation()` | `org.bukkit.Location` |

<a id="event-org-bukkit-event-entity-stridertemperaturechangeevent"></a>
### StriderTemperatureChangeEvent

- Java 类：`org.bukkit.event.entity.StriderTemperatureChangeEvent`；父类：`org.bukkit.event.entity.EntityEvent`。
- Python 订阅：`@bridge.on("StriderTemperatureChangeEvent")`；也可使用 `Events.STRIDER_TEMPERATURE_CHANGE`。
- 可取消：否；关联玩家：可能有，取决于实际对象。
- [Paper 官方 Javadoc](https://jd.papermc.io/paper/1.16.5/org/bukkit/event/entity/StriderTemperatureChangeEvent.html)：事件含义、触发条件和 Java API。

| `data` 字段 | JSON 类型 | Java getter | Java 返回类型 |
| --- | --- | --- | --- |
| `entity` | 实体摘要 | `getEntity()` | `org.bukkit.entity.Entity` |
| `entityType` | 字符串 | `getEntityType()` | `org.bukkit.entity.EntityType` |
| `shivering` | 布尔值 | `isShivering()` | `boolean` |

<a id="event-com-destroystokyo-paper-event-entity-thrownegghatchevent"></a>
### ThrownEggHatchEvent

- Java 类：`com.destroystokyo.paper.event.entity.ThrownEggHatchEvent`；父类：`org.bukkit.event.Event`。
- Python 订阅：`@bridge.on("ThrownEggHatchEvent")`；也可使用 `Events.THROWN_EGG_HATCH`。
- 可取消：否；关联玩家：无已知玩家 getter。
- [Paper 官方 Javadoc](https://jd.papermc.io/paper/1.16.5/com/destroystokyo/paper/event/entity/ThrownEggHatchEvent.html)：事件含义、触发条件和 Java API。

| `data` 字段 | JSON 类型 | Java getter | Java 返回类型 |
| --- | --- | --- | --- |
| `egg` | 实体摘要 | `getEgg()` | `org.bukkit.entity.Egg` |
| `hatchingType` | 字符串 | `getHatchingType()` | `org.bukkit.entity.EntityType` |
| `numHatches` | 数字 | `getNumHatches()` | `byte` |
| `hatching` | 布尔值 | `isHatching()` | `boolean` |

<a id="event-com-destroystokyo-paper-event-entity-turtlegohomeevent"></a>
### TurtleGoHomeEvent

- Java 类：`com.destroystokyo.paper.event.entity.TurtleGoHomeEvent`；父类：`org.bukkit.event.entity.EntityEvent`。
- Python 订阅：`@bridge.on("TurtleGoHomeEvent")`；也可使用 `Events.TURTLE_GO_HOME`。
- 可取消：是；关联玩家：可能有，取决于实际对象。
- [Paper 官方 Javadoc](https://jd.papermc.io/paper/1.16.5/com/destroystokyo/paper/event/entity/TurtleGoHomeEvent.html)：事件含义、触发条件和 Java API。

| `data` 字段 | JSON 类型 | Java getter | Java 返回类型 |
| --- | --- | --- | --- |
| `entity` | 实体摘要 | `getEntity()` | `org.bukkit.entity.Entity` |
| `entityType` | 字符串 | `getEntityType()` | `org.bukkit.entity.EntityType` |

<a id="event-com-destroystokyo-paper-event-entity-turtlelayeggevent"></a>
### TurtleLayEggEvent

- Java 类：`com.destroystokyo.paper.event.entity.TurtleLayEggEvent`；父类：`org.bukkit.event.entity.EntityEvent`。
- Python 订阅：`@bridge.on("TurtleLayEggEvent")`；也可使用 `Events.TURTLE_LAY_EGG`。
- 可取消：是；关联玩家：可能有，取决于实际对象。
- [Paper 官方 Javadoc](https://jd.papermc.io/paper/1.16.5/com/destroystokyo/paper/event/entity/TurtleLayEggEvent.html)：事件含义、触发条件和 Java API。

| `data` 字段 | JSON 类型 | Java getter | Java 返回类型 |
| --- | --- | --- | --- |
| `eggCount` | 数字 | `getEggCount()` | `int` |
| `entity` | 实体摘要 | `getEntity()` | `org.bukkit.entity.Turtle` |
| `entityType` | 字符串 | `getEntityType()` | `org.bukkit.entity.EntityType` |
| `location` | 位置摘要 | `getLocation()` | `org.bukkit.Location` |

<a id="event-com-destroystokyo-paper-event-entity-turtlestartdiggingevent"></a>
### TurtleStartDiggingEvent

- Java 类：`com.destroystokyo.paper.event.entity.TurtleStartDiggingEvent`；父类：`org.bukkit.event.entity.EntityEvent`。
- Python 订阅：`@bridge.on("TurtleStartDiggingEvent")`；也可使用 `Events.TURTLE_START_DIGGING`。
- 可取消：是；关联玩家：可能有，取决于实际对象。
- [Paper 官方 Javadoc](https://jd.papermc.io/paper/1.16.5/com/destroystokyo/paper/event/entity/TurtleStartDiggingEvent.html)：事件含义、触发条件和 Java API。

| `data` 字段 | JSON 类型 | Java getter | Java 返回类型 |
| --- | --- | --- | --- |
| `entity` | 实体摘要 | `getEntity()` | `org.bukkit.entity.Turtle` |
| `entityType` | 字符串 | `getEntityType()` | `org.bukkit.entity.EntityType` |
| `location` | 位置摘要 | `getLocation()` | `org.bukkit.Location` |

<a id="event-org-bukkit-event-entity-villageracquiretradeevent"></a>
### VillagerAcquireTradeEvent

- Java 类：`org.bukkit.event.entity.VillagerAcquireTradeEvent`；父类：`org.bukkit.event.entity.EntityEvent`。
- Python 订阅：`@bridge.on("VillagerAcquireTradeEvent")`；也可使用 `Events.VILLAGER_ACQUIRE_TRADE`。
- 可取消：是；关联玩家：可能有，取决于实际对象。
- [Paper 官方 Javadoc](https://jd.papermc.io/paper/1.16.5/org/bukkit/event/entity/VillagerAcquireTradeEvent.html)：事件含义、触发条件和 Java API。

| `data` 字段 | JSON 类型 | Java getter | Java 返回类型 |
| --- | --- | --- | --- |
| `entity` | 实体摘要 | `getEntity()` | `org.bukkit.entity.Entity` |
| `entityType` | 字符串 | `getEntityType()` | `org.bukkit.entity.EntityType` |

<a id="event-org-bukkit-event-entity-villagercareerchangeevent"></a>
### VillagerCareerChangeEvent

- Java 类：`org.bukkit.event.entity.VillagerCareerChangeEvent`；父类：`org.bukkit.event.entity.EntityEvent`。
- Python 订阅：`@bridge.on("VillagerCareerChangeEvent")`；也可使用 `Events.VILLAGER_CAREER_CHANGE`。
- 可取消：是；关联玩家：可能有，取决于实际对象。
- [Paper 官方 Javadoc](https://jd.papermc.io/paper/1.16.5/org/bukkit/event/entity/VillagerCareerChangeEvent.html)：事件含义、触发条件和 Java API。

| `data` 字段 | JSON 类型 | Java getter | Java 返回类型 |
| --- | --- | --- | --- |
| `entity` | 实体摘要 | `getEntity()` | `org.bukkit.entity.Entity` |
| `entityType` | 字符串 | `getEntityType()` | `org.bukkit.entity.EntityType` |
| `profession` | 字符串 | `getProfession()` | `org.bukkit.entity.Villager$Profession` |
| `reason` | 字符串 | `getReason()` | `org.bukkit.event.entity.VillagerCareerChangeEvent$ChangeReason` |

<a id="event-org-bukkit-event-entity-villagerreplenishtradeevent"></a>
### VillagerReplenishTradeEvent

- Java 类：`org.bukkit.event.entity.VillagerReplenishTradeEvent`；父类：`org.bukkit.event.entity.EntityEvent`。
- Python 订阅：`@bridge.on("VillagerReplenishTradeEvent")`；也可使用 `Events.VILLAGER_REPLENISH_TRADE`。
- 可取消：是；关联玩家：可能有，取决于实际对象。
- [Paper 官方 Javadoc](https://jd.papermc.io/paper/1.16.5/org/bukkit/event/entity/VillagerReplenishTradeEvent.html)：事件含义、触发条件和 Java API。

| `data` 字段 | JSON 类型 | Java getter | Java 返回类型 |
| --- | --- | --- | --- |
| `bonus` | 数字 | `getBonus()` | `int` |
| `entity` | 实体摘要 | `getEntity()` | `org.bukkit.entity.Entity` |
| `entityType` | 字符串 | `getEntityType()` | `org.bukkit.entity.EntityType` |

<a id="event-com-destroystokyo-paper-event-entity-witchconsumepotionevent"></a>
### WitchConsumePotionEvent

- Java 类：`com.destroystokyo.paper.event.entity.WitchConsumePotionEvent`；父类：`org.bukkit.event.entity.EntityEvent`。
- Python 订阅：`@bridge.on("WitchConsumePotionEvent")`；也可使用 `Events.WITCH_CONSUME_POTION`。
- 可取消：是；关联玩家：可能有，取决于实际对象。
- [Paper 官方 Javadoc](https://jd.papermc.io/paper/1.16.5/com/destroystokyo/paper/event/entity/WitchConsumePotionEvent.html)：事件含义、触发条件和 Java API。

| `data` 字段 | JSON 类型 | Java getter | Java 返回类型 |
| --- | --- | --- | --- |
| `entity` | 实体摘要 | `getEntity()` | `org.bukkit.entity.Entity` |
| `entityType` | 字符串 | `getEntityType()` | `org.bukkit.entity.EntityType` |
| `potion` | 物品摘要 | `getPotion()` | `org.bukkit.inventory.ItemStack` |

<a id="event-com-destroystokyo-paper-event-entity-witchreadypotionevent"></a>
### WitchReadyPotionEvent

- Java 类：`com.destroystokyo.paper.event.entity.WitchReadyPotionEvent`；父类：`org.bukkit.event.entity.EntityEvent`。
- Python 订阅：`@bridge.on("WitchReadyPotionEvent")`；也可使用 `Events.WITCH_READY_POTION`。
- 可取消：是；关联玩家：可能有，取决于实际对象。
- [Paper 官方 Javadoc](https://jd.papermc.io/paper/1.16.5/com/destroystokyo/paper/event/entity/WitchReadyPotionEvent.html)：事件含义、触发条件和 Java API。

| `data` 字段 | JSON 类型 | Java getter | Java 返回类型 |
| --- | --- | --- | --- |
| `entity` | 实体摘要 | `getEntity()` | `org.bukkit.entity.Entity` |
| `entityType` | 字符串 | `getEntityType()` | `org.bukkit.entity.EntityType` |
| `potion` | 物品摘要 | `getPotion()` | `org.bukkit.inventory.ItemStack` |

<a id="event-com-destroystokyo-paper-event-entity-witchthrowpotionevent"></a>
### WitchThrowPotionEvent

- Java 类：`com.destroystokyo.paper.event.entity.WitchThrowPotionEvent`；父类：`org.bukkit.event.entity.EntityEvent`。
- Python 订阅：`@bridge.on("WitchThrowPotionEvent")`；也可使用 `Events.WITCH_THROW_POTION`。
- 可取消：是；关联玩家：可能有，取决于实际对象。
- [Paper 官方 Javadoc](https://jd.papermc.io/paper/1.16.5/com/destroystokyo/paper/event/entity/WitchThrowPotionEvent.html)：事件含义、触发条件和 Java API。

| `data` 字段 | JSON 类型 | Java getter | Java 返回类型 |
| --- | --- | --- | --- |
| `entity` | 实体摘要 | `getEntity()` | `org.bukkit.entity.Entity` |
| `entityType` | 字符串 | `getEntityType()` | `org.bukkit.entity.EntityType` |
| `potion` | 物品摘要 | `getPotion()` | `org.bukkit.inventory.ItemStack` |
| `target` | 实体摘要 | `getTarget()` | `org.bukkit.entity.LivingEntity` |

<a id="category-hanging"></a>
## 悬挂实体 / hanging

| 事件 | Python `type` | `data` 候选字段数 | 可取消 |
| --- | --- | ---: | --- |
| [HangingBreakByEntityEvent](#event-org-bukkit-event-hanging-hangingbreakbyentityevent) | `HangingBreakByEntityEvent` | 3 | 是 |
| [HangingBreakEvent](#event-org-bukkit-event-hanging-hangingbreakevent) | `HangingBreakEvent` | 2 | 是 |
| [HangingPlaceEvent](#event-org-bukkit-event-hanging-hangingplaceevent) | `HangingPlaceEvent` | 3 | 是 |

<a id="event-org-bukkit-event-hanging-hangingbreakbyentityevent"></a>
### HangingBreakByEntityEvent

- Java 类：`org.bukkit.event.hanging.HangingBreakByEntityEvent`；父类：`org.bukkit.event.hanging.HangingBreakEvent`。
- Python 订阅：`@bridge.on("HangingBreakByEntityEvent")`；也可使用 `Events.HANGING_BREAK_BY_ENTITY`。
- 可取消：是；关联玩家：可能有，取决于实际对象。
- [Paper 官方 Javadoc](https://jd.papermc.io/paper/1.16.5/org/bukkit/event/hanging/HangingBreakByEntityEvent.html)：事件含义、触发条件和 Java API。

| `data` 字段 | JSON 类型 | Java getter | Java 返回类型 |
| --- | --- | --- | --- |
| `cause` | 字符串 | `getCause()` | `org.bukkit.event.hanging.HangingBreakEvent$RemoveCause` |
| `entity` | 实体摘要 | `getEntity()` | `org.bukkit.entity.Hanging` |
| `remover` | 实体摘要 | `getRemover()` | `org.bukkit.entity.Entity` |

<a id="event-org-bukkit-event-hanging-hangingbreakevent"></a>
### HangingBreakEvent

- Java 类：`org.bukkit.event.hanging.HangingBreakEvent`；父类：`org.bukkit.event.hanging.HangingEvent`。
- Python 订阅：`@bridge.on("HangingBreakEvent")`；也可使用 `Events.HANGING_BREAK`。
- 可取消：是；关联玩家：可能有，取决于实际对象。
- [Paper 官方 Javadoc](https://jd.papermc.io/paper/1.16.5/org/bukkit/event/hanging/HangingBreakEvent.html)：事件含义、触发条件和 Java API。

| `data` 字段 | JSON 类型 | Java getter | Java 返回类型 |
| --- | --- | --- | --- |
| `cause` | 字符串 | `getCause()` | `org.bukkit.event.hanging.HangingBreakEvent$RemoveCause` |
| `entity` | 实体摘要 | `getEntity()` | `org.bukkit.entity.Hanging` |

<a id="event-org-bukkit-event-hanging-hangingplaceevent"></a>
### HangingPlaceEvent

- Java 类：`org.bukkit.event.hanging.HangingPlaceEvent`；父类：`org.bukkit.event.hanging.HangingEvent`。
- Python 订阅：`@bridge.on("HangingPlaceEvent")`；也可使用 `Events.HANGING_PLACE`。
- 可取消：是；关联玩家：可能有，取决于实际对象。
- [Paper 官方 Javadoc](https://jd.papermc.io/paper/1.16.5/org/bukkit/event/hanging/HangingPlaceEvent.html)：事件含义、触发条件和 Java API。

| `data` 字段 | JSON 类型 | Java getter | Java 返回类型 |
| --- | --- | --- | --- |
| `block` | 方块摘要 | `getBlock()` | `org.bukkit.block.Block` |
| `blockFace` | 字符串 | `getBlockFace()` | `org.bukkit.block.BlockFace` |
| `entity` | 实体摘要 | `getEntity()` | `org.bukkit.entity.Hanging` |

<a id="category-inventory"></a>
## 物品栏 / inventory

| 事件 | Python `type` | `data` 候选字段数 | 可取消 |
| --- | --- | ---: | --- |
| [BrewEvent](#event-org-bukkit-event-inventory-brewevent) | `BrewEvent` | 2 | 是 |
| [BrewingStandFuelEvent](#event-org-bukkit-event-inventory-brewingstandfuelevent) | `BrewingStandFuelEvent` | 4 | 是 |
| [CraftItemEvent](#event-org-bukkit-event-inventory-craftitemevent) | `CraftItemEvent` | 13 | 是 |
| [FurnaceBurnEvent](#event-org-bukkit-event-inventory-furnaceburnevent) | `FurnaceBurnEvent` | 4 | 是 |
| [FurnaceExtractEvent](#event-org-bukkit-event-inventory-furnaceextractevent) | `FurnaceExtractEvent` | 4 | 否 |
| [FurnaceSmeltEvent](#event-org-bukkit-event-inventory-furnacesmeltevent) | `FurnaceSmeltEvent` | 3 | 是 |
| [InventoryClickEvent](#event-org-bukkit-event-inventory-inventoryclickevent) | `InventoryClickEvent` | 13 | 是 |
| [InventoryCloseEvent](#event-org-bukkit-event-inventory-inventorycloseevent) | `InventoryCloseEvent` | 1 | 否 |
| [InventoryCreativeEvent](#event-org-bukkit-event-inventory-inventorycreativeevent) | `InventoryCreativeEvent` | 13 | 是 |
| [InventoryDragEvent](#event-org-bukkit-event-inventory-inventorydragevent) | `InventoryDragEvent` | 5 | 是 |
| [InventoryEvent](#event-org-bukkit-event-inventory-inventoryevent) | `InventoryEvent` | 0 | 否 |
| [InventoryMoveItemEvent](#event-org-bukkit-event-inventory-inventorymoveitemevent) | `InventoryMoveItemEvent` | 1 | 是 |
| [InventoryOpenEvent](#event-org-bukkit-event-inventory-inventoryopenevent) | `InventoryOpenEvent` | 0 | 是 |
| [InventoryPickupItemEvent](#event-org-bukkit-event-inventory-inventorypickupitemevent) | `InventoryPickupItemEvent` | 1 | 是 |
| [PrepareAnvilEvent](#event-org-bukkit-event-inventory-prepareanvilevent) | `PrepareAnvilEvent` | 1 | 否 |
| [PrepareGrindstoneEvent](#event-com-destroystokyo-paper-event-inventory-preparegrindstoneevent) | `PrepareGrindstoneEvent` | 1 | 否 |
| [PrepareItemCraftEvent](#event-org-bukkit-event-inventory-prepareitemcraftevent) | `PrepareItemCraftEvent` | 1 | 否 |
| [PrepareResultEvent](#event-com-destroystokyo-paper-event-inventory-prepareresultevent) | `PrepareResultEvent` | 1 | 否 |
| [PrepareSmithingEvent](#event-org-bukkit-event-inventory-preparesmithingevent) | `PrepareSmithingEvent` | 1 | 否 |
| [SmithItemEvent](#event-org-bukkit-event-inventory-smithitemevent) | `SmithItemEvent` | 13 | 是 |
| [TradeSelectEvent](#event-org-bukkit-event-inventory-tradeselectevent) | `TradeSelectEvent` | 3 | 是 |

<a id="event-org-bukkit-event-inventory-brewevent"></a>
### BrewEvent

- Java 类：`org.bukkit.event.inventory.BrewEvent`；父类：`org.bukkit.event.block.BlockEvent`。
- Python 订阅：`@bridge.on("BrewEvent")`；也可使用 `Events.BREW`。
- 可取消：是；关联玩家：无已知玩家 getter。
- [Paper 官方 Javadoc](https://jd.papermc.io/paper/1.16.5/org/bukkit/event/inventory/BrewEvent.html)：事件含义、触发条件和 Java API。

| `data` 字段 | JSON 类型 | Java getter | Java 返回类型 |
| --- | --- | --- | --- |
| `block` | 方块摘要 | `getBlock()` | `org.bukkit.block.Block` |
| `fuelLevel` | 数字 | `getFuelLevel()` | `int` |

<a id="event-org-bukkit-event-inventory-brewingstandfuelevent"></a>
### BrewingStandFuelEvent

- Java 类：`org.bukkit.event.inventory.BrewingStandFuelEvent`；父类：`org.bukkit.event.block.BlockEvent`。
- Python 订阅：`@bridge.on("BrewingStandFuelEvent")`；也可使用 `Events.BREWING_STAND_FUEL`。
- 可取消：是；关联玩家：无已知玩家 getter。
- [Paper 官方 Javadoc](https://jd.papermc.io/paper/1.16.5/org/bukkit/event/inventory/BrewingStandFuelEvent.html)：事件含义、触发条件和 Java API。

| `data` 字段 | JSON 类型 | Java getter | Java 返回类型 |
| --- | --- | --- | --- |
| `block` | 方块摘要 | `getBlock()` | `org.bukkit.block.Block` |
| `fuel` | 物品摘要 | `getFuel()` | `org.bukkit.inventory.ItemStack` |
| `fuelPower` | 数字 | `getFuelPower()` | `int` |
| `consuming` | 布尔值 | `isConsuming()` | `boolean` |

<a id="event-org-bukkit-event-inventory-craftitemevent"></a>
### CraftItemEvent

- Java 类：`org.bukkit.event.inventory.CraftItemEvent`；父类：`org.bukkit.event.inventory.InventoryClickEvent`。
- Python 订阅：`@bridge.on("CraftItemEvent")`；也可使用 `Events.CRAFT_ITEM`。
- 可取消：是；关联玩家：可能有，取决于实际对象。
- [Paper 官方 Javadoc](https://jd.papermc.io/paper/1.16.5/org/bukkit/event/inventory/CraftItemEvent.html)：事件含义、触发条件和 Java API。

| `data` 字段 | JSON 类型 | Java getter | Java 返回类型 |
| --- | --- | --- | --- |
| `action` | 字符串 | `getAction()` | `org.bukkit.event.inventory.InventoryAction` |
| `click` | 字符串 | `getClick()` | `org.bukkit.event.inventory.ClickType` |
| `currentItem` | 物品摘要 | `getCurrentItem()` | `org.bukkit.inventory.ItemStack` |
| `cursor` | 物品摘要 | `getCursor()` | `org.bukkit.inventory.ItemStack` |
| `hotbarButton` | 数字 | `getHotbarButton()` | `int` |
| `rawSlot` | 数字 | `getRawSlot()` | `int` |
| `result` | 字符串 | `getResult()` | `org.bukkit.event.Event$Result` |
| `slot` | 数字 | `getSlot()` | `int` |
| `slotType` | 字符串 | `getSlotType()` | `org.bukkit.event.inventory.InventoryType$SlotType` |
| `whoClicked` | 实体摘要 | `getWhoClicked()` | `org.bukkit.entity.HumanEntity` |
| `leftClick` | 布尔值 | `isLeftClick()` | `boolean` |
| `rightClick` | 布尔值 | `isRightClick()` | `boolean` |
| `shiftClick` | 布尔值 | `isShiftClick()` | `boolean` |

<a id="event-org-bukkit-event-inventory-furnaceburnevent"></a>
### FurnaceBurnEvent

- Java 类：`org.bukkit.event.inventory.FurnaceBurnEvent`；父类：`org.bukkit.event.block.BlockEvent`。
- Python 订阅：`@bridge.on("FurnaceBurnEvent")`；也可使用 `Events.FURNACE_BURN`。
- 可取消：是；关联玩家：无已知玩家 getter。
- [Paper 官方 Javadoc](https://jd.papermc.io/paper/1.16.5/org/bukkit/event/inventory/FurnaceBurnEvent.html)：事件含义、触发条件和 Java API。

| `data` 字段 | JSON 类型 | Java getter | Java 返回类型 |
| --- | --- | --- | --- |
| `block` | 方块摘要 | `getBlock()` | `org.bukkit.block.Block` |
| `burnTime` | 数字 | `getBurnTime()` | `int` |
| `fuel` | 物品摘要 | `getFuel()` | `org.bukkit.inventory.ItemStack` |
| `burning` | 布尔值 | `isBurning()` | `boolean` |

<a id="event-org-bukkit-event-inventory-furnaceextractevent"></a>
### FurnaceExtractEvent

- Java 类：`org.bukkit.event.inventory.FurnaceExtractEvent`；父类：`org.bukkit.event.block.BlockExpEvent`。
- Python 订阅：`@bridge.on("FurnaceExtractEvent")`；也可使用 `Events.FURNACE_EXTRACT`。
- 可取消：否；关联玩家：可能有，取决于实际对象。
- [Paper 官方 Javadoc](https://jd.papermc.io/paper/1.16.5/org/bukkit/event/inventory/FurnaceExtractEvent.html)：事件含义、触发条件和 Java API。

| `data` 字段 | JSON 类型 | Java getter | Java 返回类型 |
| --- | --- | --- | --- |
| `block` | 方块摘要 | `getBlock()` | `org.bukkit.block.Block` |
| `expToDrop` | 数字 | `getExpToDrop()` | `int` |
| `itemAmount` | 数字 | `getItemAmount()` | `int` |
| `itemType` | 字符串 | `getItemType()` | `org.bukkit.Material` |

<a id="event-org-bukkit-event-inventory-furnacesmeltevent"></a>
### FurnaceSmeltEvent

- Java 类：`org.bukkit.event.inventory.FurnaceSmeltEvent`；父类：`org.bukkit.event.block.BlockCookEvent`。
- Python 订阅：`@bridge.on("FurnaceSmeltEvent")`；也可使用 `Events.FURNACE_SMELT`。
- 可取消：是；关联玩家：无已知玩家 getter。
- [Paper 官方 Javadoc](https://jd.papermc.io/paper/1.16.5/org/bukkit/event/inventory/FurnaceSmeltEvent.html)：事件含义、触发条件和 Java API。

| `data` 字段 | JSON 类型 | Java getter | Java 返回类型 |
| --- | --- | --- | --- |
| `block` | 方块摘要 | `getBlock()` | `org.bukkit.block.Block` |
| `result` | 物品摘要 | `getResult()` | `org.bukkit.inventory.ItemStack` |
| `source` | 物品摘要 | `getSource()` | `org.bukkit.inventory.ItemStack` |

<a id="event-org-bukkit-event-inventory-inventoryclickevent"></a>
### InventoryClickEvent

- Java 类：`org.bukkit.event.inventory.InventoryClickEvent`；父类：`org.bukkit.event.inventory.InventoryInteractEvent`。
- Python 订阅：`@bridge.on("InventoryClickEvent")`；也可使用 `Events.INVENTORY_CLICK`。
- 可取消：是；关联玩家：可能有，取决于实际对象。
- [Paper 官方 Javadoc](https://jd.papermc.io/paper/1.16.5/org/bukkit/event/inventory/InventoryClickEvent.html)：事件含义、触发条件和 Java API。

| `data` 字段 | JSON 类型 | Java getter | Java 返回类型 |
| --- | --- | --- | --- |
| `action` | 字符串 | `getAction()` | `org.bukkit.event.inventory.InventoryAction` |
| `click` | 字符串 | `getClick()` | `org.bukkit.event.inventory.ClickType` |
| `currentItem` | 物品摘要 | `getCurrentItem()` | `org.bukkit.inventory.ItemStack` |
| `cursor` | 物品摘要 | `getCursor()` | `org.bukkit.inventory.ItemStack` |
| `hotbarButton` | 数字 | `getHotbarButton()` | `int` |
| `rawSlot` | 数字 | `getRawSlot()` | `int` |
| `result` | 字符串 | `getResult()` | `org.bukkit.event.Event$Result` |
| `slot` | 数字 | `getSlot()` | `int` |
| `slotType` | 字符串 | `getSlotType()` | `org.bukkit.event.inventory.InventoryType$SlotType` |
| `whoClicked` | 实体摘要 | `getWhoClicked()` | `org.bukkit.entity.HumanEntity` |
| `leftClick` | 布尔值 | `isLeftClick()` | `boolean` |
| `rightClick` | 布尔值 | `isRightClick()` | `boolean` |
| `shiftClick` | 布尔值 | `isShiftClick()` | `boolean` |

<a id="event-org-bukkit-event-inventory-inventorycloseevent"></a>
### InventoryCloseEvent

- Java 类：`org.bukkit.event.inventory.InventoryCloseEvent`；父类：`org.bukkit.event.inventory.InventoryEvent`。
- Python 订阅：`@bridge.on("InventoryCloseEvent")`；也可使用 `Events.INVENTORY_CLOSE`。
- 可取消：否；关联玩家：可能有，取决于实际对象。
- [Paper 官方 Javadoc](https://jd.papermc.io/paper/1.16.5/org/bukkit/event/inventory/InventoryCloseEvent.html)：事件含义、触发条件和 Java API。

| `data` 字段 | JSON 类型 | Java getter | Java 返回类型 |
| --- | --- | --- | --- |
| `reason` | 字符串 | `getReason()` | `org.bukkit.event.inventory.InventoryCloseEvent$Reason` |

<a id="event-org-bukkit-event-inventory-inventorycreativeevent"></a>
### InventoryCreativeEvent

- Java 类：`org.bukkit.event.inventory.InventoryCreativeEvent`；父类：`org.bukkit.event.inventory.InventoryClickEvent`。
- Python 订阅：`@bridge.on("InventoryCreativeEvent")`；也可使用 `Events.INVENTORY_CREATIVE`。
- 可取消：是；关联玩家：可能有，取决于实际对象。
- [Paper 官方 Javadoc](https://jd.papermc.io/paper/1.16.5/org/bukkit/event/inventory/InventoryCreativeEvent.html)：事件含义、触发条件和 Java API。

| `data` 字段 | JSON 类型 | Java getter | Java 返回类型 |
| --- | --- | --- | --- |
| `action` | 字符串 | `getAction()` | `org.bukkit.event.inventory.InventoryAction` |
| `click` | 字符串 | `getClick()` | `org.bukkit.event.inventory.ClickType` |
| `currentItem` | 物品摘要 | `getCurrentItem()` | `org.bukkit.inventory.ItemStack` |
| `cursor` | 物品摘要 | `getCursor()` | `org.bukkit.inventory.ItemStack` |
| `hotbarButton` | 数字 | `getHotbarButton()` | `int` |
| `rawSlot` | 数字 | `getRawSlot()` | `int` |
| `result` | 字符串 | `getResult()` | `org.bukkit.event.Event$Result` |
| `slot` | 数字 | `getSlot()` | `int` |
| `slotType` | 字符串 | `getSlotType()` | `org.bukkit.event.inventory.InventoryType$SlotType` |
| `whoClicked` | 实体摘要 | `getWhoClicked()` | `org.bukkit.entity.HumanEntity` |
| `leftClick` | 布尔值 | `isLeftClick()` | `boolean` |
| `rightClick` | 布尔值 | `isRightClick()` | `boolean` |
| `shiftClick` | 布尔值 | `isShiftClick()` | `boolean` |

<a id="event-org-bukkit-event-inventory-inventorydragevent"></a>
### InventoryDragEvent

- Java 类：`org.bukkit.event.inventory.InventoryDragEvent`；父类：`org.bukkit.event.inventory.InventoryInteractEvent`。
- Python 订阅：`@bridge.on("InventoryDragEvent")`；也可使用 `Events.INVENTORY_DRAG`。
- 可取消：是；关联玩家：可能有，取决于实际对象。
- [Paper 官方 Javadoc](https://jd.papermc.io/paper/1.16.5/org/bukkit/event/inventory/InventoryDragEvent.html)：事件含义、触发条件和 Java API。

| `data` 字段 | JSON 类型 | Java getter | Java 返回类型 |
| --- | --- | --- | --- |
| `cursor` | 物品摘要 | `getCursor()` | `org.bukkit.inventory.ItemStack` |
| `oldCursor` | 物品摘要 | `getOldCursor()` | `org.bukkit.inventory.ItemStack` |
| `result` | 字符串 | `getResult()` | `org.bukkit.event.Event$Result` |
| `type` | 字符串 | `getType()` | `org.bukkit.event.inventory.DragType` |
| `whoClicked` | 实体摘要 | `getWhoClicked()` | `org.bukkit.entity.HumanEntity` |

<a id="event-org-bukkit-event-inventory-inventoryevent"></a>
### InventoryEvent

- Java 类：`org.bukkit.event.inventory.InventoryEvent`；父类：`org.bukkit.event.Event`。
- Python 订阅：`@bridge.on("InventoryEvent")`；也可使用 `Events.INVENTORY`。
- 可取消：否；关联玩家：无已知玩家 getter。
- [Paper 官方 Javadoc](https://jd.papermc.io/paper/1.16.5/org/bukkit/event/inventory/InventoryEvent.html)：事件含义、触发条件和 Java API。

没有可序列化的 `data` 字段；仍会收到通用事件字段。

<a id="event-org-bukkit-event-inventory-inventorymoveitemevent"></a>
### InventoryMoveItemEvent

- Java 类：`org.bukkit.event.inventory.InventoryMoveItemEvent`；父类：`org.bukkit.event.Event`。
- Python 订阅：`@bridge.on("InventoryMoveItemEvent")`；也可使用 `Events.INVENTORY_MOVE_ITEM`。
- 可取消：是；关联玩家：无已知玩家 getter。
- [Paper 官方 Javadoc](https://jd.papermc.io/paper/1.16.5/org/bukkit/event/inventory/InventoryMoveItemEvent.html)：事件含义、触发条件和 Java API。

| `data` 字段 | JSON 类型 | Java getter | Java 返回类型 |
| --- | --- | --- | --- |
| `item` | 物品摘要 | `getItem()` | `org.bukkit.inventory.ItemStack` |

<a id="event-org-bukkit-event-inventory-inventoryopenevent"></a>
### InventoryOpenEvent

- Java 类：`org.bukkit.event.inventory.InventoryOpenEvent`；父类：`org.bukkit.event.inventory.InventoryEvent`。
- Python 订阅：`@bridge.on("InventoryOpenEvent")`；也可使用 `Events.INVENTORY_OPEN`。
- 可取消：是；关联玩家：可能有，取决于实际对象。
- [Paper 官方 Javadoc](https://jd.papermc.io/paper/1.16.5/org/bukkit/event/inventory/InventoryOpenEvent.html)：事件含义、触发条件和 Java API。

没有可序列化的 `data` 字段；仍会收到通用事件字段。

<a id="event-org-bukkit-event-inventory-inventorypickupitemevent"></a>
### InventoryPickupItemEvent

- Java 类：`org.bukkit.event.inventory.InventoryPickupItemEvent`；父类：`org.bukkit.event.Event`。
- Python 订阅：`@bridge.on("InventoryPickupItemEvent")`；也可使用 `Events.INVENTORY_PICKUP_ITEM`。
- 可取消：是；关联玩家：无已知玩家 getter。
- [Paper 官方 Javadoc](https://jd.papermc.io/paper/1.16.5/org/bukkit/event/inventory/InventoryPickupItemEvent.html)：事件含义、触发条件和 Java API。

| `data` 字段 | JSON 类型 | Java getter | Java 返回类型 |
| --- | --- | --- | --- |
| `item` | 实体摘要 | `getItem()` | `org.bukkit.entity.Item` |

<a id="event-org-bukkit-event-inventory-prepareanvilevent"></a>
### PrepareAnvilEvent

- Java 类：`org.bukkit.event.inventory.PrepareAnvilEvent`；父类：`com.destroystokyo.paper.event.inventory.PrepareResultEvent`。
- Python 订阅：`@bridge.on("PrepareAnvilEvent")`；也可使用 `Events.PREPARE_ANVIL`。
- 可取消：否；关联玩家：无已知玩家 getter。
- [Paper 官方 Javadoc](https://jd.papermc.io/paper/1.16.5/org/bukkit/event/inventory/PrepareAnvilEvent.html)：事件含义、触发条件和 Java API。

| `data` 字段 | JSON 类型 | Java getter | Java 返回类型 |
| --- | --- | --- | --- |
| `result` | 物品摘要 | `getResult()` | `org.bukkit.inventory.ItemStack` |

<a id="event-com-destroystokyo-paper-event-inventory-preparegrindstoneevent"></a>
### PrepareGrindstoneEvent

- Java 类：`com.destroystokyo.paper.event.inventory.PrepareGrindstoneEvent`；父类：`com.destroystokyo.paper.event.inventory.PrepareResultEvent`。
- Python 订阅：`@bridge.on("PrepareGrindstoneEvent")`；也可使用 `Events.PREPARE_GRINDSTONE`。
- 可取消：否；关联玩家：无已知玩家 getter。
- [Paper 官方 Javadoc](https://jd.papermc.io/paper/1.16.5/com/destroystokyo/paper/event/inventory/PrepareGrindstoneEvent.html)：事件含义、触发条件和 Java API。

| `data` 字段 | JSON 类型 | Java getter | Java 返回类型 |
| --- | --- | --- | --- |
| `result` | 物品摘要 | `getResult()` | `org.bukkit.inventory.ItemStack` |

<a id="event-org-bukkit-event-inventory-prepareitemcraftevent"></a>
### PrepareItemCraftEvent

- Java 类：`org.bukkit.event.inventory.PrepareItemCraftEvent`；父类：`org.bukkit.event.inventory.InventoryEvent`。
- Python 订阅：`@bridge.on("PrepareItemCraftEvent")`；也可使用 `Events.PREPARE_ITEM_CRAFT`。
- 可取消：否；关联玩家：无已知玩家 getter。
- [Paper 官方 Javadoc](https://jd.papermc.io/paper/1.16.5/org/bukkit/event/inventory/PrepareItemCraftEvent.html)：事件含义、触发条件和 Java API。

| `data` 字段 | JSON 类型 | Java getter | Java 返回类型 |
| --- | --- | --- | --- |
| `repair` | 布尔值 | `isRepair()` | `boolean` |

<a id="event-com-destroystokyo-paper-event-inventory-prepareresultevent"></a>
### PrepareResultEvent

- Java 类：`com.destroystokyo.paper.event.inventory.PrepareResultEvent`；父类：`org.bukkit.event.inventory.InventoryEvent`。
- Python 订阅：`@bridge.on("PrepareResultEvent")`；也可使用 `Events.PREPARE_RESULT`。
- 可取消：否；关联玩家：无已知玩家 getter。
- [Paper 官方 Javadoc](https://jd.papermc.io/paper/1.16.5/com/destroystokyo/paper/event/inventory/PrepareResultEvent.html)：事件含义、触发条件和 Java API。

| `data` 字段 | JSON 类型 | Java getter | Java 返回类型 |
| --- | --- | --- | --- |
| `result` | 物品摘要 | `getResult()` | `org.bukkit.inventory.ItemStack` |

<a id="event-org-bukkit-event-inventory-preparesmithingevent"></a>
### PrepareSmithingEvent

- Java 类：`org.bukkit.event.inventory.PrepareSmithingEvent`；父类：`com.destroystokyo.paper.event.inventory.PrepareResultEvent`。
- Python 订阅：`@bridge.on("PrepareSmithingEvent")`；也可使用 `Events.PREPARE_SMITHING`。
- 可取消：否；关联玩家：无已知玩家 getter。
- [Paper 官方 Javadoc](https://jd.papermc.io/paper/1.16.5/org/bukkit/event/inventory/PrepareSmithingEvent.html)：事件含义、触发条件和 Java API。

| `data` 字段 | JSON 类型 | Java getter | Java 返回类型 |
| --- | --- | --- | --- |
| `result` | 物品摘要 | `getResult()` | `org.bukkit.inventory.ItemStack` |

<a id="event-org-bukkit-event-inventory-smithitemevent"></a>
### SmithItemEvent

- Java 类：`org.bukkit.event.inventory.SmithItemEvent`；父类：`org.bukkit.event.inventory.InventoryClickEvent`。
- Python 订阅：`@bridge.on("SmithItemEvent")`；也可使用 `Events.SMITH_ITEM`。
- 可取消：是；关联玩家：可能有，取决于实际对象。
- [Paper 官方 Javadoc](https://jd.papermc.io/paper/1.16.5/org/bukkit/event/inventory/SmithItemEvent.html)：事件含义、触发条件和 Java API。

| `data` 字段 | JSON 类型 | Java getter | Java 返回类型 |
| --- | --- | --- | --- |
| `action` | 字符串 | `getAction()` | `org.bukkit.event.inventory.InventoryAction` |
| `click` | 字符串 | `getClick()` | `org.bukkit.event.inventory.ClickType` |
| `currentItem` | 物品摘要 | `getCurrentItem()` | `org.bukkit.inventory.ItemStack` |
| `cursor` | 物品摘要 | `getCursor()` | `org.bukkit.inventory.ItemStack` |
| `hotbarButton` | 数字 | `getHotbarButton()` | `int` |
| `rawSlot` | 数字 | `getRawSlot()` | `int` |
| `result` | 字符串 | `getResult()` | `org.bukkit.event.Event$Result` |
| `slot` | 数字 | `getSlot()` | `int` |
| `slotType` | 字符串 | `getSlotType()` | `org.bukkit.event.inventory.InventoryType$SlotType` |
| `whoClicked` | 实体摘要 | `getWhoClicked()` | `org.bukkit.entity.HumanEntity` |
| `leftClick` | 布尔值 | `isLeftClick()` | `boolean` |
| `rightClick` | 布尔值 | `isRightClick()` | `boolean` |
| `shiftClick` | 布尔值 | `isShiftClick()` | `boolean` |

<a id="event-org-bukkit-event-inventory-tradeselectevent"></a>
### TradeSelectEvent

- Java 类：`org.bukkit.event.inventory.TradeSelectEvent`；父类：`org.bukkit.event.inventory.InventoryInteractEvent`。
- Python 订阅：`@bridge.on("TradeSelectEvent")`；也可使用 `Events.TRADE_SELECT`。
- 可取消：是；关联玩家：可能有，取决于实际对象。
- [Paper 官方 Javadoc](https://jd.papermc.io/paper/1.16.5/org/bukkit/event/inventory/TradeSelectEvent.html)：事件含义、触发条件和 Java API。

| `data` 字段 | JSON 类型 | Java getter | Java 返回类型 |
| --- | --- | --- | --- |
| `index` | 数字 | `getIndex()` | `int` |
| `result` | 字符串 | `getResult()` | `org.bukkit.event.Event$Result` |
| `whoClicked` | 实体摘要 | `getWhoClicked()` | `org.bukkit.entity.HumanEntity` |

<a id="category-packet"></a>
## 网络包 / packet

| 事件 | Python `type` | `data` 候选字段数 | 可取消 |
| --- | --- | ---: | --- |
| [PlayerChunkLoadEvent](#event-io-papermc-paper-event-packet-playerchunkloadevent) | `PlayerChunkLoadEvent` | 1 | 否 |
| [PlayerChunkUnloadEvent](#event-io-papermc-paper-event-packet-playerchunkunloadevent) | `PlayerChunkUnloadEvent` | 1 | 否 |

<a id="event-io-papermc-paper-event-packet-playerchunkloadevent"></a>
### PlayerChunkLoadEvent

- Java 类：`io.papermc.paper.event.packet.PlayerChunkLoadEvent`；父类：`org.bukkit.event.world.ChunkEvent`。
- Python 订阅：`@bridge.on("PlayerChunkLoadEvent")`；也可使用 `Events.PLAYER_CHUNK_LOAD`。
- 可取消：否；关联玩家：可能有，取决于实际对象。
- [Paper 官方 Javadoc](https://jd.papermc.io/paper/1.16.5/io/papermc/paper/event/packet/PlayerChunkLoadEvent.html)：事件含义、触发条件和 Java API。

| `data` 字段 | JSON 类型 | Java getter | Java 返回类型 |
| --- | --- | --- | --- |
| `world` | 世界摘要 | `getWorld()` | `org.bukkit.World` |

<a id="event-io-papermc-paper-event-packet-playerchunkunloadevent"></a>
### PlayerChunkUnloadEvent

- Java 类：`io.papermc.paper.event.packet.PlayerChunkUnloadEvent`；父类：`org.bukkit.event.world.ChunkEvent`。
- Python 订阅：`@bridge.on("PlayerChunkUnloadEvent")`；也可使用 `Events.PLAYER_CHUNK_UNLOAD`。
- 可取消：否；关联玩家：可能有，取决于实际对象。
- [Paper 官方 Javadoc](https://jd.papermc.io/paper/1.16.5/io/papermc/paper/event/packet/PlayerChunkUnloadEvent.html)：事件含义、触发条件和 Java API。

| `data` 字段 | JSON 类型 | Java getter | Java 返回类型 |
| --- | --- | --- | --- |
| `world` | 世界摘要 | `getWorld()` | `org.bukkit.World` |

<a id="category-player"></a>
## 玩家 / player

| 事件 | Python `type` | `data` 候选字段数 | 可取消 |
| --- | --- | ---: | --- |
| [AsyncChatEvent](#event-io-papermc-paper-event-player-asyncchatevent) | `AsyncChatEvent` | 0 | 是 |
| [AsyncPlayerChatEvent](#event-org-bukkit-event-player-asyncplayerchatevent) | `chat` | 2 | 是 |
| [AsyncPlayerPreLoginEvent](#event-org-bukkit-event-player-asyncplayerpreloginevent) | `AsyncPlayerPreLoginEvent` | 5 | 否 |
| [ChatEvent](#event-io-papermc-paper-event-player-chatevent) | `ChatEvent` | 0 | 是 |
| [IllegalPacketEvent](#event-com-destroystokyo-paper-event-player-illegalpacketevent) | `IllegalPacketEvent` | 4 | 否 |
| [PlayerAdvancementCriterionGrantEvent](#event-com-destroystokyo-paper-event-player-playeradvancementcriteriongrantevent) | `PlayerAdvancementCriterionGrantEvent` | 1 | 是 |
| [PlayerAdvancementDoneEvent](#event-org-bukkit-event-player-playeradvancementdoneevent) | `PlayerAdvancementDoneEvent` | 0 | 否 |
| [PlayerAnimationEvent](#event-org-bukkit-event-player-playeranimationevent) | `PlayerAnimationEvent` | 1 | 是 |
| [PlayerArmorChangeEvent](#event-com-destroystokyo-paper-event-player-playerarmorchangeevent) | `PlayerArmorChangeEvent` | 3 | 否 |
| [PlayerArmorStandManipulateEvent](#event-org-bukkit-event-player-playerarmorstandmanipulateevent) | `PlayerArmorStandManipulateEvent` | 5 | 是 |
| [PlayerArmSwingEvent](#event-io-papermc-paper-event-player-playerarmswingevent) | `PlayerArmSwingEvent` | 2 | 是 |
| [PlayerAttackEntityCooldownResetEvent](#event-com-destroystokyo-paper-event-player-playerattackentitycooldownresetevent) | `PlayerAttackEntityCooldownResetEvent` | 2 | 是 |
| [PlayerAttemptPickupItemEvent](#event-org-bukkit-event-player-playerattemptpickupitemevent) | `PlayerAttemptPickupItemEvent` | 3 | 是 |
| [PlayerBedEnterEvent](#event-org-bukkit-event-player-playerbedenterevent) | `PlayerBedEnterEvent` | 2 | 是 |
| [PlayerBedFailEnterEvent](#event-io-papermc-paper-event-player-playerbedfailenterevent) | `PlayerBedFailEnterEvent` | 3 | 是 |
| [PlayerBedLeaveEvent](#event-org-bukkit-event-player-playerbedleaveevent) | `PlayerBedLeaveEvent` | 1 | 是 |
| [PlayerBucketEmptyEvent](#event-org-bukkit-event-player-playerbucketemptyevent) | `PlayerBucketEmptyEvent` | 6 | 是 |
| [PlayerBucketEntityEvent](#event-org-bukkit-event-player-playerbucketentityevent) | `PlayerBucketEntityEvent` | 3 | 是 |
| [PlayerBucketFillEvent](#event-org-bukkit-event-player-playerbucketfillevent) | `PlayerBucketFillEvent` | 6 | 是 |
| [PlayerBucketFishEvent](#event-org-bukkit-event-player-playerbucketfishevent) | `PlayerBucketFishEvent` | 5 | 是 |
| [PlayerChangeBeaconEffectEvent](#event-io-papermc-paper-event-player-playerchangebeaconeffectevent) | `PlayerChangeBeaconEffectEvent` | 1 | 是 |
| [PlayerChangedMainHandEvent](#event-org-bukkit-event-player-playerchangedmainhandevent) | `PlayerChangedMainHandEvent` | 1 | 否 |
| [PlayerChangedWorldEvent](#event-org-bukkit-event-player-playerchangedworldevent) | `PlayerChangedWorldEvent` | 1 | 否 |
| [PlayerChatEvent](#event-org-bukkit-event-player-playerchatevent) | `PlayerChatEvent` | 2 | 是 |
| [PlayerChatTabCompleteEvent](#event-org-bukkit-event-player-playerchattabcompleteevent) | `PlayerChatTabCompleteEvent` | 2 | 否 |
| [PlayerClientOptionsChangeEvent](#event-com-destroystokyo-paper-event-player-playerclientoptionschangeevent) | `PlayerClientOptionsChangeEvent` | 4 | 否 |
| [PlayerCommandPreprocessEvent](#event-org-bukkit-event-player-playercommandpreprocessevent) | `PlayerCommandPreprocessEvent` | 1 | 是 |
| [PlayerCommandSendEvent](#event-org-bukkit-event-player-playercommandsendevent) | `PlayerCommandSendEvent` | 0 | 否 |
| [PlayerConnectionCloseEvent](#event-com-destroystokyo-paper-event-player-playerconnectioncloseevent) | `PlayerConnectionCloseEvent` | 2 | 否 |
| [PlayerDeepSleepEvent](#event-io-papermc-paper-event-player-playerdeepsleepevent) | `PlayerDeepSleepEvent` | 0 | 是 |
| [PlayerDropItemEvent](#event-org-bukkit-event-player-playerdropitemevent) | `PlayerDropItemEvent` | 1 | 是 |
| [PlayerEditBookEvent](#event-org-bukkit-event-player-playereditbookevent) | `PlayerEditBookEvent` | 2 | 是 |
| [PlayerEggThrowEvent](#event-org-bukkit-event-player-playereggthrowevent) | `PlayerEggThrowEvent` | 4 | 否 |
| [PlayerElytraBoostEvent](#event-com-destroystokyo-paper-event-player-playerelytraboostevent) | `PlayerElytraBoostEvent` | 2 | 是 |
| [PlayerExpChangeEvent](#event-org-bukkit-event-player-playerexpchangeevent) | `PlayerExpChangeEvent` | 2 | 否 |
| [PlayerFishEvent](#event-org-bukkit-event-player-playerfishevent) | `PlayerFishEvent` | 4 | 是 |
| [PlayerFlowerPotManipulateEvent](#event-io-papermc-paper-event-player-playerflowerpotmanipulateevent) | `PlayerFlowerPotManipulateEvent` | 3 | 是 |
| [PlayerGameModeChangeEvent](#event-org-bukkit-event-player-playergamemodechangeevent) | `PlayerGameModeChangeEvent` | 2 | 是 |
| [PlayerHandshakeEvent](#event-com-destroystokyo-paper-event-player-playerhandshakeevent) | `PlayerHandshakeEvent` | 8 | 是 |
| [PlayerHarvestBlockEvent](#event-org-bukkit-event-player-playerharvestblockevent) | `PlayerHarvestBlockEvent` | 1 | 是 |
| [PlayerInitialSpawnEvent](#event-com-destroystokyo-paper-event-player-playerinitialspawnevent) | `PlayerInitialSpawnEvent` | 1 | 否 |
| [PlayerInteractAtEntityEvent](#event-org-bukkit-event-player-playerinteractatentityevent) | `PlayerInteractAtEntityEvent` | 2 | 是 |
| [PlayerInteractEntityEvent](#event-org-bukkit-event-player-playerinteractentityevent) | `PlayerInteractEntityEvent` | 2 | 是 |
| [PlayerInteractEvent](#event-org-bukkit-event-player-playerinteractevent) | `PlayerInteractEvent` | 8 | 是 |
| [PlayerItemBreakEvent](#event-org-bukkit-event-player-playeritembreakevent) | `PlayerItemBreakEvent` | 1 | 否 |
| [PlayerItemConsumeEvent](#event-org-bukkit-event-player-playeritemconsumeevent) | `PlayerItemConsumeEvent` | 2 | 是 |
| [PlayerItemCooldownEvent](#event-io-papermc-paper-event-player-playeritemcooldownevent) | `PlayerItemCooldownEvent` | 2 | 是 |
| [PlayerItemDamageEvent](#event-org-bukkit-event-player-playeritemdamageevent) | `PlayerItemDamageEvent` | 2 | 是 |
| [PlayerItemHeldEvent](#event-org-bukkit-event-player-playeritemheldevent) | `PlayerItemHeldEvent` | 2 | 是 |
| [PlayerItemMendEvent](#event-org-bukkit-event-player-playeritemmendevent) | `PlayerItemMendEvent` | 3 | 是 |
| [PlayerJoinEvent](#event-org-bukkit-event-player-playerjoinevent) | `join` | 1 | 否 |
| [PlayerJumpEvent](#event-com-destroystokyo-paper-event-player-playerjumpevent) | `PlayerJumpEvent` | 2 | 是 |
| [PlayerKickEvent](#event-org-bukkit-event-player-playerkickevent) | `PlayerKickEvent` | 3 | 是 |
| [PlayerLaunchProjectileEvent](#event-com-destroystokyo-paper-event-player-playerlaunchprojectileevent) | `PlayerLaunchProjectileEvent` | 2 | 是 |
| [PlayerLecternPageChangeEvent](#event-io-papermc-paper-event-player-playerlecternpagechangeevent) | `PlayerLecternPageChangeEvent` | 4 | 是 |
| [PlayerLevelChangeEvent](#event-org-bukkit-event-player-playerlevelchangeevent) | `PlayerLevelChangeEvent` | 2 | 否 |
| [PlayerLocaleChangeEvent](#event-com-destroystokyo-paper-event-player-playerlocalechangeevent) | `PlayerLocaleChangeEvent` | 2 | 否 |
| [PlayerLocaleChangeEvent](#event-org-bukkit-event-player-playerlocalechangeevent) | `PlayerLocaleChangeEvent` | 1 | 否 |
| [PlayerLoginEvent](#event-org-bukkit-event-player-playerloginevent) | `PlayerLoginEvent` | 3 | 否 |
| [PlayerLoomPatternSelectEvent](#event-io-papermc-paper-event-player-playerloompatternselectevent) | `PlayerLoomPatternSelectEvent` | 1 | 是 |
| [PlayerMoveEvent](#event-org-bukkit-event-player-playermoveevent) | `PlayerMoveEvent` | 2 | 是 |
| [PlayerNameEntityEvent](#event-io-papermc-paper-event-player-playernameentityevent) | `PlayerNameEntityEvent` | 2 | 是 |
| [PlayerPickupArrowEvent](#event-org-bukkit-event-player-playerpickuparrowevent) | `PlayerPickupArrowEvent` | 4 | 是 |
| [PlayerPickupExperienceEvent](#event-com-destroystokyo-paper-event-player-playerpickupexperienceevent) | `PlayerPickupExperienceEvent` | 1 | 是 |
| [PlayerPickupItemEvent](#event-org-bukkit-event-player-playerpickupitemevent) | `PlayerPickupItemEvent` | 3 | 是 |
| [PlayerPortalEvent](#event-org-bukkit-event-player-playerportalevent) | `PlayerPortalEvent` | 6 | 是 |
| [PlayerPostRespawnEvent](#event-com-destroystokyo-paper-event-player-playerpostrespawnevent) | `PlayerPostRespawnEvent` | 2 | 否 |
| [PlayerPreLoginEvent](#event-org-bukkit-event-player-playerpreloginevent) | `PlayerPreLoginEvent` | 4 | 否 |
| [PlayerPurchaseEvent](#event-io-papermc-paper-event-player-playerpurchaseevent) | `PlayerPurchaseEvent` | 1 | 是 |
| [PlayerQuitEvent](#event-org-bukkit-event-player-playerquitevent) | `quit` | 2 | 否 |
| [PlayerReadyArrowEvent](#event-com-destroystokyo-paper-event-player-playerreadyarrowevent) | `PlayerReadyArrowEvent` | 2 | 是 |
| [PlayerRecipeBookClickEvent](#event-com-destroystokyo-paper-event-player-playerrecipebookclickevent) | `PlayerRecipeBookClickEvent` | 1 | 是 |
| [PlayerRecipeDiscoverEvent](#event-org-bukkit-event-player-playerrecipediscoverevent) | `PlayerRecipeDiscoverEvent` | 0 | 是 |
| [PlayerRegisterChannelEvent](#event-org-bukkit-event-player-playerregisterchannelevent) | `PlayerRegisterChannelEvent` | 1 | 否 |
| [PlayerResourcePackStatusEvent](#event-org-bukkit-event-player-playerresourcepackstatusevent) | `PlayerResourcePackStatusEvent` | 2 | 否 |
| [PlayerRespawnEvent](#event-org-bukkit-event-player-playerrespawnevent) | `PlayerRespawnEvent` | 3 | 否 |
| [PlayerRiptideEvent](#event-org-bukkit-event-player-playerriptideevent) | `PlayerRiptideEvent` | 1 | 否 |
| [PlayerShearEntityEvent](#event-org-bukkit-event-player-playershearentityevent) | `PlayerShearEntityEvent` | 3 | 是 |
| [PlayerSignCommandPreprocessEvent](#event-io-papermc-paper-event-player-playersigncommandpreprocessevent) | `PlayerSignCommandPreprocessEvent` | 1 | 是 |
| [PlayerStartSpectatingEntityEvent](#event-com-destroystokyo-paper-event-player-playerstartspectatingentityevent) | `PlayerStartSpectatingEntityEvent` | 2 | 是 |
| [PlayerStatisticIncrementEvent](#event-org-bukkit-event-player-playerstatisticincrementevent) | `PlayerStatisticIncrementEvent` | 5 | 是 |
| [PlayerStonecutterRecipeSelectEvent](#event-io-papermc-paper-event-player-playerstonecutterrecipeselectevent) | `PlayerStonecutterRecipeSelectEvent` | 0 | 是 |
| [PlayerStopSpectatingEntityEvent](#event-com-destroystokyo-paper-event-player-playerstopspectatingentityevent) | `PlayerStopSpectatingEntityEvent` | 1 | 是 |
| [PlayerSwapHandItemsEvent](#event-org-bukkit-event-player-playerswaphanditemsevent) | `PlayerSwapHandItemsEvent` | 2 | 是 |
| [PlayerTakeLecternBookEvent](#event-org-bukkit-event-player-playertakelecternbookevent) | `PlayerTakeLecternBookEvent` | 1 | 是 |
| [PlayerTeleportEndGatewayEvent](#event-com-destroystokyo-paper-event-player-playerteleportendgatewayevent) | `PlayerTeleportEndGatewayEvent` | 3 | 是 |
| [PlayerTeleportEvent](#event-org-bukkit-event-player-playerteleportevent) | `PlayerTeleportEvent` | 3 | 是 |
| [PlayerToggleFlightEvent](#event-org-bukkit-event-player-playertoggleflightevent) | `PlayerToggleFlightEvent` | 1 | 是 |
| [PlayerToggleSneakEvent](#event-org-bukkit-event-player-playertogglesneakevent) | `PlayerToggleSneakEvent` | 1 | 是 |
| [PlayerToggleSprintEvent](#event-org-bukkit-event-player-playertogglesprintevent) | `PlayerToggleSprintEvent` | 1 | 是 |
| [PlayerTradeEvent](#event-io-papermc-paper-event-player-playertradeevent) | `PlayerTradeEvent` | 2 | 是 |
| [PlayerUnleashEntityEvent](#event-org-bukkit-event-player-playerunleashentityevent) | `PlayerUnleashEntityEvent` | 4 | 是 |
| [PlayerUnregisterChannelEvent](#event-org-bukkit-event-player-playerunregisterchannelevent) | `PlayerUnregisterChannelEvent` | 1 | 否 |
| [PlayerUseUnknownEntityEvent](#event-com-destroystokyo-paper-event-player-playeruseunknownentityevent) | `PlayerUseUnknownEntityEvent` | 3 | 否 |
| [PlayerVelocityEvent](#event-org-bukkit-event-player-playervelocityevent) | `PlayerVelocityEvent` | 0 | 是 |

<a id="event-io-papermc-paper-event-player-asyncchatevent"></a>
### AsyncChatEvent

- Java 类：`io.papermc.paper.event.player.AsyncChatEvent`；父类：`io.papermc.paper.event.player.AbstractChatEvent`。
- Python 订阅：`@bridge.on("AsyncChatEvent")`；也可使用 `Events.ASYNC_CHAT`。
- 可取消：是；关联玩家：可能有，取决于实际对象。
- [Paper 官方 Javadoc](https://jd.papermc.io/paper/1.16.5/io/papermc/paper/event/player/AsyncChatEvent.html)：事件含义、触发条件和 Java API。

没有可序列化的 `data` 字段；仍会收到通用事件字段。

<a id="event-org-bukkit-event-player-asyncplayerchatevent"></a>
### AsyncPlayerChatEvent

- Java 类：`org.bukkit.event.player.AsyncPlayerChatEvent`；父类：`org.bukkit.event.player.PlayerEvent`。
- Python 订阅：`@bridge.on("chat")`；也可使用 `Events.ASYNC_PLAYER_CHAT`。
- 可取消：是；关联玩家：可能有，取决于实际对象。
- [Paper 官方 Javadoc](https://jd.papermc.io/paper/1.16.5/org/bukkit/event/player/AsyncPlayerChatEvent.html)：事件含义、触发条件和 Java API。

| `data` 字段 | JSON 类型 | Java getter | Java 返回类型 |
| --- | --- | --- | --- |
| `format` | 字符串 | `getFormat()` | `java.lang.String` |
| `message` | 字符串 | `getMessage()` | `java.lang.String` |

<a id="event-org-bukkit-event-player-asyncplayerpreloginevent"></a>
### AsyncPlayerPreLoginEvent

- Java 类：`org.bukkit.event.player.AsyncPlayerPreLoginEvent`；父类：`org.bukkit.event.Event`。
- Python 订阅：`@bridge.on("AsyncPlayerPreLoginEvent")`；也可使用 `Events.ASYNC_PLAYER_PRE_LOGIN`。
- 可取消：否；关联玩家：无已知玩家 getter。
- [Paper 官方 Javadoc](https://jd.papermc.io/paper/1.16.5/org/bukkit/event/player/AsyncPlayerPreLoginEvent.html)：事件含义、触发条件和 Java API。

| `data` 字段 | JSON 类型 | Java getter | Java 返回类型 |
| --- | --- | --- | --- |
| `kickMessage` | 字符串 | `getKickMessage()` | `java.lang.String` |
| `loginResult` | 字符串 | `getLoginResult()` | `org.bukkit.event.player.AsyncPlayerPreLoginEvent$Result` |
| `name` | 字符串 | `getName()` | `java.lang.String` |
| `result` | 字符串 | `getResult()` | `org.bukkit.event.player.PlayerPreLoginEvent$Result` |
| `uniqueId` | 字符串 | `getUniqueId()` | `java.util.UUID` |

<a id="event-io-papermc-paper-event-player-chatevent"></a>
### ChatEvent

- Java 类：`io.papermc.paper.event.player.ChatEvent`；父类：`io.papermc.paper.event.player.AbstractChatEvent`。
- Python 订阅：`@bridge.on("ChatEvent")`；也可使用 `Events.CHAT`。
- 可取消：是；关联玩家：可能有，取决于实际对象。
- [Paper 官方 Javadoc](https://jd.papermc.io/paper/1.16.5/io/papermc/paper/event/player/ChatEvent.html)：事件含义、触发条件和 Java API。

没有可序列化的 `data` 字段；仍会收到通用事件字段。

<a id="event-com-destroystokyo-paper-event-player-illegalpacketevent"></a>
### IllegalPacketEvent

- Java 类：`com.destroystokyo.paper.event.player.IllegalPacketEvent`；父类：`org.bukkit.event.player.PlayerEvent`。
- Python 订阅：`@bridge.on("IllegalPacketEvent")`；也可使用 `Events.ILLEGAL_PACKET`。
- 可取消：否；关联玩家：可能有，取决于实际对象。
- [Paper 官方 Javadoc](https://jd.papermc.io/paper/1.16.5/com/destroystokyo/paper/event/player/IllegalPacketEvent.html)：事件含义、触发条件和 Java API。

| `data` 字段 | JSON 类型 | Java getter | Java 返回类型 |
| --- | --- | --- | --- |
| `exceptionMessage` | 字符串 | `getExceptionMessage()` | `java.lang.String` |
| `kickMessage` | 字符串 | `getKickMessage()` | `java.lang.String` |
| `type` | 字符串 | `getType()` | `java.lang.String` |
| `shouldKick` | 布尔值 | `isShouldKick()` | `boolean` |

<a id="event-com-destroystokyo-paper-event-player-playeradvancementcriteriongrantevent"></a>
### PlayerAdvancementCriterionGrantEvent

- Java 类：`com.destroystokyo.paper.event.player.PlayerAdvancementCriterionGrantEvent`；父类：`org.bukkit.event.player.PlayerEvent`。
- Python 订阅：`@bridge.on("PlayerAdvancementCriterionGrantEvent")`；也可使用 `Events.PLAYER_ADVANCEMENT_CRITERION_GRANT`。
- 可取消：是；关联玩家：可能有，取决于实际对象。
- [Paper 官方 Javadoc](https://jd.papermc.io/paper/1.16.5/com/destroystokyo/paper/event/player/PlayerAdvancementCriterionGrantEvent.html)：事件含义、触发条件和 Java API。

| `data` 字段 | JSON 类型 | Java getter | Java 返回类型 |
| --- | --- | --- | --- |
| `criterion` | 字符串 | `getCriterion()` | `java.lang.String` |

<a id="event-org-bukkit-event-player-playeradvancementdoneevent"></a>
### PlayerAdvancementDoneEvent

- Java 类：`org.bukkit.event.player.PlayerAdvancementDoneEvent`；父类：`org.bukkit.event.player.PlayerEvent`。
- Python 订阅：`@bridge.on("PlayerAdvancementDoneEvent")`；也可使用 `Events.PLAYER_ADVANCEMENT_DONE`。
- 可取消：否；关联玩家：可能有，取决于实际对象。
- [Paper 官方 Javadoc](https://jd.papermc.io/paper/1.16.5/org/bukkit/event/player/PlayerAdvancementDoneEvent.html)：事件含义、触发条件和 Java API。

没有可序列化的 `data` 字段；仍会收到通用事件字段。

<a id="event-org-bukkit-event-player-playeranimationevent"></a>
### PlayerAnimationEvent

- Java 类：`org.bukkit.event.player.PlayerAnimationEvent`；父类：`org.bukkit.event.player.PlayerEvent`。
- Python 订阅：`@bridge.on("PlayerAnimationEvent")`；也可使用 `Events.PLAYER_ANIMATION`。
- 可取消：是；关联玩家：可能有，取决于实际对象。
- [Paper 官方 Javadoc](https://jd.papermc.io/paper/1.16.5/org/bukkit/event/player/PlayerAnimationEvent.html)：事件含义、触发条件和 Java API。

| `data` 字段 | JSON 类型 | Java getter | Java 返回类型 |
| --- | --- | --- | --- |
| `animationType` | 字符串 | `getAnimationType()` | `org.bukkit.event.player.PlayerAnimationType` |

<a id="event-com-destroystokyo-paper-event-player-playerarmorchangeevent"></a>
### PlayerArmorChangeEvent

- Java 类：`com.destroystokyo.paper.event.player.PlayerArmorChangeEvent`；父类：`org.bukkit.event.player.PlayerEvent`。
- Python 订阅：`@bridge.on("PlayerArmorChangeEvent")`；也可使用 `Events.PLAYER_ARMOR_CHANGE`。
- 可取消：否；关联玩家：可能有，取决于实际对象。
- [Paper 官方 Javadoc](https://jd.papermc.io/paper/1.16.5/com/destroystokyo/paper/event/player/PlayerArmorChangeEvent.html)：事件含义、触发条件和 Java API。

| `data` 字段 | JSON 类型 | Java getter | Java 返回类型 |
| --- | --- | --- | --- |
| `newItem` | 物品摘要 | `getNewItem()` | `org.bukkit.inventory.ItemStack` |
| `oldItem` | 物品摘要 | `getOldItem()` | `org.bukkit.inventory.ItemStack` |
| `slotType` | 字符串 | `getSlotType()` | `com.destroystokyo.paper.event.player.PlayerArmorChangeEvent$SlotType` |

<a id="event-org-bukkit-event-player-playerarmorstandmanipulateevent"></a>
### PlayerArmorStandManipulateEvent

- Java 类：`org.bukkit.event.player.PlayerArmorStandManipulateEvent`；父类：`org.bukkit.event.player.PlayerInteractEntityEvent`。
- Python 订阅：`@bridge.on("PlayerArmorStandManipulateEvent")`；也可使用 `Events.PLAYER_ARMOR_STAND_MANIPULATE`。
- 可取消：是；关联玩家：可能有，取决于实际对象。
- [Paper 官方 Javadoc](https://jd.papermc.io/paper/1.16.5/org/bukkit/event/player/PlayerArmorStandManipulateEvent.html)：事件含义、触发条件和 Java API。

| `data` 字段 | JSON 类型 | Java getter | Java 返回类型 |
| --- | --- | --- | --- |
| `armorStandItem` | 物品摘要 | `getArmorStandItem()` | `org.bukkit.inventory.ItemStack` |
| `hand` | 字符串 | `getHand()` | `org.bukkit.inventory.EquipmentSlot` |
| `playerItem` | 物品摘要 | `getPlayerItem()` | `org.bukkit.inventory.ItemStack` |
| `rightClicked` | 实体摘要 | `getRightClicked()` | `org.bukkit.entity.ArmorStand` |
| `slot` | 字符串 | `getSlot()` | `org.bukkit.inventory.EquipmentSlot` |

<a id="event-io-papermc-paper-event-player-playerarmswingevent"></a>
### PlayerArmSwingEvent

- Java 类：`io.papermc.paper.event.player.PlayerArmSwingEvent`；父类：`org.bukkit.event.player.PlayerAnimationEvent`。
- Python 订阅：`@bridge.on("PlayerArmSwingEvent")`；也可使用 `Events.PLAYER_ARM_SWING`。
- 可取消：是；关联玩家：可能有，取决于实际对象。
- [Paper 官方 Javadoc](https://jd.papermc.io/paper/1.16.5/io/papermc/paper/event/player/PlayerArmSwingEvent.html)：事件含义、触发条件和 Java API。

| `data` 字段 | JSON 类型 | Java getter | Java 返回类型 |
| --- | --- | --- | --- |
| `animationType` | 字符串 | `getAnimationType()` | `org.bukkit.event.player.PlayerAnimationType` |
| `hand` | 字符串 | `getHand()` | `org.bukkit.inventory.EquipmentSlot` |

<a id="event-com-destroystokyo-paper-event-player-playerattackentitycooldownresetevent"></a>
### PlayerAttackEntityCooldownResetEvent

- Java 类：`com.destroystokyo.paper.event.player.PlayerAttackEntityCooldownResetEvent`；父类：`org.bukkit.event.player.PlayerEvent`。
- Python 订阅：`@bridge.on("PlayerAttackEntityCooldownResetEvent")`；也可使用 `Events.PLAYER_ATTACK_ENTITY_COOLDOWN_RESET`。
- 可取消：是；关联玩家：可能有，取决于实际对象。
- [Paper 官方 Javadoc](https://jd.papermc.io/paper/1.16.5/com/destroystokyo/paper/event/player/PlayerAttackEntityCooldownResetEvent.html)：事件含义、触发条件和 Java API。

| `data` 字段 | JSON 类型 | Java getter | Java 返回类型 |
| --- | --- | --- | --- |
| `attackedEntity` | 实体摘要 | `getAttackedEntity()` | `org.bukkit.entity.Entity` |
| `cooledAttackStrength` | 数字 | `getCooledAttackStrength()` | `float` |

<a id="event-org-bukkit-event-player-playerattemptpickupitemevent"></a>
### PlayerAttemptPickupItemEvent

- Java 类：`org.bukkit.event.player.PlayerAttemptPickupItemEvent`；父类：`org.bukkit.event.player.PlayerEvent`。
- Python 订阅：`@bridge.on("PlayerAttemptPickupItemEvent")`；也可使用 `Events.PLAYER_ATTEMPT_PICKUP_ITEM`。
- 可取消：是；关联玩家：可能有，取决于实际对象。
- [Paper 官方 Javadoc](https://jd.papermc.io/paper/1.16.5/org/bukkit/event/player/PlayerAttemptPickupItemEvent.html)：事件含义、触发条件和 Java API。

| `data` 字段 | JSON 类型 | Java getter | Java 返回类型 |
| --- | --- | --- | --- |
| `flyAtPlayer` | 布尔值 | `getFlyAtPlayer()` | `boolean` |
| `item` | 实体摘要 | `getItem()` | `org.bukkit.entity.Item` |
| `remaining` | 数字 | `getRemaining()` | `int` |

<a id="event-org-bukkit-event-player-playerbedenterevent"></a>
### PlayerBedEnterEvent

- Java 类：`org.bukkit.event.player.PlayerBedEnterEvent`；父类：`org.bukkit.event.player.PlayerEvent`。
- Python 订阅：`@bridge.on("PlayerBedEnterEvent")`；也可使用 `Events.PLAYER_BED_ENTER`。
- 可取消：是；关联玩家：可能有，取决于实际对象。
- [Paper 官方 Javadoc](https://jd.papermc.io/paper/1.16.5/org/bukkit/event/player/PlayerBedEnterEvent.html)：事件含义、触发条件和 Java API。

| `data` 字段 | JSON 类型 | Java getter | Java 返回类型 |
| --- | --- | --- | --- |
| `bed` | 方块摘要 | `getBed()` | `org.bukkit.block.Block` |
| `bedEnterResult` | 字符串 | `getBedEnterResult()` | `org.bukkit.event.player.PlayerBedEnterEvent$BedEnterResult` |

<a id="event-io-papermc-paper-event-player-playerbedfailenterevent"></a>
### PlayerBedFailEnterEvent

- Java 类：`io.papermc.paper.event.player.PlayerBedFailEnterEvent`；父类：`org.bukkit.event.player.PlayerEvent`。
- Python 订阅：`@bridge.on("PlayerBedFailEnterEvent")`；也可使用 `Events.PLAYER_BED_FAIL_ENTER`。
- 可取消：是；关联玩家：可能有，取决于实际对象。
- [Paper 官方 Javadoc](https://jd.papermc.io/paper/1.16.5/io/papermc/paper/event/player/PlayerBedFailEnterEvent.html)：事件含义、触发条件和 Java API。

| `data` 字段 | JSON 类型 | Java getter | Java 返回类型 |
| --- | --- | --- | --- |
| `bed` | 方块摘要 | `getBed()` | `org.bukkit.block.Block` |
| `failReason` | 字符串 | `getFailReason()` | `io.papermc.paper.event.player.PlayerBedFailEnterEvent$FailReason` |
| `willExplode` | 布尔值 | `getWillExplode()` | `boolean` |

<a id="event-org-bukkit-event-player-playerbedleaveevent"></a>
### PlayerBedLeaveEvent

- Java 类：`org.bukkit.event.player.PlayerBedLeaveEvent`；父类：`org.bukkit.event.player.PlayerEvent`。
- Python 订阅：`@bridge.on("PlayerBedLeaveEvent")`；也可使用 `Events.PLAYER_BED_LEAVE`。
- 可取消：是；关联玩家：可能有，取决于实际对象。
- [Paper 官方 Javadoc](https://jd.papermc.io/paper/1.16.5/org/bukkit/event/player/PlayerBedLeaveEvent.html)：事件含义、触发条件和 Java API。

| `data` 字段 | JSON 类型 | Java getter | Java 返回类型 |
| --- | --- | --- | --- |
| `bed` | 方块摘要 | `getBed()` | `org.bukkit.block.Block` |

<a id="event-org-bukkit-event-player-playerbucketemptyevent"></a>
### PlayerBucketEmptyEvent

- Java 类：`org.bukkit.event.player.PlayerBucketEmptyEvent`；父类：`org.bukkit.event.player.PlayerBucketEvent`。
- Python 订阅：`@bridge.on("PlayerBucketEmptyEvent")`；也可使用 `Events.PLAYER_BUCKET_EMPTY`。
- 可取消：是；关联玩家：可能有，取决于实际对象。
- [Paper 官方 Javadoc](https://jd.papermc.io/paper/1.16.5/org/bukkit/event/player/PlayerBucketEmptyEvent.html)：事件含义、触发条件和 Java API。

| `data` 字段 | JSON 类型 | Java getter | Java 返回类型 |
| --- | --- | --- | --- |
| `block` | 方块摘要 | `getBlock()` | `org.bukkit.block.Block` |
| `blockClicked` | 方块摘要 | `getBlockClicked()` | `org.bukkit.block.Block` |
| `blockFace` | 字符串 | `getBlockFace()` | `org.bukkit.block.BlockFace` |
| `bucket` | 字符串 | `getBucket()` | `org.bukkit.Material` |
| `hand` | 字符串 | `getHand()` | `org.bukkit.inventory.EquipmentSlot` |
| `itemStack` | 物品摘要 | `getItemStack()` | `org.bukkit.inventory.ItemStack` |

<a id="event-org-bukkit-event-player-playerbucketentityevent"></a>
### PlayerBucketEntityEvent

- Java 类：`org.bukkit.event.player.PlayerBucketEntityEvent`；父类：`org.bukkit.event.player.PlayerEvent`。
- Python 订阅：`@bridge.on("PlayerBucketEntityEvent")`；也可使用 `Events.PLAYER_BUCKET_ENTITY`。
- 可取消：是；关联玩家：可能有，取决于实际对象。
- [Paper 官方 Javadoc](https://jd.papermc.io/paper/1.16.5/org/bukkit/event/player/PlayerBucketEntityEvent.html)：事件含义、触发条件和 Java API。

| `data` 字段 | JSON 类型 | Java getter | Java 返回类型 |
| --- | --- | --- | --- |
| `entity` | 实体摘要 | `getEntity()` | `org.bukkit.entity.Entity` |
| `entityBucket` | 物品摘要 | `getEntityBucket()` | `org.bukkit.inventory.ItemStack` |
| `originalBucket` | 物品摘要 | `getOriginalBucket()` | `org.bukkit.inventory.ItemStack` |

<a id="event-org-bukkit-event-player-playerbucketfillevent"></a>
### PlayerBucketFillEvent

- Java 类：`org.bukkit.event.player.PlayerBucketFillEvent`；父类：`org.bukkit.event.player.PlayerBucketEvent`。
- Python 订阅：`@bridge.on("PlayerBucketFillEvent")`；也可使用 `Events.PLAYER_BUCKET_FILL`。
- 可取消：是；关联玩家：可能有，取决于实际对象。
- [Paper 官方 Javadoc](https://jd.papermc.io/paper/1.16.5/org/bukkit/event/player/PlayerBucketFillEvent.html)：事件含义、触发条件和 Java API。

| `data` 字段 | JSON 类型 | Java getter | Java 返回类型 |
| --- | --- | --- | --- |
| `block` | 方块摘要 | `getBlock()` | `org.bukkit.block.Block` |
| `blockClicked` | 方块摘要 | `getBlockClicked()` | `org.bukkit.block.Block` |
| `blockFace` | 字符串 | `getBlockFace()` | `org.bukkit.block.BlockFace` |
| `bucket` | 字符串 | `getBucket()` | `org.bukkit.Material` |
| `hand` | 字符串 | `getHand()` | `org.bukkit.inventory.EquipmentSlot` |
| `itemStack` | 物品摘要 | `getItemStack()` | `org.bukkit.inventory.ItemStack` |

<a id="event-org-bukkit-event-player-playerbucketfishevent"></a>
### PlayerBucketFishEvent

- Java 类：`org.bukkit.event.player.PlayerBucketFishEvent`；父类：`org.bukkit.event.player.PlayerBucketEntityEvent`。
- Python 订阅：`@bridge.on("PlayerBucketFishEvent")`；也可使用 `Events.PLAYER_BUCKET_FISH`。
- 可取消：是；关联玩家：可能有，取决于实际对象。
- [Paper 官方 Javadoc](https://jd.papermc.io/paper/1.16.5/org/bukkit/event/player/PlayerBucketFishEvent.html)：事件含义、触发条件和 Java API。

| `data` 字段 | JSON 类型 | Java getter | Java 返回类型 |
| --- | --- | --- | --- |
| `entity` | 实体摘要 | `getEntity()` | `org.bukkit.entity.Fish` |
| `entityBucket` | 物品摘要 | `getEntityBucket()` | `org.bukkit.inventory.ItemStack` |
| `fishBucket` | 物品摘要 | `getFishBucket()` | `org.bukkit.inventory.ItemStack` |
| `originalBucket` | 物品摘要 | `getOriginalBucket()` | `org.bukkit.inventory.ItemStack` |
| `waterBucket` | 物品摘要 | `getWaterBucket()` | `org.bukkit.inventory.ItemStack` |

<a id="event-io-papermc-paper-event-player-playerchangebeaconeffectevent"></a>
### PlayerChangeBeaconEffectEvent

- Java 类：`io.papermc.paper.event.player.PlayerChangeBeaconEffectEvent`；父类：`org.bukkit.event.player.PlayerEvent`。
- Python 订阅：`@bridge.on("PlayerChangeBeaconEffectEvent")`；也可使用 `Events.PLAYER_CHANGE_BEACON_EFFECT`。
- 可取消：是；关联玩家：可能有，取决于实际对象。
- [Paper 官方 Javadoc](https://jd.papermc.io/paper/1.16.5/io/papermc/paper/event/player/PlayerChangeBeaconEffectEvent.html)：事件含义、触发条件和 Java API。

| `data` 字段 | JSON 类型 | Java getter | Java 返回类型 |
| --- | --- | --- | --- |
| `beacon` | 方块摘要 | `getBeacon()` | `org.bukkit.block.Block` |

<a id="event-org-bukkit-event-player-playerchangedmainhandevent"></a>
### PlayerChangedMainHandEvent

- Java 类：`org.bukkit.event.player.PlayerChangedMainHandEvent`；父类：`org.bukkit.event.player.PlayerEvent`。
- Python 订阅：`@bridge.on("PlayerChangedMainHandEvent")`；也可使用 `Events.PLAYER_CHANGED_MAIN_HAND`。
- 可取消：否；关联玩家：可能有，取决于实际对象。
- [Paper 官方 Javadoc](https://jd.papermc.io/paper/1.16.5/org/bukkit/event/player/PlayerChangedMainHandEvent.html)：事件含义、触发条件和 Java API。

| `data` 字段 | JSON 类型 | Java getter | Java 返回类型 |
| --- | --- | --- | --- |
| `mainHand` | 字符串 | `getMainHand()` | `org.bukkit.inventory.MainHand` |

<a id="event-org-bukkit-event-player-playerchangedworldevent"></a>
### PlayerChangedWorldEvent

- Java 类：`org.bukkit.event.player.PlayerChangedWorldEvent`；父类：`org.bukkit.event.player.PlayerEvent`。
- Python 订阅：`@bridge.on("PlayerChangedWorldEvent")`；也可使用 `Events.PLAYER_CHANGED_WORLD`。
- 可取消：否；关联玩家：可能有，取决于实际对象。
- [Paper 官方 Javadoc](https://jd.papermc.io/paper/1.16.5/org/bukkit/event/player/PlayerChangedWorldEvent.html)：事件含义、触发条件和 Java API。

| `data` 字段 | JSON 类型 | Java getter | Java 返回类型 |
| --- | --- | --- | --- |
| `from` | 世界摘要 | `getFrom()` | `org.bukkit.World` |

<a id="event-org-bukkit-event-player-playerchatevent"></a>
### PlayerChatEvent

- Java 类：`org.bukkit.event.player.PlayerChatEvent`；父类：`org.bukkit.event.player.PlayerEvent`。
- Python 订阅：`@bridge.on("PlayerChatEvent")`；也可使用 `Events.PLAYER_CHAT`。
- 可取消：是；关联玩家：可能有，取决于实际对象。
- [Paper 官方 Javadoc](https://jd.papermc.io/paper/1.16.5/org/bukkit/event/player/PlayerChatEvent.html)：事件含义、触发条件和 Java API。

| `data` 字段 | JSON 类型 | Java getter | Java 返回类型 |
| --- | --- | --- | --- |
| `format` | 字符串 | `getFormat()` | `java.lang.String` |
| `message` | 字符串 | `getMessage()` | `java.lang.String` |

<a id="event-org-bukkit-event-player-playerchattabcompleteevent"></a>
### PlayerChatTabCompleteEvent

- Java 类：`org.bukkit.event.player.PlayerChatTabCompleteEvent`；父类：`org.bukkit.event.player.PlayerEvent`。
- Python 订阅：`@bridge.on("PlayerChatTabCompleteEvent")`；也可使用 `Events.PLAYER_CHAT_TAB_COMPLETE`。
- 可取消：否；关联玩家：可能有，取决于实际对象。
- [Paper 官方 Javadoc](https://jd.papermc.io/paper/1.16.5/org/bukkit/event/player/PlayerChatTabCompleteEvent.html)：事件含义、触发条件和 Java API。

| `data` 字段 | JSON 类型 | Java getter | Java 返回类型 |
| --- | --- | --- | --- |
| `chatMessage` | 字符串 | `getChatMessage()` | `java.lang.String` |
| `lastToken` | 字符串 | `getLastToken()` | `java.lang.String` |

<a id="event-com-destroystokyo-paper-event-player-playerclientoptionschangeevent"></a>
### PlayerClientOptionsChangeEvent

- Java 类：`com.destroystokyo.paper.event.player.PlayerClientOptionsChangeEvent`；父类：`org.bukkit.event.player.PlayerEvent`。
- Python 订阅：`@bridge.on("PlayerClientOptionsChangeEvent")`；也可使用 `Events.PLAYER_CLIENT_OPTIONS_CHANGE`。
- 可取消：否；关联玩家：可能有，取决于实际对象。
- [Paper 官方 Javadoc](https://jd.papermc.io/paper/1.16.5/com/destroystokyo/paper/event/player/PlayerClientOptionsChangeEvent.html)：事件含义、触发条件和 Java API。

| `data` 字段 | JSON 类型 | Java getter | Java 返回类型 |
| --- | --- | --- | --- |
| `chatVisibility` | 字符串 | `getChatVisibility()` | `com.destroystokyo.paper.ClientOption$ChatVisibility` |
| `locale` | 字符串 | `getLocale()` | `java.lang.String` |
| `mainHand` | 字符串 | `getMainHand()` | `org.bukkit.inventory.MainHand` |
| `viewDistance` | 数字 | `getViewDistance()` | `int` |

<a id="event-org-bukkit-event-player-playercommandpreprocessevent"></a>
### PlayerCommandPreprocessEvent

- Java 类：`org.bukkit.event.player.PlayerCommandPreprocessEvent`；父类：`org.bukkit.event.player.PlayerEvent`。
- Python 订阅：`@bridge.on("PlayerCommandPreprocessEvent")`；也可使用 `Events.PLAYER_COMMAND_PREPROCESS`。
- 可取消：是；关联玩家：可能有，取决于实际对象。
- [Paper 官方 Javadoc](https://jd.papermc.io/paper/1.16.5/org/bukkit/event/player/PlayerCommandPreprocessEvent.html)：事件含义、触发条件和 Java API。

| `data` 字段 | JSON 类型 | Java getter | Java 返回类型 |
| --- | --- | --- | --- |
| `message` | 字符串 | `getMessage()` | `java.lang.String` |

<a id="event-org-bukkit-event-player-playercommandsendevent"></a>
### PlayerCommandSendEvent

- Java 类：`org.bukkit.event.player.PlayerCommandSendEvent`；父类：`org.bukkit.event.player.PlayerEvent`。
- Python 订阅：`@bridge.on("PlayerCommandSendEvent")`；也可使用 `Events.PLAYER_COMMAND_SEND`。
- 可取消：否；关联玩家：可能有，取决于实际对象。
- [Paper 官方 Javadoc](https://jd.papermc.io/paper/1.16.5/org/bukkit/event/player/PlayerCommandSendEvent.html)：事件含义、触发条件和 Java API。

没有可序列化的 `data` 字段；仍会收到通用事件字段。

<a id="event-com-destroystokyo-paper-event-player-playerconnectioncloseevent"></a>
### PlayerConnectionCloseEvent

- Java 类：`com.destroystokyo.paper.event.player.PlayerConnectionCloseEvent`；父类：`org.bukkit.event.Event`。
- Python 订阅：`@bridge.on("PlayerConnectionCloseEvent")`；也可使用 `Events.PLAYER_CONNECTION_CLOSE`。
- 可取消：否；关联玩家：无已知玩家 getter。
- [Paper 官方 Javadoc](https://jd.papermc.io/paper/1.16.5/com/destroystokyo/paper/event/player/PlayerConnectionCloseEvent.html)：事件含义、触发条件和 Java API。

| `data` 字段 | JSON 类型 | Java getter | Java 返回类型 |
| --- | --- | --- | --- |
| `playerName` | 字符串 | `getPlayerName()` | `java.lang.String` |
| `playerUniqueId` | 字符串 | `getPlayerUniqueId()` | `java.util.UUID` |

<a id="event-io-papermc-paper-event-player-playerdeepsleepevent"></a>
### PlayerDeepSleepEvent

- Java 类：`io.papermc.paper.event.player.PlayerDeepSleepEvent`；父类：`org.bukkit.event.player.PlayerEvent`。
- Python 订阅：`@bridge.on("PlayerDeepSleepEvent")`；也可使用 `Events.PLAYER_DEEP_SLEEP`。
- 可取消：是；关联玩家：可能有，取决于实际对象。
- [Paper 官方 Javadoc](https://jd.papermc.io/paper/1.16.5/io/papermc/paper/event/player/PlayerDeepSleepEvent.html)：事件含义、触发条件和 Java API。

没有可序列化的 `data` 字段；仍会收到通用事件字段。

<a id="event-org-bukkit-event-player-playerdropitemevent"></a>
### PlayerDropItemEvent

- Java 类：`org.bukkit.event.player.PlayerDropItemEvent`；父类：`org.bukkit.event.player.PlayerEvent`。
- Python 订阅：`@bridge.on("PlayerDropItemEvent")`；也可使用 `Events.PLAYER_DROP_ITEM`。
- 可取消：是；关联玩家：可能有，取决于实际对象。
- [Paper 官方 Javadoc](https://jd.papermc.io/paper/1.16.5/org/bukkit/event/player/PlayerDropItemEvent.html)：事件含义、触发条件和 Java API。

| `data` 字段 | JSON 类型 | Java getter | Java 返回类型 |
| --- | --- | --- | --- |
| `itemDrop` | 实体摘要 | `getItemDrop()` | `org.bukkit.entity.Item` |

<a id="event-org-bukkit-event-player-playereditbookevent"></a>
### PlayerEditBookEvent

- Java 类：`org.bukkit.event.player.PlayerEditBookEvent`；父类：`org.bukkit.event.player.PlayerEvent`。
- Python 订阅：`@bridge.on("PlayerEditBookEvent")`；也可使用 `Events.PLAYER_EDIT_BOOK`。
- 可取消：是；关联玩家：可能有，取决于实际对象。
- [Paper 官方 Javadoc](https://jd.papermc.io/paper/1.16.5/org/bukkit/event/player/PlayerEditBookEvent.html)：事件含义、触发条件和 Java API。

| `data` 字段 | JSON 类型 | Java getter | Java 返回类型 |
| --- | --- | --- | --- |
| `slot` | 数字 | `getSlot()` | `int` |
| `signing` | 布尔值 | `isSigning()` | `boolean` |

<a id="event-org-bukkit-event-player-playereggthrowevent"></a>
### PlayerEggThrowEvent

- Java 类：`org.bukkit.event.player.PlayerEggThrowEvent`；父类：`org.bukkit.event.player.PlayerEvent`。
- Python 订阅：`@bridge.on("PlayerEggThrowEvent")`；也可使用 `Events.PLAYER_EGG_THROW`。
- 可取消：否；关联玩家：可能有，取决于实际对象。
- [Paper 官方 Javadoc](https://jd.papermc.io/paper/1.16.5/org/bukkit/event/player/PlayerEggThrowEvent.html)：事件含义、触发条件和 Java API。

| `data` 字段 | JSON 类型 | Java getter | Java 返回类型 |
| --- | --- | --- | --- |
| `egg` | 实体摘要 | `getEgg()` | `org.bukkit.entity.Egg` |
| `hatchingType` | 字符串 | `getHatchingType()` | `org.bukkit.entity.EntityType` |
| `numHatches` | 数字 | `getNumHatches()` | `byte` |
| `hatching` | 布尔值 | `isHatching()` | `boolean` |

<a id="event-com-destroystokyo-paper-event-player-playerelytraboostevent"></a>
### PlayerElytraBoostEvent

- Java 类：`com.destroystokyo.paper.event.player.PlayerElytraBoostEvent`；父类：`org.bukkit.event.player.PlayerEvent`。
- Python 订阅：`@bridge.on("PlayerElytraBoostEvent")`；也可使用 `Events.PLAYER_ELYTRA_BOOST`。
- 可取消：是；关联玩家：可能有，取决于实际对象。
- [Paper 官方 Javadoc](https://jd.papermc.io/paper/1.16.5/com/destroystokyo/paper/event/player/PlayerElytraBoostEvent.html)：事件含义、触发条件和 Java API。

| `data` 字段 | JSON 类型 | Java getter | Java 返回类型 |
| --- | --- | --- | --- |
| `firework` | 实体摘要 | `getFirework()` | `org.bukkit.entity.Firework` |
| `itemStack` | 物品摘要 | `getItemStack()` | `org.bukkit.inventory.ItemStack` |

<a id="event-org-bukkit-event-player-playerexpchangeevent"></a>
### PlayerExpChangeEvent

- Java 类：`org.bukkit.event.player.PlayerExpChangeEvent`；父类：`org.bukkit.event.player.PlayerEvent`。
- Python 订阅：`@bridge.on("PlayerExpChangeEvent")`；也可使用 `Events.PLAYER_EXP_CHANGE`。
- 可取消：否；关联玩家：可能有，取决于实际对象。
- [Paper 官方 Javadoc](https://jd.papermc.io/paper/1.16.5/org/bukkit/event/player/PlayerExpChangeEvent.html)：事件含义、触发条件和 Java API。

| `data` 字段 | JSON 类型 | Java getter | Java 返回类型 |
| --- | --- | --- | --- |
| `amount` | 数字 | `getAmount()` | `int` |
| `source` | 实体摘要 | `getSource()` | `org.bukkit.entity.Entity` |

<a id="event-org-bukkit-event-player-playerfishevent"></a>
### PlayerFishEvent

- Java 类：`org.bukkit.event.player.PlayerFishEvent`；父类：`org.bukkit.event.player.PlayerEvent`。
- Python 订阅：`@bridge.on("PlayerFishEvent")`；也可使用 `Events.PLAYER_FISH`。
- 可取消：是；关联玩家：可能有，取决于实际对象。
- [Paper 官方 Javadoc](https://jd.papermc.io/paper/1.16.5/org/bukkit/event/player/PlayerFishEvent.html)：事件含义、触发条件和 Java API。

| `data` 字段 | JSON 类型 | Java getter | Java 返回类型 |
| --- | --- | --- | --- |
| `caught` | 实体摘要 | `getCaught()` | `org.bukkit.entity.Entity` |
| `expToDrop` | 数字 | `getExpToDrop()` | `int` |
| `hook` | 实体摘要 | `getHook()` | `org.bukkit.entity.FishHook` |
| `state` | 字符串 | `getState()` | `org.bukkit.event.player.PlayerFishEvent$State` |

<a id="event-io-papermc-paper-event-player-playerflowerpotmanipulateevent"></a>
### PlayerFlowerPotManipulateEvent

- Java 类：`io.papermc.paper.event.player.PlayerFlowerPotManipulateEvent`；父类：`org.bukkit.event.player.PlayerEvent`。
- Python 订阅：`@bridge.on("PlayerFlowerPotManipulateEvent")`；也可使用 `Events.PLAYER_FLOWER_POT_MANIPULATE`。
- 可取消：是；关联玩家：可能有，取决于实际对象。
- [Paper 官方 Javadoc](https://jd.papermc.io/paper/1.16.5/io/papermc/paper/event/player/PlayerFlowerPotManipulateEvent.html)：事件含义、触发条件和 Java API。

| `data` 字段 | JSON 类型 | Java getter | Java 返回类型 |
| --- | --- | --- | --- |
| `flowerpot` | 方块摘要 | `getFlowerpot()` | `org.bukkit.block.Block` |
| `item` | 物品摘要 | `getItem()` | `org.bukkit.inventory.ItemStack` |
| `placing` | 布尔值 | `isPlacing()` | `boolean` |

<a id="event-org-bukkit-event-player-playergamemodechangeevent"></a>
### PlayerGameModeChangeEvent

- Java 类：`org.bukkit.event.player.PlayerGameModeChangeEvent`；父类：`org.bukkit.event.player.PlayerEvent`。
- Python 订阅：`@bridge.on("PlayerGameModeChangeEvent")`；也可使用 `Events.PLAYER_GAME_MODE_CHANGE`。
- 可取消：是；关联玩家：可能有，取决于实际对象。
- [Paper 官方 Javadoc](https://jd.papermc.io/paper/1.16.5/org/bukkit/event/player/PlayerGameModeChangeEvent.html)：事件含义、触发条件和 Java API。

| `data` 字段 | JSON 类型 | Java getter | Java 返回类型 |
| --- | --- | --- | --- |
| `cause` | 字符串 | `getCause()` | `org.bukkit.event.player.PlayerGameModeChangeEvent$Cause` |
| `newGameMode` | 字符串 | `getNewGameMode()` | `org.bukkit.GameMode` |

<a id="event-com-destroystokyo-paper-event-player-playerhandshakeevent"></a>
### PlayerHandshakeEvent

- Java 类：`com.destroystokyo.paper.event.player.PlayerHandshakeEvent`；父类：`org.bukkit.event.Event`。
- Python 订阅：`@bridge.on("PlayerHandshakeEvent")`；也可使用 `Events.PLAYER_HANDSHAKE`。
- 可取消：是；关联玩家：无已知玩家 getter。
- [Paper 官方 Javadoc](https://jd.papermc.io/paper/1.16.5/com/destroystokyo/paper/event/player/PlayerHandshakeEvent.html)：事件含义、触发条件和 Java API。

| `data` 字段 | JSON 类型 | Java getter | Java 返回类型 |
| --- | --- | --- | --- |
| `failMessage` | 字符串 | `getFailMessage()` | `java.lang.String` |
| `originalHandshake` | 字符串 | `getOriginalHandshake()` | `java.lang.String` |
| `originalSocketAddressHostname` | 字符串 | `getOriginalSocketAddressHostname()` | `java.lang.String` |
| `propertiesJson` | 字符串 | `getPropertiesJson()` | `java.lang.String` |
| `serverHostname` | 字符串 | `getServerHostname()` | `java.lang.String` |
| `socketAddressHostname` | 字符串 | `getSocketAddressHostname()` | `java.lang.String` |
| `uniqueId` | 字符串 | `getUniqueId()` | `java.util.UUID` |
| `failed` | 布尔值 | `isFailed()` | `boolean` |

<a id="event-org-bukkit-event-player-playerharvestblockevent"></a>
### PlayerHarvestBlockEvent

- Java 类：`org.bukkit.event.player.PlayerHarvestBlockEvent`；父类：`org.bukkit.event.player.PlayerEvent`。
- Python 订阅：`@bridge.on("PlayerHarvestBlockEvent")`；也可使用 `Events.PLAYER_HARVEST_BLOCK`。
- 可取消：是；关联玩家：可能有，取决于实际对象。
- [Paper 官方 Javadoc](https://jd.papermc.io/paper/1.16.5/org/bukkit/event/player/PlayerHarvestBlockEvent.html)：事件含义、触发条件和 Java API。

| `data` 字段 | JSON 类型 | Java getter | Java 返回类型 |
| --- | --- | --- | --- |
| `harvestedBlock` | 方块摘要 | `getHarvestedBlock()` | `org.bukkit.block.Block` |

<a id="event-com-destroystokyo-paper-event-player-playerinitialspawnevent"></a>
### PlayerInitialSpawnEvent

- Java 类：`com.destroystokyo.paper.event.player.PlayerInitialSpawnEvent`；父类：`org.spigotmc.event.player.PlayerSpawnLocationEvent`。
- Python 订阅：`@bridge.on("PlayerInitialSpawnEvent")`；也可使用 `Events.PLAYER_INITIAL_SPAWN`。
- 可取消：否；关联玩家：可能有，取决于实际对象。
- [Paper 官方 Javadoc](https://jd.papermc.io/paper/1.16.5/com/destroystokyo/paper/event/player/PlayerInitialSpawnEvent.html)：事件含义、触发条件和 Java API。

| `data` 字段 | JSON 类型 | Java getter | Java 返回类型 |
| --- | --- | --- | --- |
| `spawnLocation` | 位置摘要 | `getSpawnLocation()` | `org.bukkit.Location` |

<a id="event-org-bukkit-event-player-playerinteractatentityevent"></a>
### PlayerInteractAtEntityEvent

- Java 类：`org.bukkit.event.player.PlayerInteractAtEntityEvent`；父类：`org.bukkit.event.player.PlayerInteractEntityEvent`。
- Python 订阅：`@bridge.on("PlayerInteractAtEntityEvent")`；也可使用 `Events.PLAYER_INTERACT_AT_ENTITY`。
- 可取消：是；关联玩家：可能有，取决于实际对象。
- [Paper 官方 Javadoc](https://jd.papermc.io/paper/1.16.5/org/bukkit/event/player/PlayerInteractAtEntityEvent.html)：事件含义、触发条件和 Java API。

| `data` 字段 | JSON 类型 | Java getter | Java 返回类型 |
| --- | --- | --- | --- |
| `hand` | 字符串 | `getHand()` | `org.bukkit.inventory.EquipmentSlot` |
| `rightClicked` | 实体摘要 | `getRightClicked()` | `org.bukkit.entity.Entity` |

<a id="event-org-bukkit-event-player-playerinteractentityevent"></a>
### PlayerInteractEntityEvent

- Java 类：`org.bukkit.event.player.PlayerInteractEntityEvent`；父类：`org.bukkit.event.player.PlayerEvent`。
- Python 订阅：`@bridge.on("PlayerInteractEntityEvent")`；也可使用 `Events.PLAYER_INTERACT_ENTITY`。
- 可取消：是；关联玩家：可能有，取决于实际对象。
- [Paper 官方 Javadoc](https://jd.papermc.io/paper/1.16.5/org/bukkit/event/player/PlayerInteractEntityEvent.html)：事件含义、触发条件和 Java API。

| `data` 字段 | JSON 类型 | Java getter | Java 返回类型 |
| --- | --- | --- | --- |
| `hand` | 字符串 | `getHand()` | `org.bukkit.inventory.EquipmentSlot` |
| `rightClicked` | 实体摘要 | `getRightClicked()` | `org.bukkit.entity.Entity` |

<a id="event-org-bukkit-event-player-playerinteractevent"></a>
### PlayerInteractEvent

- Java 类：`org.bukkit.event.player.PlayerInteractEvent`；父类：`org.bukkit.event.player.PlayerEvent`。
- Python 订阅：`@bridge.on("PlayerInteractEvent")`；也可使用 `Events.PLAYER_INTERACT`。
- 可取消：是；关联玩家：可能有，取决于实际对象。
- [Paper 官方 Javadoc](https://jd.papermc.io/paper/1.16.5/org/bukkit/event/player/PlayerInteractEvent.html)：事件含义、触发条件和 Java API。

| `data` 字段 | JSON 类型 | Java getter | Java 返回类型 |
| --- | --- | --- | --- |
| `action` | 字符串 | `getAction()` | `org.bukkit.event.block.Action` |
| `blockFace` | 字符串 | `getBlockFace()` | `org.bukkit.block.BlockFace` |
| `clickedBlock` | 方块摘要 | `getClickedBlock()` | `org.bukkit.block.Block` |
| `hand` | 字符串 | `getHand()` | `org.bukkit.inventory.EquipmentSlot` |
| `interactionPoint` | 位置摘要 | `getInteractionPoint()` | `org.bukkit.Location` |
| `item` | 物品摘要 | `getItem()` | `org.bukkit.inventory.ItemStack` |
| `material` | 字符串 | `getMaterial()` | `org.bukkit.Material` |
| `blockInHand` | 布尔值 | `isBlockInHand()` | `boolean` |

<a id="event-org-bukkit-event-player-playeritembreakevent"></a>
### PlayerItemBreakEvent

- Java 类：`org.bukkit.event.player.PlayerItemBreakEvent`；父类：`org.bukkit.event.player.PlayerEvent`。
- Python 订阅：`@bridge.on("PlayerItemBreakEvent")`；也可使用 `Events.PLAYER_ITEM_BREAK`。
- 可取消：否；关联玩家：可能有，取决于实际对象。
- [Paper 官方 Javadoc](https://jd.papermc.io/paper/1.16.5/org/bukkit/event/player/PlayerItemBreakEvent.html)：事件含义、触发条件和 Java API。

| `data` 字段 | JSON 类型 | Java getter | Java 返回类型 |
| --- | --- | --- | --- |
| `brokenItem` | 物品摘要 | `getBrokenItem()` | `org.bukkit.inventory.ItemStack` |

<a id="event-org-bukkit-event-player-playeritemconsumeevent"></a>
### PlayerItemConsumeEvent

- Java 类：`org.bukkit.event.player.PlayerItemConsumeEvent`；父类：`org.bukkit.event.player.PlayerEvent`。
- Python 订阅：`@bridge.on("PlayerItemConsumeEvent")`；也可使用 `Events.PLAYER_ITEM_CONSUME`。
- 可取消：是；关联玩家：可能有，取决于实际对象。
- [Paper 官方 Javadoc](https://jd.papermc.io/paper/1.16.5/org/bukkit/event/player/PlayerItemConsumeEvent.html)：事件含义、触发条件和 Java API。

| `data` 字段 | JSON 类型 | Java getter | Java 返回类型 |
| --- | --- | --- | --- |
| `item` | 物品摘要 | `getItem()` | `org.bukkit.inventory.ItemStack` |
| `replacement` | 物品摘要 | `getReplacement()` | `org.bukkit.inventory.ItemStack` |

<a id="event-io-papermc-paper-event-player-playeritemcooldownevent"></a>
### PlayerItemCooldownEvent

- Java 类：`io.papermc.paper.event.player.PlayerItemCooldownEvent`；父类：`org.bukkit.event.player.PlayerEvent`。
- Python 订阅：`@bridge.on("PlayerItemCooldownEvent")`；也可使用 `Events.PLAYER_ITEM_COOLDOWN`。
- 可取消：是；关联玩家：可能有，取决于实际对象。
- [Paper 官方 Javadoc](https://jd.papermc.io/paper/1.16.5/io/papermc/paper/event/player/PlayerItemCooldownEvent.html)：事件含义、触发条件和 Java API。

| `data` 字段 | JSON 类型 | Java getter | Java 返回类型 |
| --- | --- | --- | --- |
| `cooldown` | 数字 | `getCooldown()` | `int` |
| `type` | 字符串 | `getType()` | `org.bukkit.Material` |

<a id="event-org-bukkit-event-player-playeritemdamageevent"></a>
### PlayerItemDamageEvent

- Java 类：`org.bukkit.event.player.PlayerItemDamageEvent`；父类：`org.bukkit.event.player.PlayerEvent`。
- Python 订阅：`@bridge.on("PlayerItemDamageEvent")`；也可使用 `Events.PLAYER_ITEM_DAMAGE`。
- 可取消：是；关联玩家：可能有，取决于实际对象。
- [Paper 官方 Javadoc](https://jd.papermc.io/paper/1.16.5/org/bukkit/event/player/PlayerItemDamageEvent.html)：事件含义、触发条件和 Java API。

| `data` 字段 | JSON 类型 | Java getter | Java 返回类型 |
| --- | --- | --- | --- |
| `damage` | 数字 | `getDamage()` | `int` |
| `item` | 物品摘要 | `getItem()` | `org.bukkit.inventory.ItemStack` |

<a id="event-org-bukkit-event-player-playeritemheldevent"></a>
### PlayerItemHeldEvent

- Java 类：`org.bukkit.event.player.PlayerItemHeldEvent`；父类：`org.bukkit.event.player.PlayerEvent`。
- Python 订阅：`@bridge.on("PlayerItemHeldEvent")`；也可使用 `Events.PLAYER_ITEM_HELD`。
- 可取消：是；关联玩家：可能有，取决于实际对象。
- [Paper 官方 Javadoc](https://jd.papermc.io/paper/1.16.5/org/bukkit/event/player/PlayerItemHeldEvent.html)：事件含义、触发条件和 Java API。

| `data` 字段 | JSON 类型 | Java getter | Java 返回类型 |
| --- | --- | --- | --- |
| `newSlot` | 数字 | `getNewSlot()` | `int` |
| `previousSlot` | 数字 | `getPreviousSlot()` | `int` |

<a id="event-org-bukkit-event-player-playeritemmendevent"></a>
### PlayerItemMendEvent

- Java 类：`org.bukkit.event.player.PlayerItemMendEvent`；父类：`org.bukkit.event.player.PlayerEvent`。
- Python 订阅：`@bridge.on("PlayerItemMendEvent")`；也可使用 `Events.PLAYER_ITEM_MEND`。
- 可取消：是；关联玩家：可能有，取决于实际对象。
- [Paper 官方 Javadoc](https://jd.papermc.io/paper/1.16.5/org/bukkit/event/player/PlayerItemMendEvent.html)：事件含义、触发条件和 Java API。

| `data` 字段 | JSON 类型 | Java getter | Java 返回类型 |
| --- | --- | --- | --- |
| `experienceOrb` | 实体摘要 | `getExperienceOrb()` | `org.bukkit.entity.ExperienceOrb` |
| `item` | 物品摘要 | `getItem()` | `org.bukkit.inventory.ItemStack` |
| `repairAmount` | 数字 | `getRepairAmount()` | `int` |

<a id="event-org-bukkit-event-player-playerjoinevent"></a>
### PlayerJoinEvent

- Java 类：`org.bukkit.event.player.PlayerJoinEvent`；父类：`org.bukkit.event.player.PlayerEvent`。
- Python 订阅：`@bridge.on("join")`；也可使用 `Events.PLAYER_JOIN`。
- 可取消：否；关联玩家：可能有，取决于实际对象。
- [Paper 官方 Javadoc](https://jd.papermc.io/paper/1.16.5/org/bukkit/event/player/PlayerJoinEvent.html)：事件含义、触发条件和 Java API。

| `data` 字段 | JSON 类型 | Java getter | Java 返回类型 |
| --- | --- | --- | --- |
| `joinMessage` | 字符串 | `getJoinMessage()` | `java.lang.String` |

<a id="event-com-destroystokyo-paper-event-player-playerjumpevent"></a>
### PlayerJumpEvent

- Java 类：`com.destroystokyo.paper.event.player.PlayerJumpEvent`；父类：`org.bukkit.event.player.PlayerEvent`。
- Python 订阅：`@bridge.on("PlayerJumpEvent")`；也可使用 `Events.PLAYER_JUMP`。
- 可取消：是；关联玩家：可能有，取决于实际对象。
- [Paper 官方 Javadoc](https://jd.papermc.io/paper/1.16.5/com/destroystokyo/paper/event/player/PlayerJumpEvent.html)：事件含义、触发条件和 Java API。

| `data` 字段 | JSON 类型 | Java getter | Java 返回类型 |
| --- | --- | --- | --- |
| `from` | 位置摘要 | `getFrom()` | `org.bukkit.Location` |
| `to` | 位置摘要 | `getTo()` | `org.bukkit.Location` |

<a id="event-org-bukkit-event-player-playerkickevent"></a>
### PlayerKickEvent

- Java 类：`org.bukkit.event.player.PlayerKickEvent`；父类：`org.bukkit.event.player.PlayerEvent`。
- Python 订阅：`@bridge.on("PlayerKickEvent")`；也可使用 `Events.PLAYER_KICK`。
- 可取消：是；关联玩家：可能有，取决于实际对象。
- [Paper 官方 Javadoc](https://jd.papermc.io/paper/1.16.5/org/bukkit/event/player/PlayerKickEvent.html)：事件含义、触发条件和 Java API。

| `data` 字段 | JSON 类型 | Java getter | Java 返回类型 |
| --- | --- | --- | --- |
| `cause` | 字符串 | `getCause()` | `org.bukkit.event.player.PlayerKickEvent$Cause` |
| `leaveMessage` | 字符串 | `getLeaveMessage()` | `java.lang.String` |
| `reason` | 字符串 | `getReason()` | `java.lang.String` |

<a id="event-com-destroystokyo-paper-event-player-playerlaunchprojectileevent"></a>
### PlayerLaunchProjectileEvent

- Java 类：`com.destroystokyo.paper.event.player.PlayerLaunchProjectileEvent`；父类：`org.bukkit.event.player.PlayerEvent`。
- Python 订阅：`@bridge.on("PlayerLaunchProjectileEvent")`；也可使用 `Events.PLAYER_LAUNCH_PROJECTILE`。
- 可取消：是；关联玩家：可能有，取决于实际对象。
- [Paper 官方 Javadoc](https://jd.papermc.io/paper/1.16.5/com/destroystokyo/paper/event/player/PlayerLaunchProjectileEvent.html)：事件含义、触发条件和 Java API。

| `data` 字段 | JSON 类型 | Java getter | Java 返回类型 |
| --- | --- | --- | --- |
| `itemStack` | 物品摘要 | `getItemStack()` | `org.bukkit.inventory.ItemStack` |
| `projectile` | 实体摘要 | `getProjectile()` | `org.bukkit.entity.Projectile` |

<a id="event-io-papermc-paper-event-player-playerlecternpagechangeevent"></a>
### PlayerLecternPageChangeEvent

- Java 类：`io.papermc.paper.event.player.PlayerLecternPageChangeEvent`；父类：`org.bukkit.event.player.PlayerEvent`。
- Python 订阅：`@bridge.on("PlayerLecternPageChangeEvent")`；也可使用 `Events.PLAYER_LECTERN_PAGE_CHANGE`。
- 可取消：是；关联玩家：可能有，取决于实际对象。
- [Paper 官方 Javadoc](https://jd.papermc.io/paper/1.16.5/io/papermc/paper/event/player/PlayerLecternPageChangeEvent.html)：事件含义、触发条件和 Java API。

| `data` 字段 | JSON 类型 | Java getter | Java 返回类型 |
| --- | --- | --- | --- |
| `book` | 物品摘要 | `getBook()` | `org.bukkit.inventory.ItemStack` |
| `newPage` | 数字 | `getNewPage()` | `int` |
| `oldPage` | 数字 | `getOldPage()` | `int` |
| `pageChangeDirection` | 字符串 | `getPageChangeDirection()` | `io.papermc.paper.event.player.PlayerLecternPageChangeEvent$PageChangeDirection` |

<a id="event-org-bukkit-event-player-playerlevelchangeevent"></a>
### PlayerLevelChangeEvent

- Java 类：`org.bukkit.event.player.PlayerLevelChangeEvent`；父类：`org.bukkit.event.player.PlayerEvent`。
- Python 订阅：`@bridge.on("PlayerLevelChangeEvent")`；也可使用 `Events.PLAYER_LEVEL_CHANGE`。
- 可取消：否；关联玩家：可能有，取决于实际对象。
- [Paper 官方 Javadoc](https://jd.papermc.io/paper/1.16.5/org/bukkit/event/player/PlayerLevelChangeEvent.html)：事件含义、触发条件和 Java API。

| `data` 字段 | JSON 类型 | Java getter | Java 返回类型 |
| --- | --- | --- | --- |
| `newLevel` | 数字 | `getNewLevel()` | `int` |
| `oldLevel` | 数字 | `getOldLevel()` | `int` |

<a id="event-com-destroystokyo-paper-event-player-playerlocalechangeevent"></a>
### PlayerLocaleChangeEvent

- Java 类：`com.destroystokyo.paper.event.player.PlayerLocaleChangeEvent`；父类：`org.bukkit.event.player.PlayerEvent`。
- Python 订阅：`@bridge.on("PlayerLocaleChangeEvent")`；也可使用 `Events.PAPER_PLAYER_LOCALE_CHANGE`。
- 可取消：否；关联玩家：可能有，取决于实际对象。
- [Paper 官方 Javadoc](https://jd.papermc.io/paper/1.16.5/com/destroystokyo/paper/event/player/PlayerLocaleChangeEvent.html)：事件含义、触发条件和 Java API。

| `data` 字段 | JSON 类型 | Java getter | Java 返回类型 |
| --- | --- | --- | --- |
| `newLocale` | 字符串 | `getNewLocale()` | `java.lang.String` |
| `oldLocale` | 字符串 | `getOldLocale()` | `java.lang.String` |

<a id="event-org-bukkit-event-player-playerlocalechangeevent"></a>
### PlayerLocaleChangeEvent

- Java 类：`org.bukkit.event.player.PlayerLocaleChangeEvent`；父类：`org.bukkit.event.player.PlayerEvent`。
- Python 订阅：`@bridge.on("PlayerLocaleChangeEvent")`；也可使用 `Events.PLAYER_LOCALE_CHANGE`。
- 可取消：否；关联玩家：可能有，取决于实际对象。
- [Paper 官方 Javadoc](https://jd.papermc.io/paper/1.16.5/org/bukkit/event/player/PlayerLocaleChangeEvent.html)：事件含义、触发条件和 Java API。

| `data` 字段 | JSON 类型 | Java getter | Java 返回类型 |
| --- | --- | --- | --- |
| `locale` | 字符串 | `getLocale()` | `java.lang.String` |

<a id="event-org-bukkit-event-player-playerloginevent"></a>
### PlayerLoginEvent

- Java 类：`org.bukkit.event.player.PlayerLoginEvent`；父类：`org.bukkit.event.player.PlayerEvent`。
- Python 订阅：`@bridge.on("PlayerLoginEvent")`；也可使用 `Events.PLAYER_LOGIN`。
- 可取消：否；关联玩家：可能有，取决于实际对象。
- [Paper 官方 Javadoc](https://jd.papermc.io/paper/1.16.5/org/bukkit/event/player/PlayerLoginEvent.html)：事件含义、触发条件和 Java API。

| `data` 字段 | JSON 类型 | Java getter | Java 返回类型 |
| --- | --- | --- | --- |
| `hostname` | 字符串 | `getHostname()` | `java.lang.String` |
| `kickMessage` | 字符串 | `getKickMessage()` | `java.lang.String` |
| `result` | 字符串 | `getResult()` | `org.bukkit.event.player.PlayerLoginEvent$Result` |

<a id="event-io-papermc-paper-event-player-playerloompatternselectevent"></a>
### PlayerLoomPatternSelectEvent

- Java 类：`io.papermc.paper.event.player.PlayerLoomPatternSelectEvent`；父类：`org.bukkit.event.player.PlayerEvent`。
- Python 订阅：`@bridge.on("PlayerLoomPatternSelectEvent")`；也可使用 `Events.PLAYER_LOOM_PATTERN_SELECT`。
- 可取消：是；关联玩家：可能有，取决于实际对象。
- [Paper 官方 Javadoc](https://jd.papermc.io/paper/1.16.5/io/papermc/paper/event/player/PlayerLoomPatternSelectEvent.html)：事件含义、触发条件和 Java API。

| `data` 字段 | JSON 类型 | Java getter | Java 返回类型 |
| --- | --- | --- | --- |
| `patternType` | 字符串 | `getPatternType()` | `org.bukkit.block.banner.PatternType` |

<a id="event-org-bukkit-event-player-playermoveevent"></a>
### PlayerMoveEvent

- Java 类：`org.bukkit.event.player.PlayerMoveEvent`；父类：`org.bukkit.event.player.PlayerEvent`。
- Python 订阅：`@bridge.on("PlayerMoveEvent")`；也可使用 `Events.PLAYER_MOVE`。
- 可取消：是；关联玩家：可能有，取决于实际对象。
- [Paper 官方 Javadoc](https://jd.papermc.io/paper/1.16.5/org/bukkit/event/player/PlayerMoveEvent.html)：事件含义、触发条件和 Java API。

| `data` 字段 | JSON 类型 | Java getter | Java 返回类型 |
| --- | --- | --- | --- |
| `from` | 位置摘要 | `getFrom()` | `org.bukkit.Location` |
| `to` | 位置摘要 | `getTo()` | `org.bukkit.Location` |

<a id="event-io-papermc-paper-event-player-playernameentityevent"></a>
### PlayerNameEntityEvent

- Java 类：`io.papermc.paper.event.player.PlayerNameEntityEvent`；父类：`org.bukkit.event.player.PlayerEvent`。
- Python 订阅：`@bridge.on("PlayerNameEntityEvent")`；也可使用 `Events.PLAYER_NAME_ENTITY`。
- 可取消：是；关联玩家：可能有，取决于实际对象。
- [Paper 官方 Javadoc](https://jd.papermc.io/paper/1.16.5/io/papermc/paper/event/player/PlayerNameEntityEvent.html)：事件含义、触发条件和 Java API。

| `data` 字段 | JSON 类型 | Java getter | Java 返回类型 |
| --- | --- | --- | --- |
| `entity` | 实体摘要 | `getEntity()` | `org.bukkit.entity.LivingEntity` |
| `persistent` | 布尔值 | `isPersistent()` | `boolean` |

<a id="event-org-bukkit-event-player-playerpickuparrowevent"></a>
### PlayerPickupArrowEvent

- Java 类：`org.bukkit.event.player.PlayerPickupArrowEvent`；父类：`org.bukkit.event.player.PlayerPickupItemEvent`。
- Python 订阅：`@bridge.on("PlayerPickupArrowEvent")`；也可使用 `Events.PLAYER_PICKUP_ARROW`。
- 可取消：是；关联玩家：可能有，取决于实际对象。
- [Paper 官方 Javadoc](https://jd.papermc.io/paper/1.16.5/org/bukkit/event/player/PlayerPickupArrowEvent.html)：事件含义、触发条件和 Java API。

| `data` 字段 | JSON 类型 | Java getter | Java 返回类型 |
| --- | --- | --- | --- |
| `arrow` | 实体摘要 | `getArrow()` | `org.bukkit.entity.AbstractArrow` |
| `flyAtPlayer` | 布尔值 | `getFlyAtPlayer()` | `boolean` |
| `item` | 实体摘要 | `getItem()` | `org.bukkit.entity.Item` |
| `remaining` | 数字 | `getRemaining()` | `int` |

<a id="event-com-destroystokyo-paper-event-player-playerpickupexperienceevent"></a>
### PlayerPickupExperienceEvent

- Java 类：`com.destroystokyo.paper.event.player.PlayerPickupExperienceEvent`；父类：`org.bukkit.event.player.PlayerEvent`。
- Python 订阅：`@bridge.on("PlayerPickupExperienceEvent")`；也可使用 `Events.PLAYER_PICKUP_EXPERIENCE`。
- 可取消：是；关联玩家：可能有，取决于实际对象。
- [Paper 官方 Javadoc](https://jd.papermc.io/paper/1.16.5/com/destroystokyo/paper/event/player/PlayerPickupExperienceEvent.html)：事件含义、触发条件和 Java API。

| `data` 字段 | JSON 类型 | Java getter | Java 返回类型 |
| --- | --- | --- | --- |
| `experienceOrb` | 实体摘要 | `getExperienceOrb()` | `org.bukkit.entity.ExperienceOrb` |

<a id="event-org-bukkit-event-player-playerpickupitemevent"></a>
### PlayerPickupItemEvent

- Java 类：`org.bukkit.event.player.PlayerPickupItemEvent`；父类：`org.bukkit.event.player.PlayerEvent`。
- Python 订阅：`@bridge.on("PlayerPickupItemEvent")`；也可使用 `Events.PLAYER_PICKUP_ITEM`。
- 可取消：是；关联玩家：可能有，取决于实际对象。
- [Paper 官方 Javadoc](https://jd.papermc.io/paper/1.16.5/org/bukkit/event/player/PlayerPickupItemEvent.html)：事件含义、触发条件和 Java API。

| `data` 字段 | JSON 类型 | Java getter | Java 返回类型 |
| --- | --- | --- | --- |
| `flyAtPlayer` | 布尔值 | `getFlyAtPlayer()` | `boolean` |
| `item` | 实体摘要 | `getItem()` | `org.bukkit.entity.Item` |
| `remaining` | 数字 | `getRemaining()` | `int` |

<a id="event-org-bukkit-event-player-playerportalevent"></a>
### PlayerPortalEvent

- Java 类：`org.bukkit.event.player.PlayerPortalEvent`；父类：`org.bukkit.event.player.PlayerTeleportEvent`。
- Python 订阅：`@bridge.on("PlayerPortalEvent")`；也可使用 `Events.PLAYER_PORTAL`。
- 可取消：是；关联玩家：可能有，取决于实际对象。
- [Paper 官方 Javadoc](https://jd.papermc.io/paper/1.16.5/org/bukkit/event/player/PlayerPortalEvent.html)：事件含义、触发条件和 Java API。

| `data` 字段 | JSON 类型 | Java getter | Java 返回类型 |
| --- | --- | --- | --- |
| `canCreatePortal` | 布尔值 | `getCanCreatePortal()` | `boolean` |
| `cause` | 字符串 | `getCause()` | `org.bukkit.event.player.PlayerTeleportEvent$TeleportCause` |
| `creationRadius` | 数字 | `getCreationRadius()` | `int` |
| `from` | 位置摘要 | `getFrom()` | `org.bukkit.Location` |
| `searchRadius` | 数字 | `getSearchRadius()` | `int` |
| `to` | 位置摘要 | `getTo()` | `org.bukkit.Location` |

<a id="event-com-destroystokyo-paper-event-player-playerpostrespawnevent"></a>
### PlayerPostRespawnEvent

- Java 类：`com.destroystokyo.paper.event.player.PlayerPostRespawnEvent`；父类：`org.bukkit.event.player.PlayerEvent`。
- Python 订阅：`@bridge.on("PlayerPostRespawnEvent")`；也可使用 `Events.PLAYER_POST_RESPAWN`。
- 可取消：否；关联玩家：可能有，取决于实际对象。
- [Paper 官方 Javadoc](https://jd.papermc.io/paper/1.16.5/com/destroystokyo/paper/event/player/PlayerPostRespawnEvent.html)：事件含义、触发条件和 Java API。

| `data` 字段 | JSON 类型 | Java getter | Java 返回类型 |
| --- | --- | --- | --- |
| `respawnedLocation` | 位置摘要 | `getRespawnedLocation()` | `org.bukkit.Location` |
| `bedSpawn` | 布尔值 | `isBedSpawn()` | `boolean` |

<a id="event-org-bukkit-event-player-playerpreloginevent"></a>
### PlayerPreLoginEvent

- Java 类：`org.bukkit.event.player.PlayerPreLoginEvent`；父类：`org.bukkit.event.Event`。
- Python 订阅：`@bridge.on("PlayerPreLoginEvent")`；也可使用 `Events.PLAYER_PRE_LOGIN`。
- 可取消：否；关联玩家：无已知玩家 getter。
- [Paper 官方 Javadoc](https://jd.papermc.io/paper/1.16.5/org/bukkit/event/player/PlayerPreLoginEvent.html)：事件含义、触发条件和 Java API。

| `data` 字段 | JSON 类型 | Java getter | Java 返回类型 |
| --- | --- | --- | --- |
| `kickMessage` | 字符串 | `getKickMessage()` | `java.lang.String` |
| `name` | 字符串 | `getName()` | `java.lang.String` |
| `result` | 字符串 | `getResult()` | `org.bukkit.event.player.PlayerPreLoginEvent$Result` |
| `uniqueId` | 字符串 | `getUniqueId()` | `java.util.UUID` |

<a id="event-io-papermc-paper-event-player-playerpurchaseevent"></a>
### PlayerPurchaseEvent

- Java 类：`io.papermc.paper.event.player.PlayerPurchaseEvent`；父类：`org.bukkit.event.player.PlayerEvent`。
- Python 订阅：`@bridge.on("PlayerPurchaseEvent")`；也可使用 `Events.PLAYER_PURCHASE`。
- 可取消：是；关联玩家：可能有，取决于实际对象。
- [Paper 官方 Javadoc](https://jd.papermc.io/paper/1.16.5/io/papermc/paper/event/player/PlayerPurchaseEvent.html)：事件含义、触发条件和 Java API。

| `data` 字段 | JSON 类型 | Java getter | Java 返回类型 |
| --- | --- | --- | --- |
| `rewardingExp` | 布尔值 | `isRewardingExp()` | `boolean` |

<a id="event-org-bukkit-event-player-playerquitevent"></a>
### PlayerQuitEvent

- Java 类：`org.bukkit.event.player.PlayerQuitEvent`；父类：`org.bukkit.event.player.PlayerEvent`。
- Python 订阅：`@bridge.on("quit")`；也可使用 `Events.PLAYER_QUIT`。
- 可取消：否；关联玩家：可能有，取决于实际对象。
- [Paper 官方 Javadoc](https://jd.papermc.io/paper/1.16.5/org/bukkit/event/player/PlayerQuitEvent.html)：事件含义、触发条件和 Java API。

| `data` 字段 | JSON 类型 | Java getter | Java 返回类型 |
| --- | --- | --- | --- |
| `quitMessage` | 字符串 | `getQuitMessage()` | `java.lang.String` |
| `reason` | 字符串 | `getReason()` | `org.bukkit.event.player.PlayerQuitEvent$QuitReason` |

<a id="event-com-destroystokyo-paper-event-player-playerreadyarrowevent"></a>
### PlayerReadyArrowEvent

- Java 类：`com.destroystokyo.paper.event.player.PlayerReadyArrowEvent`；父类：`org.bukkit.event.player.PlayerEvent`。
- Python 订阅：`@bridge.on("PlayerReadyArrowEvent")`；也可使用 `Events.PLAYER_READY_ARROW`。
- 可取消：是；关联玩家：可能有，取决于实际对象。
- [Paper 官方 Javadoc](https://jd.papermc.io/paper/1.16.5/com/destroystokyo/paper/event/player/PlayerReadyArrowEvent.html)：事件含义、触发条件和 Java API。

| `data` 字段 | JSON 类型 | Java getter | Java 返回类型 |
| --- | --- | --- | --- |
| `arrow` | 物品摘要 | `getArrow()` | `org.bukkit.inventory.ItemStack` |
| `bow` | 物品摘要 | `getBow()` | `org.bukkit.inventory.ItemStack` |

<a id="event-com-destroystokyo-paper-event-player-playerrecipebookclickevent"></a>
### PlayerRecipeBookClickEvent

- Java 类：`com.destroystokyo.paper.event.player.PlayerRecipeBookClickEvent`；父类：`org.bukkit.event.player.PlayerEvent`。
- Python 订阅：`@bridge.on("PlayerRecipeBookClickEvent")`；也可使用 `Events.PLAYER_RECIPE_BOOK_CLICK`。
- 可取消：是；关联玩家：可能有，取决于实际对象。
- [Paper 官方 Javadoc](https://jd.papermc.io/paper/1.16.5/com/destroystokyo/paper/event/player/PlayerRecipeBookClickEvent.html)：事件含义、触发条件和 Java API。

| `data` 字段 | JSON 类型 | Java getter | Java 返回类型 |
| --- | --- | --- | --- |
| `makeAll` | 布尔值 | `isMakeAll()` | `boolean` |

<a id="event-org-bukkit-event-player-playerrecipediscoverevent"></a>
### PlayerRecipeDiscoverEvent

- Java 类：`org.bukkit.event.player.PlayerRecipeDiscoverEvent`；父类：`org.bukkit.event.player.PlayerEvent`。
- Python 订阅：`@bridge.on("PlayerRecipeDiscoverEvent")`；也可使用 `Events.PLAYER_RECIPE_DISCOVER`。
- 可取消：是；关联玩家：可能有，取决于实际对象。
- [Paper 官方 Javadoc](https://jd.papermc.io/paper/1.16.5/org/bukkit/event/player/PlayerRecipeDiscoverEvent.html)：事件含义、触发条件和 Java API。

没有可序列化的 `data` 字段；仍会收到通用事件字段。

<a id="event-org-bukkit-event-player-playerregisterchannelevent"></a>
### PlayerRegisterChannelEvent

- Java 类：`org.bukkit.event.player.PlayerRegisterChannelEvent`；父类：`org.bukkit.event.player.PlayerChannelEvent`。
- Python 订阅：`@bridge.on("PlayerRegisterChannelEvent")`；也可使用 `Events.PLAYER_REGISTER_CHANNEL`。
- 可取消：否；关联玩家：可能有，取决于实际对象。
- [Paper 官方 Javadoc](https://jd.papermc.io/paper/1.16.5/org/bukkit/event/player/PlayerRegisterChannelEvent.html)：事件含义、触发条件和 Java API。

| `data` 字段 | JSON 类型 | Java getter | Java 返回类型 |
| --- | --- | --- | --- |
| `channel` | 字符串 | `getChannel()` | `java.lang.String` |

<a id="event-org-bukkit-event-player-playerresourcepackstatusevent"></a>
### PlayerResourcePackStatusEvent

- Java 类：`org.bukkit.event.player.PlayerResourcePackStatusEvent`；父类：`org.bukkit.event.player.PlayerEvent`。
- Python 订阅：`@bridge.on("PlayerResourcePackStatusEvent")`；也可使用 `Events.PLAYER_RESOURCE_PACK_STATUS`。
- 可取消：否；关联玩家：可能有，取决于实际对象。
- [Paper 官方 Javadoc](https://jd.papermc.io/paper/1.16.5/org/bukkit/event/player/PlayerResourcePackStatusEvent.html)：事件含义、触发条件和 Java API。

| `data` 字段 | JSON 类型 | Java getter | Java 返回类型 |
| --- | --- | --- | --- |
| `hash` | 字符串 | `getHash()` | `java.lang.String` |
| `status` | 字符串 | `getStatus()` | `org.bukkit.event.player.PlayerResourcePackStatusEvent$Status` |

<a id="event-org-bukkit-event-player-playerrespawnevent"></a>
### PlayerRespawnEvent

- Java 类：`org.bukkit.event.player.PlayerRespawnEvent`；父类：`org.bukkit.event.player.PlayerEvent`。
- Python 订阅：`@bridge.on("PlayerRespawnEvent")`；也可使用 `Events.PLAYER_RESPAWN`。
- 可取消：否；关联玩家：可能有，取决于实际对象。
- [Paper 官方 Javadoc](https://jd.papermc.io/paper/1.16.5/org/bukkit/event/player/PlayerRespawnEvent.html)：事件含义、触发条件和 Java API。

| `data` 字段 | JSON 类型 | Java getter | Java 返回类型 |
| --- | --- | --- | --- |
| `respawnLocation` | 位置摘要 | `getRespawnLocation()` | `org.bukkit.Location` |
| `anchorSpawn` | 布尔值 | `isAnchorSpawn()` | `boolean` |
| `bedSpawn` | 布尔值 | `isBedSpawn()` | `boolean` |

<a id="event-org-bukkit-event-player-playerriptideevent"></a>
### PlayerRiptideEvent

- Java 类：`org.bukkit.event.player.PlayerRiptideEvent`；父类：`org.bukkit.event.player.PlayerEvent`。
- Python 订阅：`@bridge.on("PlayerRiptideEvent")`；也可使用 `Events.PLAYER_RIPTIDE`。
- 可取消：否；关联玩家：可能有，取决于实际对象。
- [Paper 官方 Javadoc](https://jd.papermc.io/paper/1.16.5/org/bukkit/event/player/PlayerRiptideEvent.html)：事件含义、触发条件和 Java API。

| `data` 字段 | JSON 类型 | Java getter | Java 返回类型 |
| --- | --- | --- | --- |
| `item` | 物品摘要 | `getItem()` | `org.bukkit.inventory.ItemStack` |

<a id="event-org-bukkit-event-player-playershearentityevent"></a>
### PlayerShearEntityEvent

- Java 类：`org.bukkit.event.player.PlayerShearEntityEvent`；父类：`org.bukkit.event.player.PlayerEvent`。
- Python 订阅：`@bridge.on("PlayerShearEntityEvent")`；也可使用 `Events.PLAYER_SHEAR_ENTITY`。
- 可取消：是；关联玩家：可能有，取决于实际对象。
- [Paper 官方 Javadoc](https://jd.papermc.io/paper/1.16.5/org/bukkit/event/player/PlayerShearEntityEvent.html)：事件含义、触发条件和 Java API。

| `data` 字段 | JSON 类型 | Java getter | Java 返回类型 |
| --- | --- | --- | --- |
| `entity` | 实体摘要 | `getEntity()` | `org.bukkit.entity.Entity` |
| `hand` | 字符串 | `getHand()` | `org.bukkit.inventory.EquipmentSlot` |
| `item` | 物品摘要 | `getItem()` | `org.bukkit.inventory.ItemStack` |

<a id="event-io-papermc-paper-event-player-playersigncommandpreprocessevent"></a>
### PlayerSignCommandPreprocessEvent

- Java 类：`io.papermc.paper.event.player.PlayerSignCommandPreprocessEvent`；父类：`org.bukkit.event.player.PlayerCommandPreprocessEvent`。
- Python 订阅：`@bridge.on("PlayerSignCommandPreprocessEvent")`；也可使用 `Events.PLAYER_SIGN_COMMAND_PREPROCESS`。
- 可取消：是；关联玩家：可能有，取决于实际对象。
- [Paper 官方 Javadoc](https://jd.papermc.io/paper/1.16.5/io/papermc/paper/event/player/PlayerSignCommandPreprocessEvent.html)：事件含义、触发条件和 Java API。

| `data` 字段 | JSON 类型 | Java getter | Java 返回类型 |
| --- | --- | --- | --- |
| `message` | 字符串 | `getMessage()` | `java.lang.String` |

<a id="event-com-destroystokyo-paper-event-player-playerstartspectatingentityevent"></a>
### PlayerStartSpectatingEntityEvent

- Java 类：`com.destroystokyo.paper.event.player.PlayerStartSpectatingEntityEvent`；父类：`org.bukkit.event.player.PlayerEvent`。
- Python 订阅：`@bridge.on("PlayerStartSpectatingEntityEvent")`；也可使用 `Events.PLAYER_START_SPECTATING_ENTITY`。
- 可取消：是；关联玩家：可能有，取决于实际对象。
- [Paper 官方 Javadoc](https://jd.papermc.io/paper/1.16.5/com/destroystokyo/paper/event/player/PlayerStartSpectatingEntityEvent.html)：事件含义、触发条件和 Java API。

| `data` 字段 | JSON 类型 | Java getter | Java 返回类型 |
| --- | --- | --- | --- |
| `currentSpectatorTarget` | 实体摘要 | `getCurrentSpectatorTarget()` | `org.bukkit.entity.Entity` |
| `newSpectatorTarget` | 实体摘要 | `getNewSpectatorTarget()` | `org.bukkit.entity.Entity` |

<a id="event-org-bukkit-event-player-playerstatisticincrementevent"></a>
### PlayerStatisticIncrementEvent

- Java 类：`org.bukkit.event.player.PlayerStatisticIncrementEvent`；父类：`org.bukkit.event.player.PlayerEvent`。
- Python 订阅：`@bridge.on("PlayerStatisticIncrementEvent")`；也可使用 `Events.PLAYER_STATISTIC_INCREMENT`。
- 可取消：是；关联玩家：可能有，取决于实际对象。
- [Paper 官方 Javadoc](https://jd.papermc.io/paper/1.16.5/org/bukkit/event/player/PlayerStatisticIncrementEvent.html)：事件含义、触发条件和 Java API。

| `data` 字段 | JSON 类型 | Java getter | Java 返回类型 |
| --- | --- | --- | --- |
| `entityType` | 字符串 | `getEntityType()` | `org.bukkit.entity.EntityType` |
| `material` | 字符串 | `getMaterial()` | `org.bukkit.Material` |
| `newValue` | 数字 | `getNewValue()` | `int` |
| `previousValue` | 数字 | `getPreviousValue()` | `int` |
| `statistic` | 字符串 | `getStatistic()` | `org.bukkit.Statistic` |

<a id="event-io-papermc-paper-event-player-playerstonecutterrecipeselectevent"></a>
### PlayerStonecutterRecipeSelectEvent

- Java 类：`io.papermc.paper.event.player.PlayerStonecutterRecipeSelectEvent`；父类：`org.bukkit.event.player.PlayerEvent`。
- Python 订阅：`@bridge.on("PlayerStonecutterRecipeSelectEvent")`；也可使用 `Events.PLAYER_STONECUTTER_RECIPE_SELECT`。
- 可取消：是；关联玩家：可能有，取决于实际对象。
- [Paper 官方 Javadoc](https://jd.papermc.io/paper/1.16.5/io/papermc/paper/event/player/PlayerStonecutterRecipeSelectEvent.html)：事件含义、触发条件和 Java API。

没有可序列化的 `data` 字段；仍会收到通用事件字段。

<a id="event-com-destroystokyo-paper-event-player-playerstopspectatingentityevent"></a>
### PlayerStopSpectatingEntityEvent

- Java 类：`com.destroystokyo.paper.event.player.PlayerStopSpectatingEntityEvent`；父类：`org.bukkit.event.player.PlayerEvent`。
- Python 订阅：`@bridge.on("PlayerStopSpectatingEntityEvent")`；也可使用 `Events.PLAYER_STOP_SPECTATING_ENTITY`。
- 可取消：是；关联玩家：可能有，取决于实际对象。
- [Paper 官方 Javadoc](https://jd.papermc.io/paper/1.16.5/com/destroystokyo/paper/event/player/PlayerStopSpectatingEntityEvent.html)：事件含义、触发条件和 Java API。

| `data` 字段 | JSON 类型 | Java getter | Java 返回类型 |
| --- | --- | --- | --- |
| `spectatorTarget` | 实体摘要 | `getSpectatorTarget()` | `org.bukkit.entity.Entity` |

<a id="event-org-bukkit-event-player-playerswaphanditemsevent"></a>
### PlayerSwapHandItemsEvent

- Java 类：`org.bukkit.event.player.PlayerSwapHandItemsEvent`；父类：`org.bukkit.event.player.PlayerEvent`。
- Python 订阅：`@bridge.on("PlayerSwapHandItemsEvent")`；也可使用 `Events.PLAYER_SWAP_HAND_ITEMS`。
- 可取消：是；关联玩家：可能有，取决于实际对象。
- [Paper 官方 Javadoc](https://jd.papermc.io/paper/1.16.5/org/bukkit/event/player/PlayerSwapHandItemsEvent.html)：事件含义、触发条件和 Java API。

| `data` 字段 | JSON 类型 | Java getter | Java 返回类型 |
| --- | --- | --- | --- |
| `mainHandItem` | 物品摘要 | `getMainHandItem()` | `org.bukkit.inventory.ItemStack` |
| `offHandItem` | 物品摘要 | `getOffHandItem()` | `org.bukkit.inventory.ItemStack` |

<a id="event-org-bukkit-event-player-playertakelecternbookevent"></a>
### PlayerTakeLecternBookEvent

- Java 类：`org.bukkit.event.player.PlayerTakeLecternBookEvent`；父类：`org.bukkit.event.player.PlayerEvent`。
- Python 订阅：`@bridge.on("PlayerTakeLecternBookEvent")`；也可使用 `Events.PLAYER_TAKE_LECTERN_BOOK`。
- 可取消：是；关联玩家：可能有，取决于实际对象。
- [Paper 官方 Javadoc](https://jd.papermc.io/paper/1.16.5/org/bukkit/event/player/PlayerTakeLecternBookEvent.html)：事件含义、触发条件和 Java API。

| `data` 字段 | JSON 类型 | Java getter | Java 返回类型 |
| --- | --- | --- | --- |
| `book` | 物品摘要 | `getBook()` | `org.bukkit.inventory.ItemStack` |

<a id="event-com-destroystokyo-paper-event-player-playerteleportendgatewayevent"></a>
### PlayerTeleportEndGatewayEvent

- Java 类：`com.destroystokyo.paper.event.player.PlayerTeleportEndGatewayEvent`；父类：`org.bukkit.event.player.PlayerTeleportEvent`。
- Python 订阅：`@bridge.on("PlayerTeleportEndGatewayEvent")`；也可使用 `Events.PLAYER_TELEPORT_END_GATEWAY`。
- 可取消：是；关联玩家：可能有，取决于实际对象。
- [Paper 官方 Javadoc](https://jd.papermc.io/paper/1.16.5/com/destroystokyo/paper/event/player/PlayerTeleportEndGatewayEvent.html)：事件含义、触发条件和 Java API。

| `data` 字段 | JSON 类型 | Java getter | Java 返回类型 |
| --- | --- | --- | --- |
| `cause` | 字符串 | `getCause()` | `org.bukkit.event.player.PlayerTeleportEvent$TeleportCause` |
| `from` | 位置摘要 | `getFrom()` | `org.bukkit.Location` |
| `to` | 位置摘要 | `getTo()` | `org.bukkit.Location` |

<a id="event-org-bukkit-event-player-playerteleportevent"></a>
### PlayerTeleportEvent

- Java 类：`org.bukkit.event.player.PlayerTeleportEvent`；父类：`org.bukkit.event.player.PlayerMoveEvent`。
- Python 订阅：`@bridge.on("PlayerTeleportEvent")`；也可使用 `Events.PLAYER_TELEPORT`。
- 可取消：是；关联玩家：可能有，取决于实际对象。
- [Paper 官方 Javadoc](https://jd.papermc.io/paper/1.16.5/org/bukkit/event/player/PlayerTeleportEvent.html)：事件含义、触发条件和 Java API。

| `data` 字段 | JSON 类型 | Java getter | Java 返回类型 |
| --- | --- | --- | --- |
| `cause` | 字符串 | `getCause()` | `org.bukkit.event.player.PlayerTeleportEvent$TeleportCause` |
| `from` | 位置摘要 | `getFrom()` | `org.bukkit.Location` |
| `to` | 位置摘要 | `getTo()` | `org.bukkit.Location` |

<a id="event-org-bukkit-event-player-playertoggleflightevent"></a>
### PlayerToggleFlightEvent

- Java 类：`org.bukkit.event.player.PlayerToggleFlightEvent`；父类：`org.bukkit.event.player.PlayerEvent`。
- Python 订阅：`@bridge.on("PlayerToggleFlightEvent")`；也可使用 `Events.PLAYER_TOGGLE_FLIGHT`。
- 可取消：是；关联玩家：可能有，取决于实际对象。
- [Paper 官方 Javadoc](https://jd.papermc.io/paper/1.16.5/org/bukkit/event/player/PlayerToggleFlightEvent.html)：事件含义、触发条件和 Java API。

| `data` 字段 | JSON 类型 | Java getter | Java 返回类型 |
| --- | --- | --- | --- |
| `flying` | 布尔值 | `isFlying()` | `boolean` |

<a id="event-org-bukkit-event-player-playertogglesneakevent"></a>
### PlayerToggleSneakEvent

- Java 类：`org.bukkit.event.player.PlayerToggleSneakEvent`；父类：`org.bukkit.event.player.PlayerEvent`。
- Python 订阅：`@bridge.on("PlayerToggleSneakEvent")`；也可使用 `Events.PLAYER_TOGGLE_SNEAK`。
- 可取消：是；关联玩家：可能有，取决于实际对象。
- [Paper 官方 Javadoc](https://jd.papermc.io/paper/1.16.5/org/bukkit/event/player/PlayerToggleSneakEvent.html)：事件含义、触发条件和 Java API。

| `data` 字段 | JSON 类型 | Java getter | Java 返回类型 |
| --- | --- | --- | --- |
| `sneaking` | 布尔值 | `isSneaking()` | `boolean` |

<a id="event-org-bukkit-event-player-playertogglesprintevent"></a>
### PlayerToggleSprintEvent

- Java 类：`org.bukkit.event.player.PlayerToggleSprintEvent`；父类：`org.bukkit.event.player.PlayerEvent`。
- Python 订阅：`@bridge.on("PlayerToggleSprintEvent")`；也可使用 `Events.PLAYER_TOGGLE_SPRINT`。
- 可取消：是；关联玩家：可能有，取决于实际对象。
- [Paper 官方 Javadoc](https://jd.papermc.io/paper/1.16.5/org/bukkit/event/player/PlayerToggleSprintEvent.html)：事件含义、触发条件和 Java API。

| `data` 字段 | JSON 类型 | Java getter | Java 返回类型 |
| --- | --- | --- | --- |
| `sprinting` | 布尔值 | `isSprinting()` | `boolean` |

<a id="event-io-papermc-paper-event-player-playertradeevent"></a>
### PlayerTradeEvent

- Java 类：`io.papermc.paper.event.player.PlayerTradeEvent`；父类：`io.papermc.paper.event.player.PlayerPurchaseEvent`。
- Python 订阅：`@bridge.on("PlayerTradeEvent")`；也可使用 `Events.PLAYER_TRADE`。
- 可取消：是；关联玩家：可能有，取决于实际对象。
- [Paper 官方 Javadoc](https://jd.papermc.io/paper/1.16.5/io/papermc/paper/event/player/PlayerTradeEvent.html)：事件含义、触发条件和 Java API。

| `data` 字段 | JSON 类型 | Java getter | Java 返回类型 |
| --- | --- | --- | --- |
| `villager` | 实体摘要 | `getVillager()` | `org.bukkit.entity.AbstractVillager` |
| `rewardingExp` | 布尔值 | `isRewardingExp()` | `boolean` |

<a id="event-org-bukkit-event-player-playerunleashentityevent"></a>
### PlayerUnleashEntityEvent

- Java 类：`org.bukkit.event.player.PlayerUnleashEntityEvent`；父类：`org.bukkit.event.entity.EntityUnleashEvent`。
- Python 订阅：`@bridge.on("PlayerUnleashEntityEvent")`；也可使用 `Events.PLAYER_UNLEASH_ENTITY`。
- 可取消：是；关联玩家：可能有，取决于实际对象。
- [Paper 官方 Javadoc](https://jd.papermc.io/paper/1.16.5/org/bukkit/event/player/PlayerUnleashEntityEvent.html)：事件含义、触发条件和 Java API。

| `data` 字段 | JSON 类型 | Java getter | Java 返回类型 |
| --- | --- | --- | --- |
| `entity` | 实体摘要 | `getEntity()` | `org.bukkit.entity.Entity` |
| `entityType` | 字符串 | `getEntityType()` | `org.bukkit.entity.EntityType` |
| `reason` | 字符串 | `getReason()` | `org.bukkit.event.entity.EntityUnleashEvent$UnleashReason` |
| `dropLeash` | 布尔值 | `isDropLeash()` | `boolean` |

<a id="event-org-bukkit-event-player-playerunregisterchannelevent"></a>
### PlayerUnregisterChannelEvent

- Java 类：`org.bukkit.event.player.PlayerUnregisterChannelEvent`；父类：`org.bukkit.event.player.PlayerChannelEvent`。
- Python 订阅：`@bridge.on("PlayerUnregisterChannelEvent")`；也可使用 `Events.PLAYER_UNREGISTER_CHANNEL`。
- 可取消：否；关联玩家：可能有，取决于实际对象。
- [Paper 官方 Javadoc](https://jd.papermc.io/paper/1.16.5/org/bukkit/event/player/PlayerUnregisterChannelEvent.html)：事件含义、触发条件和 Java API。

| `data` 字段 | JSON 类型 | Java getter | Java 返回类型 |
| --- | --- | --- | --- |
| `channel` | 字符串 | `getChannel()` | `java.lang.String` |

<a id="event-com-destroystokyo-paper-event-player-playeruseunknownentityevent"></a>
### PlayerUseUnknownEntityEvent

- Java 类：`com.destroystokyo.paper.event.player.PlayerUseUnknownEntityEvent`；父类：`org.bukkit.event.player.PlayerEvent`。
- Python 订阅：`@bridge.on("PlayerUseUnknownEntityEvent")`；也可使用 `Events.PLAYER_USE_UNKNOWN_ENTITY`。
- 可取消：否；关联玩家：可能有，取决于实际对象。
- [Paper 官方 Javadoc](https://jd.papermc.io/paper/1.16.5/com/destroystokyo/paper/event/player/PlayerUseUnknownEntityEvent.html)：事件含义、触发条件和 Java API。

| `data` 字段 | JSON 类型 | Java getter | Java 返回类型 |
| --- | --- | --- | --- |
| `entityId` | 数字 | `getEntityId()` | `int` |
| `hand` | 字符串 | `getHand()` | `org.bukkit.inventory.EquipmentSlot` |
| `attack` | 布尔值 | `isAttack()` | `boolean` |

<a id="event-org-bukkit-event-player-playervelocityevent"></a>
### PlayerVelocityEvent

- Java 类：`org.bukkit.event.player.PlayerVelocityEvent`；父类：`org.bukkit.event.player.PlayerEvent`。
- Python 订阅：`@bridge.on("PlayerVelocityEvent")`；也可使用 `Events.PLAYER_VELOCITY`。
- 可取消：是；关联玩家：可能有，取决于实际对象。
- [Paper 官方 Javadoc](https://jd.papermc.io/paper/1.16.5/org/bukkit/event/player/PlayerVelocityEvent.html)：事件含义、触发条件和 Java API。

没有可序列化的 `data` 字段；仍会收到通用事件字段。

<a id="category-profile"></a>
## 玩家资料 / profile

| 事件 | Python `type` | `data` 候选字段数 | 可取消 |
| --- | --- | ---: | --- |
| [FillProfileEvent](#event-com-destroystokyo-paper-event-profile-fillprofileevent) | `FillProfileEvent` | 0 | 否 |
| [LookupProfileEvent](#event-com-destroystokyo-paper-event-profile-lookupprofileevent) | `LookupProfileEvent` | 0 | 否 |
| [PreFillProfileEvent](#event-com-destroystokyo-paper-event-profile-prefillprofileevent) | `PreFillProfileEvent` | 0 | 否 |
| [PreLookupProfileEvent](#event-com-destroystokyo-paper-event-profile-prelookupprofileevent) | `PreLookupProfileEvent` | 2 | 否 |
| [ProfileWhitelistVerifyEvent](#event-com-destroystokyo-paper-event-profile-profilewhitelistverifyevent) | `ProfileWhitelistVerifyEvent` | 4 | 否 |

<a id="event-com-destroystokyo-paper-event-profile-fillprofileevent"></a>
### FillProfileEvent

- Java 类：`com.destroystokyo.paper.event.profile.FillProfileEvent`；父类：`org.bukkit.event.Event`。
- Python 订阅：`@bridge.on("FillProfileEvent")`；也可使用 `Events.FILL_PROFILE`。
- 可取消：否；关联玩家：无已知玩家 getter。
- [Paper 官方 Javadoc](https://jd.papermc.io/paper/1.16.5/com/destroystokyo/paper/event/profile/FillProfileEvent.html)：事件含义、触发条件和 Java API。

没有可序列化的 `data` 字段；仍会收到通用事件字段。

<a id="event-com-destroystokyo-paper-event-profile-lookupprofileevent"></a>
### LookupProfileEvent

- Java 类：`com.destroystokyo.paper.event.profile.LookupProfileEvent`；父类：`org.bukkit.event.Event`。
- Python 订阅：`@bridge.on("LookupProfileEvent")`；也可使用 `Events.LOOKUP_PROFILE`。
- 可取消：否；关联玩家：无已知玩家 getter。
- [Paper 官方 Javadoc](https://jd.papermc.io/paper/1.16.5/com/destroystokyo/paper/event/profile/LookupProfileEvent.html)：事件含义、触发条件和 Java API。

没有可序列化的 `data` 字段；仍会收到通用事件字段。

<a id="event-com-destroystokyo-paper-event-profile-prefillprofileevent"></a>
### PreFillProfileEvent

- Java 类：`com.destroystokyo.paper.event.profile.PreFillProfileEvent`；父类：`org.bukkit.event.Event`。
- Python 订阅：`@bridge.on("PreFillProfileEvent")`；也可使用 `Events.PRE_FILL_PROFILE`。
- 可取消：否；关联玩家：无已知玩家 getter。
- [Paper 官方 Javadoc](https://jd.papermc.io/paper/1.16.5/com/destroystokyo/paper/event/profile/PreFillProfileEvent.html)：事件含义、触发条件和 Java API。

没有可序列化的 `data` 字段；仍会收到通用事件字段。

<a id="event-com-destroystokyo-paper-event-profile-prelookupprofileevent"></a>
### PreLookupProfileEvent

- Java 类：`com.destroystokyo.paper.event.profile.PreLookupProfileEvent`；父类：`org.bukkit.event.Event`。
- Python 订阅：`@bridge.on("PreLookupProfileEvent")`；也可使用 `Events.PRE_LOOKUP_PROFILE`。
- 可取消：否；关联玩家：无已知玩家 getter。
- [Paper 官方 Javadoc](https://jd.papermc.io/paper/1.16.5/com/destroystokyo/paper/event/profile/PreLookupProfileEvent.html)：事件含义、触发条件和 Java API。

| `data` 字段 | JSON 类型 | Java getter | Java 返回类型 |
| --- | --- | --- | --- |
| `name` | 字符串 | `getName()` | `java.lang.String` |
| `uUID` | 字符串 | `getUUID()` | `java.util.UUID` |

<a id="event-com-destroystokyo-paper-event-profile-profilewhitelistverifyevent"></a>
### ProfileWhitelistVerifyEvent

- Java 类：`com.destroystokyo.paper.event.profile.ProfileWhitelistVerifyEvent`；父类：`org.bukkit.event.Event`。
- Python 订阅：`@bridge.on("ProfileWhitelistVerifyEvent")`；也可使用 `Events.PROFILE_WHITELIST_VERIFY`。
- 可取消：否；关联玩家：无已知玩家 getter。
- [Paper 官方 Javadoc](https://jd.papermc.io/paper/1.16.5/com/destroystokyo/paper/event/profile/ProfileWhitelistVerifyEvent.html)：事件含义、触发条件和 Java API。

| `data` 字段 | JSON 类型 | Java getter | Java 返回类型 |
| --- | --- | --- | --- |
| `kickMessage` | 字符串 | `getKickMessage()` | `java.lang.String` |
| `op` | 布尔值 | `isOp()` | `boolean` |
| `whitelistEnabled` | 布尔值 | `isWhitelistEnabled()` | `boolean` |
| `whitelisted` | 布尔值 | `isWhitelisted()` | `boolean` |

<a id="category-raid"></a>
## 袭击 / raid

| 事件 | Python `type` | `data` 候选字段数 | 可取消 |
| --- | --- | ---: | --- |
| [RaidFinishEvent](#event-org-bukkit-event-raid-raidfinishevent) | `RaidFinishEvent` | 1 | 否 |
| [RaidSpawnWaveEvent](#event-org-bukkit-event-raid-raidspawnwaveevent) | `RaidSpawnWaveEvent` | 2 | 否 |
| [RaidStopEvent](#event-org-bukkit-event-raid-raidstopevent) | `RaidStopEvent` | 2 | 否 |
| [RaidTriggerEvent](#event-org-bukkit-event-raid-raidtriggerevent) | `RaidTriggerEvent` | 1 | 是 |

<a id="event-org-bukkit-event-raid-raidfinishevent"></a>
### RaidFinishEvent

- Java 类：`org.bukkit.event.raid.RaidFinishEvent`；父类：`org.bukkit.event.raid.RaidEvent`。
- Python 订阅：`@bridge.on("RaidFinishEvent")`；也可使用 `Events.RAID_FINISH`。
- 可取消：否；关联玩家：无已知玩家 getter。
- [Paper 官方 Javadoc](https://jd.papermc.io/paper/1.16.5/org/bukkit/event/raid/RaidFinishEvent.html)：事件含义、触发条件和 Java API。

| `data` 字段 | JSON 类型 | Java getter | Java 返回类型 |
| --- | --- | --- | --- |
| `world` | 世界摘要 | `getWorld()` | `org.bukkit.World` |

<a id="event-org-bukkit-event-raid-raidspawnwaveevent"></a>
### RaidSpawnWaveEvent

- Java 类：`org.bukkit.event.raid.RaidSpawnWaveEvent`；父类：`org.bukkit.event.raid.RaidEvent`。
- Python 订阅：`@bridge.on("RaidSpawnWaveEvent")`；也可使用 `Events.RAID_SPAWN_WAVE`。
- 可取消：否；关联玩家：无已知玩家 getter。
- [Paper 官方 Javadoc](https://jd.papermc.io/paper/1.16.5/org/bukkit/event/raid/RaidSpawnWaveEvent.html)：事件含义、触发条件和 Java API。

| `data` 字段 | JSON 类型 | Java getter | Java 返回类型 |
| --- | --- | --- | --- |
| `patrolLeader` | 实体摘要 | `getPatrolLeader()` | `org.bukkit.entity.Raider` |
| `world` | 世界摘要 | `getWorld()` | `org.bukkit.World` |

<a id="event-org-bukkit-event-raid-raidstopevent"></a>
### RaidStopEvent

- Java 类：`org.bukkit.event.raid.RaidStopEvent`；父类：`org.bukkit.event.raid.RaidEvent`。
- Python 订阅：`@bridge.on("RaidStopEvent")`；也可使用 `Events.RAID_STOP`。
- 可取消：否；关联玩家：无已知玩家 getter。
- [Paper 官方 Javadoc](https://jd.papermc.io/paper/1.16.5/org/bukkit/event/raid/RaidStopEvent.html)：事件含义、触发条件和 Java API。

| `data` 字段 | JSON 类型 | Java getter | Java 返回类型 |
| --- | --- | --- | --- |
| `reason` | 字符串 | `getReason()` | `org.bukkit.event.raid.RaidStopEvent$Reason` |
| `world` | 世界摘要 | `getWorld()` | `org.bukkit.World` |

<a id="event-org-bukkit-event-raid-raidtriggerevent"></a>
### RaidTriggerEvent

- Java 类：`org.bukkit.event.raid.RaidTriggerEvent`；父类：`org.bukkit.event.raid.RaidEvent`。
- Python 订阅：`@bridge.on("RaidTriggerEvent")`；也可使用 `Events.RAID_TRIGGER`。
- 可取消：是；关联玩家：可能有，取决于实际对象。
- [Paper 官方 Javadoc](https://jd.papermc.io/paper/1.16.5/org/bukkit/event/raid/RaidTriggerEvent.html)：事件含义、触发条件和 Java API。

| `data` 字段 | JSON 类型 | Java getter | Java 返回类型 |
| --- | --- | --- | --- |
| `world` | 世界摘要 | `getWorld()` | `org.bukkit.World` |

<a id="category-server"></a>
## 服务端 / server

| 事件 | Python `type` | `data` 候选字段数 | 可取消 |
| --- | --- | ---: | --- |
| [AsyncTabCompleteEvent](#event-com-destroystokyo-paper-event-server-asynctabcompleteevent) | `AsyncTabCompleteEvent` | 4 | 是 |
| [BroadcastMessageEvent](#event-org-bukkit-event-server-broadcastmessageevent) | `BroadcastMessageEvent` | 1 | 是 |
| [GS4QueryEvent](#event-com-destroystokyo-paper-event-server-gs4queryevent) | `GS4QueryEvent` | 1 | 否 |
| [MapInitializeEvent](#event-org-bukkit-event-server-mapinitializeevent) | `MapInitializeEvent` | 0 | 否 |
| [PaperServerListPingEvent](#event-com-destroystokyo-paper-event-server-paperserverlistpingevent) | `PaperServerListPingEvent` | 5 | 是 |
| [PluginDisableEvent](#event-org-bukkit-event-server-plugindisableevent) | `PluginDisableEvent` | 0 | 否 |
| [PluginEnableEvent](#event-org-bukkit-event-server-pluginenableevent) | `PluginEnableEvent` | 0 | 否 |
| [RemoteServerCommandEvent](#event-org-bukkit-event-server-remoteservercommandevent) | `RemoteServerCommandEvent` | 1 | 是 |
| [ServerCommandEvent](#event-org-bukkit-event-server-servercommandevent) | `ServerCommandEvent` | 1 | 是 |
| [ServerExceptionEvent](#event-com-destroystokyo-paper-event-server-serverexceptionevent) | `ServerExceptionEvent` | 0 | 否 |
| [ServerListPingEvent](#event-org-bukkit-event-server-serverlistpingevent) | `ServerListPingEvent` | 3 | 否 |
| [ServerLoadEvent](#event-org-bukkit-event-server-serverloadevent) | `ServerLoadEvent` | 1 | 否 |
| [ServerResourcesReloadedEvent](#event-io-papermc-paper-event-server-serverresourcesreloadedevent) | `ServerResourcesReloadedEvent` | 1 | 否 |
| [ServerTickEndEvent](#event-com-destroystokyo-paper-event-server-servertickendevent) | `ServerTickEndEvent` | 3 | 否 |
| [ServerTickStartEvent](#event-com-destroystokyo-paper-event-server-servertickstartevent) | `ServerTickStartEvent` | 1 | 否 |
| [ServiceRegisterEvent](#event-org-bukkit-event-server-serviceregisterevent) | `ServiceRegisterEvent` | 0 | 否 |
| [ServiceUnregisterEvent](#event-org-bukkit-event-server-serviceunregisterevent) | `ServiceUnregisterEvent` | 0 | 否 |
| [TabCompleteEvent](#event-org-bukkit-event-server-tabcompleteevent) | `TabCompleteEvent` | 3 | 是 |
| [WhitelistToggleEvent](#event-com-destroystokyo-paper-event-server-whitelisttoggleevent) | `WhitelistToggleEvent` | 1 | 否 |

<a id="event-com-destroystokyo-paper-event-server-asynctabcompleteevent"></a>
### AsyncTabCompleteEvent

- Java 类：`com.destroystokyo.paper.event.server.AsyncTabCompleteEvent`；父类：`org.bukkit.event.Event`。
- Python 订阅：`@bridge.on("AsyncTabCompleteEvent")`；也可使用 `Events.ASYNC_TAB_COMPLETE`。
- 可取消：是；关联玩家：无已知玩家 getter。
- [Paper 官方 Javadoc](https://jd.papermc.io/paper/1.16.5/com/destroystokyo/paper/event/server/AsyncTabCompleteEvent.html)：事件含义、触发条件和 Java API。

| `data` 字段 | JSON 类型 | Java getter | Java 返回类型 |
| --- | --- | --- | --- |
| `buffer` | 字符串 | `getBuffer()` | `java.lang.String` |
| `location` | 位置摘要 | `getLocation()` | `org.bukkit.Location` |
| `command` | 布尔值 | `isCommand()` | `boolean` |
| `handled` | 布尔值 | `isHandled()` | `boolean` |

<a id="event-org-bukkit-event-server-broadcastmessageevent"></a>
### BroadcastMessageEvent

- Java 类：`org.bukkit.event.server.BroadcastMessageEvent`；父类：`org.bukkit.event.server.ServerEvent`。
- Python 订阅：`@bridge.on("BroadcastMessageEvent")`；也可使用 `Events.BROADCAST_MESSAGE`。
- 可取消：是；关联玩家：无已知玩家 getter。
- [Paper 官方 Javadoc](https://jd.papermc.io/paper/1.16.5/org/bukkit/event/server/BroadcastMessageEvent.html)：事件含义、触发条件和 Java API。

| `data` 字段 | JSON 类型 | Java getter | Java 返回类型 |
| --- | --- | --- | --- |
| `message` | 字符串 | `getMessage()` | `java.lang.String` |

<a id="event-com-destroystokyo-paper-event-server-gs4queryevent"></a>
### GS4QueryEvent

- Java 类：`com.destroystokyo.paper.event.server.GS4QueryEvent`；父类：`org.bukkit.event.Event`。
- Python 订阅：`@bridge.on("GS4QueryEvent")`；也可使用 `Events.GS4_QUERY`。
- 可取消：否；关联玩家：无已知玩家 getter。
- [Paper 官方 Javadoc](https://jd.papermc.io/paper/1.16.5/com/destroystokyo/paper/event/server/GS4QueryEvent.html)：事件含义、触发条件和 Java API。

| `data` 字段 | JSON 类型 | Java getter | Java 返回类型 |
| --- | --- | --- | --- |
| `queryType` | 字符串 | `getQueryType()` | `com.destroystokyo.paper.event.server.GS4QueryEvent$QueryType` |

<a id="event-org-bukkit-event-server-mapinitializeevent"></a>
### MapInitializeEvent

- Java 类：`org.bukkit.event.server.MapInitializeEvent`；父类：`org.bukkit.event.server.ServerEvent`。
- Python 订阅：`@bridge.on("MapInitializeEvent")`；也可使用 `Events.MAP_INITIALIZE`。
- 可取消：否；关联玩家：无已知玩家 getter。
- [Paper 官方 Javadoc](https://jd.papermc.io/paper/1.16.5/org/bukkit/event/server/MapInitializeEvent.html)：事件含义、触发条件和 Java API。

没有可序列化的 `data` 字段；仍会收到通用事件字段。

<a id="event-com-destroystokyo-paper-event-server-paperserverlistpingevent"></a>
### PaperServerListPingEvent

- Java 类：`com.destroystokyo.paper.event.server.PaperServerListPingEvent`；父类：`org.bukkit.event.server.ServerListPingEvent`。
- Python 订阅：`@bridge.on("PaperServerListPingEvent")`；也可使用 `Events.PAPER_SERVER_LIST_PING`。
- 可取消：是；关联玩家：无已知玩家 getter。
- [Paper 官方 Javadoc](https://jd.papermc.io/paper/1.16.5/com/destroystokyo/paper/event/server/PaperServerListPingEvent.html)：事件含义、触发条件和 Java API。

| `data` 字段 | JSON 类型 | Java getter | Java 返回类型 |
| --- | --- | --- | --- |
| `maxPlayers` | 数字 | `getMaxPlayers()` | `int` |
| `motd` | 字符串 | `getMotd()` | `java.lang.String` |
| `numPlayers` | 数字 | `getNumPlayers()` | `int` |
| `protocolVersion` | 数字 | `getProtocolVersion()` | `int` |
| `version` | 字符串 | `getVersion()` | `java.lang.String` |

<a id="event-org-bukkit-event-server-plugindisableevent"></a>
### PluginDisableEvent

- Java 类：`org.bukkit.event.server.PluginDisableEvent`；父类：`org.bukkit.event.server.PluginEvent`。
- Python 订阅：`@bridge.on("PluginDisableEvent")`；也可使用 `Events.PLUGIN_DISABLE`。
- 可取消：否；关联玩家：无已知玩家 getter。
- [Paper 官方 Javadoc](https://jd.papermc.io/paper/1.16.5/org/bukkit/event/server/PluginDisableEvent.html)：事件含义、触发条件和 Java API。

没有可序列化的 `data` 字段；仍会收到通用事件字段。

<a id="event-org-bukkit-event-server-pluginenableevent"></a>
### PluginEnableEvent

- Java 类：`org.bukkit.event.server.PluginEnableEvent`；父类：`org.bukkit.event.server.PluginEvent`。
- Python 订阅：`@bridge.on("PluginEnableEvent")`；也可使用 `Events.PLUGIN_ENABLE`。
- 可取消：否；关联玩家：无已知玩家 getter。
- [Paper 官方 Javadoc](https://jd.papermc.io/paper/1.16.5/org/bukkit/event/server/PluginEnableEvent.html)：事件含义、触发条件和 Java API。

没有可序列化的 `data` 字段；仍会收到通用事件字段。

<a id="event-org-bukkit-event-server-remoteservercommandevent"></a>
### RemoteServerCommandEvent

- Java 类：`org.bukkit.event.server.RemoteServerCommandEvent`；父类：`org.bukkit.event.server.ServerCommandEvent`。
- Python 订阅：`@bridge.on("RemoteServerCommandEvent")`；也可使用 `Events.REMOTE_SERVER_COMMAND`。
- 可取消：是；关联玩家：无已知玩家 getter。
- [Paper 官方 Javadoc](https://jd.papermc.io/paper/1.16.5/org/bukkit/event/server/RemoteServerCommandEvent.html)：事件含义、触发条件和 Java API。

| `data` 字段 | JSON 类型 | Java getter | Java 返回类型 |
| --- | --- | --- | --- |
| `command` | 字符串 | `getCommand()` | `java.lang.String` |

<a id="event-org-bukkit-event-server-servercommandevent"></a>
### ServerCommandEvent

- Java 类：`org.bukkit.event.server.ServerCommandEvent`；父类：`org.bukkit.event.server.ServerEvent`。
- Python 订阅：`@bridge.on("ServerCommandEvent")`；也可使用 `Events.SERVER_COMMAND`。
- 可取消：是；关联玩家：无已知玩家 getter。
- [Paper 官方 Javadoc](https://jd.papermc.io/paper/1.16.5/org/bukkit/event/server/ServerCommandEvent.html)：事件含义、触发条件和 Java API。

| `data` 字段 | JSON 类型 | Java getter | Java 返回类型 |
| --- | --- | --- | --- |
| `command` | 字符串 | `getCommand()` | `java.lang.String` |

<a id="event-com-destroystokyo-paper-event-server-serverexceptionevent"></a>
### ServerExceptionEvent

- Java 类：`com.destroystokyo.paper.event.server.ServerExceptionEvent`；父类：`org.bukkit.event.Event`。
- Python 订阅：`@bridge.on("ServerExceptionEvent")`；也可使用 `Events.SERVER_EXCEPTION`。
- 可取消：否；关联玩家：无已知玩家 getter。
- [Paper 官方 Javadoc](https://jd.papermc.io/paper/1.16.5/com/destroystokyo/paper/event/server/ServerExceptionEvent.html)：事件含义、触发条件和 Java API。

没有可序列化的 `data` 字段；仍会收到通用事件字段。

<a id="event-org-bukkit-event-server-serverlistpingevent"></a>
### ServerListPingEvent

- Java 类：`org.bukkit.event.server.ServerListPingEvent`；父类：`org.bukkit.event.server.ServerEvent`。
- Python 订阅：`@bridge.on("ServerListPingEvent")`；也可使用 `Events.SERVER_LIST_PING`。
- 可取消：否；关联玩家：无已知玩家 getter。
- [Paper 官方 Javadoc](https://jd.papermc.io/paper/1.16.5/org/bukkit/event/server/ServerListPingEvent.html)：事件含义、触发条件和 Java API。

| `data` 字段 | JSON 类型 | Java getter | Java 返回类型 |
| --- | --- | --- | --- |
| `maxPlayers` | 数字 | `getMaxPlayers()` | `int` |
| `motd` | 字符串 | `getMotd()` | `java.lang.String` |
| `numPlayers` | 数字 | `getNumPlayers()` | `int` |

<a id="event-org-bukkit-event-server-serverloadevent"></a>
### ServerLoadEvent

- Java 类：`org.bukkit.event.server.ServerLoadEvent`；父类：`org.bukkit.event.server.ServerEvent`。
- Python 订阅：`@bridge.on("ServerLoadEvent")`；也可使用 `Events.SERVER_LOAD`。
- 可取消：否；关联玩家：无已知玩家 getter。
- [Paper 官方 Javadoc](https://jd.papermc.io/paper/1.16.5/org/bukkit/event/server/ServerLoadEvent.html)：事件含义、触发条件和 Java API。

| `data` 字段 | JSON 类型 | Java getter | Java 返回类型 |
| --- | --- | --- | --- |
| `type` | 字符串 | `getType()` | `org.bukkit.event.server.ServerLoadEvent$LoadType` |

<a id="event-io-papermc-paper-event-server-serverresourcesreloadedevent"></a>
### ServerResourcesReloadedEvent

- Java 类：`io.papermc.paper.event.server.ServerResourcesReloadedEvent`；父类：`org.bukkit.event.server.ServerEvent`。
- Python 订阅：`@bridge.on("ServerResourcesReloadedEvent")`；也可使用 `Events.SERVER_RESOURCES_RELOADED`。
- 可取消：否；关联玩家：无已知玩家 getter。
- [Paper 官方 Javadoc](https://jd.papermc.io/paper/1.16.5/io/papermc/paper/event/server/ServerResourcesReloadedEvent.html)：事件含义、触发条件和 Java API。

| `data` 字段 | JSON 类型 | Java getter | Java 返回类型 |
| --- | --- | --- | --- |
| `cause` | 字符串 | `getCause()` | `io.papermc.paper.event.server.ServerResourcesReloadedEvent$Cause` |

<a id="event-com-destroystokyo-paper-event-server-servertickendevent"></a>
### ServerTickEndEvent

- Java 类：`com.destroystokyo.paper.event.server.ServerTickEndEvent`；父类：`org.bukkit.event.Event`。
- Python 订阅：`@bridge.on("ServerTickEndEvent")`；也可使用 `Events.SERVER_TICK_END`。
- 可取消：否；关联玩家：无已知玩家 getter。
- [Paper 官方 Javadoc](https://jd.papermc.io/paper/1.16.5/com/destroystokyo/paper/event/server/ServerTickEndEvent.html)：事件含义、触发条件和 Java API。

| `data` 字段 | JSON 类型 | Java getter | Java 返回类型 |
| --- | --- | --- | --- |
| `tickDuration` | 数字 | `getTickDuration()` | `double` |
| `tickNumber` | 数字 | `getTickNumber()` | `int` |
| `timeRemaining` | 数字 | `getTimeRemaining()` | `long` |

<a id="event-com-destroystokyo-paper-event-server-servertickstartevent"></a>
### ServerTickStartEvent

- Java 类：`com.destroystokyo.paper.event.server.ServerTickStartEvent`；父类：`org.bukkit.event.Event`。
- Python 订阅：`@bridge.on("ServerTickStartEvent")`；也可使用 `Events.SERVER_TICK_START`。
- 可取消：否；关联玩家：无已知玩家 getter。
- [Paper 官方 Javadoc](https://jd.papermc.io/paper/1.16.5/com/destroystokyo/paper/event/server/ServerTickStartEvent.html)：事件含义、触发条件和 Java API。

| `data` 字段 | JSON 类型 | Java getter | Java 返回类型 |
| --- | --- | --- | --- |
| `tickNumber` | 数字 | `getTickNumber()` | `int` |

<a id="event-org-bukkit-event-server-serviceregisterevent"></a>
### ServiceRegisterEvent

- Java 类：`org.bukkit.event.server.ServiceRegisterEvent`；父类：`org.bukkit.event.server.ServiceEvent`。
- Python 订阅：`@bridge.on("ServiceRegisterEvent")`；也可使用 `Events.SERVICE_REGISTER`。
- 可取消：否；关联玩家：无已知玩家 getter。
- [Paper 官方 Javadoc](https://jd.papermc.io/paper/1.16.5/org/bukkit/event/server/ServiceRegisterEvent.html)：事件含义、触发条件和 Java API。

没有可序列化的 `data` 字段；仍会收到通用事件字段。

<a id="event-org-bukkit-event-server-serviceunregisterevent"></a>
### ServiceUnregisterEvent

- Java 类：`org.bukkit.event.server.ServiceUnregisterEvent`；父类：`org.bukkit.event.server.ServiceEvent`。
- Python 订阅：`@bridge.on("ServiceUnregisterEvent")`；也可使用 `Events.SERVICE_UNREGISTER`。
- 可取消：否；关联玩家：无已知玩家 getter。
- [Paper 官方 Javadoc](https://jd.papermc.io/paper/1.16.5/org/bukkit/event/server/ServiceUnregisterEvent.html)：事件含义、触发条件和 Java API。

没有可序列化的 `data` 字段；仍会收到通用事件字段。

<a id="event-org-bukkit-event-server-tabcompleteevent"></a>
### TabCompleteEvent

- Java 类：`org.bukkit.event.server.TabCompleteEvent`；父类：`org.bukkit.event.Event`。
- Python 订阅：`@bridge.on("TabCompleteEvent")`；也可使用 `Events.TAB_COMPLETE`。
- 可取消：是；关联玩家：无已知玩家 getter。
- [Paper 官方 Javadoc](https://jd.papermc.io/paper/1.16.5/org/bukkit/event/server/TabCompleteEvent.html)：事件含义、触发条件和 Java API。

| `data` 字段 | JSON 类型 | Java getter | Java 返回类型 |
| --- | --- | --- | --- |
| `buffer` | 字符串 | `getBuffer()` | `java.lang.String` |
| `location` | 位置摘要 | `getLocation()` | `org.bukkit.Location` |
| `command` | 布尔值 | `isCommand()` | `boolean` |

<a id="event-com-destroystokyo-paper-event-server-whitelisttoggleevent"></a>
### WhitelistToggleEvent

- Java 类：`com.destroystokyo.paper.event.server.WhitelistToggleEvent`；父类：`org.bukkit.event.Event`。
- Python 订阅：`@bridge.on("WhitelistToggleEvent")`；也可使用 `Events.WHITELIST_TOGGLE`。
- 可取消：否；关联玩家：无已知玩家 getter。
- [Paper 官方 Javadoc](https://jd.papermc.io/paper/1.16.5/com/destroystokyo/paper/event/server/WhitelistToggleEvent.html)：事件含义、触发条件和 Java API。

| `data` 字段 | JSON 类型 | Java getter | Java 返回类型 |
| --- | --- | --- | --- |
| `enabled` | 布尔值 | `isEnabled()` | `boolean` |

<a id="category-vehicle"></a>
## 载具 / vehicle

| 事件 | Python `type` | `data` 候选字段数 | 可取消 |
| --- | --- | ---: | --- |
| [VehicleBlockCollisionEvent](#event-org-bukkit-event-vehicle-vehicleblockcollisionevent) | `VehicleBlockCollisionEvent` | 2 | 否 |
| [VehicleCreateEvent](#event-org-bukkit-event-vehicle-vehiclecreateevent) | `VehicleCreateEvent` | 1 | 是 |
| [VehicleDamageEvent](#event-org-bukkit-event-vehicle-vehicledamageevent) | `VehicleDamageEvent` | 3 | 是 |
| [VehicleDestroyEvent](#event-org-bukkit-event-vehicle-vehicledestroyevent) | `VehicleDestroyEvent` | 2 | 是 |
| [VehicleEnterEvent](#event-org-bukkit-event-vehicle-vehicleenterevent) | `VehicleEnterEvent` | 2 | 是 |
| [VehicleEntityCollisionEvent](#event-org-bukkit-event-vehicle-vehicleentitycollisionevent) | `VehicleEntityCollisionEvent` | 4 | 是 |
| [VehicleExitEvent](#event-org-bukkit-event-vehicle-vehicleexitevent) | `VehicleExitEvent` | 3 | 是 |
| [VehicleMoveEvent](#event-org-bukkit-event-vehicle-vehiclemoveevent) | `VehicleMoveEvent` | 3 | 否 |
| [VehicleUpdateEvent](#event-org-bukkit-event-vehicle-vehicleupdateevent) | `VehicleUpdateEvent` | 1 | 否 |

<a id="event-org-bukkit-event-vehicle-vehicleblockcollisionevent"></a>
### VehicleBlockCollisionEvent

- Java 类：`org.bukkit.event.vehicle.VehicleBlockCollisionEvent`；父类：`org.bukkit.event.vehicle.VehicleCollisionEvent`。
- Python 订阅：`@bridge.on("VehicleBlockCollisionEvent")`；也可使用 `Events.VEHICLE_BLOCK_COLLISION`。
- 可取消：否；关联玩家：无已知玩家 getter。
- [Paper 官方 Javadoc](https://jd.papermc.io/paper/1.16.5/org/bukkit/event/vehicle/VehicleBlockCollisionEvent.html)：事件含义、触发条件和 Java API。

| `data` 字段 | JSON 类型 | Java getter | Java 返回类型 |
| --- | --- | --- | --- |
| `block` | 方块摘要 | `getBlock()` | `org.bukkit.block.Block` |
| `vehicle` | 实体摘要 | `getVehicle()` | `org.bukkit.entity.Vehicle` |

<a id="event-org-bukkit-event-vehicle-vehiclecreateevent"></a>
### VehicleCreateEvent

- Java 类：`org.bukkit.event.vehicle.VehicleCreateEvent`；父类：`org.bukkit.event.vehicle.VehicleEvent`。
- Python 订阅：`@bridge.on("VehicleCreateEvent")`；也可使用 `Events.VEHICLE_CREATE`。
- 可取消：是；关联玩家：无已知玩家 getter。
- [Paper 官方 Javadoc](https://jd.papermc.io/paper/1.16.5/org/bukkit/event/vehicle/VehicleCreateEvent.html)：事件含义、触发条件和 Java API。

| `data` 字段 | JSON 类型 | Java getter | Java 返回类型 |
| --- | --- | --- | --- |
| `vehicle` | 实体摘要 | `getVehicle()` | `org.bukkit.entity.Vehicle` |

<a id="event-org-bukkit-event-vehicle-vehicledamageevent"></a>
### VehicleDamageEvent

- Java 类：`org.bukkit.event.vehicle.VehicleDamageEvent`；父类：`org.bukkit.event.vehicle.VehicleEvent`。
- Python 订阅：`@bridge.on("VehicleDamageEvent")`；也可使用 `Events.VEHICLE_DAMAGE`。
- 可取消：是；关联玩家：无已知玩家 getter。
- [Paper 官方 Javadoc](https://jd.papermc.io/paper/1.16.5/org/bukkit/event/vehicle/VehicleDamageEvent.html)：事件含义、触发条件和 Java API。

| `data` 字段 | JSON 类型 | Java getter | Java 返回类型 |
| --- | --- | --- | --- |
| `attacker` | 实体摘要 | `getAttacker()` | `org.bukkit.entity.Entity` |
| `damage` | 数字 | `getDamage()` | `double` |
| `vehicle` | 实体摘要 | `getVehicle()` | `org.bukkit.entity.Vehicle` |

<a id="event-org-bukkit-event-vehicle-vehicledestroyevent"></a>
### VehicleDestroyEvent

- Java 类：`org.bukkit.event.vehicle.VehicleDestroyEvent`；父类：`org.bukkit.event.vehicle.VehicleEvent`。
- Python 订阅：`@bridge.on("VehicleDestroyEvent")`；也可使用 `Events.VEHICLE_DESTROY`。
- 可取消：是；关联玩家：无已知玩家 getter。
- [Paper 官方 Javadoc](https://jd.papermc.io/paper/1.16.5/org/bukkit/event/vehicle/VehicleDestroyEvent.html)：事件含义、触发条件和 Java API。

| `data` 字段 | JSON 类型 | Java getter | Java 返回类型 |
| --- | --- | --- | --- |
| `attacker` | 实体摘要 | `getAttacker()` | `org.bukkit.entity.Entity` |
| `vehicle` | 实体摘要 | `getVehicle()` | `org.bukkit.entity.Vehicle` |

<a id="event-org-bukkit-event-vehicle-vehicleenterevent"></a>
### VehicleEnterEvent

- Java 类：`org.bukkit.event.vehicle.VehicleEnterEvent`；父类：`org.bukkit.event.vehicle.VehicleEvent`。
- Python 订阅：`@bridge.on("VehicleEnterEvent")`；也可使用 `Events.VEHICLE_ENTER`。
- 可取消：是；关联玩家：无已知玩家 getter。
- [Paper 官方 Javadoc](https://jd.papermc.io/paper/1.16.5/org/bukkit/event/vehicle/VehicleEnterEvent.html)：事件含义、触发条件和 Java API。

| `data` 字段 | JSON 类型 | Java getter | Java 返回类型 |
| --- | --- | --- | --- |
| `entered` | 实体摘要 | `getEntered()` | `org.bukkit.entity.Entity` |
| `vehicle` | 实体摘要 | `getVehicle()` | `org.bukkit.entity.Vehicle` |

<a id="event-org-bukkit-event-vehicle-vehicleentitycollisionevent"></a>
### VehicleEntityCollisionEvent

- Java 类：`org.bukkit.event.vehicle.VehicleEntityCollisionEvent`；父类：`org.bukkit.event.vehicle.VehicleCollisionEvent`。
- Python 订阅：`@bridge.on("VehicleEntityCollisionEvent")`；也可使用 `Events.VEHICLE_ENTITY_COLLISION`。
- 可取消：是；关联玩家：可能有，取决于实际对象。
- [Paper 官方 Javadoc](https://jd.papermc.io/paper/1.16.5/org/bukkit/event/vehicle/VehicleEntityCollisionEvent.html)：事件含义、触发条件和 Java API。

| `data` 字段 | JSON 类型 | Java getter | Java 返回类型 |
| --- | --- | --- | --- |
| `entity` | 实体摘要 | `getEntity()` | `org.bukkit.entity.Entity` |
| `vehicle` | 实体摘要 | `getVehicle()` | `org.bukkit.entity.Vehicle` |
| `collisionCancelled` | 布尔值 | `isCollisionCancelled()` | `boolean` |
| `pickupCancelled` | 布尔值 | `isPickupCancelled()` | `boolean` |

<a id="event-org-bukkit-event-vehicle-vehicleexitevent"></a>
### VehicleExitEvent

- Java 类：`org.bukkit.event.vehicle.VehicleExitEvent`；父类：`org.bukkit.event.vehicle.VehicleEvent`。
- Python 订阅：`@bridge.on("VehicleExitEvent")`；也可使用 `Events.VEHICLE_EXIT`。
- 可取消：是；关联玩家：无已知玩家 getter。
- [Paper 官方 Javadoc](https://jd.papermc.io/paper/1.16.5/org/bukkit/event/vehicle/VehicleExitEvent.html)：事件含义、触发条件和 Java API。

| `data` 字段 | JSON 类型 | Java getter | Java 返回类型 |
| --- | --- | --- | --- |
| `exited` | 实体摘要 | `getExited()` | `org.bukkit.entity.LivingEntity` |
| `vehicle` | 实体摘要 | `getVehicle()` | `org.bukkit.entity.Vehicle` |
| `cancellable` | 布尔值 | `isCancellable()` | `boolean` |

<a id="event-org-bukkit-event-vehicle-vehiclemoveevent"></a>
### VehicleMoveEvent

- Java 类：`org.bukkit.event.vehicle.VehicleMoveEvent`；父类：`org.bukkit.event.vehicle.VehicleEvent`。
- Python 订阅：`@bridge.on("VehicleMoveEvent")`；也可使用 `Events.VEHICLE_MOVE`。
- 可取消：否；关联玩家：无已知玩家 getter。
- [Paper 官方 Javadoc](https://jd.papermc.io/paper/1.16.5/org/bukkit/event/vehicle/VehicleMoveEvent.html)：事件含义、触发条件和 Java API。

| `data` 字段 | JSON 类型 | Java getter | Java 返回类型 |
| --- | --- | --- | --- |
| `from` | 位置摘要 | `getFrom()` | `org.bukkit.Location` |
| `to` | 位置摘要 | `getTo()` | `org.bukkit.Location` |
| `vehicle` | 实体摘要 | `getVehicle()` | `org.bukkit.entity.Vehicle` |

<a id="event-org-bukkit-event-vehicle-vehicleupdateevent"></a>
### VehicleUpdateEvent

- Java 类：`org.bukkit.event.vehicle.VehicleUpdateEvent`；父类：`org.bukkit.event.vehicle.VehicleEvent`。
- Python 订阅：`@bridge.on("VehicleUpdateEvent")`；也可使用 `Events.VEHICLE_UPDATE`。
- 可取消：否；关联玩家：无已知玩家 getter。
- [Paper 官方 Javadoc](https://jd.papermc.io/paper/1.16.5/org/bukkit/event/vehicle/VehicleUpdateEvent.html)：事件含义、触发条件和 Java API。

| `data` 字段 | JSON 类型 | Java getter | Java 返回类型 |
| --- | --- | --- | --- |
| `vehicle` | 实体摘要 | `getVehicle()` | `org.bukkit.entity.Vehicle` |

<a id="category-weather"></a>
## 天气 / weather

| 事件 | Python `type` | `data` 候选字段数 | 可取消 |
| --- | --- | ---: | --- |
| [LightningStrikeEvent](#event-org-bukkit-event-weather-lightningstrikeevent) | `LightningStrikeEvent` | 3 | 是 |
| [ThunderChangeEvent](#event-org-bukkit-event-weather-thunderchangeevent) | `ThunderChangeEvent` | 2 | 是 |
| [WeatherChangeEvent](#event-org-bukkit-event-weather-weatherchangeevent) | `WeatherChangeEvent` | 2 | 是 |

<a id="event-org-bukkit-event-weather-lightningstrikeevent"></a>
### LightningStrikeEvent

- Java 类：`org.bukkit.event.weather.LightningStrikeEvent`；父类：`org.bukkit.event.weather.WeatherEvent`。
- Python 订阅：`@bridge.on("LightningStrikeEvent")`；也可使用 `Events.LIGHTNING_STRIKE`。
- 可取消：是；关联玩家：无已知玩家 getter。
- [Paper 官方 Javadoc](https://jd.papermc.io/paper/1.16.5/org/bukkit/event/weather/LightningStrikeEvent.html)：事件含义、触发条件和 Java API。

| `data` 字段 | JSON 类型 | Java getter | Java 返回类型 |
| --- | --- | --- | --- |
| `cause` | 字符串 | `getCause()` | `org.bukkit.event.weather.LightningStrikeEvent$Cause` |
| `lightning` | 实体摘要 | `getLightning()` | `org.bukkit.entity.LightningStrike` |
| `world` | 世界摘要 | `getWorld()` | `org.bukkit.World` |

<a id="event-org-bukkit-event-weather-thunderchangeevent"></a>
### ThunderChangeEvent

- Java 类：`org.bukkit.event.weather.ThunderChangeEvent`；父类：`org.bukkit.event.weather.WeatherEvent`。
- Python 订阅：`@bridge.on("ThunderChangeEvent")`；也可使用 `Events.THUNDER_CHANGE`。
- 可取消：是；关联玩家：无已知玩家 getter。
- [Paper 官方 Javadoc](https://jd.papermc.io/paper/1.16.5/org/bukkit/event/weather/ThunderChangeEvent.html)：事件含义、触发条件和 Java API。

| `data` 字段 | JSON 类型 | Java getter | Java 返回类型 |
| --- | --- | --- | --- |
| `cause` | 字符串 | `getCause()` | `org.bukkit.event.weather.ThunderChangeEvent$Cause` |
| `world` | 世界摘要 | `getWorld()` | `org.bukkit.World` |

<a id="event-org-bukkit-event-weather-weatherchangeevent"></a>
### WeatherChangeEvent

- Java 类：`org.bukkit.event.weather.WeatherChangeEvent`；父类：`org.bukkit.event.weather.WeatherEvent`。
- Python 订阅：`@bridge.on("WeatherChangeEvent")`；也可使用 `Events.WEATHER_CHANGE`。
- 可取消：是；关联玩家：无已知玩家 getter。
- [Paper 官方 Javadoc](https://jd.papermc.io/paper/1.16.5/org/bukkit/event/weather/WeatherChangeEvent.html)：事件含义、触发条件和 Java API。

| `data` 字段 | JSON 类型 | Java getter | Java 返回类型 |
| --- | --- | --- | --- |
| `cause` | 字符串 | `getCause()` | `org.bukkit.event.weather.WeatherChangeEvent$Cause` |
| `world` | 世界摘要 | `getWorld()` | `org.bukkit.World` |

<a id="category-world"></a>
## 世界 / world

| 事件 | Python `type` | `data` 候选字段数 | 可取消 |
| --- | --- | ---: | --- |
| [ChunkLoadEvent](#event-org-bukkit-event-world-chunkloadevent) | `ChunkLoadEvent` | 2 | 否 |
| [ChunkPopulateEvent](#event-org-bukkit-event-world-chunkpopulateevent) | `ChunkPopulateEvent` | 1 | 否 |
| [ChunkUnloadEvent](#event-org-bukkit-event-world-chunkunloadevent) | `ChunkUnloadEvent` | 2 | 否 |
| [LootGenerateEvent](#event-org-bukkit-event-world-lootgenerateevent) | `LootGenerateEvent` | 3 | 是 |
| [PortalCreateEvent](#event-org-bukkit-event-world-portalcreateevent) | `PortalCreateEvent` | 3 | 是 |
| [SpawnChangeEvent](#event-org-bukkit-event-world-spawnchangeevent) | `SpawnChangeEvent` | 2 | 否 |
| [StructureGrowEvent](#event-org-bukkit-event-world-structuregrowevent) | `StructureGrowEvent` | 4 | 是 |
| [StructureLocateEvent](#event-io-papermc-paper-event-world-structurelocateevent) | `StructureLocateEvent` | 4 | 是 |
| [TimeSkipEvent](#event-org-bukkit-event-world-timeskipevent) | `TimeSkipEvent` | 3 | 是 |
| [WorldBorderBoundsChangeEvent](#event-io-papermc-paper-event-world-border-worldborderboundschangeevent) | `WorldBorderBoundsChangeEvent` | 5 | 是 |
| [WorldBorderBoundsChangeFinishEvent](#event-io-papermc-paper-event-world-border-worldborderboundschangefinishevent) | `WorldBorderBoundsChangeFinishEvent` | 4 | 否 |
| [WorldBorderCenterChangeEvent](#event-io-papermc-paper-event-world-border-worldbordercenterchangeevent) | `WorldBorderCenterChangeEvent` | 3 | 是 |
| [WorldGameRuleChangeEvent](#event-io-papermc-paper-event-world-worldgamerulechangeevent) | `WorldGameRuleChangeEvent` | 2 | 是 |
| [WorldInitEvent](#event-org-bukkit-event-world-worldinitevent) | `WorldInitEvent` | 1 | 否 |
| [WorldLoadEvent](#event-org-bukkit-event-world-worldloadevent) | `WorldLoadEvent` | 1 | 否 |
| [WorldSaveEvent](#event-org-bukkit-event-world-worldsaveevent) | `WorldSaveEvent` | 1 | 否 |
| [WorldUnloadEvent](#event-org-bukkit-event-world-worldunloadevent) | `WorldUnloadEvent` | 1 | 是 |

<a id="event-org-bukkit-event-world-chunkloadevent"></a>
### ChunkLoadEvent

- Java 类：`org.bukkit.event.world.ChunkLoadEvent`；父类：`org.bukkit.event.world.ChunkEvent`。
- Python 订阅：`@bridge.on("ChunkLoadEvent")`；也可使用 `Events.CHUNK_LOAD`。
- 可取消：否；关联玩家：无已知玩家 getter。
- [Paper 官方 Javadoc](https://jd.papermc.io/paper/1.16.5/org/bukkit/event/world/ChunkLoadEvent.html)：事件含义、触发条件和 Java API。

| `data` 字段 | JSON 类型 | Java getter | Java 返回类型 |
| --- | --- | --- | --- |
| `world` | 世界摘要 | `getWorld()` | `org.bukkit.World` |
| `newChunk` | 布尔值 | `isNewChunk()` | `boolean` |

<a id="event-org-bukkit-event-world-chunkpopulateevent"></a>
### ChunkPopulateEvent

- Java 类：`org.bukkit.event.world.ChunkPopulateEvent`；父类：`org.bukkit.event.world.ChunkEvent`。
- Python 订阅：`@bridge.on("ChunkPopulateEvent")`；也可使用 `Events.CHUNK_POPULATE`。
- 可取消：否；关联玩家：无已知玩家 getter。
- [Paper 官方 Javadoc](https://jd.papermc.io/paper/1.16.5/org/bukkit/event/world/ChunkPopulateEvent.html)：事件含义、触发条件和 Java API。

| `data` 字段 | JSON 类型 | Java getter | Java 返回类型 |
| --- | --- | --- | --- |
| `world` | 世界摘要 | `getWorld()` | `org.bukkit.World` |

<a id="event-org-bukkit-event-world-chunkunloadevent"></a>
### ChunkUnloadEvent

- Java 类：`org.bukkit.event.world.ChunkUnloadEvent`；父类：`org.bukkit.event.world.ChunkEvent`。
- Python 订阅：`@bridge.on("ChunkUnloadEvent")`；也可使用 `Events.CHUNK_UNLOAD`。
- 可取消：否；关联玩家：无已知玩家 getter。
- [Paper 官方 Javadoc](https://jd.papermc.io/paper/1.16.5/org/bukkit/event/world/ChunkUnloadEvent.html)：事件含义、触发条件和 Java API。

| `data` 字段 | JSON 类型 | Java getter | Java 返回类型 |
| --- | --- | --- | --- |
| `world` | 世界摘要 | `getWorld()` | `org.bukkit.World` |
| `saveChunk` | 布尔值 | `isSaveChunk()` | `boolean` |

<a id="event-org-bukkit-event-world-lootgenerateevent"></a>
### LootGenerateEvent

- Java 类：`org.bukkit.event.world.LootGenerateEvent`；父类：`org.bukkit.event.world.WorldEvent`。
- Python 订阅：`@bridge.on("LootGenerateEvent")`；也可使用 `Events.LOOT_GENERATE`。
- 可取消：是；关联玩家：可能有，取决于实际对象。
- [Paper 官方 Javadoc](https://jd.papermc.io/paper/1.16.5/org/bukkit/event/world/LootGenerateEvent.html)：事件含义、触发条件和 Java API。

| `data` 字段 | JSON 类型 | Java getter | Java 返回类型 |
| --- | --- | --- | --- |
| `entity` | 实体摘要 | `getEntity()` | `org.bukkit.entity.Entity` |
| `world` | 世界摘要 | `getWorld()` | `org.bukkit.World` |
| `plugin` | 布尔值 | `isPlugin()` | `boolean` |

<a id="event-org-bukkit-event-world-portalcreateevent"></a>
### PortalCreateEvent

- Java 类：`org.bukkit.event.world.PortalCreateEvent`；父类：`org.bukkit.event.world.WorldEvent`。
- Python 订阅：`@bridge.on("PortalCreateEvent")`；也可使用 `Events.PORTAL_CREATE`。
- 可取消：是；关联玩家：可能有，取决于实际对象。
- [Paper 官方 Javadoc](https://jd.papermc.io/paper/1.16.5/org/bukkit/event/world/PortalCreateEvent.html)：事件含义、触发条件和 Java API。

| `data` 字段 | JSON 类型 | Java getter | Java 返回类型 |
| --- | --- | --- | --- |
| `entity` | 实体摘要 | `getEntity()` | `org.bukkit.entity.Entity` |
| `reason` | 字符串 | `getReason()` | `org.bukkit.event.world.PortalCreateEvent$CreateReason` |
| `world` | 世界摘要 | `getWorld()` | `org.bukkit.World` |

<a id="event-org-bukkit-event-world-spawnchangeevent"></a>
### SpawnChangeEvent

- Java 类：`org.bukkit.event.world.SpawnChangeEvent`；父类：`org.bukkit.event.world.WorldEvent`。
- Python 订阅：`@bridge.on("SpawnChangeEvent")`；也可使用 `Events.SPAWN_CHANGE`。
- 可取消：否；关联玩家：无已知玩家 getter。
- [Paper 官方 Javadoc](https://jd.papermc.io/paper/1.16.5/org/bukkit/event/world/SpawnChangeEvent.html)：事件含义、触发条件和 Java API。

| `data` 字段 | JSON 类型 | Java getter | Java 返回类型 |
| --- | --- | --- | --- |
| `previousLocation` | 位置摘要 | `getPreviousLocation()` | `org.bukkit.Location` |
| `world` | 世界摘要 | `getWorld()` | `org.bukkit.World` |

<a id="event-org-bukkit-event-world-structuregrowevent"></a>
### StructureGrowEvent

- Java 类：`org.bukkit.event.world.StructureGrowEvent`；父类：`org.bukkit.event.world.WorldEvent`。
- Python 订阅：`@bridge.on("StructureGrowEvent")`；也可使用 `Events.STRUCTURE_GROW`。
- 可取消：是；关联玩家：可能有，取决于实际对象。
- [Paper 官方 Javadoc](https://jd.papermc.io/paper/1.16.5/org/bukkit/event/world/StructureGrowEvent.html)：事件含义、触发条件和 Java API。

| `data` 字段 | JSON 类型 | Java getter | Java 返回类型 |
| --- | --- | --- | --- |
| `location` | 位置摘要 | `getLocation()` | `org.bukkit.Location` |
| `species` | 字符串 | `getSpecies()` | `org.bukkit.TreeType` |
| `world` | 世界摘要 | `getWorld()` | `org.bukkit.World` |
| `fromBonemeal` | 布尔值 | `isFromBonemeal()` | `boolean` |

<a id="event-io-papermc-paper-event-world-structurelocateevent"></a>
### StructureLocateEvent

- Java 类：`io.papermc.paper.event.world.StructureLocateEvent`；父类：`org.bukkit.event.world.WorldEvent`。
- Python 订阅：`@bridge.on("StructureLocateEvent")`；也可使用 `Events.STRUCTURE_LOCATE`。
- 可取消：是；关联玩家：无已知玩家 getter。
- [Paper 官方 Javadoc](https://jd.papermc.io/paper/1.16.5/io/papermc/paper/event/world/StructureLocateEvent.html)：事件含义、触发条件和 Java API。

| `data` 字段 | JSON 类型 | Java getter | Java 返回类型 |
| --- | --- | --- | --- |
| `origin` | 位置摘要 | `getOrigin()` | `org.bukkit.Location` |
| `radius` | 数字 | `getRadius()` | `int` |
| `result` | 位置摘要 | `getResult()` | `org.bukkit.Location` |
| `world` | 世界摘要 | `getWorld()` | `org.bukkit.World` |

<a id="event-org-bukkit-event-world-timeskipevent"></a>
### TimeSkipEvent

- Java 类：`org.bukkit.event.world.TimeSkipEvent`；父类：`org.bukkit.event.world.WorldEvent`。
- Python 订阅：`@bridge.on("TimeSkipEvent")`；也可使用 `Events.TIME_SKIP`。
- 可取消：是；关联玩家：无已知玩家 getter。
- [Paper 官方 Javadoc](https://jd.papermc.io/paper/1.16.5/org/bukkit/event/world/TimeSkipEvent.html)：事件含义、触发条件和 Java API。

| `data` 字段 | JSON 类型 | Java getter | Java 返回类型 |
| --- | --- | --- | --- |
| `skipAmount` | 数字 | `getSkipAmount()` | `long` |
| `skipReason` | 字符串 | `getSkipReason()` | `org.bukkit.event.world.TimeSkipEvent$SkipReason` |
| `world` | 世界摘要 | `getWorld()` | `org.bukkit.World` |

<a id="event-io-papermc-paper-event-world-border-worldborderboundschangeevent"></a>
### WorldBorderBoundsChangeEvent

- Java 类：`io.papermc.paper.event.world.border.WorldBorderBoundsChangeEvent`；父类：`io.papermc.paper.event.world.border.WorldBorderEvent`。
- Python 订阅：`@bridge.on("WorldBorderBoundsChangeEvent")`；也可使用 `Events.WORLD_BORDER_BOUNDS_CHANGE`。
- 可取消：是；关联玩家：无已知玩家 getter。
- [Paper 官方 Javadoc](https://jd.papermc.io/paper/1.16.5/io/papermc/paper/event/world/border/WorldBorderBoundsChangeEvent.html)：事件含义、触发条件和 Java API。

| `data` 字段 | JSON 类型 | Java getter | Java 返回类型 |
| --- | --- | --- | --- |
| `duration` | 数字 | `getDuration()` | `long` |
| `newSize` | 数字 | `getNewSize()` | `double` |
| `oldSize` | 数字 | `getOldSize()` | `double` |
| `type` | 字符串 | `getType()` | `io.papermc.paper.event.world.border.WorldBorderBoundsChangeEvent$Type` |
| `world` | 世界摘要 | `getWorld()` | `org.bukkit.World` |

<a id="event-io-papermc-paper-event-world-border-worldborderboundschangefinishevent"></a>
### WorldBorderBoundsChangeFinishEvent

- Java 类：`io.papermc.paper.event.world.border.WorldBorderBoundsChangeFinishEvent`；父类：`io.papermc.paper.event.world.border.WorldBorderEvent`。
- Python 订阅：`@bridge.on("WorldBorderBoundsChangeFinishEvent")`；也可使用 `Events.WORLD_BORDER_BOUNDS_CHANGE_FINISH`。
- 可取消：否；关联玩家：无已知玩家 getter。
- [Paper 官方 Javadoc](https://jd.papermc.io/paper/1.16.5/io/papermc/paper/event/world/border/WorldBorderBoundsChangeFinishEvent.html)：事件含义、触发条件和 Java API。

| `data` 字段 | JSON 类型 | Java getter | Java 返回类型 |
| --- | --- | --- | --- |
| `duration` | 数字 | `getDuration()` | `double` |
| `newSize` | 数字 | `getNewSize()` | `double` |
| `oldSize` | 数字 | `getOldSize()` | `double` |
| `world` | 世界摘要 | `getWorld()` | `org.bukkit.World` |

<a id="event-io-papermc-paper-event-world-border-worldbordercenterchangeevent"></a>
### WorldBorderCenterChangeEvent

- Java 类：`io.papermc.paper.event.world.border.WorldBorderCenterChangeEvent`；父类：`io.papermc.paper.event.world.border.WorldBorderEvent`。
- Python 订阅：`@bridge.on("WorldBorderCenterChangeEvent")`；也可使用 `Events.WORLD_BORDER_CENTER_CHANGE`。
- 可取消：是；关联玩家：无已知玩家 getter。
- [Paper 官方 Javadoc](https://jd.papermc.io/paper/1.16.5/io/papermc/paper/event/world/border/WorldBorderCenterChangeEvent.html)：事件含义、触发条件和 Java API。

| `data` 字段 | JSON 类型 | Java getter | Java 返回类型 |
| --- | --- | --- | --- |
| `newCenter` | 位置摘要 | `getNewCenter()` | `org.bukkit.Location` |
| `oldCenter` | 位置摘要 | `getOldCenter()` | `org.bukkit.Location` |
| `world` | 世界摘要 | `getWorld()` | `org.bukkit.World` |

<a id="event-io-papermc-paper-event-world-worldgamerulechangeevent"></a>
### WorldGameRuleChangeEvent

- Java 类：`io.papermc.paper.event.world.WorldGameRuleChangeEvent`；父类：`org.bukkit.event.world.WorldEvent`。
- Python 订阅：`@bridge.on("WorldGameRuleChangeEvent")`；也可使用 `Events.WORLD_GAME_RULE_CHANGE`。
- 可取消：是；关联玩家：无已知玩家 getter。
- [Paper 官方 Javadoc](https://jd.papermc.io/paper/1.16.5/io/papermc/paper/event/world/WorldGameRuleChangeEvent.html)：事件含义、触发条件和 Java API。

| `data` 字段 | JSON 类型 | Java getter | Java 返回类型 |
| --- | --- | --- | --- |
| `value` | 字符串 | `getValue()` | `java.lang.String` |
| `world` | 世界摘要 | `getWorld()` | `org.bukkit.World` |

<a id="event-org-bukkit-event-world-worldinitevent"></a>
### WorldInitEvent

- Java 类：`org.bukkit.event.world.WorldInitEvent`；父类：`org.bukkit.event.world.WorldEvent`。
- Python 订阅：`@bridge.on("WorldInitEvent")`；也可使用 `Events.WORLD_INIT`。
- 可取消：否；关联玩家：无已知玩家 getter。
- [Paper 官方 Javadoc](https://jd.papermc.io/paper/1.16.5/org/bukkit/event/world/WorldInitEvent.html)：事件含义、触发条件和 Java API。

| `data` 字段 | JSON 类型 | Java getter | Java 返回类型 |
| --- | --- | --- | --- |
| `world` | 世界摘要 | `getWorld()` | `org.bukkit.World` |

<a id="event-org-bukkit-event-world-worldloadevent"></a>
### WorldLoadEvent

- Java 类：`org.bukkit.event.world.WorldLoadEvent`；父类：`org.bukkit.event.world.WorldEvent`。
- Python 订阅：`@bridge.on("WorldLoadEvent")`；也可使用 `Events.WORLD_LOAD`。
- 可取消：否；关联玩家：无已知玩家 getter。
- [Paper 官方 Javadoc](https://jd.papermc.io/paper/1.16.5/org/bukkit/event/world/WorldLoadEvent.html)：事件含义、触发条件和 Java API。

| `data` 字段 | JSON 类型 | Java getter | Java 返回类型 |
| --- | --- | --- | --- |
| `world` | 世界摘要 | `getWorld()` | `org.bukkit.World` |

<a id="event-org-bukkit-event-world-worldsaveevent"></a>
### WorldSaveEvent

- Java 类：`org.bukkit.event.world.WorldSaveEvent`；父类：`org.bukkit.event.world.WorldEvent`。
- Python 订阅：`@bridge.on("WorldSaveEvent")`；也可使用 `Events.WORLD_SAVE`。
- 可取消：否；关联玩家：无已知玩家 getter。
- [Paper 官方 Javadoc](https://jd.papermc.io/paper/1.16.5/org/bukkit/event/world/WorldSaveEvent.html)：事件含义、触发条件和 Java API。

| `data` 字段 | JSON 类型 | Java getter | Java 返回类型 |
| --- | --- | --- | --- |
| `world` | 世界摘要 | `getWorld()` | `org.bukkit.World` |

<a id="event-org-bukkit-event-world-worldunloadevent"></a>
### WorldUnloadEvent

- Java 类：`org.bukkit.event.world.WorldUnloadEvent`；父类：`org.bukkit.event.world.WorldEvent`。
- Python 订阅：`@bridge.on("WorldUnloadEvent")`；也可使用 `Events.WORLD_UNLOAD`。
- 可取消：是；关联玩家：无已知玩家 getter。
- [Paper 官方 Javadoc](https://jd.papermc.io/paper/1.16.5/org/bukkit/event/world/WorldUnloadEvent.html)：事件含义、触发条件和 Java API。

| `data` 字段 | JSON 类型 | Java getter | Java 返回类型 |
| --- | --- | --- | --- |
| `world` | 世界摘要 | `getWorld()` | `org.bukkit.World` |
