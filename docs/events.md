# PaperPyBridge Event Reference: Paper 1.16.5

This page lists **333 concrete event classes** that the plugin can forward, based on its `paper-events.txt` catalog and current `EventSnapshot` serialization rules.
They share **292 HandlerLists**. Classes sharing a list need only one listener registration, so this count is smaller than the class count.
Only chat, player join, and player quit are forwarded by default. Add other events to the Paper plugin's `events.include`; listing an event here does not enable it.
Follow each event's official Paper Javadoc link for its meaning and trigger conditions. This page documents what Python actually receives.

## Common event format

```json
{"protocol_version":1,"type":"PlayerMoveEvent","event":"org.bukkit.event.player.PlayerMoveEvent","name":"PlayerMoveEvent","server":"survival","asynchronous":false,"timestamp_ms":1234567890000,"cancelled":false,"player":{"uuid":"...","name":"Steve"},"data":{"from":{"world":"world","x":1,"y":64,"z":2,"yaw":0,"pitch":0},"to":{"world":"world","x":2,"y":64,"z":2,"yaw":0,"pitch":0}}}
```

- `protocol_version`, `type`, `event`, `name`, `server`, `asynchronous`, `timestamp_ms`, and `data` are always produced.
- `cancelled` appears only for `Cancellable` events; `player` appears only when a player is actually associated. String `data.message` is also copied to top-level `message`.
- `type` is the Python subscription name. Chat, join, and quit keep the aliases `chat`, `join`, and `quit`; other events use the simple class name. You can also subscribe by full class name or `*`.
- `data` comes from public zero-argument `get...()`/`is...()` methods with supported return types. Null or failing getters are omitted. A snapshot has at most 24 fields and 4096 bytes; strings are limited to 512 characters, and trailing fields are removed if needed.
- Worlds, locations, blocks, entities, and items become **summary objects**, not live Bukkit objects. Python cannot synchronously cancel or mutate a forwarded event.

| Summary type | JSON properties |
| --- | --- |
| `world` | `name`, `uuid` |
| `location` | optional `world`, `x`, `y`, `z`, `yaw`, `pitch` |
| `block` | `world`, `x`, `y`, `z`, `type` |
| `entity` | `uuid`, `type`, optional player `name` |
| `item` | `type`, `amount` |

## Package index

| Package category | Events |
| --- | ---: |
| [`block`](#category-block) | 45 |
| [`command`](#category-command) | 1 |
| [`enchantment`](#category-enchantment) | 2 |
| [`entity`](#category-entity) | 107 |
| [`hanging`](#category-hanging) | 3 |
| [`inventory`](#category-inventory) | 21 |
| [`packet`](#category-packet) | 2 |
| [`player`](#category-player) | 95 |
| [`profile`](#category-profile) | 5 |
| [`raid`](#category-raid) | 4 |
| [`server`](#category-server) | 19 |
| [`vehicle`](#category-vehicle) | 9 |
| [`weather`](#category-weather) | 3 |
| [`world`](#category-world) | 17 |

<a id="category-block"></a>
## block

| Event | Python `type` | possible `data` fields | Cancellable |
| --- | --- | ---: | --- |
| [AnvilDamagedEvent](#event-com-destroystokyo-paper-event-block-anvildamagedevent) | `AnvilDamagedEvent` | 2 | Yes |
| [BeaconActivatedEvent](#event-io-papermc-paper-event-block-beaconactivatedevent) | `BeaconActivatedEvent` | 1 | No |
| [BeaconDeactivatedEvent](#event-io-papermc-paper-event-block-beacondeactivatedevent) | `BeaconDeactivatedEvent` | 1 | No |
| [BeaconEffectEvent](#event-com-destroystokyo-paper-event-block-beaconeffectevent) | `BeaconEffectEvent` | 2 | Yes |
| [BellRevealRaiderEvent](#event-io-papermc-paper-event-block-bellrevealraiderevent) | `BellRevealRaiderEvent` | 2 | Yes |
| [BellRingEvent](#event-io-papermc-paper-event-block-bellringevent) | `BellRingEvent` | 2 | Yes |
| [BlockBreakEvent](#event-org-bukkit-event-block-blockbreakevent) | `BlockBreakEvent` | 3 | Yes |
| [BlockBurnEvent](#event-org-bukkit-event-block-blockburnevent) | `BlockBurnEvent` | 2 | Yes |
| [BlockCanBuildEvent](#event-org-bukkit-event-block-blockcanbuildevent) | `BlockCanBuildEvent` | 3 | No |
| [BlockCookEvent](#event-org-bukkit-event-block-blockcookevent) | `BlockCookEvent` | 3 | Yes |
| [BlockDamageEvent](#event-org-bukkit-event-block-blockdamageevent) | `BlockDamageEvent` | 3 | Yes |
| [BlockDestroyEvent](#event-com-destroystokyo-paper-event-block-blockdestroyevent) | `BlockDestroyEvent` | 1 | Yes |
| [BlockDispenseArmorEvent](#event-org-bukkit-event-block-blockdispensearmorevent) | `BlockDispenseArmorEvent` | 3 | Yes |
| [BlockDispenseEvent](#event-org-bukkit-event-block-blockdispenseevent) | `BlockDispenseEvent` | 2 | Yes |
| [BlockDropItemEvent](#event-org-bukkit-event-block-blockdropitemevent) | `BlockDropItemEvent` | 1 | Yes |
| [BlockExpEvent](#event-org-bukkit-event-block-blockexpevent) | `BlockExpEvent` | 2 | No |
| [BlockExplodeEvent](#event-org-bukkit-event-block-blockexplodeevent) | `BlockExplodeEvent` | 2 | Yes |
| [BlockFadeEvent](#event-org-bukkit-event-block-blockfadeevent) | `BlockFadeEvent` | 1 | Yes |
| [BlockFailedDispenseEvent](#event-io-papermc-paper-event-block-blockfaileddispenseevent) | `BlockFailedDispenseEvent` | 1 | No |
| [BlockFertilizeEvent](#event-org-bukkit-event-block-blockfertilizeevent) | `BlockFertilizeEvent` | 1 | Yes |
| [BlockFormEvent](#event-org-bukkit-event-block-blockformevent) | `BlockFormEvent` | 1 | Yes |
| [BlockFromToEvent](#event-org-bukkit-event-block-blockfromtoevent) | `BlockFromToEvent` | 3 | Yes |
| [BlockGrowEvent](#event-org-bukkit-event-block-blockgrowevent) | `BlockGrowEvent` | 1 | Yes |
| [BlockIgniteEvent](#event-org-bukkit-event-block-blockigniteevent) | `BlockIgniteEvent` | 4 | Yes |
| [BlockMultiPlaceEvent](#event-org-bukkit-event-block-blockmultiplaceevent) | `BlockMultiPlaceEvent` | 5 | Yes |
| [BlockPhysicsEvent](#event-org-bukkit-event-block-blockphysicsevent) | `BlockPhysicsEvent` | 3 | Yes |
| [BlockPistonExtendEvent](#event-org-bukkit-event-block-blockpistonextendevent) | `BlockPistonExtendEvent` | 4 | Yes |
| [BlockPistonRetractEvent](#event-org-bukkit-event-block-blockpistonretractevent) | `BlockPistonRetractEvent` | 4 | Yes |
| [BlockPlaceEvent](#event-org-bukkit-event-block-blockplaceevent) | `BlockPlaceEvent` | 5 | Yes |
| [BlockPreDispenseEvent](#event-io-papermc-paper-event-block-blockpredispenseevent) | `BlockPreDispenseEvent` | 3 | Yes |
| [BlockRedstoneEvent](#event-org-bukkit-event-block-blockredstoneevent) | `BlockRedstoneEvent` | 3 | No |
| [BlockShearEntityEvent](#event-org-bukkit-event-block-blockshearentityevent) | `BlockShearEntityEvent` | 3 | Yes |
| [BlockSpreadEvent](#event-org-bukkit-event-block-blockspreadevent) | `BlockSpreadEvent` | 2 | Yes |
| [CauldronLevelChangeEvent](#event-org-bukkit-event-block-cauldronlevelchangeevent) | `CauldronLevelChangeEvent` | 5 | Yes |
| [DragonEggFormEvent](#event-io-papermc-paper-event-block-dragoneggformevent) | `DragonEggFormEvent` | 1 | Yes |
| [EntityBlockFormEvent](#event-org-bukkit-event-block-entityblockformevent) | `EntityBlockFormEvent` | 2 | Yes |
| [FluidLevelChangeEvent](#event-org-bukkit-event-block-fluidlevelchangeevent) | `FluidLevelChangeEvent` | 1 | Yes |
| [LeavesDecayEvent](#event-org-bukkit-event-block-leavesdecayevent) | `LeavesDecayEvent` | 1 | Yes |
| [MoistureChangeEvent](#event-org-bukkit-event-block-moisturechangeevent) | `MoistureChangeEvent` | 1 | Yes |
| [NotePlayEvent](#event-org-bukkit-event-block-noteplayevent) | `NotePlayEvent` | 2 | Yes |
| [PlayerShearBlockEvent](#event-io-papermc-paper-event-block-playershearblockevent) | `PlayerShearBlockEvent` | 3 | Yes |
| [SignChangeEvent](#event-org-bukkit-event-block-signchangeevent) | `SignChangeEvent` | 1 | Yes |
| [SpongeAbsorbEvent](#event-org-bukkit-event-block-spongeabsorbevent) | `SpongeAbsorbEvent` | 1 | Yes |
| [TargetHitEvent](#event-io-papermc-paper-event-block-targethitevent) | `TargetHitEvent` | 6 | Yes |
| [TNTPrimeEvent](#event-com-destroystokyo-paper-event-block-tntprimeevent) | `TNTPrimeEvent` | 3 | Yes |

<a id="event-com-destroystokyo-paper-event-block-anvildamagedevent"></a>
### AnvilDamagedEvent

- Java class: `com.destroystokyo.paper.event.block.AnvilDamagedEvent`; parent: `org.bukkit.event.inventory.InventoryEvent`.
- Python subscription: `@bridge.on("AnvilDamagedEvent")`; `Events.ANVIL_DAMAGED` also works.
- Cancellable: yes; player: no known player getter.
- [Official Paper Javadoc](https://jd.papermc.io/paper/1.16.5/com/destroystokyo/paper/event/block/AnvilDamagedEvent.html) for meaning, trigger conditions, and Java API.

| `data` field | JSON type | Java getter | Java return type |
| --- | --- | --- | --- |
| `damageState` | string | `getDamageState()` | `com.destroystokyo.paper.event.block.AnvilDamagedEvent$DamageState` |
| `breaking` | boolean | `isBreaking()` | `boolean` |

<a id="event-io-papermc-paper-event-block-beaconactivatedevent"></a>
### BeaconActivatedEvent

- Java class: `io.papermc.paper.event.block.BeaconActivatedEvent`; parent: `org.bukkit.event.block.BlockEvent`.
- Python subscription: `@bridge.on("BeaconActivatedEvent")`; `Events.BEACON_ACTIVATED` also works.
- Cancellable: no; player: no known player getter.
- [Official Paper Javadoc](https://jd.papermc.io/paper/1.16.5/io/papermc/paper/event/block/BeaconActivatedEvent.html) for meaning, trigger conditions, and Java API.

| `data` field | JSON type | Java getter | Java return type |
| --- | --- | --- | --- |
| `block` | block summary | `getBlock()` | `org.bukkit.block.Block` |

<a id="event-io-papermc-paper-event-block-beacondeactivatedevent"></a>
### BeaconDeactivatedEvent

- Java class: `io.papermc.paper.event.block.BeaconDeactivatedEvent`; parent: `org.bukkit.event.block.BlockEvent`.
- Python subscription: `@bridge.on("BeaconDeactivatedEvent")`; `Events.BEACON_DEACTIVATED` also works.
- Cancellable: no; player: no known player getter.
- [Official Paper Javadoc](https://jd.papermc.io/paper/1.16.5/io/papermc/paper/event/block/BeaconDeactivatedEvent.html) for meaning, trigger conditions, and Java API.

| `data` field | JSON type | Java getter | Java return type |
| --- | --- | --- | --- |
| `block` | block summary | `getBlock()` | `org.bukkit.block.Block` |

<a id="event-com-destroystokyo-paper-event-block-beaconeffectevent"></a>
### BeaconEffectEvent

- Java class: `com.destroystokyo.paper.event.block.BeaconEffectEvent`; parent: `org.bukkit.event.block.BlockEvent`.
- Python subscription: `@bridge.on("BeaconEffectEvent")`; `Events.BEACON_EFFECT` also works.
- Cancellable: yes; player: possible, depending on the runtime object.
- [Official Paper Javadoc](https://jd.papermc.io/paper/1.16.5/com/destroystokyo/paper/event/block/BeaconEffectEvent.html) for meaning, trigger conditions, and Java API.

| `data` field | JSON type | Java getter | Java return type |
| --- | --- | --- | --- |
| `block` | block summary | `getBlock()` | `org.bukkit.block.Block` |
| `primary` | boolean | `isPrimary()` | `boolean` |

<a id="event-io-papermc-paper-event-block-bellrevealraiderevent"></a>
### BellRevealRaiderEvent

- Java class: `io.papermc.paper.event.block.BellRevealRaiderEvent`; parent: `org.bukkit.event.block.BlockEvent`.
- Python subscription: `@bridge.on("BellRevealRaiderEvent")`; `Events.BELL_REVEAL_RAIDER` also works.
- Cancellable: yes; player: possible, depending on the runtime object.
- [Official Paper Javadoc](https://jd.papermc.io/paper/1.16.5/io/papermc/paper/event/block/BellRevealRaiderEvent.html) for meaning, trigger conditions, and Java API.

| `data` field | JSON type | Java getter | Java return type |
| --- | --- | --- | --- |
| `block` | block summary | `getBlock()` | `org.bukkit.block.Block` |
| `entity` | entity summary | `getEntity()` | `org.bukkit.entity.Raider` |

<a id="event-io-papermc-paper-event-block-bellringevent"></a>
### BellRingEvent

- Java class: `io.papermc.paper.event.block.BellRingEvent`; parent: `org.bukkit.event.block.BlockEvent`.
- Python subscription: `@bridge.on("BellRingEvent")`; `Events.BELL_RING` also works.
- Cancellable: yes; player: possible, depending on the runtime object.
- [Official Paper Javadoc](https://jd.papermc.io/paper/1.16.5/io/papermc/paper/event/block/BellRingEvent.html) for meaning, trigger conditions, and Java API.

| `data` field | JSON type | Java getter | Java return type |
| --- | --- | --- | --- |
| `block` | block summary | `getBlock()` | `org.bukkit.block.Block` |
| `entity` | entity summary | `getEntity()` | `org.bukkit.entity.Entity` |

<a id="event-org-bukkit-event-block-blockbreakevent"></a>
### BlockBreakEvent

- Java class: `org.bukkit.event.block.BlockBreakEvent`; parent: `org.bukkit.event.block.BlockExpEvent`.
- Python subscription: `@bridge.on("BlockBreakEvent")`; `Events.BLOCK_BREAK` also works.
- Cancellable: yes; player: possible, depending on the runtime object.
- [Official Paper Javadoc](https://jd.papermc.io/paper/1.16.5/org/bukkit/event/block/BlockBreakEvent.html) for meaning, trigger conditions, and Java API.

| `data` field | JSON type | Java getter | Java return type |
| --- | --- | --- | --- |
| `block` | block summary | `getBlock()` | `org.bukkit.block.Block` |
| `expToDrop` | number | `getExpToDrop()` | `int` |
| `dropItems` | boolean | `isDropItems()` | `boolean` |

<a id="event-org-bukkit-event-block-blockburnevent"></a>
### BlockBurnEvent

- Java class: `org.bukkit.event.block.BlockBurnEvent`; parent: `org.bukkit.event.block.BlockEvent`.
- Python subscription: `@bridge.on("BlockBurnEvent")`; `Events.BLOCK_BURN` also works.
- Cancellable: yes; player: no known player getter.
- [Official Paper Javadoc](https://jd.papermc.io/paper/1.16.5/org/bukkit/event/block/BlockBurnEvent.html) for meaning, trigger conditions, and Java API.

| `data` field | JSON type | Java getter | Java return type |
| --- | --- | --- | --- |
| `block` | block summary | `getBlock()` | `org.bukkit.block.Block` |
| `ignitingBlock` | block summary | `getIgnitingBlock()` | `org.bukkit.block.Block` |

<a id="event-org-bukkit-event-block-blockcanbuildevent"></a>
### BlockCanBuildEvent

- Java class: `org.bukkit.event.block.BlockCanBuildEvent`; parent: `org.bukkit.event.block.BlockEvent`.
- Python subscription: `@bridge.on("BlockCanBuildEvent")`; `Events.BLOCK_CAN_BUILD` also works.
- Cancellable: no; player: possible, depending on the runtime object.
- [Official Paper Javadoc](https://jd.papermc.io/paper/1.16.5/org/bukkit/event/block/BlockCanBuildEvent.html) for meaning, trigger conditions, and Java API.

| `data` field | JSON type | Java getter | Java return type |
| --- | --- | --- | --- |
| `block` | block summary | `getBlock()` | `org.bukkit.block.Block` |
| `material` | string | `getMaterial()` | `org.bukkit.Material` |
| `buildable` | boolean | `isBuildable()` | `boolean` |

<a id="event-org-bukkit-event-block-blockcookevent"></a>
### BlockCookEvent

- Java class: `org.bukkit.event.block.BlockCookEvent`; parent: `org.bukkit.event.block.BlockEvent`.
- Python subscription: `@bridge.on("BlockCookEvent")`; `Events.BLOCK_COOK` also works.
- Cancellable: yes; player: no known player getter.
- [Official Paper Javadoc](https://jd.papermc.io/paper/1.16.5/org/bukkit/event/block/BlockCookEvent.html) for meaning, trigger conditions, and Java API.

| `data` field | JSON type | Java getter | Java return type |
| --- | --- | --- | --- |
| `block` | block summary | `getBlock()` | `org.bukkit.block.Block` |
| `result` | item summary | `getResult()` | `org.bukkit.inventory.ItemStack` |
| `source` | item summary | `getSource()` | `org.bukkit.inventory.ItemStack` |

<a id="event-org-bukkit-event-block-blockdamageevent"></a>
### BlockDamageEvent

- Java class: `org.bukkit.event.block.BlockDamageEvent`; parent: `org.bukkit.event.block.BlockEvent`.
- Python subscription: `@bridge.on("BlockDamageEvent")`; `Events.BLOCK_DAMAGE` also works.
- Cancellable: yes; player: possible, depending on the runtime object.
- [Official Paper Javadoc](https://jd.papermc.io/paper/1.16.5/org/bukkit/event/block/BlockDamageEvent.html) for meaning, trigger conditions, and Java API.

| `data` field | JSON type | Java getter | Java return type |
| --- | --- | --- | --- |
| `block` | block summary | `getBlock()` | `org.bukkit.block.Block` |
| `instaBreak` | boolean | `getInstaBreak()` | `boolean` |
| `itemInHand` | item summary | `getItemInHand()` | `org.bukkit.inventory.ItemStack` |

<a id="event-com-destroystokyo-paper-event-block-blockdestroyevent"></a>
### BlockDestroyEvent

- Java class: `com.destroystokyo.paper.event.block.BlockDestroyEvent`; parent: `org.bukkit.event.block.BlockEvent`.
- Python subscription: `@bridge.on("BlockDestroyEvent")`; `Events.BLOCK_DESTROY` also works.
- Cancellable: yes; player: no known player getter.
- [Official Paper Javadoc](https://jd.papermc.io/paper/1.16.5/com/destroystokyo/paper/event/block/BlockDestroyEvent.html) for meaning, trigger conditions, and Java API.

| `data` field | JSON type | Java getter | Java return type |
| --- | --- | --- | --- |
| `block` | block summary | `getBlock()` | `org.bukkit.block.Block` |

<a id="event-org-bukkit-event-block-blockdispensearmorevent"></a>
### BlockDispenseArmorEvent

- Java class: `org.bukkit.event.block.BlockDispenseArmorEvent`; parent: `org.bukkit.event.block.BlockDispenseEvent`.
- Python subscription: `@bridge.on("BlockDispenseArmorEvent")`; `Events.BLOCK_DISPENSE_ARMOR` also works.
- Cancellable: yes; player: no known player getter.
- [Official Paper Javadoc](https://jd.papermc.io/paper/1.16.5/org/bukkit/event/block/BlockDispenseArmorEvent.html) for meaning, trigger conditions, and Java API.

| `data` field | JSON type | Java getter | Java return type |
| --- | --- | --- | --- |
| `block` | block summary | `getBlock()` | `org.bukkit.block.Block` |
| `item` | item summary | `getItem()` | `org.bukkit.inventory.ItemStack` |
| `targetEntity` | entity summary | `getTargetEntity()` | `org.bukkit.entity.LivingEntity` |

<a id="event-org-bukkit-event-block-blockdispenseevent"></a>
### BlockDispenseEvent

- Java class: `org.bukkit.event.block.BlockDispenseEvent`; parent: `org.bukkit.event.block.BlockEvent`.
- Python subscription: `@bridge.on("BlockDispenseEvent")`; `Events.BLOCK_DISPENSE` also works.
- Cancellable: yes; player: no known player getter.
- [Official Paper Javadoc](https://jd.papermc.io/paper/1.16.5/org/bukkit/event/block/BlockDispenseEvent.html) for meaning, trigger conditions, and Java API.

| `data` field | JSON type | Java getter | Java return type |
| --- | --- | --- | --- |
| `block` | block summary | `getBlock()` | `org.bukkit.block.Block` |
| `item` | item summary | `getItem()` | `org.bukkit.inventory.ItemStack` |

<a id="event-org-bukkit-event-block-blockdropitemevent"></a>
### BlockDropItemEvent

- Java class: `org.bukkit.event.block.BlockDropItemEvent`; parent: `org.bukkit.event.block.BlockEvent`.
- Python subscription: `@bridge.on("BlockDropItemEvent")`; `Events.BLOCK_DROP_ITEM` also works.
- Cancellable: yes; player: possible, depending on the runtime object.
- [Official Paper Javadoc](https://jd.papermc.io/paper/1.16.5/org/bukkit/event/block/BlockDropItemEvent.html) for meaning, trigger conditions, and Java API.

| `data` field | JSON type | Java getter | Java return type |
| --- | --- | --- | --- |
| `block` | block summary | `getBlock()` | `org.bukkit.block.Block` |

<a id="event-org-bukkit-event-block-blockexpevent"></a>
### BlockExpEvent

- Java class: `org.bukkit.event.block.BlockExpEvent`; parent: `org.bukkit.event.block.BlockEvent`.
- Python subscription: `@bridge.on("BlockExpEvent")`; `Events.BLOCK_EXP` also works.
- Cancellable: no; player: no known player getter.
- [Official Paper Javadoc](https://jd.papermc.io/paper/1.16.5/org/bukkit/event/block/BlockExpEvent.html) for meaning, trigger conditions, and Java API.

| `data` field | JSON type | Java getter | Java return type |
| --- | --- | --- | --- |
| `block` | block summary | `getBlock()` | `org.bukkit.block.Block` |
| `expToDrop` | number | `getExpToDrop()` | `int` |

<a id="event-org-bukkit-event-block-blockexplodeevent"></a>
### BlockExplodeEvent

- Java class: `org.bukkit.event.block.BlockExplodeEvent`; parent: `org.bukkit.event.block.BlockEvent`.
- Python subscription: `@bridge.on("BlockExplodeEvent")`; `Events.BLOCK_EXPLODE` also works.
- Cancellable: yes; player: no known player getter.
- [Official Paper Javadoc](https://jd.papermc.io/paper/1.16.5/org/bukkit/event/block/BlockExplodeEvent.html) for meaning, trigger conditions, and Java API.

| `data` field | JSON type | Java getter | Java return type |
| --- | --- | --- | --- |
| `block` | block summary | `getBlock()` | `org.bukkit.block.Block` |
| `yield` | number | `getYield()` | `float` |

<a id="event-org-bukkit-event-block-blockfadeevent"></a>
### BlockFadeEvent

- Java class: `org.bukkit.event.block.BlockFadeEvent`; parent: `org.bukkit.event.block.BlockEvent`.
- Python subscription: `@bridge.on("BlockFadeEvent")`; `Events.BLOCK_FADE` also works.
- Cancellable: yes; player: no known player getter.
- [Official Paper Javadoc](https://jd.papermc.io/paper/1.16.5/org/bukkit/event/block/BlockFadeEvent.html) for meaning, trigger conditions, and Java API.

| `data` field | JSON type | Java getter | Java return type |
| --- | --- | --- | --- |
| `block` | block summary | `getBlock()` | `org.bukkit.block.Block` |

<a id="event-io-papermc-paper-event-block-blockfaileddispenseevent"></a>
### BlockFailedDispenseEvent

- Java class: `io.papermc.paper.event.block.BlockFailedDispenseEvent`; parent: `org.bukkit.event.block.BlockEvent`.
- Python subscription: `@bridge.on("BlockFailedDispenseEvent")`; `Events.BLOCK_FAILED_DISPENSE` also works.
- Cancellable: no; player: no known player getter.
- [Official Paper Javadoc](https://jd.papermc.io/paper/1.16.5/io/papermc/paper/event/block/BlockFailedDispenseEvent.html) for meaning, trigger conditions, and Java API.

| `data` field | JSON type | Java getter | Java return type |
| --- | --- | --- | --- |
| `block` | block summary | `getBlock()` | `org.bukkit.block.Block` |

<a id="event-org-bukkit-event-block-blockfertilizeevent"></a>
### BlockFertilizeEvent

- Java class: `org.bukkit.event.block.BlockFertilizeEvent`; parent: `org.bukkit.event.block.BlockEvent`.
- Python subscription: `@bridge.on("BlockFertilizeEvent")`; `Events.BLOCK_FERTILIZE` also works.
- Cancellable: yes; player: possible, depending on the runtime object.
- [Official Paper Javadoc](https://jd.papermc.io/paper/1.16.5/org/bukkit/event/block/BlockFertilizeEvent.html) for meaning, trigger conditions, and Java API.

| `data` field | JSON type | Java getter | Java return type |
| --- | --- | --- | --- |
| `block` | block summary | `getBlock()` | `org.bukkit.block.Block` |

<a id="event-org-bukkit-event-block-blockformevent"></a>
### BlockFormEvent

- Java class: `org.bukkit.event.block.BlockFormEvent`; parent: `org.bukkit.event.block.BlockGrowEvent`.
- Python subscription: `@bridge.on("BlockFormEvent")`; `Events.BLOCK_FORM` also works.
- Cancellable: yes; player: no known player getter.
- [Official Paper Javadoc](https://jd.papermc.io/paper/1.16.5/org/bukkit/event/block/BlockFormEvent.html) for meaning, trigger conditions, and Java API.

| `data` field | JSON type | Java getter | Java return type |
| --- | --- | --- | --- |
| `block` | block summary | `getBlock()` | `org.bukkit.block.Block` |

<a id="event-org-bukkit-event-block-blockfromtoevent"></a>
### BlockFromToEvent

- Java class: `org.bukkit.event.block.BlockFromToEvent`; parent: `org.bukkit.event.block.BlockEvent`.
- Python subscription: `@bridge.on("BlockFromToEvent")`; `Events.BLOCK_FROM_TO` also works.
- Cancellable: yes; player: no known player getter.
- [Official Paper Javadoc](https://jd.papermc.io/paper/1.16.5/org/bukkit/event/block/BlockFromToEvent.html) for meaning, trigger conditions, and Java API.

| `data` field | JSON type | Java getter | Java return type |
| --- | --- | --- | --- |
| `block` | block summary | `getBlock()` | `org.bukkit.block.Block` |
| `face` | string | `getFace()` | `org.bukkit.block.BlockFace` |
| `toBlock` | block summary | `getToBlock()` | `org.bukkit.block.Block` |

<a id="event-org-bukkit-event-block-blockgrowevent"></a>
### BlockGrowEvent

- Java class: `org.bukkit.event.block.BlockGrowEvent`; parent: `org.bukkit.event.block.BlockEvent`.
- Python subscription: `@bridge.on("BlockGrowEvent")`; `Events.BLOCK_GROW` also works.
- Cancellable: yes; player: no known player getter.
- [Official Paper Javadoc](https://jd.papermc.io/paper/1.16.5/org/bukkit/event/block/BlockGrowEvent.html) for meaning, trigger conditions, and Java API.

| `data` field | JSON type | Java getter | Java return type |
| --- | --- | --- | --- |
| `block` | block summary | `getBlock()` | `org.bukkit.block.Block` |

<a id="event-org-bukkit-event-block-blockigniteevent"></a>
### BlockIgniteEvent

- Java class: `org.bukkit.event.block.BlockIgniteEvent`; parent: `org.bukkit.event.block.BlockEvent`.
- Python subscription: `@bridge.on("BlockIgniteEvent")`; `Events.BLOCK_IGNITE` also works.
- Cancellable: yes; player: possible, depending on the runtime object.
- [Official Paper Javadoc](https://jd.papermc.io/paper/1.16.5/org/bukkit/event/block/BlockIgniteEvent.html) for meaning, trigger conditions, and Java API.

| `data` field | JSON type | Java getter | Java return type |
| --- | --- | --- | --- |
| `block` | block summary | `getBlock()` | `org.bukkit.block.Block` |
| `cause` | string | `getCause()` | `org.bukkit.event.block.BlockIgniteEvent$IgniteCause` |
| `ignitingBlock` | block summary | `getIgnitingBlock()` | `org.bukkit.block.Block` |
| `ignitingEntity` | entity summary | `getIgnitingEntity()` | `org.bukkit.entity.Entity` |

<a id="event-org-bukkit-event-block-blockmultiplaceevent"></a>
### BlockMultiPlaceEvent

- Java class: `org.bukkit.event.block.BlockMultiPlaceEvent`; parent: `org.bukkit.event.block.BlockPlaceEvent`.
- Python subscription: `@bridge.on("BlockMultiPlaceEvent")`; `Events.BLOCK_MULTI_PLACE` also works.
- Cancellable: yes; player: possible, depending on the runtime object.
- [Official Paper Javadoc](https://jd.papermc.io/paper/1.16.5/org/bukkit/event/block/BlockMultiPlaceEvent.html) for meaning, trigger conditions, and Java API.

| `data` field | JSON type | Java getter | Java return type |
| --- | --- | --- | --- |
| `block` | block summary | `getBlock()` | `org.bukkit.block.Block` |
| `blockAgainst` | block summary | `getBlockAgainst()` | `org.bukkit.block.Block` |
| `blockPlaced` | block summary | `getBlockPlaced()` | `org.bukkit.block.Block` |
| `hand` | string | `getHand()` | `org.bukkit.inventory.EquipmentSlot` |
| `itemInHand` | item summary | `getItemInHand()` | `org.bukkit.inventory.ItemStack` |

<a id="event-org-bukkit-event-block-blockphysicsevent"></a>
### BlockPhysicsEvent

- Java class: `org.bukkit.event.block.BlockPhysicsEvent`; parent: `org.bukkit.event.block.BlockEvent`.
- Python subscription: `@bridge.on("BlockPhysicsEvent")`; `Events.BLOCK_PHYSICS` also works.
- Cancellable: yes; player: no known player getter.
- [Official Paper Javadoc](https://jd.papermc.io/paper/1.16.5/org/bukkit/event/block/BlockPhysicsEvent.html) for meaning, trigger conditions, and Java API.

| `data` field | JSON type | Java getter | Java return type |
| --- | --- | --- | --- |
| `block` | block summary | `getBlock()` | `org.bukkit.block.Block` |
| `changedType` | string | `getChangedType()` | `org.bukkit.Material` |
| `sourceBlock` | block summary | `getSourceBlock()` | `org.bukkit.block.Block` |

<a id="event-org-bukkit-event-block-blockpistonextendevent"></a>
### BlockPistonExtendEvent

- Java class: `org.bukkit.event.block.BlockPistonExtendEvent`; parent: `org.bukkit.event.block.BlockPistonEvent`.
- Python subscription: `@bridge.on("BlockPistonExtendEvent")`; `Events.BLOCK_PISTON_EXTEND` also works.
- Cancellable: yes; player: no known player getter.
- [Official Paper Javadoc](https://jd.papermc.io/paper/1.16.5/org/bukkit/event/block/BlockPistonExtendEvent.html) for meaning, trigger conditions, and Java API.

| `data` field | JSON type | Java getter | Java return type |
| --- | --- | --- | --- |
| `block` | block summary | `getBlock()` | `org.bukkit.block.Block` |
| `direction` | string | `getDirection()` | `org.bukkit.block.BlockFace` |
| `length` | number | `getLength()` | `int` |
| `sticky` | boolean | `isSticky()` | `boolean` |

<a id="event-org-bukkit-event-block-blockpistonretractevent"></a>
### BlockPistonRetractEvent

- Java class: `org.bukkit.event.block.BlockPistonRetractEvent`; parent: `org.bukkit.event.block.BlockPistonEvent`.
- Python subscription: `@bridge.on("BlockPistonRetractEvent")`; `Events.BLOCK_PISTON_RETRACT` also works.
- Cancellable: yes; player: no known player getter.
- [Official Paper Javadoc](https://jd.papermc.io/paper/1.16.5/org/bukkit/event/block/BlockPistonRetractEvent.html) for meaning, trigger conditions, and Java API.

| `data` field | JSON type | Java getter | Java return type |
| --- | --- | --- | --- |
| `block` | block summary | `getBlock()` | `org.bukkit.block.Block` |
| `direction` | string | `getDirection()` | `org.bukkit.block.BlockFace` |
| `retractLocation` | location summary | `getRetractLocation()` | `org.bukkit.Location` |
| `sticky` | boolean | `isSticky()` | `boolean` |

<a id="event-org-bukkit-event-block-blockplaceevent"></a>
### BlockPlaceEvent

- Java class: `org.bukkit.event.block.BlockPlaceEvent`; parent: `org.bukkit.event.block.BlockEvent`.
- Python subscription: `@bridge.on("BlockPlaceEvent")`; `Events.BLOCK_PLACE` also works.
- Cancellable: yes; player: possible, depending on the runtime object.
- [Official Paper Javadoc](https://jd.papermc.io/paper/1.16.5/org/bukkit/event/block/BlockPlaceEvent.html) for meaning, trigger conditions, and Java API.

| `data` field | JSON type | Java getter | Java return type |
| --- | --- | --- | --- |
| `block` | block summary | `getBlock()` | `org.bukkit.block.Block` |
| `blockAgainst` | block summary | `getBlockAgainst()` | `org.bukkit.block.Block` |
| `blockPlaced` | block summary | `getBlockPlaced()` | `org.bukkit.block.Block` |
| `hand` | string | `getHand()` | `org.bukkit.inventory.EquipmentSlot` |
| `itemInHand` | item summary | `getItemInHand()` | `org.bukkit.inventory.ItemStack` |

<a id="event-io-papermc-paper-event-block-blockpredispenseevent"></a>
### BlockPreDispenseEvent

- Java class: `io.papermc.paper.event.block.BlockPreDispenseEvent`; parent: `org.bukkit.event.block.BlockEvent`.
- Python subscription: `@bridge.on("BlockPreDispenseEvent")`; `Events.BLOCK_PRE_DISPENSE` also works.
- Cancellable: yes; player: no known player getter.
- [Official Paper Javadoc](https://jd.papermc.io/paper/1.16.5/io/papermc/paper/event/block/BlockPreDispenseEvent.html) for meaning, trigger conditions, and Java API.

| `data` field | JSON type | Java getter | Java return type |
| --- | --- | --- | --- |
| `block` | block summary | `getBlock()` | `org.bukkit.block.Block` |
| `itemStack` | item summary | `getItemStack()` | `org.bukkit.inventory.ItemStack` |
| `slot` | number | `getSlot()` | `int` |

<a id="event-org-bukkit-event-block-blockredstoneevent"></a>
### BlockRedstoneEvent

- Java class: `org.bukkit.event.block.BlockRedstoneEvent`; parent: `org.bukkit.event.block.BlockEvent`.
- Python subscription: `@bridge.on("BlockRedstoneEvent")`; `Events.BLOCK_REDSTONE` also works.
- Cancellable: no; player: no known player getter.
- [Official Paper Javadoc](https://jd.papermc.io/paper/1.16.5/org/bukkit/event/block/BlockRedstoneEvent.html) for meaning, trigger conditions, and Java API.

| `data` field | JSON type | Java getter | Java return type |
| --- | --- | --- | --- |
| `block` | block summary | `getBlock()` | `org.bukkit.block.Block` |
| `newCurrent` | number | `getNewCurrent()` | `int` |
| `oldCurrent` | number | `getOldCurrent()` | `int` |

<a id="event-org-bukkit-event-block-blockshearentityevent"></a>
### BlockShearEntityEvent

- Java class: `org.bukkit.event.block.BlockShearEntityEvent`; parent: `org.bukkit.event.block.BlockEvent`.
- Python subscription: `@bridge.on("BlockShearEntityEvent")`; `Events.BLOCK_SHEAR_ENTITY` also works.
- Cancellable: yes; player: possible, depending on the runtime object.
- [Official Paper Javadoc](https://jd.papermc.io/paper/1.16.5/org/bukkit/event/block/BlockShearEntityEvent.html) for meaning, trigger conditions, and Java API.

| `data` field | JSON type | Java getter | Java return type |
| --- | --- | --- | --- |
| `block` | block summary | `getBlock()` | `org.bukkit.block.Block` |
| `entity` | entity summary | `getEntity()` | `org.bukkit.entity.Entity` |
| `tool` | item summary | `getTool()` | `org.bukkit.inventory.ItemStack` |

<a id="event-org-bukkit-event-block-blockspreadevent"></a>
### BlockSpreadEvent

- Java class: `org.bukkit.event.block.BlockSpreadEvent`; parent: `org.bukkit.event.block.BlockFormEvent`.
- Python subscription: `@bridge.on("BlockSpreadEvent")`; `Events.BLOCK_SPREAD` also works.
- Cancellable: yes; player: no known player getter.
- [Official Paper Javadoc](https://jd.papermc.io/paper/1.16.5/org/bukkit/event/block/BlockSpreadEvent.html) for meaning, trigger conditions, and Java API.

| `data` field | JSON type | Java getter | Java return type |
| --- | --- | --- | --- |
| `block` | block summary | `getBlock()` | `org.bukkit.block.Block` |
| `source` | block summary | `getSource()` | `org.bukkit.block.Block` |

<a id="event-org-bukkit-event-block-cauldronlevelchangeevent"></a>
### CauldronLevelChangeEvent

- Java class: `org.bukkit.event.block.CauldronLevelChangeEvent`; parent: `org.bukkit.event.block.BlockEvent`.
- Python subscription: `@bridge.on("CauldronLevelChangeEvent")`; `Events.CAULDRON_LEVEL_CHANGE` also works.
- Cancellable: yes; player: possible, depending on the runtime object.
- [Official Paper Javadoc](https://jd.papermc.io/paper/1.16.5/org/bukkit/event/block/CauldronLevelChangeEvent.html) for meaning, trigger conditions, and Java API.

| `data` field | JSON type | Java getter | Java return type |
| --- | --- | --- | --- |
| `block` | block summary | `getBlock()` | `org.bukkit.block.Block` |
| `entity` | entity summary | `getEntity()` | `org.bukkit.entity.Entity` |
| `newLevel` | number | `getNewLevel()` | `int` |
| `oldLevel` | number | `getOldLevel()` | `int` |
| `reason` | string | `getReason()` | `org.bukkit.event.block.CauldronLevelChangeEvent$ChangeReason` |

<a id="event-io-papermc-paper-event-block-dragoneggformevent"></a>
### DragonEggFormEvent

- Java class: `io.papermc.paper.event.block.DragonEggFormEvent`; parent: `org.bukkit.event.block.BlockFormEvent`.
- Python subscription: `@bridge.on("DragonEggFormEvent")`; `Events.DRAGON_EGG_FORM` also works.
- Cancellable: yes; player: no known player getter.
- [Official Paper Javadoc](https://jd.papermc.io/paper/1.16.5/io/papermc/paper/event/block/DragonEggFormEvent.html) for meaning, trigger conditions, and Java API.

| `data` field | JSON type | Java getter | Java return type |
| --- | --- | --- | --- |
| `block` | block summary | `getBlock()` | `org.bukkit.block.Block` |

<a id="event-org-bukkit-event-block-entityblockformevent"></a>
### EntityBlockFormEvent

- Java class: `org.bukkit.event.block.EntityBlockFormEvent`; parent: `org.bukkit.event.block.BlockFormEvent`.
- Python subscription: `@bridge.on("EntityBlockFormEvent")`; `Events.ENTITY_BLOCK_FORM` also works.
- Cancellable: yes; player: possible, depending on the runtime object.
- [Official Paper Javadoc](https://jd.papermc.io/paper/1.16.5/org/bukkit/event/block/EntityBlockFormEvent.html) for meaning, trigger conditions, and Java API.

| `data` field | JSON type | Java getter | Java return type |
| --- | --- | --- | --- |
| `block` | block summary | `getBlock()` | `org.bukkit.block.Block` |
| `entity` | entity summary | `getEntity()` | `org.bukkit.entity.Entity` |

<a id="event-org-bukkit-event-block-fluidlevelchangeevent"></a>
### FluidLevelChangeEvent

- Java class: `org.bukkit.event.block.FluidLevelChangeEvent`; parent: `org.bukkit.event.block.BlockEvent`.
- Python subscription: `@bridge.on("FluidLevelChangeEvent")`; `Events.FLUID_LEVEL_CHANGE` also works.
- Cancellable: yes; player: no known player getter.
- [Official Paper Javadoc](https://jd.papermc.io/paper/1.16.5/org/bukkit/event/block/FluidLevelChangeEvent.html) for meaning, trigger conditions, and Java API.

| `data` field | JSON type | Java getter | Java return type |
| --- | --- | --- | --- |
| `block` | block summary | `getBlock()` | `org.bukkit.block.Block` |

<a id="event-org-bukkit-event-block-leavesdecayevent"></a>
### LeavesDecayEvent

- Java class: `org.bukkit.event.block.LeavesDecayEvent`; parent: `org.bukkit.event.block.BlockEvent`.
- Python subscription: `@bridge.on("LeavesDecayEvent")`; `Events.LEAVES_DECAY` also works.
- Cancellable: yes; player: no known player getter.
- [Official Paper Javadoc](https://jd.papermc.io/paper/1.16.5/org/bukkit/event/block/LeavesDecayEvent.html) for meaning, trigger conditions, and Java API.

| `data` field | JSON type | Java getter | Java return type |
| --- | --- | --- | --- |
| `block` | block summary | `getBlock()` | `org.bukkit.block.Block` |

<a id="event-org-bukkit-event-block-moisturechangeevent"></a>
### MoistureChangeEvent

- Java class: `org.bukkit.event.block.MoistureChangeEvent`; parent: `org.bukkit.event.block.BlockEvent`.
- Python subscription: `@bridge.on("MoistureChangeEvent")`; `Events.MOISTURE_CHANGE` also works.
- Cancellable: yes; player: no known player getter.
- [Official Paper Javadoc](https://jd.papermc.io/paper/1.16.5/org/bukkit/event/block/MoistureChangeEvent.html) for meaning, trigger conditions, and Java API.

| `data` field | JSON type | Java getter | Java return type |
| --- | --- | --- | --- |
| `block` | block summary | `getBlock()` | `org.bukkit.block.Block` |

<a id="event-org-bukkit-event-block-noteplayevent"></a>
### NotePlayEvent

- Java class: `org.bukkit.event.block.NotePlayEvent`; parent: `org.bukkit.event.block.BlockEvent`.
- Python subscription: `@bridge.on("NotePlayEvent")`; `Events.NOTE_PLAY` also works.
- Cancellable: yes; player: no known player getter.
- [Official Paper Javadoc](https://jd.papermc.io/paper/1.16.5/org/bukkit/event/block/NotePlayEvent.html) for meaning, trigger conditions, and Java API.

| `data` field | JSON type | Java getter | Java return type |
| --- | --- | --- | --- |
| `block` | block summary | `getBlock()` | `org.bukkit.block.Block` |
| `instrument` | string | `getInstrument()` | `org.bukkit.Instrument` |

<a id="event-io-papermc-paper-event-block-playershearblockevent"></a>
### PlayerShearBlockEvent

- Java class: `io.papermc.paper.event.block.PlayerShearBlockEvent`; parent: `org.bukkit.event.player.PlayerEvent`.
- Python subscription: `@bridge.on("PlayerShearBlockEvent")`; `Events.PLAYER_SHEAR_BLOCK` also works.
- Cancellable: yes; player: possible, depending on the runtime object.
- [Official Paper Javadoc](https://jd.papermc.io/paper/1.16.5/io/papermc/paper/event/block/PlayerShearBlockEvent.html) for meaning, trigger conditions, and Java API.

| `data` field | JSON type | Java getter | Java return type |
| --- | --- | --- | --- |
| `block` | block summary | `getBlock()` | `org.bukkit.block.Block` |
| `hand` | string | `getHand()` | `org.bukkit.inventory.EquipmentSlot` |
| `item` | item summary | `getItem()` | `org.bukkit.inventory.ItemStack` |

<a id="event-org-bukkit-event-block-signchangeevent"></a>
### SignChangeEvent

- Java class: `org.bukkit.event.block.SignChangeEvent`; parent: `org.bukkit.event.block.BlockEvent`.
- Python subscription: `@bridge.on("SignChangeEvent")`; `Events.SIGN_CHANGE` also works.
- Cancellable: yes; player: possible, depending on the runtime object.
- [Official Paper Javadoc](https://jd.papermc.io/paper/1.16.5/org/bukkit/event/block/SignChangeEvent.html) for meaning, trigger conditions, and Java API.

| `data` field | JSON type | Java getter | Java return type |
| --- | --- | --- | --- |
| `block` | block summary | `getBlock()` | `org.bukkit.block.Block` |

<a id="event-org-bukkit-event-block-spongeabsorbevent"></a>
### SpongeAbsorbEvent

- Java class: `org.bukkit.event.block.SpongeAbsorbEvent`; parent: `org.bukkit.event.block.BlockEvent`.
- Python subscription: `@bridge.on("SpongeAbsorbEvent")`; `Events.SPONGE_ABSORB` also works.
- Cancellable: yes; player: no known player getter.
- [Official Paper Javadoc](https://jd.papermc.io/paper/1.16.5/org/bukkit/event/block/SpongeAbsorbEvent.html) for meaning, trigger conditions, and Java API.

| `data` field | JSON type | Java getter | Java return type |
| --- | --- | --- | --- |
| `block` | block summary | `getBlock()` | `org.bukkit.block.Block` |

<a id="event-io-papermc-paper-event-block-targethitevent"></a>
### TargetHitEvent

- Java class: `io.papermc.paper.event.block.TargetHitEvent`; parent: `org.bukkit.event.entity.ProjectileHitEvent`.
- Python subscription: `@bridge.on("TargetHitEvent")`; `Events.TARGET_HIT` also works.
- Cancellable: yes; player: possible, depending on the runtime object.
- [Official Paper Javadoc](https://jd.papermc.io/paper/1.16.5/io/papermc/paper/event/block/TargetHitEvent.html) for meaning, trigger conditions, and Java API.

| `data` field | JSON type | Java getter | Java return type |
| --- | --- | --- | --- |
| `entity` | entity summary | `getEntity()` | `org.bukkit.entity.Projectile` |
| `entityType` | string | `getEntityType()` | `org.bukkit.entity.EntityType` |
| `hitBlock` | block summary | `getHitBlock()` | `org.bukkit.block.Block` |
| `hitBlockFace` | string | `getHitBlockFace()` | `org.bukkit.block.BlockFace` |
| `hitEntity` | entity summary | `getHitEntity()` | `org.bukkit.entity.Entity` |
| `signalStrength` | number | `getSignalStrength()` | `int` |

<a id="event-com-destroystokyo-paper-event-block-tntprimeevent"></a>
### TNTPrimeEvent

- Java class: `com.destroystokyo.paper.event.block.TNTPrimeEvent`; parent: `org.bukkit.event.block.BlockEvent`.
- Python subscription: `@bridge.on("TNTPrimeEvent")`; `Events.TNT_PRIME` also works.
- Cancellable: yes; player: no known player getter.
- [Official Paper Javadoc](https://jd.papermc.io/paper/1.16.5/com/destroystokyo/paper/event/block/TNTPrimeEvent.html) for meaning, trigger conditions, and Java API.

| `data` field | JSON type | Java getter | Java return type |
| --- | --- | --- | --- |
| `block` | block summary | `getBlock()` | `org.bukkit.block.Block` |
| `primerEntity` | entity summary | `getPrimerEntity()` | `org.bukkit.entity.Entity` |
| `reason` | string | `getReason()` | `com.destroystokyo.paper.event.block.TNTPrimeEvent$PrimeReason` |

<a id="category-command"></a>
## command

| Event | Python `type` | possible `data` fields | Cancellable |
| --- | --- | ---: | --- |
| [UnknownCommandEvent](#event-org-bukkit-event-command-unknowncommandevent) | `UnknownCommandEvent` | 2 | No |

<a id="event-org-bukkit-event-command-unknowncommandevent"></a>
### UnknownCommandEvent

- Java class: `org.bukkit.event.command.UnknownCommandEvent`; parent: `org.bukkit.event.Event`.
- Python subscription: `@bridge.on("UnknownCommandEvent")`; `Events.UNKNOWN_COMMAND` also works.
- Cancellable: no; player: no known player getter.
- [Official Paper Javadoc](https://jd.papermc.io/paper/1.16.5/org/bukkit/event/command/UnknownCommandEvent.html) for meaning, trigger conditions, and Java API.

| `data` field | JSON type | Java getter | Java return type |
| --- | --- | --- | --- |
| `commandLine` | string | `getCommandLine()` | `java.lang.String` |
| `message` | string | `getMessage()` | `java.lang.String` |

<a id="category-enchantment"></a>
## enchantment

| Event | Python `type` | possible `data` fields | Cancellable |
| --- | --- | ---: | --- |
| [EnchantItemEvent](#event-org-bukkit-event-enchantment-enchantitemevent) | `EnchantItemEvent` | 4 | Yes |
| [PrepareItemEnchantEvent](#event-org-bukkit-event-enchantment-prepareitemenchantevent) | `PrepareItemEnchantEvent` | 4 | Yes |

<a id="event-org-bukkit-event-enchantment-enchantitemevent"></a>
### EnchantItemEvent

- Java class: `org.bukkit.event.enchantment.EnchantItemEvent`; parent: `org.bukkit.event.inventory.InventoryEvent`.
- Python subscription: `@bridge.on("EnchantItemEvent")`; `Events.ENCHANT_ITEM` also works.
- Cancellable: yes; player: no known player getter.
- [Official Paper Javadoc](https://jd.papermc.io/paper/1.16.5/org/bukkit/event/enchantment/EnchantItemEvent.html) for meaning, trigger conditions, and Java API.

| `data` field | JSON type | Java getter | Java return type |
| --- | --- | --- | --- |
| `enchantBlock` | block summary | `getEnchantBlock()` | `org.bukkit.block.Block` |
| `enchanter` | entity summary | `getEnchanter()` | `org.bukkit.entity.Player` |
| `expLevelCost` | number | `getExpLevelCost()` | `int` |
| `item` | item summary | `getItem()` | `org.bukkit.inventory.ItemStack` |

<a id="event-org-bukkit-event-enchantment-prepareitemenchantevent"></a>
### PrepareItemEnchantEvent

- Java class: `org.bukkit.event.enchantment.PrepareItemEnchantEvent`; parent: `org.bukkit.event.inventory.InventoryEvent`.
- Python subscription: `@bridge.on("PrepareItemEnchantEvent")`; `Events.PREPARE_ITEM_ENCHANT` also works.
- Cancellable: yes; player: no known player getter.
- [Official Paper Javadoc](https://jd.papermc.io/paper/1.16.5/org/bukkit/event/enchantment/PrepareItemEnchantEvent.html) for meaning, trigger conditions, and Java API.

| `data` field | JSON type | Java getter | Java return type |
| --- | --- | --- | --- |
| `enchantBlock` | block summary | `getEnchantBlock()` | `org.bukkit.block.Block` |
| `enchanter` | entity summary | `getEnchanter()` | `org.bukkit.entity.Player` |
| `enchantmentBonus` | number | `getEnchantmentBonus()` | `int` |
| `item` | item summary | `getItem()` | `org.bukkit.inventory.ItemStack` |

<a id="category-entity"></a>
## entity

| Event | Python `type` | possible `data` fields | Cancellable |
| --- | --- | ---: | --- |
| [AreaEffectCloudApplyEvent](#event-org-bukkit-event-entity-areaeffectcloudapplyevent) | `AreaEffectCloudApplyEvent` | 2 | Yes |
| [ArrowBodyCountChangeEvent](#event-org-bukkit-event-entity-arrowbodycountchangeevent) | `ArrowBodyCountChangeEvent` | 5 | Yes |
| [BatToggleSleepEvent](#event-org-bukkit-event-entity-battogglesleepevent) | `BatToggleSleepEvent` | 3 | Yes |
| [CreatureSpawnEvent](#event-org-bukkit-event-entity-creaturespawnevent) | `CreatureSpawnEvent` | 4 | Yes |
| [CreeperIgniteEvent](#event-com-destroystokyo-paper-event-entity-creeperigniteevent) | `CreeperIgniteEvent` | 3 | Yes |
| [CreeperPowerEvent](#event-org-bukkit-event-entity-creeperpowerevent) | `CreeperPowerEvent` | 4 | Yes |
| [ElderGuardianAppearanceEvent](#event-io-papermc-paper-event-entity-elderguardianappearanceevent) | `ElderGuardianAppearanceEvent` | 3 | Yes |
| [EnderDragonChangePhaseEvent](#event-org-bukkit-event-entity-enderdragonchangephaseevent) | `EnderDragonChangePhaseEvent` | 4 | Yes |
| [EnderDragonFireballHitEvent](#event-com-destroystokyo-paper-event-entity-enderdragonfireballhitevent) | `EnderDragonFireballHitEvent` | 3 | Yes |
| [EnderDragonFlameEvent](#event-com-destroystokyo-paper-event-entity-enderdragonflameevent) | `EnderDragonFlameEvent` | 3 | Yes |
| [EnderDragonShootFireballEvent](#event-com-destroystokyo-paper-event-entity-enderdragonshootfireballevent) | `EnderDragonShootFireballEvent` | 3 | Yes |
| [EndermanAttackPlayerEvent](#event-com-destroystokyo-paper-event-entity-endermanattackplayerevent) | `EndermanAttackPlayerEvent` | 2 | Yes |
| [EndermanEscapeEvent](#event-com-destroystokyo-paper-event-entity-endermanescapeevent) | `EndermanEscapeEvent` | 3 | Yes |
| [EntityAddToWorldEvent](#event-com-destroystokyo-paper-event-entity-entityaddtoworldevent) | `EntityAddToWorldEvent` | 2 | No |
| [EntityAirChangeEvent](#event-org-bukkit-event-entity-entityairchangeevent) | `EntityAirChangeEvent` | 3 | Yes |
| [EntityBreakDoorEvent](#event-org-bukkit-event-entity-entitybreakdoorevent) | `EntityBreakDoorEvent` | 4 | Yes |
| [EntityBreedEvent](#event-org-bukkit-event-entity-entitybreedevent) | `EntityBreedEvent` | 7 | Yes |
| [EntityChangeBlockEvent](#event-org-bukkit-event-entity-entitychangeblockevent) | `EntityChangeBlockEvent` | 4 | Yes |
| [EntityCombustByBlockEvent](#event-org-bukkit-event-entity-entitycombustbyblockevent) | `EntityCombustByBlockEvent` | 4 | Yes |
| [EntityCombustByEntityEvent](#event-org-bukkit-event-entity-entitycombustbyentityevent) | `EntityCombustByEntityEvent` | 4 | Yes |
| [EntityCombustEvent](#event-org-bukkit-event-entity-entitycombustevent) | `EntityCombustEvent` | 3 | Yes |
| [EntityCreatePortalEvent](#event-org-bukkit-event-entity-entitycreateportalevent) | `EntityCreatePortalEvent` | 3 | Yes |
| [EntityDamageByBlockEvent](#event-org-bukkit-event-entity-entitydamagebyblockevent) | `EntityDamageByBlockEvent` | 6 | Yes |
| [EntityDamageByEntityEvent](#event-org-bukkit-event-entity-entitydamagebyentityevent) | `EntityDamageByEntityEvent` | 6 | Yes |
| [EntityDamageEvent](#event-org-bukkit-event-entity-entitydamageevent) | `EntityDamageEvent` | 5 | Yes |
| [EntityDeathEvent](#event-org-bukkit-event-entity-entitydeathevent) | `EntityDeathEvent` | 8 | Yes |
| [EntityDropItemEvent](#event-org-bukkit-event-entity-entitydropitemevent) | `EntityDropItemEvent` | 3 | Yes |
| [EntityEnterBlockEvent](#event-org-bukkit-event-entity-entityenterblockevent) | `EntityEnterBlockEvent` | 3 | Yes |
| [EntityEnterLoveModeEvent](#event-org-bukkit-event-entity-entityenterlovemodeevent) | `EntityEnterLoveModeEvent` | 4 | Yes |
| [EntityExhaustionEvent](#event-org-bukkit-event-entity-entityexhaustionevent) | `EntityExhaustionEvent` | 4 | Yes |
| [EntityExplodeEvent](#event-org-bukkit-event-entity-entityexplodeevent) | `EntityExplodeEvent` | 4 | Yes |
| [EntityInsideBlockEvent](#event-io-papermc-paper-event-entity-entityinsideblockevent) | `EntityInsideBlockEvent` | 3 | Yes |
| [EntityInteractEvent](#event-org-bukkit-event-entity-entityinteractevent) | `EntityInteractEvent` | 3 | Yes |
| [EntityJumpEvent](#event-com-destroystokyo-paper-event-entity-entityjumpevent) | `EntityJumpEvent` | 2 | Yes |
| [EntityKnockbackByEntityEvent](#event-com-destroystokyo-paper-event-entity-entityknockbackbyentityevent) | `EntityKnockbackByEntityEvent` | 4 | Yes |
| [EntityLoadCrossbowEvent](#event-io-papermc-paper-event-entity-entityloadcrossbowevent) | `EntityLoadCrossbowEvent` | 4 | Yes |
| [EntityMoveEvent](#event-io-papermc-paper-event-entity-entitymoveevent) | `EntityMoveEvent` | 4 | Yes |
| [EntityPathfindEvent](#event-com-destroystokyo-paper-event-entity-entitypathfindevent) | `EntityPathfindEvent` | 4 | Yes |
| [EntityPickupItemEvent](#event-org-bukkit-event-entity-entitypickupitemevent) | `EntityPickupItemEvent` | 4 | Yes |
| [EntityPlaceEvent](#event-org-bukkit-event-entity-entityplaceevent) | `EntityPlaceEvent` | 4 | Yes |
| [EntityPortalEnterEvent](#event-org-bukkit-event-entity-entityportalenterevent) | `EntityPortalEnterEvent` | 3 | No |
| [EntityPortalEvent](#event-org-bukkit-event-entity-entityportalevent) | `EntityPortalEvent` | 5 | Yes |
| [EntityPortalExitEvent](#event-org-bukkit-event-entity-entityportalexitevent) | `EntityPortalExitEvent` | 4 | Yes |
| [EntityPoseChangeEvent](#event-org-bukkit-event-entity-entityposechangeevent) | `EntityPoseChangeEvent` | 3 | No |
| [EntityPotionEffectEvent](#event-org-bukkit-event-entity-entitypotioneffectevent) | `EntityPotionEffectEvent` | 5 | Yes |
| [EntityRegainHealthEvent](#event-org-bukkit-event-entity-entityregainhealthevent) | `EntityRegainHealthEvent` | 5 | Yes |
| [EntityRemoveFromWorldEvent](#event-com-destroystokyo-paper-event-entity-entityremovefromworldevent) | `EntityRemoveFromWorldEvent` | 2 | No |
| [EntityResurrectEvent](#event-org-bukkit-event-entity-entityresurrectevent) | `EntityResurrectEvent` | 2 | Yes |
| [EntityShootBowEvent](#event-org-bukkit-event-entity-entityshootbowevent) | `EntityShootBowEvent` | 9 | Yes |
| [EntitySpawnEvent](#event-org-bukkit-event-entity-entityspawnevent) | `EntitySpawnEvent` | 3 | Yes |
| [EntitySpellCastEvent](#event-org-bukkit-event-entity-entityspellcastevent) | `EntitySpellCastEvent` | 3 | Yes |
| [EntityTameEvent](#event-org-bukkit-event-entity-entitytameevent) | `EntityTameEvent` | 2 | Yes |
| [EntityTargetEvent](#event-org-bukkit-event-entity-entitytargetevent) | `EntityTargetEvent` | 4 | Yes |
| [EntityTargetLivingEntityEvent](#event-org-bukkit-event-entity-entitytargetlivingentityevent) | `EntityTargetLivingEntityEvent` | 4 | Yes |
| [EntityTeleportEndGatewayEvent](#event-com-destroystokyo-paper-event-entity-entityteleportendgatewayevent) | `EntityTeleportEndGatewayEvent` | 4 | Yes |
| [EntityTeleportEvent](#event-org-bukkit-event-entity-entityteleportevent) | `EntityTeleportEvent` | 4 | Yes |
| [EntityToggleGlideEvent](#event-org-bukkit-event-entity-entitytoggleglideevent) | `EntityToggleGlideEvent` | 3 | Yes |
| [EntityToggleSwimEvent](#event-org-bukkit-event-entity-entitytoggleswimevent) | `EntityToggleSwimEvent` | 3 | Yes |
| [EntityTransformedEvent](#event-com-destroystokyo-paper-event-entity-entitytransformedevent) | `EntityTransformedEvent` | 4 | Yes |
| [EntityTransformEvent](#event-org-bukkit-event-entity-entitytransformevent) | `EntityTransformEvent` | 4 | Yes |
| [EntityUnleashEvent](#event-org-bukkit-event-entity-entityunleashevent) | `EntityUnleashEvent` | 4 | No |
| [EntityZapEvent](#event-com-destroystokyo-paper-event-entity-entityzapevent) | `EntityZapEvent` | 6 | Yes |
| [ExpBottleEvent](#event-org-bukkit-event-entity-expbottleevent) | `ExpBottleEvent` | 7 | Yes |
| [ExperienceOrbMergeEvent](#event-com-destroystokyo-paper-event-entity-experienceorbmergeevent) | `ExperienceOrbMergeEvent` | 4 | Yes |
| [ExplosionPrimeEvent](#event-org-bukkit-event-entity-explosionprimeevent) | `ExplosionPrimeEvent` | 4 | Yes |
| [FireworkExplodeEvent](#event-org-bukkit-event-entity-fireworkexplodeevent) | `FireworkExplodeEvent` | 2 | Yes |
| [FoodLevelChangeEvent](#event-org-bukkit-event-entity-foodlevelchangeevent) | `FoodLevelChangeEvent` | 4 | Yes |
| [HorseJumpEvent](#event-org-bukkit-event-entity-horsejumpevent) | `HorseJumpEvent` | 3 | Yes |
| [ItemDespawnEvent](#event-org-bukkit-event-entity-itemdespawnevent) | `ItemDespawnEvent` | 3 | Yes |
| [ItemMergeEvent](#event-org-bukkit-event-entity-itemmergeevent) | `ItemMergeEvent` | 3 | Yes |
| [ItemSpawnEvent](#event-org-bukkit-event-entity-itemspawnevent) | `ItemSpawnEvent` | 3 | Yes |
| [LingeringPotionSplashEvent](#event-org-bukkit-event-entity-lingeringpotionsplashevent) | `LingeringPotionSplashEvent` | 6 | Yes |
| [PhantomPreSpawnEvent](#event-com-destroystokyo-paper-event-entity-phantomprespawnevent) | `PhantomPreSpawnEvent` | 4 | Yes |
| [PiglinBarterEvent](#event-org-bukkit-event-entity-piglinbarterevent) | `PiglinBarterEvent` | 3 | Yes |
| [PigZapEvent](#event-org-bukkit-event-entity-pigzapevent) | `PigZapEvent` | 8 | Yes |
| [PigZombieAngerEvent](#event-org-bukkit-event-entity-pigzombieangerevent) | `PigZombieAngerEvent` | 4 | Yes |
| [PlayerDeathEvent](#event-org-bukkit-event-entity-playerdeathevent) | `PlayerDeathEvent` | 14 | Yes |
| [PlayerLeashEntityEvent](#event-org-bukkit-event-entity-playerleashentityevent) | `PlayerLeashEntityEvent` | 2 | Yes |
| [PlayerNaturallySpawnCreaturesEvent](#event-com-destroystokyo-paper-event-entity-playernaturallyspawncreaturesevent) | `PlayerNaturallySpawnCreaturesEvent` | 1 | Yes |
| [PotionSplashEvent](#event-org-bukkit-event-entity-potionsplashevent) | `PotionSplashEvent` | 6 | Yes |
| [PreCreatureSpawnEvent](#event-com-destroystokyo-paper-event-entity-precreaturespawnevent) | `PreCreatureSpawnEvent` | 3 | Yes |
| [PreSpawnerSpawnEvent](#event-com-destroystokyo-paper-event-entity-prespawnerspawnevent) | `PreSpawnerSpawnEvent` | 4 | Yes |
| [ProjectileCollideEvent](#event-com-destroystokyo-paper-event-entity-projectilecollideevent) | `ProjectileCollideEvent` | 3 | Yes |
| [ProjectileHitEvent](#event-org-bukkit-event-entity-projectilehitevent) | `ProjectileHitEvent` | 5 | Yes |
| [ProjectileLaunchEvent](#event-org-bukkit-event-entity-projectilelaunchevent) | `ProjectileLaunchEvent` | 3 | Yes |
| [PufferFishStateChangeEvent](#event-io-papermc-paper-event-entity-pufferfishstatechangeevent) | `PufferFishStateChangeEvent` | 5 | Yes |
| [SheepDyeWoolEvent](#event-org-bukkit-event-entity-sheepdyewoolevent) | `SheepDyeWoolEvent` | 3 | Yes |
| [SheepRegrowWoolEvent](#event-org-bukkit-event-entity-sheepregrowwoolevent) | `SheepRegrowWoolEvent` | 2 | Yes |
| [SkeletonHorseTrapEvent](#event-com-destroystokyo-paper-event-entity-skeletonhorsetrapevent) | `SkeletonHorseTrapEvent` | 2 | Yes |
| [SlimeChangeDirectionEvent](#event-com-destroystokyo-paper-event-entity-slimechangedirectionevent) | `SlimeChangeDirectionEvent` | 3 | Yes |
| [SlimePathfindEvent](#event-com-destroystokyo-paper-event-entity-slimepathfindevent) | `SlimePathfindEvent` | 2 | Yes |
| [SlimeSplitEvent](#event-org-bukkit-event-entity-slimesplitevent) | `SlimeSplitEvent` | 3 | Yes |
| [SlimeSwimEvent](#event-com-destroystokyo-paper-event-entity-slimeswimevent) | `SlimeSwimEvent` | 2 | Yes |
| [SlimeTargetLivingEntityEvent](#event-com-destroystokyo-paper-event-entity-slimetargetlivingentityevent) | `SlimeTargetLivingEntityEvent` | 3 | Yes |
| [SlimeWanderEvent](#event-com-destroystokyo-paper-event-entity-slimewanderevent) | `SlimeWanderEvent` | 2 | Yes |
| [SpawnerSpawnEvent](#event-org-bukkit-event-entity-spawnerspawnevent) | `SpawnerSpawnEvent` | 3 | Yes |
| [StriderTemperatureChangeEvent](#event-org-bukkit-event-entity-stridertemperaturechangeevent) | `StriderTemperatureChangeEvent` | 3 | No |
| [ThrownEggHatchEvent](#event-com-destroystokyo-paper-event-entity-thrownegghatchevent) | `ThrownEggHatchEvent` | 4 | No |
| [TurtleGoHomeEvent](#event-com-destroystokyo-paper-event-entity-turtlegohomeevent) | `TurtleGoHomeEvent` | 2 | Yes |
| [TurtleLayEggEvent](#event-com-destroystokyo-paper-event-entity-turtlelayeggevent) | `TurtleLayEggEvent` | 4 | Yes |
| [TurtleStartDiggingEvent](#event-com-destroystokyo-paper-event-entity-turtlestartdiggingevent) | `TurtleStartDiggingEvent` | 3 | Yes |
| [VillagerAcquireTradeEvent](#event-org-bukkit-event-entity-villageracquiretradeevent) | `VillagerAcquireTradeEvent` | 2 | Yes |
| [VillagerCareerChangeEvent](#event-org-bukkit-event-entity-villagercareerchangeevent) | `VillagerCareerChangeEvent` | 4 | Yes |
| [VillagerReplenishTradeEvent](#event-org-bukkit-event-entity-villagerreplenishtradeevent) | `VillagerReplenishTradeEvent` | 3 | Yes |
| [WitchConsumePotionEvent](#event-com-destroystokyo-paper-event-entity-witchconsumepotionevent) | `WitchConsumePotionEvent` | 3 | Yes |
| [WitchReadyPotionEvent](#event-com-destroystokyo-paper-event-entity-witchreadypotionevent) | `WitchReadyPotionEvent` | 3 | Yes |
| [WitchThrowPotionEvent](#event-com-destroystokyo-paper-event-entity-witchthrowpotionevent) | `WitchThrowPotionEvent` | 4 | Yes |

<a id="event-org-bukkit-event-entity-areaeffectcloudapplyevent"></a>
### AreaEffectCloudApplyEvent

- Java class: `org.bukkit.event.entity.AreaEffectCloudApplyEvent`; parent: `org.bukkit.event.entity.EntityEvent`.
- Python subscription: `@bridge.on("AreaEffectCloudApplyEvent")`; `Events.AREA_EFFECT_CLOUD_APPLY` also works.
- Cancellable: yes; player: possible, depending on the runtime object.
- [Official Paper Javadoc](https://jd.papermc.io/paper/1.16.5/org/bukkit/event/entity/AreaEffectCloudApplyEvent.html) for meaning, trigger conditions, and Java API.

| `data` field | JSON type | Java getter | Java return type |
| --- | --- | --- | --- |
| `entity` | entity summary | `getEntity()` | `org.bukkit.entity.AreaEffectCloud` |
| `entityType` | string | `getEntityType()` | `org.bukkit.entity.EntityType` |

<a id="event-org-bukkit-event-entity-arrowbodycountchangeevent"></a>
### ArrowBodyCountChangeEvent

- Java class: `org.bukkit.event.entity.ArrowBodyCountChangeEvent`; parent: `org.bukkit.event.entity.EntityEvent`.
- Python subscription: `@bridge.on("ArrowBodyCountChangeEvent")`; `Events.ARROW_BODY_COUNT_CHANGE` also works.
- Cancellable: yes; player: possible, depending on the runtime object.
- [Official Paper Javadoc](https://jd.papermc.io/paper/1.16.5/org/bukkit/event/entity/ArrowBodyCountChangeEvent.html) for meaning, trigger conditions, and Java API.

| `data` field | JSON type | Java getter | Java return type |
| --- | --- | --- | --- |
| `entity` | entity summary | `getEntity()` | `org.bukkit.entity.Entity` |
| `entityType` | string | `getEntityType()` | `org.bukkit.entity.EntityType` |
| `newAmount` | number | `getNewAmount()` | `int` |
| `oldAmount` | number | `getOldAmount()` | `int` |
| `reset` | boolean | `isReset()` | `boolean` |

<a id="event-org-bukkit-event-entity-battogglesleepevent"></a>
### BatToggleSleepEvent

- Java class: `org.bukkit.event.entity.BatToggleSleepEvent`; parent: `org.bukkit.event.entity.EntityEvent`.
- Python subscription: `@bridge.on("BatToggleSleepEvent")`; `Events.BAT_TOGGLE_SLEEP` also works.
- Cancellable: yes; player: possible, depending on the runtime object.
- [Official Paper Javadoc](https://jd.papermc.io/paper/1.16.5/org/bukkit/event/entity/BatToggleSleepEvent.html) for meaning, trigger conditions, and Java API.

| `data` field | JSON type | Java getter | Java return type |
| --- | --- | --- | --- |
| `entity` | entity summary | `getEntity()` | `org.bukkit.entity.Entity` |
| `entityType` | string | `getEntityType()` | `org.bukkit.entity.EntityType` |
| `awake` | boolean | `isAwake()` | `boolean` |

<a id="event-org-bukkit-event-entity-creaturespawnevent"></a>
### CreatureSpawnEvent

- Java class: `org.bukkit.event.entity.CreatureSpawnEvent`; parent: `org.bukkit.event.entity.EntitySpawnEvent`.
- Python subscription: `@bridge.on("CreatureSpawnEvent")`; `Events.CREATURE_SPAWN` also works.
- Cancellable: yes; player: possible, depending on the runtime object.
- [Official Paper Javadoc](https://jd.papermc.io/paper/1.16.5/org/bukkit/event/entity/CreatureSpawnEvent.html) for meaning, trigger conditions, and Java API.

| `data` field | JSON type | Java getter | Java return type |
| --- | --- | --- | --- |
| `entity` | entity summary | `getEntity()` | `org.bukkit.entity.LivingEntity` |
| `entityType` | string | `getEntityType()` | `org.bukkit.entity.EntityType` |
| `location` | location summary | `getLocation()` | `org.bukkit.Location` |
| `spawnReason` | string | `getSpawnReason()` | `org.bukkit.event.entity.CreatureSpawnEvent$SpawnReason` |

<a id="event-com-destroystokyo-paper-event-entity-creeperigniteevent"></a>
### CreeperIgniteEvent

- Java class: `com.destroystokyo.paper.event.entity.CreeperIgniteEvent`; parent: `org.bukkit.event.entity.EntityEvent`.
- Python subscription: `@bridge.on("CreeperIgniteEvent")`; `Events.CREEPER_IGNITE` also works.
- Cancellable: yes; player: possible, depending on the runtime object.
- [Official Paper Javadoc](https://jd.papermc.io/paper/1.16.5/com/destroystokyo/paper/event/entity/CreeperIgniteEvent.html) for meaning, trigger conditions, and Java API.

| `data` field | JSON type | Java getter | Java return type |
| --- | --- | --- | --- |
| `entity` | entity summary | `getEntity()` | `org.bukkit.entity.Entity` |
| `entityType` | string | `getEntityType()` | `org.bukkit.entity.EntityType` |
| `ignited` | boolean | `isIgnited()` | `boolean` |

<a id="event-org-bukkit-event-entity-creeperpowerevent"></a>
### CreeperPowerEvent

- Java class: `org.bukkit.event.entity.CreeperPowerEvent`; parent: `org.bukkit.event.entity.EntityEvent`.
- Python subscription: `@bridge.on("CreeperPowerEvent")`; `Events.CREEPER_POWER` also works.
- Cancellable: yes; player: possible, depending on the runtime object.
- [Official Paper Javadoc](https://jd.papermc.io/paper/1.16.5/org/bukkit/event/entity/CreeperPowerEvent.html) for meaning, trigger conditions, and Java API.

| `data` field | JSON type | Java getter | Java return type |
| --- | --- | --- | --- |
| `cause` | string | `getCause()` | `org.bukkit.event.entity.CreeperPowerEvent$PowerCause` |
| `entity` | entity summary | `getEntity()` | `org.bukkit.entity.Entity` |
| `entityType` | string | `getEntityType()` | `org.bukkit.entity.EntityType` |
| `lightning` | entity summary | `getLightning()` | `org.bukkit.entity.LightningStrike` |

<a id="event-io-papermc-paper-event-entity-elderguardianappearanceevent"></a>
### ElderGuardianAppearanceEvent

- Java class: `io.papermc.paper.event.entity.ElderGuardianAppearanceEvent`; parent: `org.bukkit.event.entity.EntityEvent`.
- Python subscription: `@bridge.on("ElderGuardianAppearanceEvent")`; `Events.ELDER_GUARDIAN_APPEARANCE` also works.
- Cancellable: yes; player: possible, depending on the runtime object.
- [Official Paper Javadoc](https://jd.papermc.io/paper/1.16.5/io/papermc/paper/event/entity/ElderGuardianAppearanceEvent.html) for meaning, trigger conditions, and Java API.

| `data` field | JSON type | Java getter | Java return type |
| --- | --- | --- | --- |
| `affectedPlayer` | entity summary | `getAffectedPlayer()` | `org.bukkit.entity.Player` |
| `entity` | entity summary | `getEntity()` | `org.bukkit.entity.ElderGuardian` |
| `entityType` | string | `getEntityType()` | `org.bukkit.entity.EntityType` |

<a id="event-org-bukkit-event-entity-enderdragonchangephaseevent"></a>
### EnderDragonChangePhaseEvent

- Java class: `org.bukkit.event.entity.EnderDragonChangePhaseEvent`; parent: `org.bukkit.event.entity.EntityEvent`.
- Python subscription: `@bridge.on("EnderDragonChangePhaseEvent")`; `Events.ENDER_DRAGON_CHANGE_PHASE` also works.
- Cancellable: yes; player: possible, depending on the runtime object.
- [Official Paper Javadoc](https://jd.papermc.io/paper/1.16.5/org/bukkit/event/entity/EnderDragonChangePhaseEvent.html) for meaning, trigger conditions, and Java API.

| `data` field | JSON type | Java getter | Java return type |
| --- | --- | --- | --- |
| `currentPhase` | string | `getCurrentPhase()` | `org.bukkit.entity.EnderDragon$Phase` |
| `entity` | entity summary | `getEntity()` | `org.bukkit.entity.Entity` |
| `entityType` | string | `getEntityType()` | `org.bukkit.entity.EntityType` |
| `newPhase` | string | `getNewPhase()` | `org.bukkit.entity.EnderDragon$Phase` |

<a id="event-com-destroystokyo-paper-event-entity-enderdragonfireballhitevent"></a>
### EnderDragonFireballHitEvent

- Java class: `com.destroystokyo.paper.event.entity.EnderDragonFireballHitEvent`; parent: `org.bukkit.event.entity.EntityEvent`.
- Python subscription: `@bridge.on("EnderDragonFireballHitEvent")`; `Events.ENDER_DRAGON_FIREBALL_HIT` also works.
- Cancellable: yes; player: possible, depending on the runtime object.
- [Official Paper Javadoc](https://jd.papermc.io/paper/1.16.5/com/destroystokyo/paper/event/entity/EnderDragonFireballHitEvent.html) for meaning, trigger conditions, and Java API.

| `data` field | JSON type | Java getter | Java return type |
| --- | --- | --- | --- |
| `areaEffectCloud` | entity summary | `getAreaEffectCloud()` | `org.bukkit.entity.AreaEffectCloud` |
| `entity` | entity summary | `getEntity()` | `org.bukkit.entity.Entity` |
| `entityType` | string | `getEntityType()` | `org.bukkit.entity.EntityType` |

<a id="event-com-destroystokyo-paper-event-entity-enderdragonflameevent"></a>
### EnderDragonFlameEvent

- Java class: `com.destroystokyo.paper.event.entity.EnderDragonFlameEvent`; parent: `org.bukkit.event.entity.EntityEvent`.
- Python subscription: `@bridge.on("EnderDragonFlameEvent")`; `Events.ENDER_DRAGON_FLAME` also works.
- Cancellable: yes; player: possible, depending on the runtime object.
- [Official Paper Javadoc](https://jd.papermc.io/paper/1.16.5/com/destroystokyo/paper/event/entity/EnderDragonFlameEvent.html) for meaning, trigger conditions, and Java API.

| `data` field | JSON type | Java getter | Java return type |
| --- | --- | --- | --- |
| `areaEffectCloud` | entity summary | `getAreaEffectCloud()` | `org.bukkit.entity.AreaEffectCloud` |
| `entity` | entity summary | `getEntity()` | `org.bukkit.entity.EnderDragon` |
| `entityType` | string | `getEntityType()` | `org.bukkit.entity.EntityType` |

<a id="event-com-destroystokyo-paper-event-entity-enderdragonshootfireballevent"></a>
### EnderDragonShootFireballEvent

- Java class: `com.destroystokyo.paper.event.entity.EnderDragonShootFireballEvent`; parent: `org.bukkit.event.entity.EntityEvent`.
- Python subscription: `@bridge.on("EnderDragonShootFireballEvent")`; `Events.ENDER_DRAGON_SHOOT_FIREBALL` also works.
- Cancellable: yes; player: possible, depending on the runtime object.
- [Official Paper Javadoc](https://jd.papermc.io/paper/1.16.5/com/destroystokyo/paper/event/entity/EnderDragonShootFireballEvent.html) for meaning, trigger conditions, and Java API.

| `data` field | JSON type | Java getter | Java return type |
| --- | --- | --- | --- |
| `entity` | entity summary | `getEntity()` | `org.bukkit.entity.EnderDragon` |
| `entityType` | string | `getEntityType()` | `org.bukkit.entity.EntityType` |
| `fireball` | entity summary | `getFireball()` | `org.bukkit.entity.DragonFireball` |

<a id="event-com-destroystokyo-paper-event-entity-endermanattackplayerevent"></a>
### EndermanAttackPlayerEvent

- Java class: `com.destroystokyo.paper.event.entity.EndermanAttackPlayerEvent`; parent: `org.bukkit.event.entity.EntityEvent`.
- Python subscription: `@bridge.on("EndermanAttackPlayerEvent")`; `Events.ENDERMAN_ATTACK_PLAYER` also works.
- Cancellable: yes; player: possible, depending on the runtime object.
- [Official Paper Javadoc](https://jd.papermc.io/paper/1.16.5/com/destroystokyo/paper/event/entity/EndermanAttackPlayerEvent.html) for meaning, trigger conditions, and Java API.

| `data` field | JSON type | Java getter | Java return type |
| --- | --- | --- | --- |
| `entity` | entity summary | `getEntity()` | `org.bukkit.entity.Enderman` |
| `entityType` | string | `getEntityType()` | `org.bukkit.entity.EntityType` |

<a id="event-com-destroystokyo-paper-event-entity-endermanescapeevent"></a>
### EndermanEscapeEvent

- Java class: `com.destroystokyo.paper.event.entity.EndermanEscapeEvent`; parent: `org.bukkit.event.entity.EntityEvent`.
- Python subscription: `@bridge.on("EndermanEscapeEvent")`; `Events.ENDERMAN_ESCAPE` also works.
- Cancellable: yes; player: possible, depending on the runtime object.
- [Official Paper Javadoc](https://jd.papermc.io/paper/1.16.5/com/destroystokyo/paper/event/entity/EndermanEscapeEvent.html) for meaning, trigger conditions, and Java API.

| `data` field | JSON type | Java getter | Java return type |
| --- | --- | --- | --- |
| `entity` | entity summary | `getEntity()` | `org.bukkit.entity.Enderman` |
| `entityType` | string | `getEntityType()` | `org.bukkit.entity.EntityType` |
| `reason` | string | `getReason()` | `com.destroystokyo.paper.event.entity.EndermanEscapeEvent$Reason` |

<a id="event-com-destroystokyo-paper-event-entity-entityaddtoworldevent"></a>
### EntityAddToWorldEvent

- Java class: `com.destroystokyo.paper.event.entity.EntityAddToWorldEvent`; parent: `org.bukkit.event.entity.EntityEvent`.
- Python subscription: `@bridge.on("EntityAddToWorldEvent")`; `Events.ENTITY_ADD_TO_WORLD` also works.
- Cancellable: no; player: possible, depending on the runtime object.
- [Official Paper Javadoc](https://jd.papermc.io/paper/1.16.5/com/destroystokyo/paper/event/entity/EntityAddToWorldEvent.html) for meaning, trigger conditions, and Java API.

| `data` field | JSON type | Java getter | Java return type |
| --- | --- | --- | --- |
| `entity` | entity summary | `getEntity()` | `org.bukkit.entity.Entity` |
| `entityType` | string | `getEntityType()` | `org.bukkit.entity.EntityType` |

<a id="event-org-bukkit-event-entity-entityairchangeevent"></a>
### EntityAirChangeEvent

- Java class: `org.bukkit.event.entity.EntityAirChangeEvent`; parent: `org.bukkit.event.entity.EntityEvent`.
- Python subscription: `@bridge.on("EntityAirChangeEvent")`; `Events.ENTITY_AIR_CHANGE` also works.
- Cancellable: yes; player: possible, depending on the runtime object.
- [Official Paper Javadoc](https://jd.papermc.io/paper/1.16.5/org/bukkit/event/entity/EntityAirChangeEvent.html) for meaning, trigger conditions, and Java API.

| `data` field | JSON type | Java getter | Java return type |
| --- | --- | --- | --- |
| `amount` | number | `getAmount()` | `int` |
| `entity` | entity summary | `getEntity()` | `org.bukkit.entity.Entity` |
| `entityType` | string | `getEntityType()` | `org.bukkit.entity.EntityType` |

<a id="event-org-bukkit-event-entity-entitybreakdoorevent"></a>
### EntityBreakDoorEvent

- Java class: `org.bukkit.event.entity.EntityBreakDoorEvent`; parent: `org.bukkit.event.entity.EntityChangeBlockEvent`.
- Python subscription: `@bridge.on("EntityBreakDoorEvent")`; `Events.ENTITY_BREAK_DOOR` also works.
- Cancellable: yes; player: possible, depending on the runtime object.
- [Official Paper Javadoc](https://jd.papermc.io/paper/1.16.5/org/bukkit/event/entity/EntityBreakDoorEvent.html) for meaning, trigger conditions, and Java API.

| `data` field | JSON type | Java getter | Java return type |
| --- | --- | --- | --- |
| `block` | block summary | `getBlock()` | `org.bukkit.block.Block` |
| `entity` | entity summary | `getEntity()` | `org.bukkit.entity.Entity` |
| `entityType` | string | `getEntityType()` | `org.bukkit.entity.EntityType` |
| `to` | string | `getTo()` | `org.bukkit.Material` |

<a id="event-org-bukkit-event-entity-entitybreedevent"></a>
### EntityBreedEvent

- Java class: `org.bukkit.event.entity.EntityBreedEvent`; parent: `org.bukkit.event.entity.EntityEvent`.
- Python subscription: `@bridge.on("EntityBreedEvent")`; `Events.ENTITY_BREED` also works.
- Cancellable: yes; player: possible, depending on the runtime object.
- [Official Paper Javadoc](https://jd.papermc.io/paper/1.16.5/org/bukkit/event/entity/EntityBreedEvent.html) for meaning, trigger conditions, and Java API.

| `data` field | JSON type | Java getter | Java return type |
| --- | --- | --- | --- |
| `bredWith` | item summary | `getBredWith()` | `org.bukkit.inventory.ItemStack` |
| `breeder` | entity summary | `getBreeder()` | `org.bukkit.entity.LivingEntity` |
| `entity` | entity summary | `getEntity()` | `org.bukkit.entity.LivingEntity` |
| `entityType` | string | `getEntityType()` | `org.bukkit.entity.EntityType` |
| `experience` | number | `getExperience()` | `int` |
| `father` | entity summary | `getFather()` | `org.bukkit.entity.LivingEntity` |
| `mother` | entity summary | `getMother()` | `org.bukkit.entity.LivingEntity` |

<a id="event-org-bukkit-event-entity-entitychangeblockevent"></a>
### EntityChangeBlockEvent

- Java class: `org.bukkit.event.entity.EntityChangeBlockEvent`; parent: `org.bukkit.event.entity.EntityEvent`.
- Python subscription: `@bridge.on("EntityChangeBlockEvent")`; `Events.ENTITY_CHANGE_BLOCK` also works.
- Cancellable: yes; player: possible, depending on the runtime object.
- [Official Paper Javadoc](https://jd.papermc.io/paper/1.16.5/org/bukkit/event/entity/EntityChangeBlockEvent.html) for meaning, trigger conditions, and Java API.

| `data` field | JSON type | Java getter | Java return type |
| --- | --- | --- | --- |
| `block` | block summary | `getBlock()` | `org.bukkit.block.Block` |
| `entity` | entity summary | `getEntity()` | `org.bukkit.entity.Entity` |
| `entityType` | string | `getEntityType()` | `org.bukkit.entity.EntityType` |
| `to` | string | `getTo()` | `org.bukkit.Material` |

<a id="event-org-bukkit-event-entity-entitycombustbyblockevent"></a>
### EntityCombustByBlockEvent

- Java class: `org.bukkit.event.entity.EntityCombustByBlockEvent`; parent: `org.bukkit.event.entity.EntityCombustEvent`.
- Python subscription: `@bridge.on("EntityCombustByBlockEvent")`; `Events.ENTITY_COMBUST_BY_BLOCK` also works.
- Cancellable: yes; player: possible, depending on the runtime object.
- [Official Paper Javadoc](https://jd.papermc.io/paper/1.16.5/org/bukkit/event/entity/EntityCombustByBlockEvent.html) for meaning, trigger conditions, and Java API.

| `data` field | JSON type | Java getter | Java return type |
| --- | --- | --- | --- |
| `combuster` | block summary | `getCombuster()` | `org.bukkit.block.Block` |
| `duration` | number | `getDuration()` | `int` |
| `entity` | entity summary | `getEntity()` | `org.bukkit.entity.Entity` |
| `entityType` | string | `getEntityType()` | `org.bukkit.entity.EntityType` |

<a id="event-org-bukkit-event-entity-entitycombustbyentityevent"></a>
### EntityCombustByEntityEvent

- Java class: `org.bukkit.event.entity.EntityCombustByEntityEvent`; parent: `org.bukkit.event.entity.EntityCombustEvent`.
- Python subscription: `@bridge.on("EntityCombustByEntityEvent")`; `Events.ENTITY_COMBUST_BY_ENTITY` also works.
- Cancellable: yes; player: possible, depending on the runtime object.
- [Official Paper Javadoc](https://jd.papermc.io/paper/1.16.5/org/bukkit/event/entity/EntityCombustByEntityEvent.html) for meaning, trigger conditions, and Java API.

| `data` field | JSON type | Java getter | Java return type |
| --- | --- | --- | --- |
| `combuster` | entity summary | `getCombuster()` | `org.bukkit.entity.Entity` |
| `duration` | number | `getDuration()` | `int` |
| `entity` | entity summary | `getEntity()` | `org.bukkit.entity.Entity` |
| `entityType` | string | `getEntityType()` | `org.bukkit.entity.EntityType` |

<a id="event-org-bukkit-event-entity-entitycombustevent"></a>
### EntityCombustEvent

- Java class: `org.bukkit.event.entity.EntityCombustEvent`; parent: `org.bukkit.event.entity.EntityEvent`.
- Python subscription: `@bridge.on("EntityCombustEvent")`; `Events.ENTITY_COMBUST` also works.
- Cancellable: yes; player: possible, depending on the runtime object.
- [Official Paper Javadoc](https://jd.papermc.io/paper/1.16.5/org/bukkit/event/entity/EntityCombustEvent.html) for meaning, trigger conditions, and Java API.

| `data` field | JSON type | Java getter | Java return type |
| --- | --- | --- | --- |
| `duration` | number | `getDuration()` | `int` |
| `entity` | entity summary | `getEntity()` | `org.bukkit.entity.Entity` |
| `entityType` | string | `getEntityType()` | `org.bukkit.entity.EntityType` |

<a id="event-org-bukkit-event-entity-entitycreateportalevent"></a>
### EntityCreatePortalEvent

- Java class: `org.bukkit.event.entity.EntityCreatePortalEvent`; parent: `org.bukkit.event.entity.EntityEvent`.
- Python subscription: `@bridge.on("EntityCreatePortalEvent")`; `Events.ENTITY_CREATE_PORTAL` also works.
- Cancellable: yes; player: possible, depending on the runtime object.
- [Official Paper Javadoc](https://jd.papermc.io/paper/1.16.5/org/bukkit/event/entity/EntityCreatePortalEvent.html) for meaning, trigger conditions, and Java API.

| `data` field | JSON type | Java getter | Java return type |
| --- | --- | --- | --- |
| `entity` | entity summary | `getEntity()` | `org.bukkit.entity.LivingEntity` |
| `entityType` | string | `getEntityType()` | `org.bukkit.entity.EntityType` |
| `portalType` | string | `getPortalType()` | `org.bukkit.PortalType` |

<a id="event-org-bukkit-event-entity-entitydamagebyblockevent"></a>
### EntityDamageByBlockEvent

- Java class: `org.bukkit.event.entity.EntityDamageByBlockEvent`; parent: `org.bukkit.event.entity.EntityDamageEvent`.
- Python subscription: `@bridge.on("EntityDamageByBlockEvent")`; `Events.ENTITY_DAMAGE_BY_BLOCK` also works.
- Cancellable: yes; player: possible, depending on the runtime object.
- [Official Paper Javadoc](https://jd.papermc.io/paper/1.16.5/org/bukkit/event/entity/EntityDamageByBlockEvent.html) for meaning, trigger conditions, and Java API.

| `data` field | JSON type | Java getter | Java return type |
| --- | --- | --- | --- |
| `cause` | string | `getCause()` | `org.bukkit.event.entity.EntityDamageEvent$DamageCause` |
| `damage` | number | `getDamage()` | `double` |
| `damager` | block summary | `getDamager()` | `org.bukkit.block.Block` |
| `entity` | entity summary | `getEntity()` | `org.bukkit.entity.Entity` |
| `entityType` | string | `getEntityType()` | `org.bukkit.entity.EntityType` |
| `finalDamage` | number | `getFinalDamage()` | `double` |

<a id="event-org-bukkit-event-entity-entitydamagebyentityevent"></a>
### EntityDamageByEntityEvent

- Java class: `org.bukkit.event.entity.EntityDamageByEntityEvent`; parent: `org.bukkit.event.entity.EntityDamageEvent`.
- Python subscription: `@bridge.on("EntityDamageByEntityEvent")`; `Events.ENTITY_DAMAGE_BY_ENTITY` also works.
- Cancellable: yes; player: possible, depending on the runtime object.
- [Official Paper Javadoc](https://jd.papermc.io/paper/1.16.5/org/bukkit/event/entity/EntityDamageByEntityEvent.html) for meaning, trigger conditions, and Java API.

| `data` field | JSON type | Java getter | Java return type |
| --- | --- | --- | --- |
| `cause` | string | `getCause()` | `org.bukkit.event.entity.EntityDamageEvent$DamageCause` |
| `damage` | number | `getDamage()` | `double` |
| `damager` | entity summary | `getDamager()` | `org.bukkit.entity.Entity` |
| `entity` | entity summary | `getEntity()` | `org.bukkit.entity.Entity` |
| `entityType` | string | `getEntityType()` | `org.bukkit.entity.EntityType` |
| `finalDamage` | number | `getFinalDamage()` | `double` |

<a id="event-org-bukkit-event-entity-entitydamageevent"></a>
### EntityDamageEvent

- Java class: `org.bukkit.event.entity.EntityDamageEvent`; parent: `org.bukkit.event.entity.EntityEvent`.
- Python subscription: `@bridge.on("EntityDamageEvent")`; `Events.ENTITY_DAMAGE` also works.
- Cancellable: yes; player: possible, depending on the runtime object.
- [Official Paper Javadoc](https://jd.papermc.io/paper/1.16.5/org/bukkit/event/entity/EntityDamageEvent.html) for meaning, trigger conditions, and Java API.

| `data` field | JSON type | Java getter | Java return type |
| --- | --- | --- | --- |
| `cause` | string | `getCause()` | `org.bukkit.event.entity.EntityDamageEvent$DamageCause` |
| `damage` | number | `getDamage()` | `double` |
| `entity` | entity summary | `getEntity()` | `org.bukkit.entity.Entity` |
| `entityType` | string | `getEntityType()` | `org.bukkit.entity.EntityType` |
| `finalDamage` | number | `getFinalDamage()` | `double` |

<a id="event-org-bukkit-event-entity-entitydeathevent"></a>
### EntityDeathEvent

- Java class: `org.bukkit.event.entity.EntityDeathEvent`; parent: `org.bukkit.event.entity.EntityEvent`.
- Python subscription: `@bridge.on("EntityDeathEvent")`; `Events.ENTITY_DEATH` also works.
- Cancellable: yes; player: possible, depending on the runtime object.
- [Official Paper Javadoc](https://jd.papermc.io/paper/1.16.5/org/bukkit/event/entity/EntityDeathEvent.html) for meaning, trigger conditions, and Java API.

| `data` field | JSON type | Java getter | Java return type |
| --- | --- | --- | --- |
| `deathSound` | string | `getDeathSound()` | `org.bukkit.Sound` |
| `deathSoundCategory` | string | `getDeathSoundCategory()` | `org.bukkit.SoundCategory` |
| `deathSoundPitch` | number | `getDeathSoundPitch()` | `float` |
| `deathSoundVolume` | number | `getDeathSoundVolume()` | `float` |
| `droppedExp` | number | `getDroppedExp()` | `int` |
| `entity` | entity summary | `getEntity()` | `org.bukkit.entity.LivingEntity` |
| `entityType` | string | `getEntityType()` | `org.bukkit.entity.EntityType` |
| `reviveHealth` | number | `getReviveHealth()` | `double` |

<a id="event-org-bukkit-event-entity-entitydropitemevent"></a>
### EntityDropItemEvent

- Java class: `org.bukkit.event.entity.EntityDropItemEvent`; parent: `org.bukkit.event.entity.EntityEvent`.
- Python subscription: `@bridge.on("EntityDropItemEvent")`; `Events.ENTITY_DROP_ITEM` also works.
- Cancellable: yes; player: possible, depending on the runtime object.
- [Official Paper Javadoc](https://jd.papermc.io/paper/1.16.5/org/bukkit/event/entity/EntityDropItemEvent.html) for meaning, trigger conditions, and Java API.

| `data` field | JSON type | Java getter | Java return type |
| --- | --- | --- | --- |
| `entity` | entity summary | `getEntity()` | `org.bukkit.entity.Entity` |
| `entityType` | string | `getEntityType()` | `org.bukkit.entity.EntityType` |
| `itemDrop` | entity summary | `getItemDrop()` | `org.bukkit.entity.Item` |

<a id="event-org-bukkit-event-entity-entityenterblockevent"></a>
### EntityEnterBlockEvent

- Java class: `org.bukkit.event.entity.EntityEnterBlockEvent`; parent: `org.bukkit.event.entity.EntityEvent`.
- Python subscription: `@bridge.on("EntityEnterBlockEvent")`; `Events.ENTITY_ENTER_BLOCK` also works.
- Cancellable: yes; player: possible, depending on the runtime object.
- [Official Paper Javadoc](https://jd.papermc.io/paper/1.16.5/org/bukkit/event/entity/EntityEnterBlockEvent.html) for meaning, trigger conditions, and Java API.

| `data` field | JSON type | Java getter | Java return type |
| --- | --- | --- | --- |
| `block` | block summary | `getBlock()` | `org.bukkit.block.Block` |
| `entity` | entity summary | `getEntity()` | `org.bukkit.entity.Entity` |
| `entityType` | string | `getEntityType()` | `org.bukkit.entity.EntityType` |

<a id="event-org-bukkit-event-entity-entityenterlovemodeevent"></a>
### EntityEnterLoveModeEvent

- Java class: `org.bukkit.event.entity.EntityEnterLoveModeEvent`; parent: `org.bukkit.event.entity.EntityEvent`.
- Python subscription: `@bridge.on("EntityEnterLoveModeEvent")`; `Events.ENTITY_ENTER_LOVE_MODE` also works.
- Cancellable: yes; player: possible, depending on the runtime object.
- [Official Paper Javadoc](https://jd.papermc.io/paper/1.16.5/org/bukkit/event/entity/EntityEnterLoveModeEvent.html) for meaning, trigger conditions, and Java API.

| `data` field | JSON type | Java getter | Java return type |
| --- | --- | --- | --- |
| `entity` | entity summary | `getEntity()` | `org.bukkit.entity.Entity` |
| `entityType` | string | `getEntityType()` | `org.bukkit.entity.EntityType` |
| `humanEntity` | entity summary | `getHumanEntity()` | `org.bukkit.entity.HumanEntity` |
| `ticksInLove` | number | `getTicksInLove()` | `int` |

<a id="event-org-bukkit-event-entity-entityexhaustionevent"></a>
### EntityExhaustionEvent

- Java class: `org.bukkit.event.entity.EntityExhaustionEvent`; parent: `org.bukkit.event.entity.EntityEvent`.
- Python subscription: `@bridge.on("EntityExhaustionEvent")`; `Events.ENTITY_EXHAUSTION` also works.
- Cancellable: yes; player: possible, depending on the runtime object.
- [Official Paper Javadoc](https://jd.papermc.io/paper/1.16.5/org/bukkit/event/entity/EntityExhaustionEvent.html) for meaning, trigger conditions, and Java API.

| `data` field | JSON type | Java getter | Java return type |
| --- | --- | --- | --- |
| `entity` | entity summary | `getEntity()` | `org.bukkit.entity.HumanEntity` |
| `entityType` | string | `getEntityType()` | `org.bukkit.entity.EntityType` |
| `exhaustion` | number | `getExhaustion()` | `float` |
| `exhaustionReason` | string | `getExhaustionReason()` | `org.bukkit.event.entity.EntityExhaustionEvent$ExhaustionReason` |

<a id="event-org-bukkit-event-entity-entityexplodeevent"></a>
### EntityExplodeEvent

- Java class: `org.bukkit.event.entity.EntityExplodeEvent`; parent: `org.bukkit.event.entity.EntityEvent`.
- Python subscription: `@bridge.on("EntityExplodeEvent")`; `Events.ENTITY_EXPLODE` also works.
- Cancellable: yes; player: possible, depending on the runtime object.
- [Official Paper Javadoc](https://jd.papermc.io/paper/1.16.5/org/bukkit/event/entity/EntityExplodeEvent.html) for meaning, trigger conditions, and Java API.

| `data` field | JSON type | Java getter | Java return type |
| --- | --- | --- | --- |
| `entity` | entity summary | `getEntity()` | `org.bukkit.entity.Entity` |
| `entityType` | string | `getEntityType()` | `org.bukkit.entity.EntityType` |
| `location` | location summary | `getLocation()` | `org.bukkit.Location` |
| `yield` | number | `getYield()` | `float` |

<a id="event-io-papermc-paper-event-entity-entityinsideblockevent"></a>
### EntityInsideBlockEvent

- Java class: `io.papermc.paper.event.entity.EntityInsideBlockEvent`; parent: `org.bukkit.event.entity.EntityEvent`.
- Python subscription: `@bridge.on("EntityInsideBlockEvent")`; `Events.ENTITY_INSIDE_BLOCK` also works.
- Cancellable: yes; player: possible, depending on the runtime object.
- [Official Paper Javadoc](https://jd.papermc.io/paper/1.16.5/io/papermc/paper/event/entity/EntityInsideBlockEvent.html) for meaning, trigger conditions, and Java API.

| `data` field | JSON type | Java getter | Java return type |
| --- | --- | --- | --- |
| `block` | block summary | `getBlock()` | `org.bukkit.block.Block` |
| `entity` | entity summary | `getEntity()` | `org.bukkit.entity.Entity` |
| `entityType` | string | `getEntityType()` | `org.bukkit.entity.EntityType` |

<a id="event-org-bukkit-event-entity-entityinteractevent"></a>
### EntityInteractEvent

- Java class: `org.bukkit.event.entity.EntityInteractEvent`; parent: `org.bukkit.event.entity.EntityEvent`.
- Python subscription: `@bridge.on("EntityInteractEvent")`; `Events.ENTITY_INTERACT` also works.
- Cancellable: yes; player: possible, depending on the runtime object.
- [Official Paper Javadoc](https://jd.papermc.io/paper/1.16.5/org/bukkit/event/entity/EntityInteractEvent.html) for meaning, trigger conditions, and Java API.

| `data` field | JSON type | Java getter | Java return type |
| --- | --- | --- | --- |
| `block` | block summary | `getBlock()` | `org.bukkit.block.Block` |
| `entity` | entity summary | `getEntity()` | `org.bukkit.entity.Entity` |
| `entityType` | string | `getEntityType()` | `org.bukkit.entity.EntityType` |

<a id="event-com-destroystokyo-paper-event-entity-entityjumpevent"></a>
### EntityJumpEvent

- Java class: `com.destroystokyo.paper.event.entity.EntityJumpEvent`; parent: `org.bukkit.event.entity.EntityEvent`.
- Python subscription: `@bridge.on("EntityJumpEvent")`; `Events.ENTITY_JUMP` also works.
- Cancellable: yes; player: possible, depending on the runtime object.
- [Official Paper Javadoc](https://jd.papermc.io/paper/1.16.5/com/destroystokyo/paper/event/entity/EntityJumpEvent.html) for meaning, trigger conditions, and Java API.

| `data` field | JSON type | Java getter | Java return type |
| --- | --- | --- | --- |
| `entity` | entity summary | `getEntity()` | `org.bukkit.entity.Entity` |
| `entityType` | string | `getEntityType()` | `org.bukkit.entity.EntityType` |

<a id="event-com-destroystokyo-paper-event-entity-entityknockbackbyentityevent"></a>
### EntityKnockbackByEntityEvent

- Java class: `com.destroystokyo.paper.event.entity.EntityKnockbackByEntityEvent`; parent: `org.bukkit.event.entity.EntityEvent`.
- Python subscription: `@bridge.on("EntityKnockbackByEntityEvent")`; `Events.ENTITY_KNOCKBACK_BY_ENTITY` also works.
- Cancellable: yes; player: possible, depending on the runtime object.
- [Official Paper Javadoc](https://jd.papermc.io/paper/1.16.5/com/destroystokyo/paper/event/entity/EntityKnockbackByEntityEvent.html) for meaning, trigger conditions, and Java API.

| `data` field | JSON type | Java getter | Java return type |
| --- | --- | --- | --- |
| `entity` | entity summary | `getEntity()` | `org.bukkit.entity.Entity` |
| `entityType` | string | `getEntityType()` | `org.bukkit.entity.EntityType` |
| `hitBy` | entity summary | `getHitBy()` | `org.bukkit.entity.Entity` |
| `knockbackStrength` | number | `getKnockbackStrength()` | `float` |

<a id="event-io-papermc-paper-event-entity-entityloadcrossbowevent"></a>
### EntityLoadCrossbowEvent

- Java class: `io.papermc.paper.event.entity.EntityLoadCrossbowEvent`; parent: `org.bukkit.event.entity.EntityEvent`.
- Python subscription: `@bridge.on("EntityLoadCrossbowEvent")`; `Events.ENTITY_LOAD_CROSSBOW` also works.
- Cancellable: yes; player: possible, depending on the runtime object.
- [Official Paper Javadoc](https://jd.papermc.io/paper/1.16.5/io/papermc/paper/event/entity/EntityLoadCrossbowEvent.html) for meaning, trigger conditions, and Java API.

| `data` field | JSON type | Java getter | Java return type |
| --- | --- | --- | --- |
| `crossbow` | item summary | `getCrossbow()` | `org.bukkit.inventory.ItemStack` |
| `entity` | entity summary | `getEntity()` | `org.bukkit.entity.Entity` |
| `entityType` | string | `getEntityType()` | `org.bukkit.entity.EntityType` |
| `hand` | string | `getHand()` | `org.bukkit.inventory.EquipmentSlot` |

<a id="event-io-papermc-paper-event-entity-entitymoveevent"></a>
### EntityMoveEvent

- Java class: `io.papermc.paper.event.entity.EntityMoveEvent`; parent: `org.bukkit.event.entity.EntityEvent`.
- Python subscription: `@bridge.on("EntityMoveEvent")`; `Events.ENTITY_MOVE` also works.
- Cancellable: yes; player: possible, depending on the runtime object.
- [Official Paper Javadoc](https://jd.papermc.io/paper/1.16.5/io/papermc/paper/event/entity/EntityMoveEvent.html) for meaning, trigger conditions, and Java API.

| `data` field | JSON type | Java getter | Java return type |
| --- | --- | --- | --- |
| `entity` | entity summary | `getEntity()` | `org.bukkit.entity.LivingEntity` |
| `entityType` | string | `getEntityType()` | `org.bukkit.entity.EntityType` |
| `from` | location summary | `getFrom()` | `org.bukkit.Location` |
| `to` | location summary | `getTo()` | `org.bukkit.Location` |

<a id="event-com-destroystokyo-paper-event-entity-entitypathfindevent"></a>
### EntityPathfindEvent

- Java class: `com.destroystokyo.paper.event.entity.EntityPathfindEvent`; parent: `org.bukkit.event.entity.EntityEvent`.
- Python subscription: `@bridge.on("EntityPathfindEvent")`; `Events.ENTITY_PATHFIND` also works.
- Cancellable: yes; player: possible, depending on the runtime object.
- [Official Paper Javadoc](https://jd.papermc.io/paper/1.16.5/com/destroystokyo/paper/event/entity/EntityPathfindEvent.html) for meaning, trigger conditions, and Java API.

| `data` field | JSON type | Java getter | Java return type |
| --- | --- | --- | --- |
| `entity` | entity summary | `getEntity()` | `org.bukkit.entity.Entity` |
| `entityType` | string | `getEntityType()` | `org.bukkit.entity.EntityType` |
| `loc` | location summary | `getLoc()` | `org.bukkit.Location` |
| `targetEntity` | entity summary | `getTargetEntity()` | `org.bukkit.entity.Entity` |

<a id="event-org-bukkit-event-entity-entitypickupitemevent"></a>
### EntityPickupItemEvent

- Java class: `org.bukkit.event.entity.EntityPickupItemEvent`; parent: `org.bukkit.event.entity.EntityEvent`.
- Python subscription: `@bridge.on("EntityPickupItemEvent")`; `Events.ENTITY_PICKUP_ITEM` also works.
- Cancellable: yes; player: possible, depending on the runtime object.
- [Official Paper Javadoc](https://jd.papermc.io/paper/1.16.5/org/bukkit/event/entity/EntityPickupItemEvent.html) for meaning, trigger conditions, and Java API.

| `data` field | JSON type | Java getter | Java return type |
| --- | --- | --- | --- |
| `entity` | entity summary | `getEntity()` | `org.bukkit.entity.LivingEntity` |
| `entityType` | string | `getEntityType()` | `org.bukkit.entity.EntityType` |
| `item` | entity summary | `getItem()` | `org.bukkit.entity.Item` |
| `remaining` | number | `getRemaining()` | `int` |

<a id="event-org-bukkit-event-entity-entityplaceevent"></a>
### EntityPlaceEvent

- Java class: `org.bukkit.event.entity.EntityPlaceEvent`; parent: `org.bukkit.event.entity.EntityEvent`.
- Python subscription: `@bridge.on("EntityPlaceEvent")`; `Events.ENTITY_PLACE` also works.
- Cancellable: yes; player: possible, depending on the runtime object.
- [Official Paper Javadoc](https://jd.papermc.io/paper/1.16.5/org/bukkit/event/entity/EntityPlaceEvent.html) for meaning, trigger conditions, and Java API.

| `data` field | JSON type | Java getter | Java return type |
| --- | --- | --- | --- |
| `block` | block summary | `getBlock()` | `org.bukkit.block.Block` |
| `blockFace` | string | `getBlockFace()` | `org.bukkit.block.BlockFace` |
| `entity` | entity summary | `getEntity()` | `org.bukkit.entity.Entity` |
| `entityType` | string | `getEntityType()` | `org.bukkit.entity.EntityType` |

<a id="event-org-bukkit-event-entity-entityportalenterevent"></a>
### EntityPortalEnterEvent

- Java class: `org.bukkit.event.entity.EntityPortalEnterEvent`; parent: `org.bukkit.event.entity.EntityEvent`.
- Python subscription: `@bridge.on("EntityPortalEnterEvent")`; `Events.ENTITY_PORTAL_ENTER` also works.
- Cancellable: no; player: possible, depending on the runtime object.
- [Official Paper Javadoc](https://jd.papermc.io/paper/1.16.5/org/bukkit/event/entity/EntityPortalEnterEvent.html) for meaning, trigger conditions, and Java API.

| `data` field | JSON type | Java getter | Java return type |
| --- | --- | --- | --- |
| `entity` | entity summary | `getEntity()` | `org.bukkit.entity.Entity` |
| `entityType` | string | `getEntityType()` | `org.bukkit.entity.EntityType` |
| `location` | location summary | `getLocation()` | `org.bukkit.Location` |

<a id="event-org-bukkit-event-entity-entityportalevent"></a>
### EntityPortalEvent

- Java class: `org.bukkit.event.entity.EntityPortalEvent`; parent: `org.bukkit.event.entity.EntityTeleportEvent`.
- Python subscription: `@bridge.on("EntityPortalEvent")`; `Events.ENTITY_PORTAL` also works.
- Cancellable: yes; player: possible, depending on the runtime object.
- [Official Paper Javadoc](https://jd.papermc.io/paper/1.16.5/org/bukkit/event/entity/EntityPortalEvent.html) for meaning, trigger conditions, and Java API.

| `data` field | JSON type | Java getter | Java return type |
| --- | --- | --- | --- |
| `entity` | entity summary | `getEntity()` | `org.bukkit.entity.Entity` |
| `entityType` | string | `getEntityType()` | `org.bukkit.entity.EntityType` |
| `from` | location summary | `getFrom()` | `org.bukkit.Location` |
| `searchRadius` | number | `getSearchRadius()` | `int` |
| `to` | location summary | `getTo()` | `org.bukkit.Location` |

<a id="event-org-bukkit-event-entity-entityportalexitevent"></a>
### EntityPortalExitEvent

- Java class: `org.bukkit.event.entity.EntityPortalExitEvent`; parent: `org.bukkit.event.entity.EntityTeleportEvent`.
- Python subscription: `@bridge.on("EntityPortalExitEvent")`; `Events.ENTITY_PORTAL_EXIT` also works.
- Cancellable: yes; player: possible, depending on the runtime object.
- [Official Paper Javadoc](https://jd.papermc.io/paper/1.16.5/org/bukkit/event/entity/EntityPortalExitEvent.html) for meaning, trigger conditions, and Java API.

| `data` field | JSON type | Java getter | Java return type |
| --- | --- | --- | --- |
| `entity` | entity summary | `getEntity()` | `org.bukkit.entity.Entity` |
| `entityType` | string | `getEntityType()` | `org.bukkit.entity.EntityType` |
| `from` | location summary | `getFrom()` | `org.bukkit.Location` |
| `to` | location summary | `getTo()` | `org.bukkit.Location` |

<a id="event-org-bukkit-event-entity-entityposechangeevent"></a>
### EntityPoseChangeEvent

- Java class: `org.bukkit.event.entity.EntityPoseChangeEvent`; parent: `org.bukkit.event.entity.EntityEvent`.
- Python subscription: `@bridge.on("EntityPoseChangeEvent")`; `Events.ENTITY_POSE_CHANGE` also works.
- Cancellable: no; player: possible, depending on the runtime object.
- [Official Paper Javadoc](https://jd.papermc.io/paper/1.16.5/org/bukkit/event/entity/EntityPoseChangeEvent.html) for meaning, trigger conditions, and Java API.

| `data` field | JSON type | Java getter | Java return type |
| --- | --- | --- | --- |
| `entity` | entity summary | `getEntity()` | `org.bukkit.entity.Entity` |
| `entityType` | string | `getEntityType()` | `org.bukkit.entity.EntityType` |
| `pose` | string | `getPose()` | `org.bukkit.entity.Pose` |

<a id="event-org-bukkit-event-entity-entitypotioneffectevent"></a>
### EntityPotionEffectEvent

- Java class: `org.bukkit.event.entity.EntityPotionEffectEvent`; parent: `org.bukkit.event.entity.EntityEvent`.
- Python subscription: `@bridge.on("EntityPotionEffectEvent")`; `Events.ENTITY_POTION_EFFECT` also works.
- Cancellable: yes; player: possible, depending on the runtime object.
- [Official Paper Javadoc](https://jd.papermc.io/paper/1.16.5/org/bukkit/event/entity/EntityPotionEffectEvent.html) for meaning, trigger conditions, and Java API.

| `data` field | JSON type | Java getter | Java return type |
| --- | --- | --- | --- |
| `action` | string | `getAction()` | `org.bukkit.event.entity.EntityPotionEffectEvent$Action` |
| `cause` | string | `getCause()` | `org.bukkit.event.entity.EntityPotionEffectEvent$Cause` |
| `entity` | entity summary | `getEntity()` | `org.bukkit.entity.Entity` |
| `entityType` | string | `getEntityType()` | `org.bukkit.entity.EntityType` |
| `override` | boolean | `isOverride()` | `boolean` |

<a id="event-org-bukkit-event-entity-entityregainhealthevent"></a>
### EntityRegainHealthEvent

- Java class: `org.bukkit.event.entity.EntityRegainHealthEvent`; parent: `org.bukkit.event.entity.EntityEvent`.
- Python subscription: `@bridge.on("EntityRegainHealthEvent")`; `Events.ENTITY_REGAIN_HEALTH` also works.
- Cancellable: yes; player: possible, depending on the runtime object.
- [Official Paper Javadoc](https://jd.papermc.io/paper/1.16.5/org/bukkit/event/entity/EntityRegainHealthEvent.html) for meaning, trigger conditions, and Java API.

| `data` field | JSON type | Java getter | Java return type |
| --- | --- | --- | --- |
| `amount` | number | `getAmount()` | `double` |
| `entity` | entity summary | `getEntity()` | `org.bukkit.entity.Entity` |
| `entityType` | string | `getEntityType()` | `org.bukkit.entity.EntityType` |
| `regainReason` | string | `getRegainReason()` | `org.bukkit.event.entity.EntityRegainHealthEvent$RegainReason` |
| `fastRegen` | boolean | `isFastRegen()` | `boolean` |

<a id="event-com-destroystokyo-paper-event-entity-entityremovefromworldevent"></a>
### EntityRemoveFromWorldEvent

- Java class: `com.destroystokyo.paper.event.entity.EntityRemoveFromWorldEvent`; parent: `org.bukkit.event.entity.EntityEvent`.
- Python subscription: `@bridge.on("EntityRemoveFromWorldEvent")`; `Events.ENTITY_REMOVE_FROM_WORLD` also works.
- Cancellable: no; player: possible, depending on the runtime object.
- [Official Paper Javadoc](https://jd.papermc.io/paper/1.16.5/com/destroystokyo/paper/event/entity/EntityRemoveFromWorldEvent.html) for meaning, trigger conditions, and Java API.

| `data` field | JSON type | Java getter | Java return type |
| --- | --- | --- | --- |
| `entity` | entity summary | `getEntity()` | `org.bukkit.entity.Entity` |
| `entityType` | string | `getEntityType()` | `org.bukkit.entity.EntityType` |

<a id="event-org-bukkit-event-entity-entityresurrectevent"></a>
### EntityResurrectEvent

- Java class: `org.bukkit.event.entity.EntityResurrectEvent`; parent: `org.bukkit.event.entity.EntityEvent`.
- Python subscription: `@bridge.on("EntityResurrectEvent")`; `Events.ENTITY_RESURRECT` also works.
- Cancellable: yes; player: possible, depending on the runtime object.
- [Official Paper Javadoc](https://jd.papermc.io/paper/1.16.5/org/bukkit/event/entity/EntityResurrectEvent.html) for meaning, trigger conditions, and Java API.

| `data` field | JSON type | Java getter | Java return type |
| --- | --- | --- | --- |
| `entity` | entity summary | `getEntity()` | `org.bukkit.entity.Entity` |
| `entityType` | string | `getEntityType()` | `org.bukkit.entity.EntityType` |

<a id="event-org-bukkit-event-entity-entityshootbowevent"></a>
### EntityShootBowEvent

- Java class: `org.bukkit.event.entity.EntityShootBowEvent`; parent: `org.bukkit.event.entity.EntityEvent`.
- Python subscription: `@bridge.on("EntityShootBowEvent")`; `Events.ENTITY_SHOOT_BOW` also works.
- Cancellable: yes; player: possible, depending on the runtime object.
- [Official Paper Javadoc](https://jd.papermc.io/paper/1.16.5/org/bukkit/event/entity/EntityShootBowEvent.html) for meaning, trigger conditions, and Java API.

| `data` field | JSON type | Java getter | Java return type |
| --- | --- | --- | --- |
| `arrowItem` | item summary | `getArrowItem()` | `org.bukkit.inventory.ItemStack` |
| `bow` | item summary | `getBow()` | `org.bukkit.inventory.ItemStack` |
| `consumable` | item summary | `getConsumable()` | `org.bukkit.inventory.ItemStack` |
| `consumeArrow` | boolean | `getConsumeArrow()` | `boolean` |
| `entity` | entity summary | `getEntity()` | `org.bukkit.entity.LivingEntity` |
| `entityType` | string | `getEntityType()` | `org.bukkit.entity.EntityType` |
| `force` | number | `getForce()` | `float` |
| `hand` | string | `getHand()` | `org.bukkit.inventory.EquipmentSlot` |
| `projectile` | entity summary | `getProjectile()` | `org.bukkit.entity.Entity` |

<a id="event-org-bukkit-event-entity-entityspawnevent"></a>
### EntitySpawnEvent

- Java class: `org.bukkit.event.entity.EntitySpawnEvent`; parent: `org.bukkit.event.entity.EntityEvent`.
- Python subscription: `@bridge.on("EntitySpawnEvent")`; `Events.ENTITY_SPAWN` also works.
- Cancellable: yes; player: possible, depending on the runtime object.
- [Official Paper Javadoc](https://jd.papermc.io/paper/1.16.5/org/bukkit/event/entity/EntitySpawnEvent.html) for meaning, trigger conditions, and Java API.

| `data` field | JSON type | Java getter | Java return type |
| --- | --- | --- | --- |
| `entity` | entity summary | `getEntity()` | `org.bukkit.entity.Entity` |
| `entityType` | string | `getEntityType()` | `org.bukkit.entity.EntityType` |
| `location` | location summary | `getLocation()` | `org.bukkit.Location` |

<a id="event-org-bukkit-event-entity-entityspellcastevent"></a>
### EntitySpellCastEvent

- Java class: `org.bukkit.event.entity.EntitySpellCastEvent`; parent: `org.bukkit.event.entity.EntityEvent`.
- Python subscription: `@bridge.on("EntitySpellCastEvent")`; `Events.ENTITY_SPELL_CAST` also works.
- Cancellable: yes; player: possible, depending on the runtime object.
- [Official Paper Javadoc](https://jd.papermc.io/paper/1.16.5/org/bukkit/event/entity/EntitySpellCastEvent.html) for meaning, trigger conditions, and Java API.

| `data` field | JSON type | Java getter | Java return type |
| --- | --- | --- | --- |
| `entity` | entity summary | `getEntity()` | `org.bukkit.entity.Spellcaster` |
| `entityType` | string | `getEntityType()` | `org.bukkit.entity.EntityType` |
| `spell` | string | `getSpell()` | `org.bukkit.entity.Spellcaster$Spell` |

<a id="event-org-bukkit-event-entity-entitytameevent"></a>
### EntityTameEvent

- Java class: `org.bukkit.event.entity.EntityTameEvent`; parent: `org.bukkit.event.entity.EntityEvent`.
- Python subscription: `@bridge.on("EntityTameEvent")`; `Events.ENTITY_TAME` also works.
- Cancellable: yes; player: possible, depending on the runtime object.
- [Official Paper Javadoc](https://jd.papermc.io/paper/1.16.5/org/bukkit/event/entity/EntityTameEvent.html) for meaning, trigger conditions, and Java API.

| `data` field | JSON type | Java getter | Java return type |
| --- | --- | --- | --- |
| `entity` | entity summary | `getEntity()` | `org.bukkit.entity.LivingEntity` |
| `entityType` | string | `getEntityType()` | `org.bukkit.entity.EntityType` |

<a id="event-org-bukkit-event-entity-entitytargetevent"></a>
### EntityTargetEvent

- Java class: `org.bukkit.event.entity.EntityTargetEvent`; parent: `org.bukkit.event.entity.EntityEvent`.
- Python subscription: `@bridge.on("EntityTargetEvent")`; `Events.ENTITY_TARGET` also works.
- Cancellable: yes; player: possible, depending on the runtime object.
- [Official Paper Javadoc](https://jd.papermc.io/paper/1.16.5/org/bukkit/event/entity/EntityTargetEvent.html) for meaning, trigger conditions, and Java API.

| `data` field | JSON type | Java getter | Java return type |
| --- | --- | --- | --- |
| `entity` | entity summary | `getEntity()` | `org.bukkit.entity.Entity` |
| `entityType` | string | `getEntityType()` | `org.bukkit.entity.EntityType` |
| `reason` | string | `getReason()` | `org.bukkit.event.entity.EntityTargetEvent$TargetReason` |
| `target` | entity summary | `getTarget()` | `org.bukkit.entity.Entity` |

<a id="event-org-bukkit-event-entity-entitytargetlivingentityevent"></a>
### EntityTargetLivingEntityEvent

- Java class: `org.bukkit.event.entity.EntityTargetLivingEntityEvent`; parent: `org.bukkit.event.entity.EntityTargetEvent`.
- Python subscription: `@bridge.on("EntityTargetLivingEntityEvent")`; `Events.ENTITY_TARGET_LIVING_ENTITY` also works.
- Cancellable: yes; player: possible, depending on the runtime object.
- [Official Paper Javadoc](https://jd.papermc.io/paper/1.16.5/org/bukkit/event/entity/EntityTargetLivingEntityEvent.html) for meaning, trigger conditions, and Java API.

| `data` field | JSON type | Java getter | Java return type |
| --- | --- | --- | --- |
| `entity` | entity summary | `getEntity()` | `org.bukkit.entity.Entity` |
| `entityType` | string | `getEntityType()` | `org.bukkit.entity.EntityType` |
| `reason` | string | `getReason()` | `org.bukkit.event.entity.EntityTargetEvent$TargetReason` |
| `target` | entity summary | `getTarget()` | `org.bukkit.entity.LivingEntity` |

<a id="event-com-destroystokyo-paper-event-entity-entityteleportendgatewayevent"></a>
### EntityTeleportEndGatewayEvent

- Java class: `com.destroystokyo.paper.event.entity.EntityTeleportEndGatewayEvent`; parent: `org.bukkit.event.entity.EntityTeleportEvent`.
- Python subscription: `@bridge.on("EntityTeleportEndGatewayEvent")`; `Events.ENTITY_TELEPORT_END_GATEWAY` also works.
- Cancellable: yes; player: possible, depending on the runtime object.
- [Official Paper Javadoc](https://jd.papermc.io/paper/1.16.5/com/destroystokyo/paper/event/entity/EntityTeleportEndGatewayEvent.html) for meaning, trigger conditions, and Java API.

| `data` field | JSON type | Java getter | Java return type |
| --- | --- | --- | --- |
| `entity` | entity summary | `getEntity()` | `org.bukkit.entity.Entity` |
| `entityType` | string | `getEntityType()` | `org.bukkit.entity.EntityType` |
| `from` | location summary | `getFrom()` | `org.bukkit.Location` |
| `to` | location summary | `getTo()` | `org.bukkit.Location` |

<a id="event-org-bukkit-event-entity-entityteleportevent"></a>
### EntityTeleportEvent

- Java class: `org.bukkit.event.entity.EntityTeleportEvent`; parent: `org.bukkit.event.entity.EntityEvent`.
- Python subscription: `@bridge.on("EntityTeleportEvent")`; `Events.ENTITY_TELEPORT` also works.
- Cancellable: yes; player: possible, depending on the runtime object.
- [Official Paper Javadoc](https://jd.papermc.io/paper/1.16.5/org/bukkit/event/entity/EntityTeleportEvent.html) for meaning, trigger conditions, and Java API.

| `data` field | JSON type | Java getter | Java return type |
| --- | --- | --- | --- |
| `entity` | entity summary | `getEntity()` | `org.bukkit.entity.Entity` |
| `entityType` | string | `getEntityType()` | `org.bukkit.entity.EntityType` |
| `from` | location summary | `getFrom()` | `org.bukkit.Location` |
| `to` | location summary | `getTo()` | `org.bukkit.Location` |

<a id="event-org-bukkit-event-entity-entitytoggleglideevent"></a>
### EntityToggleGlideEvent

- Java class: `org.bukkit.event.entity.EntityToggleGlideEvent`; parent: `org.bukkit.event.entity.EntityEvent`.
- Python subscription: `@bridge.on("EntityToggleGlideEvent")`; `Events.ENTITY_TOGGLE_GLIDE` also works.
- Cancellable: yes; player: possible, depending on the runtime object.
- [Official Paper Javadoc](https://jd.papermc.io/paper/1.16.5/org/bukkit/event/entity/EntityToggleGlideEvent.html) for meaning, trigger conditions, and Java API.

| `data` field | JSON type | Java getter | Java return type |
| --- | --- | --- | --- |
| `entity` | entity summary | `getEntity()` | `org.bukkit.entity.Entity` |
| `entityType` | string | `getEntityType()` | `org.bukkit.entity.EntityType` |
| `gliding` | boolean | `isGliding()` | `boolean` |

<a id="event-org-bukkit-event-entity-entitytoggleswimevent"></a>
### EntityToggleSwimEvent

- Java class: `org.bukkit.event.entity.EntityToggleSwimEvent`; parent: `org.bukkit.event.entity.EntityEvent`.
- Python subscription: `@bridge.on("EntityToggleSwimEvent")`; `Events.ENTITY_TOGGLE_SWIM` also works.
- Cancellable: yes; player: possible, depending on the runtime object.
- [Official Paper Javadoc](https://jd.papermc.io/paper/1.16.5/org/bukkit/event/entity/EntityToggleSwimEvent.html) for meaning, trigger conditions, and Java API.

| `data` field | JSON type | Java getter | Java return type |
| --- | --- | --- | --- |
| `entity` | entity summary | `getEntity()` | `org.bukkit.entity.Entity` |
| `entityType` | string | `getEntityType()` | `org.bukkit.entity.EntityType` |
| `swimming` | boolean | `isSwimming()` | `boolean` |

<a id="event-com-destroystokyo-paper-event-entity-entitytransformedevent"></a>
### EntityTransformedEvent

- Java class: `com.destroystokyo.paper.event.entity.EntityTransformedEvent`; parent: `org.bukkit.event.entity.EntityEvent`.
- Python subscription: `@bridge.on("EntityTransformedEvent")`; `Events.ENTITY_TRANSFORMED` also works.
- Cancellable: yes; player: possible, depending on the runtime object.
- [Official Paper Javadoc](https://jd.papermc.io/paper/1.16.5/com/destroystokyo/paper/event/entity/EntityTransformedEvent.html) for meaning, trigger conditions, and Java API.

| `data` field | JSON type | Java getter | Java return type |
| --- | --- | --- | --- |
| `entity` | entity summary | `getEntity()` | `org.bukkit.entity.Entity` |
| `entityType` | string | `getEntityType()` | `org.bukkit.entity.EntityType` |
| `reason` | string | `getReason()` | `com.destroystokyo.paper.event.entity.EntityTransformedEvent$TransformedReason` |
| `transformed` | entity summary | `getTransformed()` | `org.bukkit.entity.Entity` |

<a id="event-org-bukkit-event-entity-entitytransformevent"></a>
### EntityTransformEvent

- Java class: `org.bukkit.event.entity.EntityTransformEvent`; parent: `org.bukkit.event.entity.EntityEvent`.
- Python subscription: `@bridge.on("EntityTransformEvent")`; `Events.ENTITY_TRANSFORM` also works.
- Cancellable: yes; player: possible, depending on the runtime object.
- [Official Paper Javadoc](https://jd.papermc.io/paper/1.16.5/org/bukkit/event/entity/EntityTransformEvent.html) for meaning, trigger conditions, and Java API.

| `data` field | JSON type | Java getter | Java return type |
| --- | --- | --- | --- |
| `entity` | entity summary | `getEntity()` | `org.bukkit.entity.Entity` |
| `entityType` | string | `getEntityType()` | `org.bukkit.entity.EntityType` |
| `transformReason` | string | `getTransformReason()` | `org.bukkit.event.entity.EntityTransformEvent$TransformReason` |
| `transformedEntity` | entity summary | `getTransformedEntity()` | `org.bukkit.entity.Entity` |

<a id="event-org-bukkit-event-entity-entityunleashevent"></a>
### EntityUnleashEvent

- Java class: `org.bukkit.event.entity.EntityUnleashEvent`; parent: `org.bukkit.event.entity.EntityEvent`.
- Python subscription: `@bridge.on("EntityUnleashEvent")`; `Events.ENTITY_UNLEASH` also works.
- Cancellable: no; player: possible, depending on the runtime object.
- [Official Paper Javadoc](https://jd.papermc.io/paper/1.16.5/org/bukkit/event/entity/EntityUnleashEvent.html) for meaning, trigger conditions, and Java API.

| `data` field | JSON type | Java getter | Java return type |
| --- | --- | --- | --- |
| `entity` | entity summary | `getEntity()` | `org.bukkit.entity.Entity` |
| `entityType` | string | `getEntityType()` | `org.bukkit.entity.EntityType` |
| `reason` | string | `getReason()` | `org.bukkit.event.entity.EntityUnleashEvent$UnleashReason` |
| `dropLeash` | boolean | `isDropLeash()` | `boolean` |

<a id="event-com-destroystokyo-paper-event-entity-entityzapevent"></a>
### EntityZapEvent

- Java class: `com.destroystokyo.paper.event.entity.EntityZapEvent`; parent: `org.bukkit.event.entity.EntityTransformEvent`.
- Python subscription: `@bridge.on("EntityZapEvent")`; `Events.ENTITY_ZAP` also works.
- Cancellable: yes; player: possible, depending on the runtime object.
- [Official Paper Javadoc](https://jd.papermc.io/paper/1.16.5/com/destroystokyo/paper/event/entity/EntityZapEvent.html) for meaning, trigger conditions, and Java API.

| `data` field | JSON type | Java getter | Java return type |
| --- | --- | --- | --- |
| `bolt` | entity summary | `getBolt()` | `org.bukkit.entity.LightningStrike` |
| `entity` | entity summary | `getEntity()` | `org.bukkit.entity.Entity` |
| `entityType` | string | `getEntityType()` | `org.bukkit.entity.EntityType` |
| `replacementEntity` | entity summary | `getReplacementEntity()` | `org.bukkit.entity.Entity` |
| `transformReason` | string | `getTransformReason()` | `org.bukkit.event.entity.EntityTransformEvent$TransformReason` |
| `transformedEntity` | entity summary | `getTransformedEntity()` | `org.bukkit.entity.Entity` |

<a id="event-org-bukkit-event-entity-expbottleevent"></a>
### ExpBottleEvent

- Java class: `org.bukkit.event.entity.ExpBottleEvent`; parent: `org.bukkit.event.entity.ProjectileHitEvent`.
- Python subscription: `@bridge.on("ExpBottleEvent")`; `Events.EXP_BOTTLE` also works.
- Cancellable: yes; player: possible, depending on the runtime object.
- [Official Paper Javadoc](https://jd.papermc.io/paper/1.16.5/org/bukkit/event/entity/ExpBottleEvent.html) for meaning, trigger conditions, and Java API.

| `data` field | JSON type | Java getter | Java return type |
| --- | --- | --- | --- |
| `entity` | entity summary | `getEntity()` | `org.bukkit.entity.Projectile` |
| `entityType` | string | `getEntityType()` | `org.bukkit.entity.EntityType` |
| `experience` | number | `getExperience()` | `int` |
| `hitBlock` | block summary | `getHitBlock()` | `org.bukkit.block.Block` |
| `hitBlockFace` | string | `getHitBlockFace()` | `org.bukkit.block.BlockFace` |
| `hitEntity` | entity summary | `getHitEntity()` | `org.bukkit.entity.Entity` |
| `showEffect` | boolean | `getShowEffect()` | `boolean` |

<a id="event-com-destroystokyo-paper-event-entity-experienceorbmergeevent"></a>
### ExperienceOrbMergeEvent

- Java class: `com.destroystokyo.paper.event.entity.ExperienceOrbMergeEvent`; parent: `org.bukkit.event.entity.EntityEvent`.
- Python subscription: `@bridge.on("ExperienceOrbMergeEvent")`; `Events.EXPERIENCE_ORB_MERGE` also works.
- Cancellable: yes; player: possible, depending on the runtime object.
- [Official Paper Javadoc](https://jd.papermc.io/paper/1.16.5/com/destroystokyo/paper/event/entity/ExperienceOrbMergeEvent.html) for meaning, trigger conditions, and Java API.

| `data` field | JSON type | Java getter | Java return type |
| --- | --- | --- | --- |
| `entity` | entity summary | `getEntity()` | `org.bukkit.entity.Entity` |
| `entityType` | string | `getEntityType()` | `org.bukkit.entity.EntityType` |
| `mergeSource` | entity summary | `getMergeSource()` | `org.bukkit.entity.ExperienceOrb` |
| `mergeTarget` | entity summary | `getMergeTarget()` | `org.bukkit.entity.ExperienceOrb` |

<a id="event-org-bukkit-event-entity-explosionprimeevent"></a>
### ExplosionPrimeEvent

- Java class: `org.bukkit.event.entity.ExplosionPrimeEvent`; parent: `org.bukkit.event.entity.EntityEvent`.
- Python subscription: `@bridge.on("ExplosionPrimeEvent")`; `Events.EXPLOSION_PRIME` also works.
- Cancellable: yes; player: possible, depending on the runtime object.
- [Official Paper Javadoc](https://jd.papermc.io/paper/1.16.5/org/bukkit/event/entity/ExplosionPrimeEvent.html) for meaning, trigger conditions, and Java API.

| `data` field | JSON type | Java getter | Java return type |
| --- | --- | --- | --- |
| `entity` | entity summary | `getEntity()` | `org.bukkit.entity.Entity` |
| `entityType` | string | `getEntityType()` | `org.bukkit.entity.EntityType` |
| `fire` | boolean | `getFire()` | `boolean` |
| `radius` | number | `getRadius()` | `float` |

<a id="event-org-bukkit-event-entity-fireworkexplodeevent"></a>
### FireworkExplodeEvent

- Java class: `org.bukkit.event.entity.FireworkExplodeEvent`; parent: `org.bukkit.event.entity.EntityEvent`.
- Python subscription: `@bridge.on("FireworkExplodeEvent")`; `Events.FIREWORK_EXPLODE` also works.
- Cancellable: yes; player: possible, depending on the runtime object.
- [Official Paper Javadoc](https://jd.papermc.io/paper/1.16.5/org/bukkit/event/entity/FireworkExplodeEvent.html) for meaning, trigger conditions, and Java API.

| `data` field | JSON type | Java getter | Java return type |
| --- | --- | --- | --- |
| `entity` | entity summary | `getEntity()` | `org.bukkit.entity.Entity` |
| `entityType` | string | `getEntityType()` | `org.bukkit.entity.EntityType` |

<a id="event-org-bukkit-event-entity-foodlevelchangeevent"></a>
### FoodLevelChangeEvent

- Java class: `org.bukkit.event.entity.FoodLevelChangeEvent`; parent: `org.bukkit.event.entity.EntityEvent`.
- Python subscription: `@bridge.on("FoodLevelChangeEvent")`; `Events.FOOD_LEVEL_CHANGE` also works.
- Cancellable: yes; player: possible, depending on the runtime object.
- [Official Paper Javadoc](https://jd.papermc.io/paper/1.16.5/org/bukkit/event/entity/FoodLevelChangeEvent.html) for meaning, trigger conditions, and Java API.

| `data` field | JSON type | Java getter | Java return type |
| --- | --- | --- | --- |
| `entity` | entity summary | `getEntity()` | `org.bukkit.entity.HumanEntity` |
| `entityType` | string | `getEntityType()` | `org.bukkit.entity.EntityType` |
| `foodLevel` | number | `getFoodLevel()` | `int` |
| `item` | item summary | `getItem()` | `org.bukkit.inventory.ItemStack` |

<a id="event-org-bukkit-event-entity-horsejumpevent"></a>
### HorseJumpEvent

- Java class: `org.bukkit.event.entity.HorseJumpEvent`; parent: `org.bukkit.event.entity.EntityEvent`.
- Python subscription: `@bridge.on("HorseJumpEvent")`; `Events.HORSE_JUMP` also works.
- Cancellable: yes; player: possible, depending on the runtime object.
- [Official Paper Javadoc](https://jd.papermc.io/paper/1.16.5/org/bukkit/event/entity/HorseJumpEvent.html) for meaning, trigger conditions, and Java API.

| `data` field | JSON type | Java getter | Java return type |
| --- | --- | --- | --- |
| `entity` | entity summary | `getEntity()` | `org.bukkit.entity.Entity` |
| `entityType` | string | `getEntityType()` | `org.bukkit.entity.EntityType` |
| `power` | number | `getPower()` | `float` |

<a id="event-org-bukkit-event-entity-itemdespawnevent"></a>
### ItemDespawnEvent

- Java class: `org.bukkit.event.entity.ItemDespawnEvent`; parent: `org.bukkit.event.entity.EntityEvent`.
- Python subscription: `@bridge.on("ItemDespawnEvent")`; `Events.ITEM_DESPAWN` also works.
- Cancellable: yes; player: possible, depending on the runtime object.
- [Official Paper Javadoc](https://jd.papermc.io/paper/1.16.5/org/bukkit/event/entity/ItemDespawnEvent.html) for meaning, trigger conditions, and Java API.

| `data` field | JSON type | Java getter | Java return type |
| --- | --- | --- | --- |
| `entity` | entity summary | `getEntity()` | `org.bukkit.entity.Entity` |
| `entityType` | string | `getEntityType()` | `org.bukkit.entity.EntityType` |
| `location` | location summary | `getLocation()` | `org.bukkit.Location` |

<a id="event-org-bukkit-event-entity-itemmergeevent"></a>
### ItemMergeEvent

- Java class: `org.bukkit.event.entity.ItemMergeEvent`; parent: `org.bukkit.event.entity.EntityEvent`.
- Python subscription: `@bridge.on("ItemMergeEvent")`; `Events.ITEM_MERGE` also works.
- Cancellable: yes; player: possible, depending on the runtime object.
- [Official Paper Javadoc](https://jd.papermc.io/paper/1.16.5/org/bukkit/event/entity/ItemMergeEvent.html) for meaning, trigger conditions, and Java API.

| `data` field | JSON type | Java getter | Java return type |
| --- | --- | --- | --- |
| `entity` | entity summary | `getEntity()` | `org.bukkit.entity.Entity` |
| `entityType` | string | `getEntityType()` | `org.bukkit.entity.EntityType` |
| `target` | entity summary | `getTarget()` | `org.bukkit.entity.Item` |

<a id="event-org-bukkit-event-entity-itemspawnevent"></a>
### ItemSpawnEvent

- Java class: `org.bukkit.event.entity.ItemSpawnEvent`; parent: `org.bukkit.event.entity.EntitySpawnEvent`.
- Python subscription: `@bridge.on("ItemSpawnEvent")`; `Events.ITEM_SPAWN` also works.
- Cancellable: yes; player: possible, depending on the runtime object.
- [Official Paper Javadoc](https://jd.papermc.io/paper/1.16.5/org/bukkit/event/entity/ItemSpawnEvent.html) for meaning, trigger conditions, and Java API.

| `data` field | JSON type | Java getter | Java return type |
| --- | --- | --- | --- |
| `entity` | entity summary | `getEntity()` | `org.bukkit.entity.Item` |
| `entityType` | string | `getEntityType()` | `org.bukkit.entity.EntityType` |
| `location` | location summary | `getLocation()` | `org.bukkit.Location` |

<a id="event-org-bukkit-event-entity-lingeringpotionsplashevent"></a>
### LingeringPotionSplashEvent

- Java class: `org.bukkit.event.entity.LingeringPotionSplashEvent`; parent: `org.bukkit.event.entity.ProjectileHitEvent`.
- Python subscription: `@bridge.on("LingeringPotionSplashEvent")`; `Events.LINGERING_POTION_SPLASH` also works.
- Cancellable: yes; player: possible, depending on the runtime object.
- [Official Paper Javadoc](https://jd.papermc.io/paper/1.16.5/org/bukkit/event/entity/LingeringPotionSplashEvent.html) for meaning, trigger conditions, and Java API.

| `data` field | JSON type | Java getter | Java return type |
| --- | --- | --- | --- |
| `areaEffectCloud` | entity summary | `getAreaEffectCloud()` | `org.bukkit.entity.AreaEffectCloud` |
| `entity` | entity summary | `getEntity()` | `org.bukkit.entity.ThrownPotion` |
| `entityType` | string | `getEntityType()` | `org.bukkit.entity.EntityType` |
| `hitBlock` | block summary | `getHitBlock()` | `org.bukkit.block.Block` |
| `hitBlockFace` | string | `getHitBlockFace()` | `org.bukkit.block.BlockFace` |
| `hitEntity` | entity summary | `getHitEntity()` | `org.bukkit.entity.Entity` |

<a id="event-com-destroystokyo-paper-event-entity-phantomprespawnevent"></a>
### PhantomPreSpawnEvent

- Java class: `com.destroystokyo.paper.event.entity.PhantomPreSpawnEvent`; parent: `com.destroystokyo.paper.event.entity.PreCreatureSpawnEvent`.
- Python subscription: `@bridge.on("PhantomPreSpawnEvent")`; `Events.PHANTOM_PRE_SPAWN` also works.
- Cancellable: yes; player: no known player getter.
- [Official Paper Javadoc](https://jd.papermc.io/paper/1.16.5/com/destroystokyo/paper/event/entity/PhantomPreSpawnEvent.html) for meaning, trigger conditions, and Java API.

| `data` field | JSON type | Java getter | Java return type |
| --- | --- | --- | --- |
| `reason` | string | `getReason()` | `org.bukkit.event.entity.CreatureSpawnEvent$SpawnReason` |
| `spawnLocation` | location summary | `getSpawnLocation()` | `org.bukkit.Location` |
| `spawningEntity` | entity summary | `getSpawningEntity()` | `org.bukkit.entity.Entity` |
| `type` | string | `getType()` | `org.bukkit.entity.EntityType` |

<a id="event-org-bukkit-event-entity-piglinbarterevent"></a>
### PiglinBarterEvent

- Java class: `org.bukkit.event.entity.PiglinBarterEvent`; parent: `org.bukkit.event.entity.EntityEvent`.
- Python subscription: `@bridge.on("PiglinBarterEvent")`; `Events.PIGLIN_BARTER` also works.
- Cancellable: yes; player: possible, depending on the runtime object.
- [Official Paper Javadoc](https://jd.papermc.io/paper/1.16.5/org/bukkit/event/entity/PiglinBarterEvent.html) for meaning, trigger conditions, and Java API.

| `data` field | JSON type | Java getter | Java return type |
| --- | --- | --- | --- |
| `entity` | entity summary | `getEntity()` | `org.bukkit.entity.Entity` |
| `entityType` | string | `getEntityType()` | `org.bukkit.entity.EntityType` |
| `input` | item summary | `getInput()` | `org.bukkit.inventory.ItemStack` |

<a id="event-org-bukkit-event-entity-pigzapevent"></a>
### PigZapEvent

- Java class: `org.bukkit.event.entity.PigZapEvent`; parent: `com.destroystokyo.paper.event.entity.EntityZapEvent`.
- Python subscription: `@bridge.on("PigZapEvent")`; `Events.PIG_ZAP` also works.
- Cancellable: yes; player: possible, depending on the runtime object.
- [Official Paper Javadoc](https://jd.papermc.io/paper/1.16.5/org/bukkit/event/entity/PigZapEvent.html) for meaning, trigger conditions, and Java API.

| `data` field | JSON type | Java getter | Java return type |
| --- | --- | --- | --- |
| `bolt` | entity summary | `getBolt()` | `org.bukkit.entity.LightningStrike` |
| `entity` | entity summary | `getEntity()` | `org.bukkit.entity.Entity` |
| `entityType` | string | `getEntityType()` | `org.bukkit.entity.EntityType` |
| `lightning` | entity summary | `getLightning()` | `org.bukkit.entity.LightningStrike` |
| `pigZombie` | entity summary | `getPigZombie()` | `org.bukkit.entity.PigZombie` |
| `replacementEntity` | entity summary | `getReplacementEntity()` | `org.bukkit.entity.Entity` |
| `transformReason` | string | `getTransformReason()` | `org.bukkit.event.entity.EntityTransformEvent$TransformReason` |
| `transformedEntity` | entity summary | `getTransformedEntity()` | `org.bukkit.entity.Entity` |

<a id="event-org-bukkit-event-entity-pigzombieangerevent"></a>
### PigZombieAngerEvent

- Java class: `org.bukkit.event.entity.PigZombieAngerEvent`; parent: `org.bukkit.event.entity.EntityEvent`.
- Python subscription: `@bridge.on("PigZombieAngerEvent")`; `Events.PIG_ZOMBIE_ANGER` also works.
- Cancellable: yes; player: possible, depending on the runtime object.
- [Official Paper Javadoc](https://jd.papermc.io/paper/1.16.5/org/bukkit/event/entity/PigZombieAngerEvent.html) for meaning, trigger conditions, and Java API.

| `data` field | JSON type | Java getter | Java return type |
| --- | --- | --- | --- |
| `entity` | entity summary | `getEntity()` | `org.bukkit.entity.PigZombie` |
| `entityType` | string | `getEntityType()` | `org.bukkit.entity.EntityType` |
| `newAnger` | number | `getNewAnger()` | `int` |
| `target` | entity summary | `getTarget()` | `org.bukkit.entity.Entity` |

<a id="event-org-bukkit-event-entity-playerdeathevent"></a>
### PlayerDeathEvent

- Java class: `org.bukkit.event.entity.PlayerDeathEvent`; parent: `org.bukkit.event.entity.EntityDeathEvent`.
- Python subscription: `@bridge.on("PlayerDeathEvent")`; `Events.PLAYER_DEATH` also works.
- Cancellable: yes; player: possible, depending on the runtime object.
- [Official Paper Javadoc](https://jd.papermc.io/paper/1.16.5/org/bukkit/event/entity/PlayerDeathEvent.html) for meaning, trigger conditions, and Java API.

| `data` field | JSON type | Java getter | Java return type |
| --- | --- | --- | --- |
| `deathMessage` | string | `getDeathMessage()` | `java.lang.String` |
| `deathSound` | string | `getDeathSound()` | `org.bukkit.Sound` |
| `deathSoundCategory` | string | `getDeathSoundCategory()` | `org.bukkit.SoundCategory` |
| `deathSoundPitch` | number | `getDeathSoundPitch()` | `float` |
| `deathSoundVolume` | number | `getDeathSoundVolume()` | `float` |
| `droppedExp` | number | `getDroppedExp()` | `int` |
| `entity` | entity summary | `getEntity()` | `org.bukkit.entity.LivingEntity` |
| `entityType` | string | `getEntityType()` | `org.bukkit.entity.EntityType` |
| `keepInventory` | boolean | `getKeepInventory()` | `boolean` |
| `keepLevel` | boolean | `getKeepLevel()` | `boolean` |
| `newExp` | number | `getNewExp()` | `int` |
| `newLevel` | number | `getNewLevel()` | `int` |
| `newTotalExp` | number | `getNewTotalExp()` | `int` |
| `reviveHealth` | number | `getReviveHealth()` | `double` |

<a id="event-org-bukkit-event-entity-playerleashentityevent"></a>
### PlayerLeashEntityEvent

- Java class: `org.bukkit.event.entity.PlayerLeashEntityEvent`; parent: `org.bukkit.event.Event`.
- Python subscription: `@bridge.on("PlayerLeashEntityEvent")`; `Events.PLAYER_LEASH_ENTITY` also works.
- Cancellable: yes; player: possible, depending on the runtime object.
- [Official Paper Javadoc](https://jd.papermc.io/paper/1.16.5/org/bukkit/event/entity/PlayerLeashEntityEvent.html) for meaning, trigger conditions, and Java API.

| `data` field | JSON type | Java getter | Java return type |
| --- | --- | --- | --- |
| `entity` | entity summary | `getEntity()` | `org.bukkit.entity.Entity` |
| `leashHolder` | entity summary | `getLeashHolder()` | `org.bukkit.entity.Entity` |

<a id="event-com-destroystokyo-paper-event-entity-playernaturallyspawncreaturesevent"></a>
### PlayerNaturallySpawnCreaturesEvent

- Java class: `com.destroystokyo.paper.event.entity.PlayerNaturallySpawnCreaturesEvent`; parent: `org.bukkit.event.player.PlayerEvent`.
- Python subscription: `@bridge.on("PlayerNaturallySpawnCreaturesEvent")`; `Events.PLAYER_NATURALLY_SPAWN_CREATURES` also works.
- Cancellable: yes; player: possible, depending on the runtime object.
- [Official Paper Javadoc](https://jd.papermc.io/paper/1.16.5/com/destroystokyo/paper/event/entity/PlayerNaturallySpawnCreaturesEvent.html) for meaning, trigger conditions, and Java API.

| `data` field | JSON type | Java getter | Java return type |
| --- | --- | --- | --- |
| `spawnRadius` | number | `getSpawnRadius()` | `byte` |

<a id="event-org-bukkit-event-entity-potionsplashevent"></a>
### PotionSplashEvent

- Java class: `org.bukkit.event.entity.PotionSplashEvent`; parent: `org.bukkit.event.entity.ProjectileHitEvent`.
- Python subscription: `@bridge.on("PotionSplashEvent")`; `Events.POTION_SPLASH` also works.
- Cancellable: yes; player: possible, depending on the runtime object.
- [Official Paper Javadoc](https://jd.papermc.io/paper/1.16.5/org/bukkit/event/entity/PotionSplashEvent.html) for meaning, trigger conditions, and Java API.

| `data` field | JSON type | Java getter | Java return type |
| --- | --- | --- | --- |
| `entity` | entity summary | `getEntity()` | `org.bukkit.entity.Entity` |
| `entityType` | string | `getEntityType()` | `org.bukkit.entity.EntityType` |
| `hitBlock` | block summary | `getHitBlock()` | `org.bukkit.block.Block` |
| `hitBlockFace` | string | `getHitBlockFace()` | `org.bukkit.block.BlockFace` |
| `hitEntity` | entity summary | `getHitEntity()` | `org.bukkit.entity.Entity` |
| `potion` | entity summary | `getPotion()` | `org.bukkit.entity.ThrownPotion` |

<a id="event-com-destroystokyo-paper-event-entity-precreaturespawnevent"></a>
### PreCreatureSpawnEvent

- Java class: `com.destroystokyo.paper.event.entity.PreCreatureSpawnEvent`; parent: `org.bukkit.event.Event`.
- Python subscription: `@bridge.on("PreCreatureSpawnEvent")`; `Events.PRE_CREATURE_SPAWN` also works.
- Cancellable: yes; player: no known player getter.
- [Official Paper Javadoc](https://jd.papermc.io/paper/1.16.5/com/destroystokyo/paper/event/entity/PreCreatureSpawnEvent.html) for meaning, trigger conditions, and Java API.

| `data` field | JSON type | Java getter | Java return type |
| --- | --- | --- | --- |
| `reason` | string | `getReason()` | `org.bukkit.event.entity.CreatureSpawnEvent$SpawnReason` |
| `spawnLocation` | location summary | `getSpawnLocation()` | `org.bukkit.Location` |
| `type` | string | `getType()` | `org.bukkit.entity.EntityType` |

<a id="event-com-destroystokyo-paper-event-entity-prespawnerspawnevent"></a>
### PreSpawnerSpawnEvent

- Java class: `com.destroystokyo.paper.event.entity.PreSpawnerSpawnEvent`; parent: `com.destroystokyo.paper.event.entity.PreCreatureSpawnEvent`.
- Python subscription: `@bridge.on("PreSpawnerSpawnEvent")`; `Events.PRE_SPAWNER_SPAWN` also works.
- Cancellable: yes; player: no known player getter.
- [Official Paper Javadoc](https://jd.papermc.io/paper/1.16.5/com/destroystokyo/paper/event/entity/PreSpawnerSpawnEvent.html) for meaning, trigger conditions, and Java API.

| `data` field | JSON type | Java getter | Java return type |
| --- | --- | --- | --- |
| `reason` | string | `getReason()` | `org.bukkit.event.entity.CreatureSpawnEvent$SpawnReason` |
| `spawnLocation` | location summary | `getSpawnLocation()` | `org.bukkit.Location` |
| `spawnerLocation` | location summary | `getSpawnerLocation()` | `org.bukkit.Location` |
| `type` | string | `getType()` | `org.bukkit.entity.EntityType` |

<a id="event-com-destroystokyo-paper-event-entity-projectilecollideevent"></a>
### ProjectileCollideEvent

- Java class: `com.destroystokyo.paper.event.entity.ProjectileCollideEvent`; parent: `org.bukkit.event.entity.EntityEvent`.
- Python subscription: `@bridge.on("ProjectileCollideEvent")`; `Events.PROJECTILE_COLLIDE` also works.
- Cancellable: yes; player: possible, depending on the runtime object.
- [Official Paper Javadoc](https://jd.papermc.io/paper/1.16.5/com/destroystokyo/paper/event/entity/ProjectileCollideEvent.html) for meaning, trigger conditions, and Java API.

| `data` field | JSON type | Java getter | Java return type |
| --- | --- | --- | --- |
| `collidedWith` | entity summary | `getCollidedWith()` | `org.bukkit.entity.Entity` |
| `entity` | entity summary | `getEntity()` | `org.bukkit.entity.Entity` |
| `entityType` | string | `getEntityType()` | `org.bukkit.entity.EntityType` |

<a id="event-org-bukkit-event-entity-projectilehitevent"></a>
### ProjectileHitEvent

- Java class: `org.bukkit.event.entity.ProjectileHitEvent`; parent: `org.bukkit.event.entity.EntityEvent`.
- Python subscription: `@bridge.on("ProjectileHitEvent")`; `Events.PROJECTILE_HIT` also works.
- Cancellable: yes; player: possible, depending on the runtime object.
- [Official Paper Javadoc](https://jd.papermc.io/paper/1.16.5/org/bukkit/event/entity/ProjectileHitEvent.html) for meaning, trigger conditions, and Java API.

| `data` field | JSON type | Java getter | Java return type |
| --- | --- | --- | --- |
| `entity` | entity summary | `getEntity()` | `org.bukkit.entity.Projectile` |
| `entityType` | string | `getEntityType()` | `org.bukkit.entity.EntityType` |
| `hitBlock` | block summary | `getHitBlock()` | `org.bukkit.block.Block` |
| `hitBlockFace` | string | `getHitBlockFace()` | `org.bukkit.block.BlockFace` |
| `hitEntity` | entity summary | `getHitEntity()` | `org.bukkit.entity.Entity` |

<a id="event-org-bukkit-event-entity-projectilelaunchevent"></a>
### ProjectileLaunchEvent

- Java class: `org.bukkit.event.entity.ProjectileLaunchEvent`; parent: `org.bukkit.event.entity.EntitySpawnEvent`.
- Python subscription: `@bridge.on("ProjectileLaunchEvent")`; `Events.PROJECTILE_LAUNCH` also works.
- Cancellable: yes; player: possible, depending on the runtime object.
- [Official Paper Javadoc](https://jd.papermc.io/paper/1.16.5/org/bukkit/event/entity/ProjectileLaunchEvent.html) for meaning, trigger conditions, and Java API.

| `data` field | JSON type | Java getter | Java return type |
| --- | --- | --- | --- |
| `entity` | entity summary | `getEntity()` | `org.bukkit.entity.Entity` |
| `entityType` | string | `getEntityType()` | `org.bukkit.entity.EntityType` |
| `location` | location summary | `getLocation()` | `org.bukkit.Location` |

<a id="event-io-papermc-paper-event-entity-pufferfishstatechangeevent"></a>
### PufferFishStateChangeEvent

- Java class: `io.papermc.paper.event.entity.PufferFishStateChangeEvent`; parent: `org.bukkit.event.entity.EntityEvent`.
- Python subscription: `@bridge.on("PufferFishStateChangeEvent")`; `Events.PUFFER_FISH_STATE_CHANGE` also works.
- Cancellable: yes; player: possible, depending on the runtime object.
- [Official Paper Javadoc](https://jd.papermc.io/paper/1.16.5/io/papermc/paper/event/entity/PufferFishStateChangeEvent.html) for meaning, trigger conditions, and Java API.

| `data` field | JSON type | Java getter | Java return type |
| --- | --- | --- | --- |
| `entity` | entity summary | `getEntity()` | `org.bukkit.entity.Entity` |
| `entityType` | string | `getEntityType()` | `org.bukkit.entity.EntityType` |
| `newPuffState` | number | `getNewPuffState()` | `int` |
| `deflating` | boolean | `isDeflating()` | `boolean` |
| `inflating` | boolean | `isInflating()` | `boolean` |

<a id="event-org-bukkit-event-entity-sheepdyewoolevent"></a>
### SheepDyeWoolEvent

- Java class: `org.bukkit.event.entity.SheepDyeWoolEvent`; parent: `org.bukkit.event.entity.EntityEvent`.
- Python subscription: `@bridge.on("SheepDyeWoolEvent")`; `Events.SHEEP_DYE_WOOL` also works.
- Cancellable: yes; player: possible, depending on the runtime object.
- [Official Paper Javadoc](https://jd.papermc.io/paper/1.16.5/org/bukkit/event/entity/SheepDyeWoolEvent.html) for meaning, trigger conditions, and Java API.

| `data` field | JSON type | Java getter | Java return type |
| --- | --- | --- | --- |
| `color` | string | `getColor()` | `org.bukkit.DyeColor` |
| `entity` | entity summary | `getEntity()` | `org.bukkit.entity.Entity` |
| `entityType` | string | `getEntityType()` | `org.bukkit.entity.EntityType` |

<a id="event-org-bukkit-event-entity-sheepregrowwoolevent"></a>
### SheepRegrowWoolEvent

- Java class: `org.bukkit.event.entity.SheepRegrowWoolEvent`; parent: `org.bukkit.event.entity.EntityEvent`.
- Python subscription: `@bridge.on("SheepRegrowWoolEvent")`; `Events.SHEEP_REGROW_WOOL` also works.
- Cancellable: yes; player: possible, depending on the runtime object.
- [Official Paper Javadoc](https://jd.papermc.io/paper/1.16.5/org/bukkit/event/entity/SheepRegrowWoolEvent.html) for meaning, trigger conditions, and Java API.

| `data` field | JSON type | Java getter | Java return type |
| --- | --- | --- | --- |
| `entity` | entity summary | `getEntity()` | `org.bukkit.entity.Entity` |
| `entityType` | string | `getEntityType()` | `org.bukkit.entity.EntityType` |

<a id="event-com-destroystokyo-paper-event-entity-skeletonhorsetrapevent"></a>
### SkeletonHorseTrapEvent

- Java class: `com.destroystokyo.paper.event.entity.SkeletonHorseTrapEvent`; parent: `org.bukkit.event.entity.EntityEvent`.
- Python subscription: `@bridge.on("SkeletonHorseTrapEvent")`; `Events.SKELETON_HORSE_TRAP` also works.
- Cancellable: yes; player: possible, depending on the runtime object.
- [Official Paper Javadoc](https://jd.papermc.io/paper/1.16.5/com/destroystokyo/paper/event/entity/SkeletonHorseTrapEvent.html) for meaning, trigger conditions, and Java API.

| `data` field | JSON type | Java getter | Java return type |
| --- | --- | --- | --- |
| `entity` | entity summary | `getEntity()` | `org.bukkit.entity.SkeletonHorse` |
| `entityType` | string | `getEntityType()` | `org.bukkit.entity.EntityType` |

<a id="event-com-destroystokyo-paper-event-entity-slimechangedirectionevent"></a>
### SlimeChangeDirectionEvent

- Java class: `com.destroystokyo.paper.event.entity.SlimeChangeDirectionEvent`; parent: `com.destroystokyo.paper.event.entity.SlimePathfindEvent`.
- Python subscription: `@bridge.on("SlimeChangeDirectionEvent")`; `Events.SLIME_CHANGE_DIRECTION` also works.
- Cancellable: yes; player: possible, depending on the runtime object.
- [Official Paper Javadoc](https://jd.papermc.io/paper/1.16.5/com/destroystokyo/paper/event/entity/SlimeChangeDirectionEvent.html) for meaning, trigger conditions, and Java API.

| `data` field | JSON type | Java getter | Java return type |
| --- | --- | --- | --- |
| `entity` | entity summary | `getEntity()` | `org.bukkit.entity.Slime` |
| `entityType` | string | `getEntityType()` | `org.bukkit.entity.EntityType` |
| `newYaw` | number | `getNewYaw()` | `float` |

<a id="event-com-destroystokyo-paper-event-entity-slimepathfindevent"></a>
### SlimePathfindEvent

- Java class: `com.destroystokyo.paper.event.entity.SlimePathfindEvent`; parent: `org.bukkit.event.entity.EntityEvent`.
- Python subscription: `@bridge.on("SlimePathfindEvent")`; `Events.SLIME_PATHFIND` also works.
- Cancellable: yes; player: possible, depending on the runtime object.
- [Official Paper Javadoc](https://jd.papermc.io/paper/1.16.5/com/destroystokyo/paper/event/entity/SlimePathfindEvent.html) for meaning, trigger conditions, and Java API.

| `data` field | JSON type | Java getter | Java return type |
| --- | --- | --- | --- |
| `entity` | entity summary | `getEntity()` | `org.bukkit.entity.Slime` |
| `entityType` | string | `getEntityType()` | `org.bukkit.entity.EntityType` |

<a id="event-org-bukkit-event-entity-slimesplitevent"></a>
### SlimeSplitEvent

- Java class: `org.bukkit.event.entity.SlimeSplitEvent`; parent: `org.bukkit.event.entity.EntityEvent`.
- Python subscription: `@bridge.on("SlimeSplitEvent")`; `Events.SLIME_SPLIT` also works.
- Cancellable: yes; player: possible, depending on the runtime object.
- [Official Paper Javadoc](https://jd.papermc.io/paper/1.16.5/org/bukkit/event/entity/SlimeSplitEvent.html) for meaning, trigger conditions, and Java API.

| `data` field | JSON type | Java getter | Java return type |
| --- | --- | --- | --- |
| `count` | number | `getCount()` | `int` |
| `entity` | entity summary | `getEntity()` | `org.bukkit.entity.Slime` |
| `entityType` | string | `getEntityType()` | `org.bukkit.entity.EntityType` |

<a id="event-com-destroystokyo-paper-event-entity-slimeswimevent"></a>
### SlimeSwimEvent

- Java class: `com.destroystokyo.paper.event.entity.SlimeSwimEvent`; parent: `com.destroystokyo.paper.event.entity.SlimeWanderEvent`.
- Python subscription: `@bridge.on("SlimeSwimEvent")`; `Events.SLIME_SWIM` also works.
- Cancellable: yes; player: possible, depending on the runtime object.
- [Official Paper Javadoc](https://jd.papermc.io/paper/1.16.5/com/destroystokyo/paper/event/entity/SlimeSwimEvent.html) for meaning, trigger conditions, and Java API.

| `data` field | JSON type | Java getter | Java return type |
| --- | --- | --- | --- |
| `entity` | entity summary | `getEntity()` | `org.bukkit.entity.Slime` |
| `entityType` | string | `getEntityType()` | `org.bukkit.entity.EntityType` |

<a id="event-com-destroystokyo-paper-event-entity-slimetargetlivingentityevent"></a>
### SlimeTargetLivingEntityEvent

- Java class: `com.destroystokyo.paper.event.entity.SlimeTargetLivingEntityEvent`; parent: `com.destroystokyo.paper.event.entity.SlimePathfindEvent`.
- Python subscription: `@bridge.on("SlimeTargetLivingEntityEvent")`; `Events.SLIME_TARGET_LIVING_ENTITY` also works.
- Cancellable: yes; player: possible, depending on the runtime object.
- [Official Paper Javadoc](https://jd.papermc.io/paper/1.16.5/com/destroystokyo/paper/event/entity/SlimeTargetLivingEntityEvent.html) for meaning, trigger conditions, and Java API.

| `data` field | JSON type | Java getter | Java return type |
| --- | --- | --- | --- |
| `entity` | entity summary | `getEntity()` | `org.bukkit.entity.Slime` |
| `entityType` | string | `getEntityType()` | `org.bukkit.entity.EntityType` |
| `target` | entity summary | `getTarget()` | `org.bukkit.entity.LivingEntity` |

<a id="event-com-destroystokyo-paper-event-entity-slimewanderevent"></a>
### SlimeWanderEvent

- Java class: `com.destroystokyo.paper.event.entity.SlimeWanderEvent`; parent: `com.destroystokyo.paper.event.entity.SlimePathfindEvent`.
- Python subscription: `@bridge.on("SlimeWanderEvent")`; `Events.SLIME_WANDER` also works.
- Cancellable: yes; player: possible, depending on the runtime object.
- [Official Paper Javadoc](https://jd.papermc.io/paper/1.16.5/com/destroystokyo/paper/event/entity/SlimeWanderEvent.html) for meaning, trigger conditions, and Java API.

| `data` field | JSON type | Java getter | Java return type |
| --- | --- | --- | --- |
| `entity` | entity summary | `getEntity()` | `org.bukkit.entity.Slime` |
| `entityType` | string | `getEntityType()` | `org.bukkit.entity.EntityType` |

<a id="event-org-bukkit-event-entity-spawnerspawnevent"></a>
### SpawnerSpawnEvent

- Java class: `org.bukkit.event.entity.SpawnerSpawnEvent`; parent: `org.bukkit.event.entity.EntitySpawnEvent`.
- Python subscription: `@bridge.on("SpawnerSpawnEvent")`; `Events.SPAWNER_SPAWN` also works.
- Cancellable: yes; player: possible, depending on the runtime object.
- [Official Paper Javadoc](https://jd.papermc.io/paper/1.16.5/org/bukkit/event/entity/SpawnerSpawnEvent.html) for meaning, trigger conditions, and Java API.

| `data` field | JSON type | Java getter | Java return type |
| --- | --- | --- | --- |
| `entity` | entity summary | `getEntity()` | `org.bukkit.entity.Entity` |
| `entityType` | string | `getEntityType()` | `org.bukkit.entity.EntityType` |
| `location` | location summary | `getLocation()` | `org.bukkit.Location` |

<a id="event-org-bukkit-event-entity-stridertemperaturechangeevent"></a>
### StriderTemperatureChangeEvent

- Java class: `org.bukkit.event.entity.StriderTemperatureChangeEvent`; parent: `org.bukkit.event.entity.EntityEvent`.
- Python subscription: `@bridge.on("StriderTemperatureChangeEvent")`; `Events.STRIDER_TEMPERATURE_CHANGE` also works.
- Cancellable: no; player: possible, depending on the runtime object.
- [Official Paper Javadoc](https://jd.papermc.io/paper/1.16.5/org/bukkit/event/entity/StriderTemperatureChangeEvent.html) for meaning, trigger conditions, and Java API.

| `data` field | JSON type | Java getter | Java return type |
| --- | --- | --- | --- |
| `entity` | entity summary | `getEntity()` | `org.bukkit.entity.Entity` |
| `entityType` | string | `getEntityType()` | `org.bukkit.entity.EntityType` |
| `shivering` | boolean | `isShivering()` | `boolean` |

<a id="event-com-destroystokyo-paper-event-entity-thrownegghatchevent"></a>
### ThrownEggHatchEvent

- Java class: `com.destroystokyo.paper.event.entity.ThrownEggHatchEvent`; parent: `org.bukkit.event.Event`.
- Python subscription: `@bridge.on("ThrownEggHatchEvent")`; `Events.THROWN_EGG_HATCH` also works.
- Cancellable: no; player: no known player getter.
- [Official Paper Javadoc](https://jd.papermc.io/paper/1.16.5/com/destroystokyo/paper/event/entity/ThrownEggHatchEvent.html) for meaning, trigger conditions, and Java API.

| `data` field | JSON type | Java getter | Java return type |
| --- | --- | --- | --- |
| `egg` | entity summary | `getEgg()` | `org.bukkit.entity.Egg` |
| `hatchingType` | string | `getHatchingType()` | `org.bukkit.entity.EntityType` |
| `numHatches` | number | `getNumHatches()` | `byte` |
| `hatching` | boolean | `isHatching()` | `boolean` |

<a id="event-com-destroystokyo-paper-event-entity-turtlegohomeevent"></a>
### TurtleGoHomeEvent

- Java class: `com.destroystokyo.paper.event.entity.TurtleGoHomeEvent`; parent: `org.bukkit.event.entity.EntityEvent`.
- Python subscription: `@bridge.on("TurtleGoHomeEvent")`; `Events.TURTLE_GO_HOME` also works.
- Cancellable: yes; player: possible, depending on the runtime object.
- [Official Paper Javadoc](https://jd.papermc.io/paper/1.16.5/com/destroystokyo/paper/event/entity/TurtleGoHomeEvent.html) for meaning, trigger conditions, and Java API.

| `data` field | JSON type | Java getter | Java return type |
| --- | --- | --- | --- |
| `entity` | entity summary | `getEntity()` | `org.bukkit.entity.Entity` |
| `entityType` | string | `getEntityType()` | `org.bukkit.entity.EntityType` |

<a id="event-com-destroystokyo-paper-event-entity-turtlelayeggevent"></a>
### TurtleLayEggEvent

- Java class: `com.destroystokyo.paper.event.entity.TurtleLayEggEvent`; parent: `org.bukkit.event.entity.EntityEvent`.
- Python subscription: `@bridge.on("TurtleLayEggEvent")`; `Events.TURTLE_LAY_EGG` also works.
- Cancellable: yes; player: possible, depending on the runtime object.
- [Official Paper Javadoc](https://jd.papermc.io/paper/1.16.5/com/destroystokyo/paper/event/entity/TurtleLayEggEvent.html) for meaning, trigger conditions, and Java API.

| `data` field | JSON type | Java getter | Java return type |
| --- | --- | --- | --- |
| `eggCount` | number | `getEggCount()` | `int` |
| `entity` | entity summary | `getEntity()` | `org.bukkit.entity.Turtle` |
| `entityType` | string | `getEntityType()` | `org.bukkit.entity.EntityType` |
| `location` | location summary | `getLocation()` | `org.bukkit.Location` |

<a id="event-com-destroystokyo-paper-event-entity-turtlestartdiggingevent"></a>
### TurtleStartDiggingEvent

- Java class: `com.destroystokyo.paper.event.entity.TurtleStartDiggingEvent`; parent: `org.bukkit.event.entity.EntityEvent`.
- Python subscription: `@bridge.on("TurtleStartDiggingEvent")`; `Events.TURTLE_START_DIGGING` also works.
- Cancellable: yes; player: possible, depending on the runtime object.
- [Official Paper Javadoc](https://jd.papermc.io/paper/1.16.5/com/destroystokyo/paper/event/entity/TurtleStartDiggingEvent.html) for meaning, trigger conditions, and Java API.

| `data` field | JSON type | Java getter | Java return type |
| --- | --- | --- | --- |
| `entity` | entity summary | `getEntity()` | `org.bukkit.entity.Turtle` |
| `entityType` | string | `getEntityType()` | `org.bukkit.entity.EntityType` |
| `location` | location summary | `getLocation()` | `org.bukkit.Location` |

<a id="event-org-bukkit-event-entity-villageracquiretradeevent"></a>
### VillagerAcquireTradeEvent

- Java class: `org.bukkit.event.entity.VillagerAcquireTradeEvent`; parent: `org.bukkit.event.entity.EntityEvent`.
- Python subscription: `@bridge.on("VillagerAcquireTradeEvent")`; `Events.VILLAGER_ACQUIRE_TRADE` also works.
- Cancellable: yes; player: possible, depending on the runtime object.
- [Official Paper Javadoc](https://jd.papermc.io/paper/1.16.5/org/bukkit/event/entity/VillagerAcquireTradeEvent.html) for meaning, trigger conditions, and Java API.

| `data` field | JSON type | Java getter | Java return type |
| --- | --- | --- | --- |
| `entity` | entity summary | `getEntity()` | `org.bukkit.entity.Entity` |
| `entityType` | string | `getEntityType()` | `org.bukkit.entity.EntityType` |

<a id="event-org-bukkit-event-entity-villagercareerchangeevent"></a>
### VillagerCareerChangeEvent

- Java class: `org.bukkit.event.entity.VillagerCareerChangeEvent`; parent: `org.bukkit.event.entity.EntityEvent`.
- Python subscription: `@bridge.on("VillagerCareerChangeEvent")`; `Events.VILLAGER_CAREER_CHANGE` also works.
- Cancellable: yes; player: possible, depending on the runtime object.
- [Official Paper Javadoc](https://jd.papermc.io/paper/1.16.5/org/bukkit/event/entity/VillagerCareerChangeEvent.html) for meaning, trigger conditions, and Java API.

| `data` field | JSON type | Java getter | Java return type |
| --- | --- | --- | --- |
| `entity` | entity summary | `getEntity()` | `org.bukkit.entity.Entity` |
| `entityType` | string | `getEntityType()` | `org.bukkit.entity.EntityType` |
| `profession` | string | `getProfession()` | `org.bukkit.entity.Villager$Profession` |
| `reason` | string | `getReason()` | `org.bukkit.event.entity.VillagerCareerChangeEvent$ChangeReason` |

<a id="event-org-bukkit-event-entity-villagerreplenishtradeevent"></a>
### VillagerReplenishTradeEvent

- Java class: `org.bukkit.event.entity.VillagerReplenishTradeEvent`; parent: `org.bukkit.event.entity.EntityEvent`.
- Python subscription: `@bridge.on("VillagerReplenishTradeEvent")`; `Events.VILLAGER_REPLENISH_TRADE` also works.
- Cancellable: yes; player: possible, depending on the runtime object.
- [Official Paper Javadoc](https://jd.papermc.io/paper/1.16.5/org/bukkit/event/entity/VillagerReplenishTradeEvent.html) for meaning, trigger conditions, and Java API.

| `data` field | JSON type | Java getter | Java return type |
| --- | --- | --- | --- |
| `bonus` | number | `getBonus()` | `int` |
| `entity` | entity summary | `getEntity()` | `org.bukkit.entity.Entity` |
| `entityType` | string | `getEntityType()` | `org.bukkit.entity.EntityType` |

<a id="event-com-destroystokyo-paper-event-entity-witchconsumepotionevent"></a>
### WitchConsumePotionEvent

- Java class: `com.destroystokyo.paper.event.entity.WitchConsumePotionEvent`; parent: `org.bukkit.event.entity.EntityEvent`.
- Python subscription: `@bridge.on("WitchConsumePotionEvent")`; `Events.WITCH_CONSUME_POTION` also works.
- Cancellable: yes; player: possible, depending on the runtime object.
- [Official Paper Javadoc](https://jd.papermc.io/paper/1.16.5/com/destroystokyo/paper/event/entity/WitchConsumePotionEvent.html) for meaning, trigger conditions, and Java API.

| `data` field | JSON type | Java getter | Java return type |
| --- | --- | --- | --- |
| `entity` | entity summary | `getEntity()` | `org.bukkit.entity.Entity` |
| `entityType` | string | `getEntityType()` | `org.bukkit.entity.EntityType` |
| `potion` | item summary | `getPotion()` | `org.bukkit.inventory.ItemStack` |

<a id="event-com-destroystokyo-paper-event-entity-witchreadypotionevent"></a>
### WitchReadyPotionEvent

- Java class: `com.destroystokyo.paper.event.entity.WitchReadyPotionEvent`; parent: `org.bukkit.event.entity.EntityEvent`.
- Python subscription: `@bridge.on("WitchReadyPotionEvent")`; `Events.WITCH_READY_POTION` also works.
- Cancellable: yes; player: possible, depending on the runtime object.
- [Official Paper Javadoc](https://jd.papermc.io/paper/1.16.5/com/destroystokyo/paper/event/entity/WitchReadyPotionEvent.html) for meaning, trigger conditions, and Java API.

| `data` field | JSON type | Java getter | Java return type |
| --- | --- | --- | --- |
| `entity` | entity summary | `getEntity()` | `org.bukkit.entity.Entity` |
| `entityType` | string | `getEntityType()` | `org.bukkit.entity.EntityType` |
| `potion` | item summary | `getPotion()` | `org.bukkit.inventory.ItemStack` |

<a id="event-com-destroystokyo-paper-event-entity-witchthrowpotionevent"></a>
### WitchThrowPotionEvent

- Java class: `com.destroystokyo.paper.event.entity.WitchThrowPotionEvent`; parent: `org.bukkit.event.entity.EntityEvent`.
- Python subscription: `@bridge.on("WitchThrowPotionEvent")`; `Events.WITCH_THROW_POTION` also works.
- Cancellable: yes; player: possible, depending on the runtime object.
- [Official Paper Javadoc](https://jd.papermc.io/paper/1.16.5/com/destroystokyo/paper/event/entity/WitchThrowPotionEvent.html) for meaning, trigger conditions, and Java API.

| `data` field | JSON type | Java getter | Java return type |
| --- | --- | --- | --- |
| `entity` | entity summary | `getEntity()` | `org.bukkit.entity.Entity` |
| `entityType` | string | `getEntityType()` | `org.bukkit.entity.EntityType` |
| `potion` | item summary | `getPotion()` | `org.bukkit.inventory.ItemStack` |
| `target` | entity summary | `getTarget()` | `org.bukkit.entity.LivingEntity` |

<a id="category-hanging"></a>
## hanging

| Event | Python `type` | possible `data` fields | Cancellable |
| --- | --- | ---: | --- |
| [HangingBreakByEntityEvent](#event-org-bukkit-event-hanging-hangingbreakbyentityevent) | `HangingBreakByEntityEvent` | 3 | Yes |
| [HangingBreakEvent](#event-org-bukkit-event-hanging-hangingbreakevent) | `HangingBreakEvent` | 2 | Yes |
| [HangingPlaceEvent](#event-org-bukkit-event-hanging-hangingplaceevent) | `HangingPlaceEvent` | 3 | Yes |

<a id="event-org-bukkit-event-hanging-hangingbreakbyentityevent"></a>
### HangingBreakByEntityEvent

- Java class: `org.bukkit.event.hanging.HangingBreakByEntityEvent`; parent: `org.bukkit.event.hanging.HangingBreakEvent`.
- Python subscription: `@bridge.on("HangingBreakByEntityEvent")`; `Events.HANGING_BREAK_BY_ENTITY` also works.
- Cancellable: yes; player: possible, depending on the runtime object.
- [Official Paper Javadoc](https://jd.papermc.io/paper/1.16.5/org/bukkit/event/hanging/HangingBreakByEntityEvent.html) for meaning, trigger conditions, and Java API.

| `data` field | JSON type | Java getter | Java return type |
| --- | --- | --- | --- |
| `cause` | string | `getCause()` | `org.bukkit.event.hanging.HangingBreakEvent$RemoveCause` |
| `entity` | entity summary | `getEntity()` | `org.bukkit.entity.Hanging` |
| `remover` | entity summary | `getRemover()` | `org.bukkit.entity.Entity` |

<a id="event-org-bukkit-event-hanging-hangingbreakevent"></a>
### HangingBreakEvent

- Java class: `org.bukkit.event.hanging.HangingBreakEvent`; parent: `org.bukkit.event.hanging.HangingEvent`.
- Python subscription: `@bridge.on("HangingBreakEvent")`; `Events.HANGING_BREAK` also works.
- Cancellable: yes; player: possible, depending on the runtime object.
- [Official Paper Javadoc](https://jd.papermc.io/paper/1.16.5/org/bukkit/event/hanging/HangingBreakEvent.html) for meaning, trigger conditions, and Java API.

| `data` field | JSON type | Java getter | Java return type |
| --- | --- | --- | --- |
| `cause` | string | `getCause()` | `org.bukkit.event.hanging.HangingBreakEvent$RemoveCause` |
| `entity` | entity summary | `getEntity()` | `org.bukkit.entity.Hanging` |

<a id="event-org-bukkit-event-hanging-hangingplaceevent"></a>
### HangingPlaceEvent

- Java class: `org.bukkit.event.hanging.HangingPlaceEvent`; parent: `org.bukkit.event.hanging.HangingEvent`.
- Python subscription: `@bridge.on("HangingPlaceEvent")`; `Events.HANGING_PLACE` also works.
- Cancellable: yes; player: possible, depending on the runtime object.
- [Official Paper Javadoc](https://jd.papermc.io/paper/1.16.5/org/bukkit/event/hanging/HangingPlaceEvent.html) for meaning, trigger conditions, and Java API.

| `data` field | JSON type | Java getter | Java return type |
| --- | --- | --- | --- |
| `block` | block summary | `getBlock()` | `org.bukkit.block.Block` |
| `blockFace` | string | `getBlockFace()` | `org.bukkit.block.BlockFace` |
| `entity` | entity summary | `getEntity()` | `org.bukkit.entity.Hanging` |

<a id="category-inventory"></a>
## inventory

| Event | Python `type` | possible `data` fields | Cancellable |
| --- | --- | ---: | --- |
| [BrewEvent](#event-org-bukkit-event-inventory-brewevent) | `BrewEvent` | 2 | Yes |
| [BrewingStandFuelEvent](#event-org-bukkit-event-inventory-brewingstandfuelevent) | `BrewingStandFuelEvent` | 4 | Yes |
| [CraftItemEvent](#event-org-bukkit-event-inventory-craftitemevent) | `CraftItemEvent` | 13 | Yes |
| [FurnaceBurnEvent](#event-org-bukkit-event-inventory-furnaceburnevent) | `FurnaceBurnEvent` | 4 | Yes |
| [FurnaceExtractEvent](#event-org-bukkit-event-inventory-furnaceextractevent) | `FurnaceExtractEvent` | 4 | No |
| [FurnaceSmeltEvent](#event-org-bukkit-event-inventory-furnacesmeltevent) | `FurnaceSmeltEvent` | 3 | Yes |
| [InventoryClickEvent](#event-org-bukkit-event-inventory-inventoryclickevent) | `InventoryClickEvent` | 13 | Yes |
| [InventoryCloseEvent](#event-org-bukkit-event-inventory-inventorycloseevent) | `InventoryCloseEvent` | 1 | No |
| [InventoryCreativeEvent](#event-org-bukkit-event-inventory-inventorycreativeevent) | `InventoryCreativeEvent` | 13 | Yes |
| [InventoryDragEvent](#event-org-bukkit-event-inventory-inventorydragevent) | `InventoryDragEvent` | 5 | Yes |
| [InventoryEvent](#event-org-bukkit-event-inventory-inventoryevent) | `InventoryEvent` | 0 | No |
| [InventoryMoveItemEvent](#event-org-bukkit-event-inventory-inventorymoveitemevent) | `InventoryMoveItemEvent` | 1 | Yes |
| [InventoryOpenEvent](#event-org-bukkit-event-inventory-inventoryopenevent) | `InventoryOpenEvent` | 0 | Yes |
| [InventoryPickupItemEvent](#event-org-bukkit-event-inventory-inventorypickupitemevent) | `InventoryPickupItemEvent` | 1 | Yes |
| [PrepareAnvilEvent](#event-org-bukkit-event-inventory-prepareanvilevent) | `PrepareAnvilEvent` | 1 | No |
| [PrepareGrindstoneEvent](#event-com-destroystokyo-paper-event-inventory-preparegrindstoneevent) | `PrepareGrindstoneEvent` | 1 | No |
| [PrepareItemCraftEvent](#event-org-bukkit-event-inventory-prepareitemcraftevent) | `PrepareItemCraftEvent` | 1 | No |
| [PrepareResultEvent](#event-com-destroystokyo-paper-event-inventory-prepareresultevent) | `PrepareResultEvent` | 1 | No |
| [PrepareSmithingEvent](#event-org-bukkit-event-inventory-preparesmithingevent) | `PrepareSmithingEvent` | 1 | No |
| [SmithItemEvent](#event-org-bukkit-event-inventory-smithitemevent) | `SmithItemEvent` | 13 | Yes |
| [TradeSelectEvent](#event-org-bukkit-event-inventory-tradeselectevent) | `TradeSelectEvent` | 3 | Yes |

<a id="event-org-bukkit-event-inventory-brewevent"></a>
### BrewEvent

- Java class: `org.bukkit.event.inventory.BrewEvent`; parent: `org.bukkit.event.block.BlockEvent`.
- Python subscription: `@bridge.on("BrewEvent")`; `Events.BREW` also works.
- Cancellable: yes; player: no known player getter.
- [Official Paper Javadoc](https://jd.papermc.io/paper/1.16.5/org/bukkit/event/inventory/BrewEvent.html) for meaning, trigger conditions, and Java API.

| `data` field | JSON type | Java getter | Java return type |
| --- | --- | --- | --- |
| `block` | block summary | `getBlock()` | `org.bukkit.block.Block` |
| `fuelLevel` | number | `getFuelLevel()` | `int` |

<a id="event-org-bukkit-event-inventory-brewingstandfuelevent"></a>
### BrewingStandFuelEvent

- Java class: `org.bukkit.event.inventory.BrewingStandFuelEvent`; parent: `org.bukkit.event.block.BlockEvent`.
- Python subscription: `@bridge.on("BrewingStandFuelEvent")`; `Events.BREWING_STAND_FUEL` also works.
- Cancellable: yes; player: no known player getter.
- [Official Paper Javadoc](https://jd.papermc.io/paper/1.16.5/org/bukkit/event/inventory/BrewingStandFuelEvent.html) for meaning, trigger conditions, and Java API.

| `data` field | JSON type | Java getter | Java return type |
| --- | --- | --- | --- |
| `block` | block summary | `getBlock()` | `org.bukkit.block.Block` |
| `fuel` | item summary | `getFuel()` | `org.bukkit.inventory.ItemStack` |
| `fuelPower` | number | `getFuelPower()` | `int` |
| `consuming` | boolean | `isConsuming()` | `boolean` |

<a id="event-org-bukkit-event-inventory-craftitemevent"></a>
### CraftItemEvent

- Java class: `org.bukkit.event.inventory.CraftItemEvent`; parent: `org.bukkit.event.inventory.InventoryClickEvent`.
- Python subscription: `@bridge.on("CraftItemEvent")`; `Events.CRAFT_ITEM` also works.
- Cancellable: yes; player: possible, depending on the runtime object.
- [Official Paper Javadoc](https://jd.papermc.io/paper/1.16.5/org/bukkit/event/inventory/CraftItemEvent.html) for meaning, trigger conditions, and Java API.

| `data` field | JSON type | Java getter | Java return type |
| --- | --- | --- | --- |
| `action` | string | `getAction()` | `org.bukkit.event.inventory.InventoryAction` |
| `click` | string | `getClick()` | `org.bukkit.event.inventory.ClickType` |
| `currentItem` | item summary | `getCurrentItem()` | `org.bukkit.inventory.ItemStack` |
| `cursor` | item summary | `getCursor()` | `org.bukkit.inventory.ItemStack` |
| `hotbarButton` | number | `getHotbarButton()` | `int` |
| `rawSlot` | number | `getRawSlot()` | `int` |
| `result` | string | `getResult()` | `org.bukkit.event.Event$Result` |
| `slot` | number | `getSlot()` | `int` |
| `slotType` | string | `getSlotType()` | `org.bukkit.event.inventory.InventoryType$SlotType` |
| `whoClicked` | entity summary | `getWhoClicked()` | `org.bukkit.entity.HumanEntity` |
| `leftClick` | boolean | `isLeftClick()` | `boolean` |
| `rightClick` | boolean | `isRightClick()` | `boolean` |
| `shiftClick` | boolean | `isShiftClick()` | `boolean` |

<a id="event-org-bukkit-event-inventory-furnaceburnevent"></a>
### FurnaceBurnEvent

- Java class: `org.bukkit.event.inventory.FurnaceBurnEvent`; parent: `org.bukkit.event.block.BlockEvent`.
- Python subscription: `@bridge.on("FurnaceBurnEvent")`; `Events.FURNACE_BURN` also works.
- Cancellable: yes; player: no known player getter.
- [Official Paper Javadoc](https://jd.papermc.io/paper/1.16.5/org/bukkit/event/inventory/FurnaceBurnEvent.html) for meaning, trigger conditions, and Java API.

| `data` field | JSON type | Java getter | Java return type |
| --- | --- | --- | --- |
| `block` | block summary | `getBlock()` | `org.bukkit.block.Block` |
| `burnTime` | number | `getBurnTime()` | `int` |
| `fuel` | item summary | `getFuel()` | `org.bukkit.inventory.ItemStack` |
| `burning` | boolean | `isBurning()` | `boolean` |

<a id="event-org-bukkit-event-inventory-furnaceextractevent"></a>
### FurnaceExtractEvent

- Java class: `org.bukkit.event.inventory.FurnaceExtractEvent`; parent: `org.bukkit.event.block.BlockExpEvent`.
- Python subscription: `@bridge.on("FurnaceExtractEvent")`; `Events.FURNACE_EXTRACT` also works.
- Cancellable: no; player: possible, depending on the runtime object.
- [Official Paper Javadoc](https://jd.papermc.io/paper/1.16.5/org/bukkit/event/inventory/FurnaceExtractEvent.html) for meaning, trigger conditions, and Java API.

| `data` field | JSON type | Java getter | Java return type |
| --- | --- | --- | --- |
| `block` | block summary | `getBlock()` | `org.bukkit.block.Block` |
| `expToDrop` | number | `getExpToDrop()` | `int` |
| `itemAmount` | number | `getItemAmount()` | `int` |
| `itemType` | string | `getItemType()` | `org.bukkit.Material` |

<a id="event-org-bukkit-event-inventory-furnacesmeltevent"></a>
### FurnaceSmeltEvent

- Java class: `org.bukkit.event.inventory.FurnaceSmeltEvent`; parent: `org.bukkit.event.block.BlockCookEvent`.
- Python subscription: `@bridge.on("FurnaceSmeltEvent")`; `Events.FURNACE_SMELT` also works.
- Cancellable: yes; player: no known player getter.
- [Official Paper Javadoc](https://jd.papermc.io/paper/1.16.5/org/bukkit/event/inventory/FurnaceSmeltEvent.html) for meaning, trigger conditions, and Java API.

| `data` field | JSON type | Java getter | Java return type |
| --- | --- | --- | --- |
| `block` | block summary | `getBlock()` | `org.bukkit.block.Block` |
| `result` | item summary | `getResult()` | `org.bukkit.inventory.ItemStack` |
| `source` | item summary | `getSource()` | `org.bukkit.inventory.ItemStack` |

<a id="event-org-bukkit-event-inventory-inventoryclickevent"></a>
### InventoryClickEvent

- Java class: `org.bukkit.event.inventory.InventoryClickEvent`; parent: `org.bukkit.event.inventory.InventoryInteractEvent`.
- Python subscription: `@bridge.on("InventoryClickEvent")`; `Events.INVENTORY_CLICK` also works.
- Cancellable: yes; player: possible, depending on the runtime object.
- [Official Paper Javadoc](https://jd.papermc.io/paper/1.16.5/org/bukkit/event/inventory/InventoryClickEvent.html) for meaning, trigger conditions, and Java API.

| `data` field | JSON type | Java getter | Java return type |
| --- | --- | --- | --- |
| `action` | string | `getAction()` | `org.bukkit.event.inventory.InventoryAction` |
| `click` | string | `getClick()` | `org.bukkit.event.inventory.ClickType` |
| `currentItem` | item summary | `getCurrentItem()` | `org.bukkit.inventory.ItemStack` |
| `cursor` | item summary | `getCursor()` | `org.bukkit.inventory.ItemStack` |
| `hotbarButton` | number | `getHotbarButton()` | `int` |
| `rawSlot` | number | `getRawSlot()` | `int` |
| `result` | string | `getResult()` | `org.bukkit.event.Event$Result` |
| `slot` | number | `getSlot()` | `int` |
| `slotType` | string | `getSlotType()` | `org.bukkit.event.inventory.InventoryType$SlotType` |
| `whoClicked` | entity summary | `getWhoClicked()` | `org.bukkit.entity.HumanEntity` |
| `leftClick` | boolean | `isLeftClick()` | `boolean` |
| `rightClick` | boolean | `isRightClick()` | `boolean` |
| `shiftClick` | boolean | `isShiftClick()` | `boolean` |

<a id="event-org-bukkit-event-inventory-inventorycloseevent"></a>
### InventoryCloseEvent

- Java class: `org.bukkit.event.inventory.InventoryCloseEvent`; parent: `org.bukkit.event.inventory.InventoryEvent`.
- Python subscription: `@bridge.on("InventoryCloseEvent")`; `Events.INVENTORY_CLOSE` also works.
- Cancellable: no; player: possible, depending on the runtime object.
- [Official Paper Javadoc](https://jd.papermc.io/paper/1.16.5/org/bukkit/event/inventory/InventoryCloseEvent.html) for meaning, trigger conditions, and Java API.

| `data` field | JSON type | Java getter | Java return type |
| --- | --- | --- | --- |
| `reason` | string | `getReason()` | `org.bukkit.event.inventory.InventoryCloseEvent$Reason` |

<a id="event-org-bukkit-event-inventory-inventorycreativeevent"></a>
### InventoryCreativeEvent

- Java class: `org.bukkit.event.inventory.InventoryCreativeEvent`; parent: `org.bukkit.event.inventory.InventoryClickEvent`.
- Python subscription: `@bridge.on("InventoryCreativeEvent")`; `Events.INVENTORY_CREATIVE` also works.
- Cancellable: yes; player: possible, depending on the runtime object.
- [Official Paper Javadoc](https://jd.papermc.io/paper/1.16.5/org/bukkit/event/inventory/InventoryCreativeEvent.html) for meaning, trigger conditions, and Java API.

| `data` field | JSON type | Java getter | Java return type |
| --- | --- | --- | --- |
| `action` | string | `getAction()` | `org.bukkit.event.inventory.InventoryAction` |
| `click` | string | `getClick()` | `org.bukkit.event.inventory.ClickType` |
| `currentItem` | item summary | `getCurrentItem()` | `org.bukkit.inventory.ItemStack` |
| `cursor` | item summary | `getCursor()` | `org.bukkit.inventory.ItemStack` |
| `hotbarButton` | number | `getHotbarButton()` | `int` |
| `rawSlot` | number | `getRawSlot()` | `int` |
| `result` | string | `getResult()` | `org.bukkit.event.Event$Result` |
| `slot` | number | `getSlot()` | `int` |
| `slotType` | string | `getSlotType()` | `org.bukkit.event.inventory.InventoryType$SlotType` |
| `whoClicked` | entity summary | `getWhoClicked()` | `org.bukkit.entity.HumanEntity` |
| `leftClick` | boolean | `isLeftClick()` | `boolean` |
| `rightClick` | boolean | `isRightClick()` | `boolean` |
| `shiftClick` | boolean | `isShiftClick()` | `boolean` |

<a id="event-org-bukkit-event-inventory-inventorydragevent"></a>
### InventoryDragEvent

- Java class: `org.bukkit.event.inventory.InventoryDragEvent`; parent: `org.bukkit.event.inventory.InventoryInteractEvent`.
- Python subscription: `@bridge.on("InventoryDragEvent")`; `Events.INVENTORY_DRAG` also works.
- Cancellable: yes; player: possible, depending on the runtime object.
- [Official Paper Javadoc](https://jd.papermc.io/paper/1.16.5/org/bukkit/event/inventory/InventoryDragEvent.html) for meaning, trigger conditions, and Java API.

| `data` field | JSON type | Java getter | Java return type |
| --- | --- | --- | --- |
| `cursor` | item summary | `getCursor()` | `org.bukkit.inventory.ItemStack` |
| `oldCursor` | item summary | `getOldCursor()` | `org.bukkit.inventory.ItemStack` |
| `result` | string | `getResult()` | `org.bukkit.event.Event$Result` |
| `type` | string | `getType()` | `org.bukkit.event.inventory.DragType` |
| `whoClicked` | entity summary | `getWhoClicked()` | `org.bukkit.entity.HumanEntity` |

<a id="event-org-bukkit-event-inventory-inventoryevent"></a>
### InventoryEvent

- Java class: `org.bukkit.event.inventory.InventoryEvent`; parent: `org.bukkit.event.Event`.
- Python subscription: `@bridge.on("InventoryEvent")`; `Events.INVENTORY` also works.
- Cancellable: no; player: no known player getter.
- [Official Paper Javadoc](https://jd.papermc.io/paper/1.16.5/org/bukkit/event/inventory/InventoryEvent.html) for meaning, trigger conditions, and Java API.

No serializable possible `data` fields; common event fields are still sent.

<a id="event-org-bukkit-event-inventory-inventorymoveitemevent"></a>
### InventoryMoveItemEvent

- Java class: `org.bukkit.event.inventory.InventoryMoveItemEvent`; parent: `org.bukkit.event.Event`.
- Python subscription: `@bridge.on("InventoryMoveItemEvent")`; `Events.INVENTORY_MOVE_ITEM` also works.
- Cancellable: yes; player: no known player getter.
- [Official Paper Javadoc](https://jd.papermc.io/paper/1.16.5/org/bukkit/event/inventory/InventoryMoveItemEvent.html) for meaning, trigger conditions, and Java API.

| `data` field | JSON type | Java getter | Java return type |
| --- | --- | --- | --- |
| `item` | item summary | `getItem()` | `org.bukkit.inventory.ItemStack` |

<a id="event-org-bukkit-event-inventory-inventoryopenevent"></a>
### InventoryOpenEvent

- Java class: `org.bukkit.event.inventory.InventoryOpenEvent`; parent: `org.bukkit.event.inventory.InventoryEvent`.
- Python subscription: `@bridge.on("InventoryOpenEvent")`; `Events.INVENTORY_OPEN` also works.
- Cancellable: yes; player: possible, depending on the runtime object.
- [Official Paper Javadoc](https://jd.papermc.io/paper/1.16.5/org/bukkit/event/inventory/InventoryOpenEvent.html) for meaning, trigger conditions, and Java API.

No serializable possible `data` fields; common event fields are still sent.

<a id="event-org-bukkit-event-inventory-inventorypickupitemevent"></a>
### InventoryPickupItemEvent

- Java class: `org.bukkit.event.inventory.InventoryPickupItemEvent`; parent: `org.bukkit.event.Event`.
- Python subscription: `@bridge.on("InventoryPickupItemEvent")`; `Events.INVENTORY_PICKUP_ITEM` also works.
- Cancellable: yes; player: no known player getter.
- [Official Paper Javadoc](https://jd.papermc.io/paper/1.16.5/org/bukkit/event/inventory/InventoryPickupItemEvent.html) for meaning, trigger conditions, and Java API.

| `data` field | JSON type | Java getter | Java return type |
| --- | --- | --- | --- |
| `item` | entity summary | `getItem()` | `org.bukkit.entity.Item` |

<a id="event-org-bukkit-event-inventory-prepareanvilevent"></a>
### PrepareAnvilEvent

- Java class: `org.bukkit.event.inventory.PrepareAnvilEvent`; parent: `com.destroystokyo.paper.event.inventory.PrepareResultEvent`.
- Python subscription: `@bridge.on("PrepareAnvilEvent")`; `Events.PREPARE_ANVIL` also works.
- Cancellable: no; player: no known player getter.
- [Official Paper Javadoc](https://jd.papermc.io/paper/1.16.5/org/bukkit/event/inventory/PrepareAnvilEvent.html) for meaning, trigger conditions, and Java API.

| `data` field | JSON type | Java getter | Java return type |
| --- | --- | --- | --- |
| `result` | item summary | `getResult()` | `org.bukkit.inventory.ItemStack` |

<a id="event-com-destroystokyo-paper-event-inventory-preparegrindstoneevent"></a>
### PrepareGrindstoneEvent

- Java class: `com.destroystokyo.paper.event.inventory.PrepareGrindstoneEvent`; parent: `com.destroystokyo.paper.event.inventory.PrepareResultEvent`.
- Python subscription: `@bridge.on("PrepareGrindstoneEvent")`; `Events.PREPARE_GRINDSTONE` also works.
- Cancellable: no; player: no known player getter.
- [Official Paper Javadoc](https://jd.papermc.io/paper/1.16.5/com/destroystokyo/paper/event/inventory/PrepareGrindstoneEvent.html) for meaning, trigger conditions, and Java API.

| `data` field | JSON type | Java getter | Java return type |
| --- | --- | --- | --- |
| `result` | item summary | `getResult()` | `org.bukkit.inventory.ItemStack` |

<a id="event-org-bukkit-event-inventory-prepareitemcraftevent"></a>
### PrepareItemCraftEvent

- Java class: `org.bukkit.event.inventory.PrepareItemCraftEvent`; parent: `org.bukkit.event.inventory.InventoryEvent`.
- Python subscription: `@bridge.on("PrepareItemCraftEvent")`; `Events.PREPARE_ITEM_CRAFT` also works.
- Cancellable: no; player: no known player getter.
- [Official Paper Javadoc](https://jd.papermc.io/paper/1.16.5/org/bukkit/event/inventory/PrepareItemCraftEvent.html) for meaning, trigger conditions, and Java API.

| `data` field | JSON type | Java getter | Java return type |
| --- | --- | --- | --- |
| `repair` | boolean | `isRepair()` | `boolean` |

<a id="event-com-destroystokyo-paper-event-inventory-prepareresultevent"></a>
### PrepareResultEvent

- Java class: `com.destroystokyo.paper.event.inventory.PrepareResultEvent`; parent: `org.bukkit.event.inventory.InventoryEvent`.
- Python subscription: `@bridge.on("PrepareResultEvent")`; `Events.PREPARE_RESULT` also works.
- Cancellable: no; player: no known player getter.
- [Official Paper Javadoc](https://jd.papermc.io/paper/1.16.5/com/destroystokyo/paper/event/inventory/PrepareResultEvent.html) for meaning, trigger conditions, and Java API.

| `data` field | JSON type | Java getter | Java return type |
| --- | --- | --- | --- |
| `result` | item summary | `getResult()` | `org.bukkit.inventory.ItemStack` |

<a id="event-org-bukkit-event-inventory-preparesmithingevent"></a>
### PrepareSmithingEvent

- Java class: `org.bukkit.event.inventory.PrepareSmithingEvent`; parent: `com.destroystokyo.paper.event.inventory.PrepareResultEvent`.
- Python subscription: `@bridge.on("PrepareSmithingEvent")`; `Events.PREPARE_SMITHING` also works.
- Cancellable: no; player: no known player getter.
- [Official Paper Javadoc](https://jd.papermc.io/paper/1.16.5/org/bukkit/event/inventory/PrepareSmithingEvent.html) for meaning, trigger conditions, and Java API.

| `data` field | JSON type | Java getter | Java return type |
| --- | --- | --- | --- |
| `result` | item summary | `getResult()` | `org.bukkit.inventory.ItemStack` |

<a id="event-org-bukkit-event-inventory-smithitemevent"></a>
### SmithItemEvent

- Java class: `org.bukkit.event.inventory.SmithItemEvent`; parent: `org.bukkit.event.inventory.InventoryClickEvent`.
- Python subscription: `@bridge.on("SmithItemEvent")`; `Events.SMITH_ITEM` also works.
- Cancellable: yes; player: possible, depending on the runtime object.
- [Official Paper Javadoc](https://jd.papermc.io/paper/1.16.5/org/bukkit/event/inventory/SmithItemEvent.html) for meaning, trigger conditions, and Java API.

| `data` field | JSON type | Java getter | Java return type |
| --- | --- | --- | --- |
| `action` | string | `getAction()` | `org.bukkit.event.inventory.InventoryAction` |
| `click` | string | `getClick()` | `org.bukkit.event.inventory.ClickType` |
| `currentItem` | item summary | `getCurrentItem()` | `org.bukkit.inventory.ItemStack` |
| `cursor` | item summary | `getCursor()` | `org.bukkit.inventory.ItemStack` |
| `hotbarButton` | number | `getHotbarButton()` | `int` |
| `rawSlot` | number | `getRawSlot()` | `int` |
| `result` | string | `getResult()` | `org.bukkit.event.Event$Result` |
| `slot` | number | `getSlot()` | `int` |
| `slotType` | string | `getSlotType()` | `org.bukkit.event.inventory.InventoryType$SlotType` |
| `whoClicked` | entity summary | `getWhoClicked()` | `org.bukkit.entity.HumanEntity` |
| `leftClick` | boolean | `isLeftClick()` | `boolean` |
| `rightClick` | boolean | `isRightClick()` | `boolean` |
| `shiftClick` | boolean | `isShiftClick()` | `boolean` |

<a id="event-org-bukkit-event-inventory-tradeselectevent"></a>
### TradeSelectEvent

- Java class: `org.bukkit.event.inventory.TradeSelectEvent`; parent: `org.bukkit.event.inventory.InventoryInteractEvent`.
- Python subscription: `@bridge.on("TradeSelectEvent")`; `Events.TRADE_SELECT` also works.
- Cancellable: yes; player: possible, depending on the runtime object.
- [Official Paper Javadoc](https://jd.papermc.io/paper/1.16.5/org/bukkit/event/inventory/TradeSelectEvent.html) for meaning, trigger conditions, and Java API.

| `data` field | JSON type | Java getter | Java return type |
| --- | --- | --- | --- |
| `index` | number | `getIndex()` | `int` |
| `result` | string | `getResult()` | `org.bukkit.event.Event$Result` |
| `whoClicked` | entity summary | `getWhoClicked()` | `org.bukkit.entity.HumanEntity` |

<a id="category-packet"></a>
## packet

| Event | Python `type` | possible `data` fields | Cancellable |
| --- | --- | ---: | --- |
| [PlayerChunkLoadEvent](#event-io-papermc-paper-event-packet-playerchunkloadevent) | `PlayerChunkLoadEvent` | 1 | No |
| [PlayerChunkUnloadEvent](#event-io-papermc-paper-event-packet-playerchunkunloadevent) | `PlayerChunkUnloadEvent` | 1 | No |

<a id="event-io-papermc-paper-event-packet-playerchunkloadevent"></a>
### PlayerChunkLoadEvent

- Java class: `io.papermc.paper.event.packet.PlayerChunkLoadEvent`; parent: `org.bukkit.event.world.ChunkEvent`.
- Python subscription: `@bridge.on("PlayerChunkLoadEvent")`; `Events.PLAYER_CHUNK_LOAD` also works.
- Cancellable: no; player: possible, depending on the runtime object.
- [Official Paper Javadoc](https://jd.papermc.io/paper/1.16.5/io/papermc/paper/event/packet/PlayerChunkLoadEvent.html) for meaning, trigger conditions, and Java API.

| `data` field | JSON type | Java getter | Java return type |
| --- | --- | --- | --- |
| `world` | world summary | `getWorld()` | `org.bukkit.World` |

<a id="event-io-papermc-paper-event-packet-playerchunkunloadevent"></a>
### PlayerChunkUnloadEvent

- Java class: `io.papermc.paper.event.packet.PlayerChunkUnloadEvent`; parent: `org.bukkit.event.world.ChunkEvent`.
- Python subscription: `@bridge.on("PlayerChunkUnloadEvent")`; `Events.PLAYER_CHUNK_UNLOAD` also works.
- Cancellable: no; player: possible, depending on the runtime object.
- [Official Paper Javadoc](https://jd.papermc.io/paper/1.16.5/io/papermc/paper/event/packet/PlayerChunkUnloadEvent.html) for meaning, trigger conditions, and Java API.

| `data` field | JSON type | Java getter | Java return type |
| --- | --- | --- | --- |
| `world` | world summary | `getWorld()` | `org.bukkit.World` |

<a id="category-player"></a>
## player

| Event | Python `type` | possible `data` fields | Cancellable |
| --- | --- | ---: | --- |
| [AsyncChatEvent](#event-io-papermc-paper-event-player-asyncchatevent) | `AsyncChatEvent` | 0 | Yes |
| [AsyncPlayerChatEvent](#event-org-bukkit-event-player-asyncplayerchatevent) | `chat` | 2 | Yes |
| [AsyncPlayerPreLoginEvent](#event-org-bukkit-event-player-asyncplayerpreloginevent) | `AsyncPlayerPreLoginEvent` | 5 | No |
| [ChatEvent](#event-io-papermc-paper-event-player-chatevent) | `ChatEvent` | 0 | Yes |
| [IllegalPacketEvent](#event-com-destroystokyo-paper-event-player-illegalpacketevent) | `IllegalPacketEvent` | 4 | No |
| [PlayerAdvancementCriterionGrantEvent](#event-com-destroystokyo-paper-event-player-playeradvancementcriteriongrantevent) | `PlayerAdvancementCriterionGrantEvent` | 1 | Yes |
| [PlayerAdvancementDoneEvent](#event-org-bukkit-event-player-playeradvancementdoneevent) | `PlayerAdvancementDoneEvent` | 0 | No |
| [PlayerAnimationEvent](#event-org-bukkit-event-player-playeranimationevent) | `PlayerAnimationEvent` | 1 | Yes |
| [PlayerArmorChangeEvent](#event-com-destroystokyo-paper-event-player-playerarmorchangeevent) | `PlayerArmorChangeEvent` | 3 | No |
| [PlayerArmorStandManipulateEvent](#event-org-bukkit-event-player-playerarmorstandmanipulateevent) | `PlayerArmorStandManipulateEvent` | 5 | Yes |
| [PlayerArmSwingEvent](#event-io-papermc-paper-event-player-playerarmswingevent) | `PlayerArmSwingEvent` | 2 | Yes |
| [PlayerAttackEntityCooldownResetEvent](#event-com-destroystokyo-paper-event-player-playerattackentitycooldownresetevent) | `PlayerAttackEntityCooldownResetEvent` | 2 | Yes |
| [PlayerAttemptPickupItemEvent](#event-org-bukkit-event-player-playerattemptpickupitemevent) | `PlayerAttemptPickupItemEvent` | 3 | Yes |
| [PlayerBedEnterEvent](#event-org-bukkit-event-player-playerbedenterevent) | `PlayerBedEnterEvent` | 2 | Yes |
| [PlayerBedFailEnterEvent](#event-io-papermc-paper-event-player-playerbedfailenterevent) | `PlayerBedFailEnterEvent` | 3 | Yes |
| [PlayerBedLeaveEvent](#event-org-bukkit-event-player-playerbedleaveevent) | `PlayerBedLeaveEvent` | 1 | Yes |
| [PlayerBucketEmptyEvent](#event-org-bukkit-event-player-playerbucketemptyevent) | `PlayerBucketEmptyEvent` | 6 | Yes |
| [PlayerBucketEntityEvent](#event-org-bukkit-event-player-playerbucketentityevent) | `PlayerBucketEntityEvent` | 3 | Yes |
| [PlayerBucketFillEvent](#event-org-bukkit-event-player-playerbucketfillevent) | `PlayerBucketFillEvent` | 6 | Yes |
| [PlayerBucketFishEvent](#event-org-bukkit-event-player-playerbucketfishevent) | `PlayerBucketFishEvent` | 5 | Yes |
| [PlayerChangeBeaconEffectEvent](#event-io-papermc-paper-event-player-playerchangebeaconeffectevent) | `PlayerChangeBeaconEffectEvent` | 1 | Yes |
| [PlayerChangedMainHandEvent](#event-org-bukkit-event-player-playerchangedmainhandevent) | `PlayerChangedMainHandEvent` | 1 | No |
| [PlayerChangedWorldEvent](#event-org-bukkit-event-player-playerchangedworldevent) | `PlayerChangedWorldEvent` | 1 | No |
| [PlayerChatEvent](#event-org-bukkit-event-player-playerchatevent) | `PlayerChatEvent` | 2 | Yes |
| [PlayerChatTabCompleteEvent](#event-org-bukkit-event-player-playerchattabcompleteevent) | `PlayerChatTabCompleteEvent` | 2 | No |
| [PlayerClientOptionsChangeEvent](#event-com-destroystokyo-paper-event-player-playerclientoptionschangeevent) | `PlayerClientOptionsChangeEvent` | 4 | No |
| [PlayerCommandPreprocessEvent](#event-org-bukkit-event-player-playercommandpreprocessevent) | `PlayerCommandPreprocessEvent` | 1 | Yes |
| [PlayerCommandSendEvent](#event-org-bukkit-event-player-playercommandsendevent) | `PlayerCommandSendEvent` | 0 | No |
| [PlayerConnectionCloseEvent](#event-com-destroystokyo-paper-event-player-playerconnectioncloseevent) | `PlayerConnectionCloseEvent` | 2 | No |
| [PlayerDeepSleepEvent](#event-io-papermc-paper-event-player-playerdeepsleepevent) | `PlayerDeepSleepEvent` | 0 | Yes |
| [PlayerDropItemEvent](#event-org-bukkit-event-player-playerdropitemevent) | `PlayerDropItemEvent` | 1 | Yes |
| [PlayerEditBookEvent](#event-org-bukkit-event-player-playereditbookevent) | `PlayerEditBookEvent` | 2 | Yes |
| [PlayerEggThrowEvent](#event-org-bukkit-event-player-playereggthrowevent) | `PlayerEggThrowEvent` | 4 | No |
| [PlayerElytraBoostEvent](#event-com-destroystokyo-paper-event-player-playerelytraboostevent) | `PlayerElytraBoostEvent` | 2 | Yes |
| [PlayerExpChangeEvent](#event-org-bukkit-event-player-playerexpchangeevent) | `PlayerExpChangeEvent` | 2 | No |
| [PlayerFishEvent](#event-org-bukkit-event-player-playerfishevent) | `PlayerFishEvent` | 4 | Yes |
| [PlayerFlowerPotManipulateEvent](#event-io-papermc-paper-event-player-playerflowerpotmanipulateevent) | `PlayerFlowerPotManipulateEvent` | 3 | Yes |
| [PlayerGameModeChangeEvent](#event-org-bukkit-event-player-playergamemodechangeevent) | `PlayerGameModeChangeEvent` | 2 | Yes |
| [PlayerHandshakeEvent](#event-com-destroystokyo-paper-event-player-playerhandshakeevent) | `PlayerHandshakeEvent` | 8 | Yes |
| [PlayerHarvestBlockEvent](#event-org-bukkit-event-player-playerharvestblockevent) | `PlayerHarvestBlockEvent` | 1 | Yes |
| [PlayerInitialSpawnEvent](#event-com-destroystokyo-paper-event-player-playerinitialspawnevent) | `PlayerInitialSpawnEvent` | 1 | No |
| [PlayerInteractAtEntityEvent](#event-org-bukkit-event-player-playerinteractatentityevent) | `PlayerInteractAtEntityEvent` | 2 | Yes |
| [PlayerInteractEntityEvent](#event-org-bukkit-event-player-playerinteractentityevent) | `PlayerInteractEntityEvent` | 2 | Yes |
| [PlayerInteractEvent](#event-org-bukkit-event-player-playerinteractevent) | `PlayerInteractEvent` | 8 | Yes |
| [PlayerItemBreakEvent](#event-org-bukkit-event-player-playeritembreakevent) | `PlayerItemBreakEvent` | 1 | No |
| [PlayerItemConsumeEvent](#event-org-bukkit-event-player-playeritemconsumeevent) | `PlayerItemConsumeEvent` | 2 | Yes |
| [PlayerItemCooldownEvent](#event-io-papermc-paper-event-player-playeritemcooldownevent) | `PlayerItemCooldownEvent` | 2 | Yes |
| [PlayerItemDamageEvent](#event-org-bukkit-event-player-playeritemdamageevent) | `PlayerItemDamageEvent` | 2 | Yes |
| [PlayerItemHeldEvent](#event-org-bukkit-event-player-playeritemheldevent) | `PlayerItemHeldEvent` | 2 | Yes |
| [PlayerItemMendEvent](#event-org-bukkit-event-player-playeritemmendevent) | `PlayerItemMendEvent` | 3 | Yes |
| [PlayerJoinEvent](#event-org-bukkit-event-player-playerjoinevent) | `join` | 1 | No |
| [PlayerJumpEvent](#event-com-destroystokyo-paper-event-player-playerjumpevent) | `PlayerJumpEvent` | 2 | Yes |
| [PlayerKickEvent](#event-org-bukkit-event-player-playerkickevent) | `PlayerKickEvent` | 3 | Yes |
| [PlayerLaunchProjectileEvent](#event-com-destroystokyo-paper-event-player-playerlaunchprojectileevent) | `PlayerLaunchProjectileEvent` | 2 | Yes |
| [PlayerLecternPageChangeEvent](#event-io-papermc-paper-event-player-playerlecternpagechangeevent) | `PlayerLecternPageChangeEvent` | 4 | Yes |
| [PlayerLevelChangeEvent](#event-org-bukkit-event-player-playerlevelchangeevent) | `PlayerLevelChangeEvent` | 2 | No |
| [PlayerLocaleChangeEvent](#event-com-destroystokyo-paper-event-player-playerlocalechangeevent) | `PlayerLocaleChangeEvent` | 2 | No |
| [PlayerLocaleChangeEvent](#event-org-bukkit-event-player-playerlocalechangeevent) | `PlayerLocaleChangeEvent` | 1 | No |
| [PlayerLoginEvent](#event-org-bukkit-event-player-playerloginevent) | `PlayerLoginEvent` | 3 | No |
| [PlayerLoomPatternSelectEvent](#event-io-papermc-paper-event-player-playerloompatternselectevent) | `PlayerLoomPatternSelectEvent` | 1 | Yes |
| [PlayerMoveEvent](#event-org-bukkit-event-player-playermoveevent) | `PlayerMoveEvent` | 2 | Yes |
| [PlayerNameEntityEvent](#event-io-papermc-paper-event-player-playernameentityevent) | `PlayerNameEntityEvent` | 2 | Yes |
| [PlayerPickupArrowEvent](#event-org-bukkit-event-player-playerpickuparrowevent) | `PlayerPickupArrowEvent` | 4 | Yes |
| [PlayerPickupExperienceEvent](#event-com-destroystokyo-paper-event-player-playerpickupexperienceevent) | `PlayerPickupExperienceEvent` | 1 | Yes |
| [PlayerPickupItemEvent](#event-org-bukkit-event-player-playerpickupitemevent) | `PlayerPickupItemEvent` | 3 | Yes |
| [PlayerPortalEvent](#event-org-bukkit-event-player-playerportalevent) | `PlayerPortalEvent` | 6 | Yes |
| [PlayerPostRespawnEvent](#event-com-destroystokyo-paper-event-player-playerpostrespawnevent) | `PlayerPostRespawnEvent` | 2 | No |
| [PlayerPreLoginEvent](#event-org-bukkit-event-player-playerpreloginevent) | `PlayerPreLoginEvent` | 4 | No |
| [PlayerPurchaseEvent](#event-io-papermc-paper-event-player-playerpurchaseevent) | `PlayerPurchaseEvent` | 1 | Yes |
| [PlayerQuitEvent](#event-org-bukkit-event-player-playerquitevent) | `quit` | 2 | No |
| [PlayerReadyArrowEvent](#event-com-destroystokyo-paper-event-player-playerreadyarrowevent) | `PlayerReadyArrowEvent` | 2 | Yes |
| [PlayerRecipeBookClickEvent](#event-com-destroystokyo-paper-event-player-playerrecipebookclickevent) | `PlayerRecipeBookClickEvent` | 1 | Yes |
| [PlayerRecipeDiscoverEvent](#event-org-bukkit-event-player-playerrecipediscoverevent) | `PlayerRecipeDiscoverEvent` | 0 | Yes |
| [PlayerRegisterChannelEvent](#event-org-bukkit-event-player-playerregisterchannelevent) | `PlayerRegisterChannelEvent` | 1 | No |
| [PlayerResourcePackStatusEvent](#event-org-bukkit-event-player-playerresourcepackstatusevent) | `PlayerResourcePackStatusEvent` | 2 | No |
| [PlayerRespawnEvent](#event-org-bukkit-event-player-playerrespawnevent) | `PlayerRespawnEvent` | 3 | No |
| [PlayerRiptideEvent](#event-org-bukkit-event-player-playerriptideevent) | `PlayerRiptideEvent` | 1 | No |
| [PlayerShearEntityEvent](#event-org-bukkit-event-player-playershearentityevent) | `PlayerShearEntityEvent` | 3 | Yes |
| [PlayerSignCommandPreprocessEvent](#event-io-papermc-paper-event-player-playersigncommandpreprocessevent) | `PlayerSignCommandPreprocessEvent` | 1 | Yes |
| [PlayerStartSpectatingEntityEvent](#event-com-destroystokyo-paper-event-player-playerstartspectatingentityevent) | `PlayerStartSpectatingEntityEvent` | 2 | Yes |
| [PlayerStatisticIncrementEvent](#event-org-bukkit-event-player-playerstatisticincrementevent) | `PlayerStatisticIncrementEvent` | 5 | Yes |
| [PlayerStonecutterRecipeSelectEvent](#event-io-papermc-paper-event-player-playerstonecutterrecipeselectevent) | `PlayerStonecutterRecipeSelectEvent` | 0 | Yes |
| [PlayerStopSpectatingEntityEvent](#event-com-destroystokyo-paper-event-player-playerstopspectatingentityevent) | `PlayerStopSpectatingEntityEvent` | 1 | Yes |
| [PlayerSwapHandItemsEvent](#event-org-bukkit-event-player-playerswaphanditemsevent) | `PlayerSwapHandItemsEvent` | 2 | Yes |
| [PlayerTakeLecternBookEvent](#event-org-bukkit-event-player-playertakelecternbookevent) | `PlayerTakeLecternBookEvent` | 1 | Yes |
| [PlayerTeleportEndGatewayEvent](#event-com-destroystokyo-paper-event-player-playerteleportendgatewayevent) | `PlayerTeleportEndGatewayEvent` | 3 | Yes |
| [PlayerTeleportEvent](#event-org-bukkit-event-player-playerteleportevent) | `PlayerTeleportEvent` | 3 | Yes |
| [PlayerToggleFlightEvent](#event-org-bukkit-event-player-playertoggleflightevent) | `PlayerToggleFlightEvent` | 1 | Yes |
| [PlayerToggleSneakEvent](#event-org-bukkit-event-player-playertogglesneakevent) | `PlayerToggleSneakEvent` | 1 | Yes |
| [PlayerToggleSprintEvent](#event-org-bukkit-event-player-playertogglesprintevent) | `PlayerToggleSprintEvent` | 1 | Yes |
| [PlayerTradeEvent](#event-io-papermc-paper-event-player-playertradeevent) | `PlayerTradeEvent` | 2 | Yes |
| [PlayerUnleashEntityEvent](#event-org-bukkit-event-player-playerunleashentityevent) | `PlayerUnleashEntityEvent` | 4 | Yes |
| [PlayerUnregisterChannelEvent](#event-org-bukkit-event-player-playerunregisterchannelevent) | `PlayerUnregisterChannelEvent` | 1 | No |
| [PlayerUseUnknownEntityEvent](#event-com-destroystokyo-paper-event-player-playeruseunknownentityevent) | `PlayerUseUnknownEntityEvent` | 3 | No |
| [PlayerVelocityEvent](#event-org-bukkit-event-player-playervelocityevent) | `PlayerVelocityEvent` | 0 | Yes |

<a id="event-io-papermc-paper-event-player-asyncchatevent"></a>
### AsyncChatEvent

- Java class: `io.papermc.paper.event.player.AsyncChatEvent`; parent: `io.papermc.paper.event.player.AbstractChatEvent`.
- Python subscription: `@bridge.on("AsyncChatEvent")`; `Events.ASYNC_CHAT` also works.
- Cancellable: yes; player: possible, depending on the runtime object.
- [Official Paper Javadoc](https://jd.papermc.io/paper/1.16.5/io/papermc/paper/event/player/AsyncChatEvent.html) for meaning, trigger conditions, and Java API.

No serializable possible `data` fields; common event fields are still sent.

<a id="event-org-bukkit-event-player-asyncplayerchatevent"></a>
### AsyncPlayerChatEvent

- Java class: `org.bukkit.event.player.AsyncPlayerChatEvent`; parent: `org.bukkit.event.player.PlayerEvent`.
- Python subscription: `@bridge.on("chat")`; `Events.ASYNC_PLAYER_CHAT` also works.
- Cancellable: yes; player: possible, depending on the runtime object.
- [Official Paper Javadoc](https://jd.papermc.io/paper/1.16.5/org/bukkit/event/player/AsyncPlayerChatEvent.html) for meaning, trigger conditions, and Java API.

| `data` field | JSON type | Java getter | Java return type |
| --- | --- | --- | --- |
| `format` | string | `getFormat()` | `java.lang.String` |
| `message` | string | `getMessage()` | `java.lang.String` |

<a id="event-org-bukkit-event-player-asyncplayerpreloginevent"></a>
### AsyncPlayerPreLoginEvent

- Java class: `org.bukkit.event.player.AsyncPlayerPreLoginEvent`; parent: `org.bukkit.event.Event`.
- Python subscription: `@bridge.on("AsyncPlayerPreLoginEvent")`; `Events.ASYNC_PLAYER_PRE_LOGIN` also works.
- Cancellable: no; player: no known player getter.
- [Official Paper Javadoc](https://jd.papermc.io/paper/1.16.5/org/bukkit/event/player/AsyncPlayerPreLoginEvent.html) for meaning, trigger conditions, and Java API.

| `data` field | JSON type | Java getter | Java return type |
| --- | --- | --- | --- |
| `kickMessage` | string | `getKickMessage()` | `java.lang.String` |
| `loginResult` | string | `getLoginResult()` | `org.bukkit.event.player.AsyncPlayerPreLoginEvent$Result` |
| `name` | string | `getName()` | `java.lang.String` |
| `result` | string | `getResult()` | `org.bukkit.event.player.PlayerPreLoginEvent$Result` |
| `uniqueId` | string | `getUniqueId()` | `java.util.UUID` |

<a id="event-io-papermc-paper-event-player-chatevent"></a>
### ChatEvent

- Java class: `io.papermc.paper.event.player.ChatEvent`; parent: `io.papermc.paper.event.player.AbstractChatEvent`.
- Python subscription: `@bridge.on("ChatEvent")`; `Events.CHAT` also works.
- Cancellable: yes; player: possible, depending on the runtime object.
- [Official Paper Javadoc](https://jd.papermc.io/paper/1.16.5/io/papermc/paper/event/player/ChatEvent.html) for meaning, trigger conditions, and Java API.

No serializable possible `data` fields; common event fields are still sent.

<a id="event-com-destroystokyo-paper-event-player-illegalpacketevent"></a>
### IllegalPacketEvent

- Java class: `com.destroystokyo.paper.event.player.IllegalPacketEvent`; parent: `org.bukkit.event.player.PlayerEvent`.
- Python subscription: `@bridge.on("IllegalPacketEvent")`; `Events.ILLEGAL_PACKET` also works.
- Cancellable: no; player: possible, depending on the runtime object.
- [Official Paper Javadoc](https://jd.papermc.io/paper/1.16.5/com/destroystokyo/paper/event/player/IllegalPacketEvent.html) for meaning, trigger conditions, and Java API.

| `data` field | JSON type | Java getter | Java return type |
| --- | --- | --- | --- |
| `exceptionMessage` | string | `getExceptionMessage()` | `java.lang.String` |
| `kickMessage` | string | `getKickMessage()` | `java.lang.String` |
| `type` | string | `getType()` | `java.lang.String` |
| `shouldKick` | boolean | `isShouldKick()` | `boolean` |

<a id="event-com-destroystokyo-paper-event-player-playeradvancementcriteriongrantevent"></a>
### PlayerAdvancementCriterionGrantEvent

- Java class: `com.destroystokyo.paper.event.player.PlayerAdvancementCriterionGrantEvent`; parent: `org.bukkit.event.player.PlayerEvent`.
- Python subscription: `@bridge.on("PlayerAdvancementCriterionGrantEvent")`; `Events.PLAYER_ADVANCEMENT_CRITERION_GRANT` also works.
- Cancellable: yes; player: possible, depending on the runtime object.
- [Official Paper Javadoc](https://jd.papermc.io/paper/1.16.5/com/destroystokyo/paper/event/player/PlayerAdvancementCriterionGrantEvent.html) for meaning, trigger conditions, and Java API.

| `data` field | JSON type | Java getter | Java return type |
| --- | --- | --- | --- |
| `criterion` | string | `getCriterion()` | `java.lang.String` |

<a id="event-org-bukkit-event-player-playeradvancementdoneevent"></a>
### PlayerAdvancementDoneEvent

- Java class: `org.bukkit.event.player.PlayerAdvancementDoneEvent`; parent: `org.bukkit.event.player.PlayerEvent`.
- Python subscription: `@bridge.on("PlayerAdvancementDoneEvent")`; `Events.PLAYER_ADVANCEMENT_DONE` also works.
- Cancellable: no; player: possible, depending on the runtime object.
- [Official Paper Javadoc](https://jd.papermc.io/paper/1.16.5/org/bukkit/event/player/PlayerAdvancementDoneEvent.html) for meaning, trigger conditions, and Java API.

No serializable possible `data` fields; common event fields are still sent.

<a id="event-org-bukkit-event-player-playeranimationevent"></a>
### PlayerAnimationEvent

- Java class: `org.bukkit.event.player.PlayerAnimationEvent`; parent: `org.bukkit.event.player.PlayerEvent`.
- Python subscription: `@bridge.on("PlayerAnimationEvent")`; `Events.PLAYER_ANIMATION` also works.
- Cancellable: yes; player: possible, depending on the runtime object.
- [Official Paper Javadoc](https://jd.papermc.io/paper/1.16.5/org/bukkit/event/player/PlayerAnimationEvent.html) for meaning, trigger conditions, and Java API.

| `data` field | JSON type | Java getter | Java return type |
| --- | --- | --- | --- |
| `animationType` | string | `getAnimationType()` | `org.bukkit.event.player.PlayerAnimationType` |

<a id="event-com-destroystokyo-paper-event-player-playerarmorchangeevent"></a>
### PlayerArmorChangeEvent

- Java class: `com.destroystokyo.paper.event.player.PlayerArmorChangeEvent`; parent: `org.bukkit.event.player.PlayerEvent`.
- Python subscription: `@bridge.on("PlayerArmorChangeEvent")`; `Events.PLAYER_ARMOR_CHANGE` also works.
- Cancellable: no; player: possible, depending on the runtime object.
- [Official Paper Javadoc](https://jd.papermc.io/paper/1.16.5/com/destroystokyo/paper/event/player/PlayerArmorChangeEvent.html) for meaning, trigger conditions, and Java API.

| `data` field | JSON type | Java getter | Java return type |
| --- | --- | --- | --- |
| `newItem` | item summary | `getNewItem()` | `org.bukkit.inventory.ItemStack` |
| `oldItem` | item summary | `getOldItem()` | `org.bukkit.inventory.ItemStack` |
| `slotType` | string | `getSlotType()` | `com.destroystokyo.paper.event.player.PlayerArmorChangeEvent$SlotType` |

<a id="event-org-bukkit-event-player-playerarmorstandmanipulateevent"></a>
### PlayerArmorStandManipulateEvent

- Java class: `org.bukkit.event.player.PlayerArmorStandManipulateEvent`; parent: `org.bukkit.event.player.PlayerInteractEntityEvent`.
- Python subscription: `@bridge.on("PlayerArmorStandManipulateEvent")`; `Events.PLAYER_ARMOR_STAND_MANIPULATE` also works.
- Cancellable: yes; player: possible, depending on the runtime object.
- [Official Paper Javadoc](https://jd.papermc.io/paper/1.16.5/org/bukkit/event/player/PlayerArmorStandManipulateEvent.html) for meaning, trigger conditions, and Java API.

| `data` field | JSON type | Java getter | Java return type |
| --- | --- | --- | --- |
| `armorStandItem` | item summary | `getArmorStandItem()` | `org.bukkit.inventory.ItemStack` |
| `hand` | string | `getHand()` | `org.bukkit.inventory.EquipmentSlot` |
| `playerItem` | item summary | `getPlayerItem()` | `org.bukkit.inventory.ItemStack` |
| `rightClicked` | entity summary | `getRightClicked()` | `org.bukkit.entity.ArmorStand` |
| `slot` | string | `getSlot()` | `org.bukkit.inventory.EquipmentSlot` |

<a id="event-io-papermc-paper-event-player-playerarmswingevent"></a>
### PlayerArmSwingEvent

- Java class: `io.papermc.paper.event.player.PlayerArmSwingEvent`; parent: `org.bukkit.event.player.PlayerAnimationEvent`.
- Python subscription: `@bridge.on("PlayerArmSwingEvent")`; `Events.PLAYER_ARM_SWING` also works.
- Cancellable: yes; player: possible, depending on the runtime object.
- [Official Paper Javadoc](https://jd.papermc.io/paper/1.16.5/io/papermc/paper/event/player/PlayerArmSwingEvent.html) for meaning, trigger conditions, and Java API.

| `data` field | JSON type | Java getter | Java return type |
| --- | --- | --- | --- |
| `animationType` | string | `getAnimationType()` | `org.bukkit.event.player.PlayerAnimationType` |
| `hand` | string | `getHand()` | `org.bukkit.inventory.EquipmentSlot` |

<a id="event-com-destroystokyo-paper-event-player-playerattackentitycooldownresetevent"></a>
### PlayerAttackEntityCooldownResetEvent

- Java class: `com.destroystokyo.paper.event.player.PlayerAttackEntityCooldownResetEvent`; parent: `org.bukkit.event.player.PlayerEvent`.
- Python subscription: `@bridge.on("PlayerAttackEntityCooldownResetEvent")`; `Events.PLAYER_ATTACK_ENTITY_COOLDOWN_RESET` also works.
- Cancellable: yes; player: possible, depending on the runtime object.
- [Official Paper Javadoc](https://jd.papermc.io/paper/1.16.5/com/destroystokyo/paper/event/player/PlayerAttackEntityCooldownResetEvent.html) for meaning, trigger conditions, and Java API.

| `data` field | JSON type | Java getter | Java return type |
| --- | --- | --- | --- |
| `attackedEntity` | entity summary | `getAttackedEntity()` | `org.bukkit.entity.Entity` |
| `cooledAttackStrength` | number | `getCooledAttackStrength()` | `float` |

<a id="event-org-bukkit-event-player-playerattemptpickupitemevent"></a>
### PlayerAttemptPickupItemEvent

- Java class: `org.bukkit.event.player.PlayerAttemptPickupItemEvent`; parent: `org.bukkit.event.player.PlayerEvent`.
- Python subscription: `@bridge.on("PlayerAttemptPickupItemEvent")`; `Events.PLAYER_ATTEMPT_PICKUP_ITEM` also works.
- Cancellable: yes; player: possible, depending on the runtime object.
- [Official Paper Javadoc](https://jd.papermc.io/paper/1.16.5/org/bukkit/event/player/PlayerAttemptPickupItemEvent.html) for meaning, trigger conditions, and Java API.

| `data` field | JSON type | Java getter | Java return type |
| --- | --- | --- | --- |
| `flyAtPlayer` | boolean | `getFlyAtPlayer()` | `boolean` |
| `item` | entity summary | `getItem()` | `org.bukkit.entity.Item` |
| `remaining` | number | `getRemaining()` | `int` |

<a id="event-org-bukkit-event-player-playerbedenterevent"></a>
### PlayerBedEnterEvent

- Java class: `org.bukkit.event.player.PlayerBedEnterEvent`; parent: `org.bukkit.event.player.PlayerEvent`.
- Python subscription: `@bridge.on("PlayerBedEnterEvent")`; `Events.PLAYER_BED_ENTER` also works.
- Cancellable: yes; player: possible, depending on the runtime object.
- [Official Paper Javadoc](https://jd.papermc.io/paper/1.16.5/org/bukkit/event/player/PlayerBedEnterEvent.html) for meaning, trigger conditions, and Java API.

| `data` field | JSON type | Java getter | Java return type |
| --- | --- | --- | --- |
| `bed` | block summary | `getBed()` | `org.bukkit.block.Block` |
| `bedEnterResult` | string | `getBedEnterResult()` | `org.bukkit.event.player.PlayerBedEnterEvent$BedEnterResult` |

<a id="event-io-papermc-paper-event-player-playerbedfailenterevent"></a>
### PlayerBedFailEnterEvent

- Java class: `io.papermc.paper.event.player.PlayerBedFailEnterEvent`; parent: `org.bukkit.event.player.PlayerEvent`.
- Python subscription: `@bridge.on("PlayerBedFailEnterEvent")`; `Events.PLAYER_BED_FAIL_ENTER` also works.
- Cancellable: yes; player: possible, depending on the runtime object.
- [Official Paper Javadoc](https://jd.papermc.io/paper/1.16.5/io/papermc/paper/event/player/PlayerBedFailEnterEvent.html) for meaning, trigger conditions, and Java API.

| `data` field | JSON type | Java getter | Java return type |
| --- | --- | --- | --- |
| `bed` | block summary | `getBed()` | `org.bukkit.block.Block` |
| `failReason` | string | `getFailReason()` | `io.papermc.paper.event.player.PlayerBedFailEnterEvent$FailReason` |
| `willExplode` | boolean | `getWillExplode()` | `boolean` |

<a id="event-org-bukkit-event-player-playerbedleaveevent"></a>
### PlayerBedLeaveEvent

- Java class: `org.bukkit.event.player.PlayerBedLeaveEvent`; parent: `org.bukkit.event.player.PlayerEvent`.
- Python subscription: `@bridge.on("PlayerBedLeaveEvent")`; `Events.PLAYER_BED_LEAVE` also works.
- Cancellable: yes; player: possible, depending on the runtime object.
- [Official Paper Javadoc](https://jd.papermc.io/paper/1.16.5/org/bukkit/event/player/PlayerBedLeaveEvent.html) for meaning, trigger conditions, and Java API.

| `data` field | JSON type | Java getter | Java return type |
| --- | --- | --- | --- |
| `bed` | block summary | `getBed()` | `org.bukkit.block.Block` |

<a id="event-org-bukkit-event-player-playerbucketemptyevent"></a>
### PlayerBucketEmptyEvent

- Java class: `org.bukkit.event.player.PlayerBucketEmptyEvent`; parent: `org.bukkit.event.player.PlayerBucketEvent`.
- Python subscription: `@bridge.on("PlayerBucketEmptyEvent")`; `Events.PLAYER_BUCKET_EMPTY` also works.
- Cancellable: yes; player: possible, depending on the runtime object.
- [Official Paper Javadoc](https://jd.papermc.io/paper/1.16.5/org/bukkit/event/player/PlayerBucketEmptyEvent.html) for meaning, trigger conditions, and Java API.

| `data` field | JSON type | Java getter | Java return type |
| --- | --- | --- | --- |
| `block` | block summary | `getBlock()` | `org.bukkit.block.Block` |
| `blockClicked` | block summary | `getBlockClicked()` | `org.bukkit.block.Block` |
| `blockFace` | string | `getBlockFace()` | `org.bukkit.block.BlockFace` |
| `bucket` | string | `getBucket()` | `org.bukkit.Material` |
| `hand` | string | `getHand()` | `org.bukkit.inventory.EquipmentSlot` |
| `itemStack` | item summary | `getItemStack()` | `org.bukkit.inventory.ItemStack` |

<a id="event-org-bukkit-event-player-playerbucketentityevent"></a>
### PlayerBucketEntityEvent

- Java class: `org.bukkit.event.player.PlayerBucketEntityEvent`; parent: `org.bukkit.event.player.PlayerEvent`.
- Python subscription: `@bridge.on("PlayerBucketEntityEvent")`; `Events.PLAYER_BUCKET_ENTITY` also works.
- Cancellable: yes; player: possible, depending on the runtime object.
- [Official Paper Javadoc](https://jd.papermc.io/paper/1.16.5/org/bukkit/event/player/PlayerBucketEntityEvent.html) for meaning, trigger conditions, and Java API.

| `data` field | JSON type | Java getter | Java return type |
| --- | --- | --- | --- |
| `entity` | entity summary | `getEntity()` | `org.bukkit.entity.Entity` |
| `entityBucket` | item summary | `getEntityBucket()` | `org.bukkit.inventory.ItemStack` |
| `originalBucket` | item summary | `getOriginalBucket()` | `org.bukkit.inventory.ItemStack` |

<a id="event-org-bukkit-event-player-playerbucketfillevent"></a>
### PlayerBucketFillEvent

- Java class: `org.bukkit.event.player.PlayerBucketFillEvent`; parent: `org.bukkit.event.player.PlayerBucketEvent`.
- Python subscription: `@bridge.on("PlayerBucketFillEvent")`; `Events.PLAYER_BUCKET_FILL` also works.
- Cancellable: yes; player: possible, depending on the runtime object.
- [Official Paper Javadoc](https://jd.papermc.io/paper/1.16.5/org/bukkit/event/player/PlayerBucketFillEvent.html) for meaning, trigger conditions, and Java API.

| `data` field | JSON type | Java getter | Java return type |
| --- | --- | --- | --- |
| `block` | block summary | `getBlock()` | `org.bukkit.block.Block` |
| `blockClicked` | block summary | `getBlockClicked()` | `org.bukkit.block.Block` |
| `blockFace` | string | `getBlockFace()` | `org.bukkit.block.BlockFace` |
| `bucket` | string | `getBucket()` | `org.bukkit.Material` |
| `hand` | string | `getHand()` | `org.bukkit.inventory.EquipmentSlot` |
| `itemStack` | item summary | `getItemStack()` | `org.bukkit.inventory.ItemStack` |

<a id="event-org-bukkit-event-player-playerbucketfishevent"></a>
### PlayerBucketFishEvent

- Java class: `org.bukkit.event.player.PlayerBucketFishEvent`; parent: `org.bukkit.event.player.PlayerBucketEntityEvent`.
- Python subscription: `@bridge.on("PlayerBucketFishEvent")`; `Events.PLAYER_BUCKET_FISH` also works.
- Cancellable: yes; player: possible, depending on the runtime object.
- [Official Paper Javadoc](https://jd.papermc.io/paper/1.16.5/org/bukkit/event/player/PlayerBucketFishEvent.html) for meaning, trigger conditions, and Java API.

| `data` field | JSON type | Java getter | Java return type |
| --- | --- | --- | --- |
| `entity` | entity summary | `getEntity()` | `org.bukkit.entity.Fish` |
| `entityBucket` | item summary | `getEntityBucket()` | `org.bukkit.inventory.ItemStack` |
| `fishBucket` | item summary | `getFishBucket()` | `org.bukkit.inventory.ItemStack` |
| `originalBucket` | item summary | `getOriginalBucket()` | `org.bukkit.inventory.ItemStack` |
| `waterBucket` | item summary | `getWaterBucket()` | `org.bukkit.inventory.ItemStack` |

<a id="event-io-papermc-paper-event-player-playerchangebeaconeffectevent"></a>
### PlayerChangeBeaconEffectEvent

- Java class: `io.papermc.paper.event.player.PlayerChangeBeaconEffectEvent`; parent: `org.bukkit.event.player.PlayerEvent`.
- Python subscription: `@bridge.on("PlayerChangeBeaconEffectEvent")`; `Events.PLAYER_CHANGE_BEACON_EFFECT` also works.
- Cancellable: yes; player: possible, depending on the runtime object.
- [Official Paper Javadoc](https://jd.papermc.io/paper/1.16.5/io/papermc/paper/event/player/PlayerChangeBeaconEffectEvent.html) for meaning, trigger conditions, and Java API.

| `data` field | JSON type | Java getter | Java return type |
| --- | --- | --- | --- |
| `beacon` | block summary | `getBeacon()` | `org.bukkit.block.Block` |

<a id="event-org-bukkit-event-player-playerchangedmainhandevent"></a>
### PlayerChangedMainHandEvent

- Java class: `org.bukkit.event.player.PlayerChangedMainHandEvent`; parent: `org.bukkit.event.player.PlayerEvent`.
- Python subscription: `@bridge.on("PlayerChangedMainHandEvent")`; `Events.PLAYER_CHANGED_MAIN_HAND` also works.
- Cancellable: no; player: possible, depending on the runtime object.
- [Official Paper Javadoc](https://jd.papermc.io/paper/1.16.5/org/bukkit/event/player/PlayerChangedMainHandEvent.html) for meaning, trigger conditions, and Java API.

| `data` field | JSON type | Java getter | Java return type |
| --- | --- | --- | --- |
| `mainHand` | string | `getMainHand()` | `org.bukkit.inventory.MainHand` |

<a id="event-org-bukkit-event-player-playerchangedworldevent"></a>
### PlayerChangedWorldEvent

- Java class: `org.bukkit.event.player.PlayerChangedWorldEvent`; parent: `org.bukkit.event.player.PlayerEvent`.
- Python subscription: `@bridge.on("PlayerChangedWorldEvent")`; `Events.PLAYER_CHANGED_WORLD` also works.
- Cancellable: no; player: possible, depending on the runtime object.
- [Official Paper Javadoc](https://jd.papermc.io/paper/1.16.5/org/bukkit/event/player/PlayerChangedWorldEvent.html) for meaning, trigger conditions, and Java API.

| `data` field | JSON type | Java getter | Java return type |
| --- | --- | --- | --- |
| `from` | world summary | `getFrom()` | `org.bukkit.World` |

<a id="event-org-bukkit-event-player-playerchatevent"></a>
### PlayerChatEvent

- Java class: `org.bukkit.event.player.PlayerChatEvent`; parent: `org.bukkit.event.player.PlayerEvent`.
- Python subscription: `@bridge.on("PlayerChatEvent")`; `Events.PLAYER_CHAT` also works.
- Cancellable: yes; player: possible, depending on the runtime object.
- [Official Paper Javadoc](https://jd.papermc.io/paper/1.16.5/org/bukkit/event/player/PlayerChatEvent.html) for meaning, trigger conditions, and Java API.

| `data` field | JSON type | Java getter | Java return type |
| --- | --- | --- | --- |
| `format` | string | `getFormat()` | `java.lang.String` |
| `message` | string | `getMessage()` | `java.lang.String` |

<a id="event-org-bukkit-event-player-playerchattabcompleteevent"></a>
### PlayerChatTabCompleteEvent

- Java class: `org.bukkit.event.player.PlayerChatTabCompleteEvent`; parent: `org.bukkit.event.player.PlayerEvent`.
- Python subscription: `@bridge.on("PlayerChatTabCompleteEvent")`; `Events.PLAYER_CHAT_TAB_COMPLETE` also works.
- Cancellable: no; player: possible, depending on the runtime object.
- [Official Paper Javadoc](https://jd.papermc.io/paper/1.16.5/org/bukkit/event/player/PlayerChatTabCompleteEvent.html) for meaning, trigger conditions, and Java API.

| `data` field | JSON type | Java getter | Java return type |
| --- | --- | --- | --- |
| `chatMessage` | string | `getChatMessage()` | `java.lang.String` |
| `lastToken` | string | `getLastToken()` | `java.lang.String` |

<a id="event-com-destroystokyo-paper-event-player-playerclientoptionschangeevent"></a>
### PlayerClientOptionsChangeEvent

- Java class: `com.destroystokyo.paper.event.player.PlayerClientOptionsChangeEvent`; parent: `org.bukkit.event.player.PlayerEvent`.
- Python subscription: `@bridge.on("PlayerClientOptionsChangeEvent")`; `Events.PLAYER_CLIENT_OPTIONS_CHANGE` also works.
- Cancellable: no; player: possible, depending on the runtime object.
- [Official Paper Javadoc](https://jd.papermc.io/paper/1.16.5/com/destroystokyo/paper/event/player/PlayerClientOptionsChangeEvent.html) for meaning, trigger conditions, and Java API.

| `data` field | JSON type | Java getter | Java return type |
| --- | --- | --- | --- |
| `chatVisibility` | string | `getChatVisibility()` | `com.destroystokyo.paper.ClientOption$ChatVisibility` |
| `locale` | string | `getLocale()` | `java.lang.String` |
| `mainHand` | string | `getMainHand()` | `org.bukkit.inventory.MainHand` |
| `viewDistance` | number | `getViewDistance()` | `int` |

<a id="event-org-bukkit-event-player-playercommandpreprocessevent"></a>
### PlayerCommandPreprocessEvent

- Java class: `org.bukkit.event.player.PlayerCommandPreprocessEvent`; parent: `org.bukkit.event.player.PlayerEvent`.
- Python subscription: `@bridge.on("PlayerCommandPreprocessEvent")`; `Events.PLAYER_COMMAND_PREPROCESS` also works.
- Cancellable: yes; player: possible, depending on the runtime object.
- [Official Paper Javadoc](https://jd.papermc.io/paper/1.16.5/org/bukkit/event/player/PlayerCommandPreprocessEvent.html) for meaning, trigger conditions, and Java API.

| `data` field | JSON type | Java getter | Java return type |
| --- | --- | --- | --- |
| `message` | string | `getMessage()` | `java.lang.String` |

<a id="event-org-bukkit-event-player-playercommandsendevent"></a>
### PlayerCommandSendEvent

- Java class: `org.bukkit.event.player.PlayerCommandSendEvent`; parent: `org.bukkit.event.player.PlayerEvent`.
- Python subscription: `@bridge.on("PlayerCommandSendEvent")`; `Events.PLAYER_COMMAND_SEND` also works.
- Cancellable: no; player: possible, depending on the runtime object.
- [Official Paper Javadoc](https://jd.papermc.io/paper/1.16.5/org/bukkit/event/player/PlayerCommandSendEvent.html) for meaning, trigger conditions, and Java API.

No serializable possible `data` fields; common event fields are still sent.

<a id="event-com-destroystokyo-paper-event-player-playerconnectioncloseevent"></a>
### PlayerConnectionCloseEvent

- Java class: `com.destroystokyo.paper.event.player.PlayerConnectionCloseEvent`; parent: `org.bukkit.event.Event`.
- Python subscription: `@bridge.on("PlayerConnectionCloseEvent")`; `Events.PLAYER_CONNECTION_CLOSE` also works.
- Cancellable: no; player: no known player getter.
- [Official Paper Javadoc](https://jd.papermc.io/paper/1.16.5/com/destroystokyo/paper/event/player/PlayerConnectionCloseEvent.html) for meaning, trigger conditions, and Java API.

| `data` field | JSON type | Java getter | Java return type |
| --- | --- | --- | --- |
| `playerName` | string | `getPlayerName()` | `java.lang.String` |
| `playerUniqueId` | string | `getPlayerUniqueId()` | `java.util.UUID` |

<a id="event-io-papermc-paper-event-player-playerdeepsleepevent"></a>
### PlayerDeepSleepEvent

- Java class: `io.papermc.paper.event.player.PlayerDeepSleepEvent`; parent: `org.bukkit.event.player.PlayerEvent`.
- Python subscription: `@bridge.on("PlayerDeepSleepEvent")`; `Events.PLAYER_DEEP_SLEEP` also works.
- Cancellable: yes; player: possible, depending on the runtime object.
- [Official Paper Javadoc](https://jd.papermc.io/paper/1.16.5/io/papermc/paper/event/player/PlayerDeepSleepEvent.html) for meaning, trigger conditions, and Java API.

No serializable possible `data` fields; common event fields are still sent.

<a id="event-org-bukkit-event-player-playerdropitemevent"></a>
### PlayerDropItemEvent

- Java class: `org.bukkit.event.player.PlayerDropItemEvent`; parent: `org.bukkit.event.player.PlayerEvent`.
- Python subscription: `@bridge.on("PlayerDropItemEvent")`; `Events.PLAYER_DROP_ITEM` also works.
- Cancellable: yes; player: possible, depending on the runtime object.
- [Official Paper Javadoc](https://jd.papermc.io/paper/1.16.5/org/bukkit/event/player/PlayerDropItemEvent.html) for meaning, trigger conditions, and Java API.

| `data` field | JSON type | Java getter | Java return type |
| --- | --- | --- | --- |
| `itemDrop` | entity summary | `getItemDrop()` | `org.bukkit.entity.Item` |

<a id="event-org-bukkit-event-player-playereditbookevent"></a>
### PlayerEditBookEvent

- Java class: `org.bukkit.event.player.PlayerEditBookEvent`; parent: `org.bukkit.event.player.PlayerEvent`.
- Python subscription: `@bridge.on("PlayerEditBookEvent")`; `Events.PLAYER_EDIT_BOOK` also works.
- Cancellable: yes; player: possible, depending on the runtime object.
- [Official Paper Javadoc](https://jd.papermc.io/paper/1.16.5/org/bukkit/event/player/PlayerEditBookEvent.html) for meaning, trigger conditions, and Java API.

| `data` field | JSON type | Java getter | Java return type |
| --- | --- | --- | --- |
| `slot` | number | `getSlot()` | `int` |
| `signing` | boolean | `isSigning()` | `boolean` |

<a id="event-org-bukkit-event-player-playereggthrowevent"></a>
### PlayerEggThrowEvent

- Java class: `org.bukkit.event.player.PlayerEggThrowEvent`; parent: `org.bukkit.event.player.PlayerEvent`.
- Python subscription: `@bridge.on("PlayerEggThrowEvent")`; `Events.PLAYER_EGG_THROW` also works.
- Cancellable: no; player: possible, depending on the runtime object.
- [Official Paper Javadoc](https://jd.papermc.io/paper/1.16.5/org/bukkit/event/player/PlayerEggThrowEvent.html) for meaning, trigger conditions, and Java API.

| `data` field | JSON type | Java getter | Java return type |
| --- | --- | --- | --- |
| `egg` | entity summary | `getEgg()` | `org.bukkit.entity.Egg` |
| `hatchingType` | string | `getHatchingType()` | `org.bukkit.entity.EntityType` |
| `numHatches` | number | `getNumHatches()` | `byte` |
| `hatching` | boolean | `isHatching()` | `boolean` |

<a id="event-com-destroystokyo-paper-event-player-playerelytraboostevent"></a>
### PlayerElytraBoostEvent

- Java class: `com.destroystokyo.paper.event.player.PlayerElytraBoostEvent`; parent: `org.bukkit.event.player.PlayerEvent`.
- Python subscription: `@bridge.on("PlayerElytraBoostEvent")`; `Events.PLAYER_ELYTRA_BOOST` also works.
- Cancellable: yes; player: possible, depending on the runtime object.
- [Official Paper Javadoc](https://jd.papermc.io/paper/1.16.5/com/destroystokyo/paper/event/player/PlayerElytraBoostEvent.html) for meaning, trigger conditions, and Java API.

| `data` field | JSON type | Java getter | Java return type |
| --- | --- | --- | --- |
| `firework` | entity summary | `getFirework()` | `org.bukkit.entity.Firework` |
| `itemStack` | item summary | `getItemStack()` | `org.bukkit.inventory.ItemStack` |

<a id="event-org-bukkit-event-player-playerexpchangeevent"></a>
### PlayerExpChangeEvent

- Java class: `org.bukkit.event.player.PlayerExpChangeEvent`; parent: `org.bukkit.event.player.PlayerEvent`.
- Python subscription: `@bridge.on("PlayerExpChangeEvent")`; `Events.PLAYER_EXP_CHANGE` also works.
- Cancellable: no; player: possible, depending on the runtime object.
- [Official Paper Javadoc](https://jd.papermc.io/paper/1.16.5/org/bukkit/event/player/PlayerExpChangeEvent.html) for meaning, trigger conditions, and Java API.

| `data` field | JSON type | Java getter | Java return type |
| --- | --- | --- | --- |
| `amount` | number | `getAmount()` | `int` |
| `source` | entity summary | `getSource()` | `org.bukkit.entity.Entity` |

<a id="event-org-bukkit-event-player-playerfishevent"></a>
### PlayerFishEvent

- Java class: `org.bukkit.event.player.PlayerFishEvent`; parent: `org.bukkit.event.player.PlayerEvent`.
- Python subscription: `@bridge.on("PlayerFishEvent")`; `Events.PLAYER_FISH` also works.
- Cancellable: yes; player: possible, depending on the runtime object.
- [Official Paper Javadoc](https://jd.papermc.io/paper/1.16.5/org/bukkit/event/player/PlayerFishEvent.html) for meaning, trigger conditions, and Java API.

| `data` field | JSON type | Java getter | Java return type |
| --- | --- | --- | --- |
| `caught` | entity summary | `getCaught()` | `org.bukkit.entity.Entity` |
| `expToDrop` | number | `getExpToDrop()` | `int` |
| `hook` | entity summary | `getHook()` | `org.bukkit.entity.FishHook` |
| `state` | string | `getState()` | `org.bukkit.event.player.PlayerFishEvent$State` |

<a id="event-io-papermc-paper-event-player-playerflowerpotmanipulateevent"></a>
### PlayerFlowerPotManipulateEvent

- Java class: `io.papermc.paper.event.player.PlayerFlowerPotManipulateEvent`; parent: `org.bukkit.event.player.PlayerEvent`.
- Python subscription: `@bridge.on("PlayerFlowerPotManipulateEvent")`; `Events.PLAYER_FLOWER_POT_MANIPULATE` also works.
- Cancellable: yes; player: possible, depending on the runtime object.
- [Official Paper Javadoc](https://jd.papermc.io/paper/1.16.5/io/papermc/paper/event/player/PlayerFlowerPotManipulateEvent.html) for meaning, trigger conditions, and Java API.

| `data` field | JSON type | Java getter | Java return type |
| --- | --- | --- | --- |
| `flowerpot` | block summary | `getFlowerpot()` | `org.bukkit.block.Block` |
| `item` | item summary | `getItem()` | `org.bukkit.inventory.ItemStack` |
| `placing` | boolean | `isPlacing()` | `boolean` |

<a id="event-org-bukkit-event-player-playergamemodechangeevent"></a>
### PlayerGameModeChangeEvent

- Java class: `org.bukkit.event.player.PlayerGameModeChangeEvent`; parent: `org.bukkit.event.player.PlayerEvent`.
- Python subscription: `@bridge.on("PlayerGameModeChangeEvent")`; `Events.PLAYER_GAME_MODE_CHANGE` also works.
- Cancellable: yes; player: possible, depending on the runtime object.
- [Official Paper Javadoc](https://jd.papermc.io/paper/1.16.5/org/bukkit/event/player/PlayerGameModeChangeEvent.html) for meaning, trigger conditions, and Java API.

| `data` field | JSON type | Java getter | Java return type |
| --- | --- | --- | --- |
| `cause` | string | `getCause()` | `org.bukkit.event.player.PlayerGameModeChangeEvent$Cause` |
| `newGameMode` | string | `getNewGameMode()` | `org.bukkit.GameMode` |

<a id="event-com-destroystokyo-paper-event-player-playerhandshakeevent"></a>
### PlayerHandshakeEvent

- Java class: `com.destroystokyo.paper.event.player.PlayerHandshakeEvent`; parent: `org.bukkit.event.Event`.
- Python subscription: `@bridge.on("PlayerHandshakeEvent")`; `Events.PLAYER_HANDSHAKE` also works.
- Cancellable: yes; player: no known player getter.
- [Official Paper Javadoc](https://jd.papermc.io/paper/1.16.5/com/destroystokyo/paper/event/player/PlayerHandshakeEvent.html) for meaning, trigger conditions, and Java API.

| `data` field | JSON type | Java getter | Java return type |
| --- | --- | --- | --- |
| `failMessage` | string | `getFailMessage()` | `java.lang.String` |
| `originalHandshake` | string | `getOriginalHandshake()` | `java.lang.String` |
| `originalSocketAddressHostname` | string | `getOriginalSocketAddressHostname()` | `java.lang.String` |
| `propertiesJson` | string | `getPropertiesJson()` | `java.lang.String` |
| `serverHostname` | string | `getServerHostname()` | `java.lang.String` |
| `socketAddressHostname` | string | `getSocketAddressHostname()` | `java.lang.String` |
| `uniqueId` | string | `getUniqueId()` | `java.util.UUID` |
| `failed` | boolean | `isFailed()` | `boolean` |

<a id="event-org-bukkit-event-player-playerharvestblockevent"></a>
### PlayerHarvestBlockEvent

- Java class: `org.bukkit.event.player.PlayerHarvestBlockEvent`; parent: `org.bukkit.event.player.PlayerEvent`.
- Python subscription: `@bridge.on("PlayerHarvestBlockEvent")`; `Events.PLAYER_HARVEST_BLOCK` also works.
- Cancellable: yes; player: possible, depending on the runtime object.
- [Official Paper Javadoc](https://jd.papermc.io/paper/1.16.5/org/bukkit/event/player/PlayerHarvestBlockEvent.html) for meaning, trigger conditions, and Java API.

| `data` field | JSON type | Java getter | Java return type |
| --- | --- | --- | --- |
| `harvestedBlock` | block summary | `getHarvestedBlock()` | `org.bukkit.block.Block` |

<a id="event-com-destroystokyo-paper-event-player-playerinitialspawnevent"></a>
### PlayerInitialSpawnEvent

- Java class: `com.destroystokyo.paper.event.player.PlayerInitialSpawnEvent`; parent: `org.spigotmc.event.player.PlayerSpawnLocationEvent`.
- Python subscription: `@bridge.on("PlayerInitialSpawnEvent")`; `Events.PLAYER_INITIAL_SPAWN` also works.
- Cancellable: no; player: possible, depending on the runtime object.
- [Official Paper Javadoc](https://jd.papermc.io/paper/1.16.5/com/destroystokyo/paper/event/player/PlayerInitialSpawnEvent.html) for meaning, trigger conditions, and Java API.

| `data` field | JSON type | Java getter | Java return type |
| --- | --- | --- | --- |
| `spawnLocation` | location summary | `getSpawnLocation()` | `org.bukkit.Location` |

<a id="event-org-bukkit-event-player-playerinteractatentityevent"></a>
### PlayerInteractAtEntityEvent

- Java class: `org.bukkit.event.player.PlayerInteractAtEntityEvent`; parent: `org.bukkit.event.player.PlayerInteractEntityEvent`.
- Python subscription: `@bridge.on("PlayerInteractAtEntityEvent")`; `Events.PLAYER_INTERACT_AT_ENTITY` also works.
- Cancellable: yes; player: possible, depending on the runtime object.
- [Official Paper Javadoc](https://jd.papermc.io/paper/1.16.5/org/bukkit/event/player/PlayerInteractAtEntityEvent.html) for meaning, trigger conditions, and Java API.

| `data` field | JSON type | Java getter | Java return type |
| --- | --- | --- | --- |
| `hand` | string | `getHand()` | `org.bukkit.inventory.EquipmentSlot` |
| `rightClicked` | entity summary | `getRightClicked()` | `org.bukkit.entity.Entity` |

<a id="event-org-bukkit-event-player-playerinteractentityevent"></a>
### PlayerInteractEntityEvent

- Java class: `org.bukkit.event.player.PlayerInteractEntityEvent`; parent: `org.bukkit.event.player.PlayerEvent`.
- Python subscription: `@bridge.on("PlayerInteractEntityEvent")`; `Events.PLAYER_INTERACT_ENTITY` also works.
- Cancellable: yes; player: possible, depending on the runtime object.
- [Official Paper Javadoc](https://jd.papermc.io/paper/1.16.5/org/bukkit/event/player/PlayerInteractEntityEvent.html) for meaning, trigger conditions, and Java API.

| `data` field | JSON type | Java getter | Java return type |
| --- | --- | --- | --- |
| `hand` | string | `getHand()` | `org.bukkit.inventory.EquipmentSlot` |
| `rightClicked` | entity summary | `getRightClicked()` | `org.bukkit.entity.Entity` |

<a id="event-org-bukkit-event-player-playerinteractevent"></a>
### PlayerInteractEvent

- Java class: `org.bukkit.event.player.PlayerInteractEvent`; parent: `org.bukkit.event.player.PlayerEvent`.
- Python subscription: `@bridge.on("PlayerInteractEvent")`; `Events.PLAYER_INTERACT` also works.
- Cancellable: yes; player: possible, depending on the runtime object.
- [Official Paper Javadoc](https://jd.papermc.io/paper/1.16.5/org/bukkit/event/player/PlayerInteractEvent.html) for meaning, trigger conditions, and Java API.

| `data` field | JSON type | Java getter | Java return type |
| --- | --- | --- | --- |
| `action` | string | `getAction()` | `org.bukkit.event.block.Action` |
| `blockFace` | string | `getBlockFace()` | `org.bukkit.block.BlockFace` |
| `clickedBlock` | block summary | `getClickedBlock()` | `org.bukkit.block.Block` |
| `hand` | string | `getHand()` | `org.bukkit.inventory.EquipmentSlot` |
| `interactionPoint` | location summary | `getInteractionPoint()` | `org.bukkit.Location` |
| `item` | item summary | `getItem()` | `org.bukkit.inventory.ItemStack` |
| `material` | string | `getMaterial()` | `org.bukkit.Material` |
| `blockInHand` | boolean | `isBlockInHand()` | `boolean` |

<a id="event-org-bukkit-event-player-playeritembreakevent"></a>
### PlayerItemBreakEvent

- Java class: `org.bukkit.event.player.PlayerItemBreakEvent`; parent: `org.bukkit.event.player.PlayerEvent`.
- Python subscription: `@bridge.on("PlayerItemBreakEvent")`; `Events.PLAYER_ITEM_BREAK` also works.
- Cancellable: no; player: possible, depending on the runtime object.
- [Official Paper Javadoc](https://jd.papermc.io/paper/1.16.5/org/bukkit/event/player/PlayerItemBreakEvent.html) for meaning, trigger conditions, and Java API.

| `data` field | JSON type | Java getter | Java return type |
| --- | --- | --- | --- |
| `brokenItem` | item summary | `getBrokenItem()` | `org.bukkit.inventory.ItemStack` |

<a id="event-org-bukkit-event-player-playeritemconsumeevent"></a>
### PlayerItemConsumeEvent

- Java class: `org.bukkit.event.player.PlayerItemConsumeEvent`; parent: `org.bukkit.event.player.PlayerEvent`.
- Python subscription: `@bridge.on("PlayerItemConsumeEvent")`; `Events.PLAYER_ITEM_CONSUME` also works.
- Cancellable: yes; player: possible, depending on the runtime object.
- [Official Paper Javadoc](https://jd.papermc.io/paper/1.16.5/org/bukkit/event/player/PlayerItemConsumeEvent.html) for meaning, trigger conditions, and Java API.

| `data` field | JSON type | Java getter | Java return type |
| --- | --- | --- | --- |
| `item` | item summary | `getItem()` | `org.bukkit.inventory.ItemStack` |
| `replacement` | item summary | `getReplacement()` | `org.bukkit.inventory.ItemStack` |

<a id="event-io-papermc-paper-event-player-playeritemcooldownevent"></a>
### PlayerItemCooldownEvent

- Java class: `io.papermc.paper.event.player.PlayerItemCooldownEvent`; parent: `org.bukkit.event.player.PlayerEvent`.
- Python subscription: `@bridge.on("PlayerItemCooldownEvent")`; `Events.PLAYER_ITEM_COOLDOWN` also works.
- Cancellable: yes; player: possible, depending on the runtime object.
- [Official Paper Javadoc](https://jd.papermc.io/paper/1.16.5/io/papermc/paper/event/player/PlayerItemCooldownEvent.html) for meaning, trigger conditions, and Java API.

| `data` field | JSON type | Java getter | Java return type |
| --- | --- | --- | --- |
| `cooldown` | number | `getCooldown()` | `int` |
| `type` | string | `getType()` | `org.bukkit.Material` |

<a id="event-org-bukkit-event-player-playeritemdamageevent"></a>
### PlayerItemDamageEvent

- Java class: `org.bukkit.event.player.PlayerItemDamageEvent`; parent: `org.bukkit.event.player.PlayerEvent`.
- Python subscription: `@bridge.on("PlayerItemDamageEvent")`; `Events.PLAYER_ITEM_DAMAGE` also works.
- Cancellable: yes; player: possible, depending on the runtime object.
- [Official Paper Javadoc](https://jd.papermc.io/paper/1.16.5/org/bukkit/event/player/PlayerItemDamageEvent.html) for meaning, trigger conditions, and Java API.

| `data` field | JSON type | Java getter | Java return type |
| --- | --- | --- | --- |
| `damage` | number | `getDamage()` | `int` |
| `item` | item summary | `getItem()` | `org.bukkit.inventory.ItemStack` |

<a id="event-org-bukkit-event-player-playeritemheldevent"></a>
### PlayerItemHeldEvent

- Java class: `org.bukkit.event.player.PlayerItemHeldEvent`; parent: `org.bukkit.event.player.PlayerEvent`.
- Python subscription: `@bridge.on("PlayerItemHeldEvent")`; `Events.PLAYER_ITEM_HELD` also works.
- Cancellable: yes; player: possible, depending on the runtime object.
- [Official Paper Javadoc](https://jd.papermc.io/paper/1.16.5/org/bukkit/event/player/PlayerItemHeldEvent.html) for meaning, trigger conditions, and Java API.

| `data` field | JSON type | Java getter | Java return type |
| --- | --- | --- | --- |
| `newSlot` | number | `getNewSlot()` | `int` |
| `previousSlot` | number | `getPreviousSlot()` | `int` |

<a id="event-org-bukkit-event-player-playeritemmendevent"></a>
### PlayerItemMendEvent

- Java class: `org.bukkit.event.player.PlayerItemMendEvent`; parent: `org.bukkit.event.player.PlayerEvent`.
- Python subscription: `@bridge.on("PlayerItemMendEvent")`; `Events.PLAYER_ITEM_MEND` also works.
- Cancellable: yes; player: possible, depending on the runtime object.
- [Official Paper Javadoc](https://jd.papermc.io/paper/1.16.5/org/bukkit/event/player/PlayerItemMendEvent.html) for meaning, trigger conditions, and Java API.

| `data` field | JSON type | Java getter | Java return type |
| --- | --- | --- | --- |
| `experienceOrb` | entity summary | `getExperienceOrb()` | `org.bukkit.entity.ExperienceOrb` |
| `item` | item summary | `getItem()` | `org.bukkit.inventory.ItemStack` |
| `repairAmount` | number | `getRepairAmount()` | `int` |

<a id="event-org-bukkit-event-player-playerjoinevent"></a>
### PlayerJoinEvent

- Java class: `org.bukkit.event.player.PlayerJoinEvent`; parent: `org.bukkit.event.player.PlayerEvent`.
- Python subscription: `@bridge.on("join")`; `Events.PLAYER_JOIN` also works.
- Cancellable: no; player: possible, depending on the runtime object.
- [Official Paper Javadoc](https://jd.papermc.io/paper/1.16.5/org/bukkit/event/player/PlayerJoinEvent.html) for meaning, trigger conditions, and Java API.

| `data` field | JSON type | Java getter | Java return type |
| --- | --- | --- | --- |
| `joinMessage` | string | `getJoinMessage()` | `java.lang.String` |

<a id="event-com-destroystokyo-paper-event-player-playerjumpevent"></a>
### PlayerJumpEvent

- Java class: `com.destroystokyo.paper.event.player.PlayerJumpEvent`; parent: `org.bukkit.event.player.PlayerEvent`.
- Python subscription: `@bridge.on("PlayerJumpEvent")`; `Events.PLAYER_JUMP` also works.
- Cancellable: yes; player: possible, depending on the runtime object.
- [Official Paper Javadoc](https://jd.papermc.io/paper/1.16.5/com/destroystokyo/paper/event/player/PlayerJumpEvent.html) for meaning, trigger conditions, and Java API.

| `data` field | JSON type | Java getter | Java return type |
| --- | --- | --- | --- |
| `from` | location summary | `getFrom()` | `org.bukkit.Location` |
| `to` | location summary | `getTo()` | `org.bukkit.Location` |

<a id="event-org-bukkit-event-player-playerkickevent"></a>
### PlayerKickEvent

- Java class: `org.bukkit.event.player.PlayerKickEvent`; parent: `org.bukkit.event.player.PlayerEvent`.
- Python subscription: `@bridge.on("PlayerKickEvent")`; `Events.PLAYER_KICK` also works.
- Cancellable: yes; player: possible, depending on the runtime object.
- [Official Paper Javadoc](https://jd.papermc.io/paper/1.16.5/org/bukkit/event/player/PlayerKickEvent.html) for meaning, trigger conditions, and Java API.

| `data` field | JSON type | Java getter | Java return type |
| --- | --- | --- | --- |
| `cause` | string | `getCause()` | `org.bukkit.event.player.PlayerKickEvent$Cause` |
| `leaveMessage` | string | `getLeaveMessage()` | `java.lang.String` |
| `reason` | string | `getReason()` | `java.lang.String` |

<a id="event-com-destroystokyo-paper-event-player-playerlaunchprojectileevent"></a>
### PlayerLaunchProjectileEvent

- Java class: `com.destroystokyo.paper.event.player.PlayerLaunchProjectileEvent`; parent: `org.bukkit.event.player.PlayerEvent`.
- Python subscription: `@bridge.on("PlayerLaunchProjectileEvent")`; `Events.PLAYER_LAUNCH_PROJECTILE` also works.
- Cancellable: yes; player: possible, depending on the runtime object.
- [Official Paper Javadoc](https://jd.papermc.io/paper/1.16.5/com/destroystokyo/paper/event/player/PlayerLaunchProjectileEvent.html) for meaning, trigger conditions, and Java API.

| `data` field | JSON type | Java getter | Java return type |
| --- | --- | --- | --- |
| `itemStack` | item summary | `getItemStack()` | `org.bukkit.inventory.ItemStack` |
| `projectile` | entity summary | `getProjectile()` | `org.bukkit.entity.Projectile` |

<a id="event-io-papermc-paper-event-player-playerlecternpagechangeevent"></a>
### PlayerLecternPageChangeEvent

- Java class: `io.papermc.paper.event.player.PlayerLecternPageChangeEvent`; parent: `org.bukkit.event.player.PlayerEvent`.
- Python subscription: `@bridge.on("PlayerLecternPageChangeEvent")`; `Events.PLAYER_LECTERN_PAGE_CHANGE` also works.
- Cancellable: yes; player: possible, depending on the runtime object.
- [Official Paper Javadoc](https://jd.papermc.io/paper/1.16.5/io/papermc/paper/event/player/PlayerLecternPageChangeEvent.html) for meaning, trigger conditions, and Java API.

| `data` field | JSON type | Java getter | Java return type |
| --- | --- | --- | --- |
| `book` | item summary | `getBook()` | `org.bukkit.inventory.ItemStack` |
| `newPage` | number | `getNewPage()` | `int` |
| `oldPage` | number | `getOldPage()` | `int` |
| `pageChangeDirection` | string | `getPageChangeDirection()` | `io.papermc.paper.event.player.PlayerLecternPageChangeEvent$PageChangeDirection` |

<a id="event-org-bukkit-event-player-playerlevelchangeevent"></a>
### PlayerLevelChangeEvent

- Java class: `org.bukkit.event.player.PlayerLevelChangeEvent`; parent: `org.bukkit.event.player.PlayerEvent`.
- Python subscription: `@bridge.on("PlayerLevelChangeEvent")`; `Events.PLAYER_LEVEL_CHANGE` also works.
- Cancellable: no; player: possible, depending on the runtime object.
- [Official Paper Javadoc](https://jd.papermc.io/paper/1.16.5/org/bukkit/event/player/PlayerLevelChangeEvent.html) for meaning, trigger conditions, and Java API.

| `data` field | JSON type | Java getter | Java return type |
| --- | --- | --- | --- |
| `newLevel` | number | `getNewLevel()` | `int` |
| `oldLevel` | number | `getOldLevel()` | `int` |

<a id="event-com-destroystokyo-paper-event-player-playerlocalechangeevent"></a>
### PlayerLocaleChangeEvent

- Java class: `com.destroystokyo.paper.event.player.PlayerLocaleChangeEvent`; parent: `org.bukkit.event.player.PlayerEvent`.
- Python subscription: `@bridge.on("PlayerLocaleChangeEvent")`; `Events.PAPER_PLAYER_LOCALE_CHANGE` also works.
- Cancellable: no; player: possible, depending on the runtime object.
- [Official Paper Javadoc](https://jd.papermc.io/paper/1.16.5/com/destroystokyo/paper/event/player/PlayerLocaleChangeEvent.html) for meaning, trigger conditions, and Java API.

| `data` field | JSON type | Java getter | Java return type |
| --- | --- | --- | --- |
| `newLocale` | string | `getNewLocale()` | `java.lang.String` |
| `oldLocale` | string | `getOldLocale()` | `java.lang.String` |

<a id="event-org-bukkit-event-player-playerlocalechangeevent"></a>
### PlayerLocaleChangeEvent

- Java class: `org.bukkit.event.player.PlayerLocaleChangeEvent`; parent: `org.bukkit.event.player.PlayerEvent`.
- Python subscription: `@bridge.on("PlayerLocaleChangeEvent")`; `Events.PLAYER_LOCALE_CHANGE` also works.
- Cancellable: no; player: possible, depending on the runtime object.
- [Official Paper Javadoc](https://jd.papermc.io/paper/1.16.5/org/bukkit/event/player/PlayerLocaleChangeEvent.html) for meaning, trigger conditions, and Java API.

| `data` field | JSON type | Java getter | Java return type |
| --- | --- | --- | --- |
| `locale` | string | `getLocale()` | `java.lang.String` |

<a id="event-org-bukkit-event-player-playerloginevent"></a>
### PlayerLoginEvent

- Java class: `org.bukkit.event.player.PlayerLoginEvent`; parent: `org.bukkit.event.player.PlayerEvent`.
- Python subscription: `@bridge.on("PlayerLoginEvent")`; `Events.PLAYER_LOGIN` also works.
- Cancellable: no; player: possible, depending on the runtime object.
- [Official Paper Javadoc](https://jd.papermc.io/paper/1.16.5/org/bukkit/event/player/PlayerLoginEvent.html) for meaning, trigger conditions, and Java API.

| `data` field | JSON type | Java getter | Java return type |
| --- | --- | --- | --- |
| `hostname` | string | `getHostname()` | `java.lang.String` |
| `kickMessage` | string | `getKickMessage()` | `java.lang.String` |
| `result` | string | `getResult()` | `org.bukkit.event.player.PlayerLoginEvent$Result` |

<a id="event-io-papermc-paper-event-player-playerloompatternselectevent"></a>
### PlayerLoomPatternSelectEvent

- Java class: `io.papermc.paper.event.player.PlayerLoomPatternSelectEvent`; parent: `org.bukkit.event.player.PlayerEvent`.
- Python subscription: `@bridge.on("PlayerLoomPatternSelectEvent")`; `Events.PLAYER_LOOM_PATTERN_SELECT` also works.
- Cancellable: yes; player: possible, depending on the runtime object.
- [Official Paper Javadoc](https://jd.papermc.io/paper/1.16.5/io/papermc/paper/event/player/PlayerLoomPatternSelectEvent.html) for meaning, trigger conditions, and Java API.

| `data` field | JSON type | Java getter | Java return type |
| --- | --- | --- | --- |
| `patternType` | string | `getPatternType()` | `org.bukkit.block.banner.PatternType` |

<a id="event-org-bukkit-event-player-playermoveevent"></a>
### PlayerMoveEvent

- Java class: `org.bukkit.event.player.PlayerMoveEvent`; parent: `org.bukkit.event.player.PlayerEvent`.
- Python subscription: `@bridge.on("PlayerMoveEvent")`; `Events.PLAYER_MOVE` also works.
- Cancellable: yes; player: possible, depending on the runtime object.
- [Official Paper Javadoc](https://jd.papermc.io/paper/1.16.5/org/bukkit/event/player/PlayerMoveEvent.html) for meaning, trigger conditions, and Java API.

| `data` field | JSON type | Java getter | Java return type |
| --- | --- | --- | --- |
| `from` | location summary | `getFrom()` | `org.bukkit.Location` |
| `to` | location summary | `getTo()` | `org.bukkit.Location` |

<a id="event-io-papermc-paper-event-player-playernameentityevent"></a>
### PlayerNameEntityEvent

- Java class: `io.papermc.paper.event.player.PlayerNameEntityEvent`; parent: `org.bukkit.event.player.PlayerEvent`.
- Python subscription: `@bridge.on("PlayerNameEntityEvent")`; `Events.PLAYER_NAME_ENTITY` also works.
- Cancellable: yes; player: possible, depending on the runtime object.
- [Official Paper Javadoc](https://jd.papermc.io/paper/1.16.5/io/papermc/paper/event/player/PlayerNameEntityEvent.html) for meaning, trigger conditions, and Java API.

| `data` field | JSON type | Java getter | Java return type |
| --- | --- | --- | --- |
| `entity` | entity summary | `getEntity()` | `org.bukkit.entity.LivingEntity` |
| `persistent` | boolean | `isPersistent()` | `boolean` |

<a id="event-org-bukkit-event-player-playerpickuparrowevent"></a>
### PlayerPickupArrowEvent

- Java class: `org.bukkit.event.player.PlayerPickupArrowEvent`; parent: `org.bukkit.event.player.PlayerPickupItemEvent`.
- Python subscription: `@bridge.on("PlayerPickupArrowEvent")`; `Events.PLAYER_PICKUP_ARROW` also works.
- Cancellable: yes; player: possible, depending on the runtime object.
- [Official Paper Javadoc](https://jd.papermc.io/paper/1.16.5/org/bukkit/event/player/PlayerPickupArrowEvent.html) for meaning, trigger conditions, and Java API.

| `data` field | JSON type | Java getter | Java return type |
| --- | --- | --- | --- |
| `arrow` | entity summary | `getArrow()` | `org.bukkit.entity.AbstractArrow` |
| `flyAtPlayer` | boolean | `getFlyAtPlayer()` | `boolean` |
| `item` | entity summary | `getItem()` | `org.bukkit.entity.Item` |
| `remaining` | number | `getRemaining()` | `int` |

<a id="event-com-destroystokyo-paper-event-player-playerpickupexperienceevent"></a>
### PlayerPickupExperienceEvent

- Java class: `com.destroystokyo.paper.event.player.PlayerPickupExperienceEvent`; parent: `org.bukkit.event.player.PlayerEvent`.
- Python subscription: `@bridge.on("PlayerPickupExperienceEvent")`; `Events.PLAYER_PICKUP_EXPERIENCE` also works.
- Cancellable: yes; player: possible, depending on the runtime object.
- [Official Paper Javadoc](https://jd.papermc.io/paper/1.16.5/com/destroystokyo/paper/event/player/PlayerPickupExperienceEvent.html) for meaning, trigger conditions, and Java API.

| `data` field | JSON type | Java getter | Java return type |
| --- | --- | --- | --- |
| `experienceOrb` | entity summary | `getExperienceOrb()` | `org.bukkit.entity.ExperienceOrb` |

<a id="event-org-bukkit-event-player-playerpickupitemevent"></a>
### PlayerPickupItemEvent

- Java class: `org.bukkit.event.player.PlayerPickupItemEvent`; parent: `org.bukkit.event.player.PlayerEvent`.
- Python subscription: `@bridge.on("PlayerPickupItemEvent")`; `Events.PLAYER_PICKUP_ITEM` also works.
- Cancellable: yes; player: possible, depending on the runtime object.
- [Official Paper Javadoc](https://jd.papermc.io/paper/1.16.5/org/bukkit/event/player/PlayerPickupItemEvent.html) for meaning, trigger conditions, and Java API.

| `data` field | JSON type | Java getter | Java return type |
| --- | --- | --- | --- |
| `flyAtPlayer` | boolean | `getFlyAtPlayer()` | `boolean` |
| `item` | entity summary | `getItem()` | `org.bukkit.entity.Item` |
| `remaining` | number | `getRemaining()` | `int` |

<a id="event-org-bukkit-event-player-playerportalevent"></a>
### PlayerPortalEvent

- Java class: `org.bukkit.event.player.PlayerPortalEvent`; parent: `org.bukkit.event.player.PlayerTeleportEvent`.
- Python subscription: `@bridge.on("PlayerPortalEvent")`; `Events.PLAYER_PORTAL` also works.
- Cancellable: yes; player: possible, depending on the runtime object.
- [Official Paper Javadoc](https://jd.papermc.io/paper/1.16.5/org/bukkit/event/player/PlayerPortalEvent.html) for meaning, trigger conditions, and Java API.

| `data` field | JSON type | Java getter | Java return type |
| --- | --- | --- | --- |
| `canCreatePortal` | boolean | `getCanCreatePortal()` | `boolean` |
| `cause` | string | `getCause()` | `org.bukkit.event.player.PlayerTeleportEvent$TeleportCause` |
| `creationRadius` | number | `getCreationRadius()` | `int` |
| `from` | location summary | `getFrom()` | `org.bukkit.Location` |
| `searchRadius` | number | `getSearchRadius()` | `int` |
| `to` | location summary | `getTo()` | `org.bukkit.Location` |

<a id="event-com-destroystokyo-paper-event-player-playerpostrespawnevent"></a>
### PlayerPostRespawnEvent

- Java class: `com.destroystokyo.paper.event.player.PlayerPostRespawnEvent`; parent: `org.bukkit.event.player.PlayerEvent`.
- Python subscription: `@bridge.on("PlayerPostRespawnEvent")`; `Events.PLAYER_POST_RESPAWN` also works.
- Cancellable: no; player: possible, depending on the runtime object.
- [Official Paper Javadoc](https://jd.papermc.io/paper/1.16.5/com/destroystokyo/paper/event/player/PlayerPostRespawnEvent.html) for meaning, trigger conditions, and Java API.

| `data` field | JSON type | Java getter | Java return type |
| --- | --- | --- | --- |
| `respawnedLocation` | location summary | `getRespawnedLocation()` | `org.bukkit.Location` |
| `bedSpawn` | boolean | `isBedSpawn()` | `boolean` |

<a id="event-org-bukkit-event-player-playerpreloginevent"></a>
### PlayerPreLoginEvent

- Java class: `org.bukkit.event.player.PlayerPreLoginEvent`; parent: `org.bukkit.event.Event`.
- Python subscription: `@bridge.on("PlayerPreLoginEvent")`; `Events.PLAYER_PRE_LOGIN` also works.
- Cancellable: no; player: no known player getter.
- [Official Paper Javadoc](https://jd.papermc.io/paper/1.16.5/org/bukkit/event/player/PlayerPreLoginEvent.html) for meaning, trigger conditions, and Java API.

| `data` field | JSON type | Java getter | Java return type |
| --- | --- | --- | --- |
| `kickMessage` | string | `getKickMessage()` | `java.lang.String` |
| `name` | string | `getName()` | `java.lang.String` |
| `result` | string | `getResult()` | `org.bukkit.event.player.PlayerPreLoginEvent$Result` |
| `uniqueId` | string | `getUniqueId()` | `java.util.UUID` |

<a id="event-io-papermc-paper-event-player-playerpurchaseevent"></a>
### PlayerPurchaseEvent

- Java class: `io.papermc.paper.event.player.PlayerPurchaseEvent`; parent: `org.bukkit.event.player.PlayerEvent`.
- Python subscription: `@bridge.on("PlayerPurchaseEvent")`; `Events.PLAYER_PURCHASE` also works.
- Cancellable: yes; player: possible, depending on the runtime object.
- [Official Paper Javadoc](https://jd.papermc.io/paper/1.16.5/io/papermc/paper/event/player/PlayerPurchaseEvent.html) for meaning, trigger conditions, and Java API.

| `data` field | JSON type | Java getter | Java return type |
| --- | --- | --- | --- |
| `rewardingExp` | boolean | `isRewardingExp()` | `boolean` |

<a id="event-org-bukkit-event-player-playerquitevent"></a>
### PlayerQuitEvent

- Java class: `org.bukkit.event.player.PlayerQuitEvent`; parent: `org.bukkit.event.player.PlayerEvent`.
- Python subscription: `@bridge.on("quit")`; `Events.PLAYER_QUIT` also works.
- Cancellable: no; player: possible, depending on the runtime object.
- [Official Paper Javadoc](https://jd.papermc.io/paper/1.16.5/org/bukkit/event/player/PlayerQuitEvent.html) for meaning, trigger conditions, and Java API.

| `data` field | JSON type | Java getter | Java return type |
| --- | --- | --- | --- |
| `quitMessage` | string | `getQuitMessage()` | `java.lang.String` |
| `reason` | string | `getReason()` | `org.bukkit.event.player.PlayerQuitEvent$QuitReason` |

<a id="event-com-destroystokyo-paper-event-player-playerreadyarrowevent"></a>
### PlayerReadyArrowEvent

- Java class: `com.destroystokyo.paper.event.player.PlayerReadyArrowEvent`; parent: `org.bukkit.event.player.PlayerEvent`.
- Python subscription: `@bridge.on("PlayerReadyArrowEvent")`; `Events.PLAYER_READY_ARROW` also works.
- Cancellable: yes; player: possible, depending on the runtime object.
- [Official Paper Javadoc](https://jd.papermc.io/paper/1.16.5/com/destroystokyo/paper/event/player/PlayerReadyArrowEvent.html) for meaning, trigger conditions, and Java API.

| `data` field | JSON type | Java getter | Java return type |
| --- | --- | --- | --- |
| `arrow` | item summary | `getArrow()` | `org.bukkit.inventory.ItemStack` |
| `bow` | item summary | `getBow()` | `org.bukkit.inventory.ItemStack` |

<a id="event-com-destroystokyo-paper-event-player-playerrecipebookclickevent"></a>
### PlayerRecipeBookClickEvent

- Java class: `com.destroystokyo.paper.event.player.PlayerRecipeBookClickEvent`; parent: `org.bukkit.event.player.PlayerEvent`.
- Python subscription: `@bridge.on("PlayerRecipeBookClickEvent")`; `Events.PLAYER_RECIPE_BOOK_CLICK` also works.
- Cancellable: yes; player: possible, depending on the runtime object.
- [Official Paper Javadoc](https://jd.papermc.io/paper/1.16.5/com/destroystokyo/paper/event/player/PlayerRecipeBookClickEvent.html) for meaning, trigger conditions, and Java API.

| `data` field | JSON type | Java getter | Java return type |
| --- | --- | --- | --- |
| `makeAll` | boolean | `isMakeAll()` | `boolean` |

<a id="event-org-bukkit-event-player-playerrecipediscoverevent"></a>
### PlayerRecipeDiscoverEvent

- Java class: `org.bukkit.event.player.PlayerRecipeDiscoverEvent`; parent: `org.bukkit.event.player.PlayerEvent`.
- Python subscription: `@bridge.on("PlayerRecipeDiscoverEvent")`; `Events.PLAYER_RECIPE_DISCOVER` also works.
- Cancellable: yes; player: possible, depending on the runtime object.
- [Official Paper Javadoc](https://jd.papermc.io/paper/1.16.5/org/bukkit/event/player/PlayerRecipeDiscoverEvent.html) for meaning, trigger conditions, and Java API.

No serializable possible `data` fields; common event fields are still sent.

<a id="event-org-bukkit-event-player-playerregisterchannelevent"></a>
### PlayerRegisterChannelEvent

- Java class: `org.bukkit.event.player.PlayerRegisterChannelEvent`; parent: `org.bukkit.event.player.PlayerChannelEvent`.
- Python subscription: `@bridge.on("PlayerRegisterChannelEvent")`; `Events.PLAYER_REGISTER_CHANNEL` also works.
- Cancellable: no; player: possible, depending on the runtime object.
- [Official Paper Javadoc](https://jd.papermc.io/paper/1.16.5/org/bukkit/event/player/PlayerRegisterChannelEvent.html) for meaning, trigger conditions, and Java API.

| `data` field | JSON type | Java getter | Java return type |
| --- | --- | --- | --- |
| `channel` | string | `getChannel()` | `java.lang.String` |

<a id="event-org-bukkit-event-player-playerresourcepackstatusevent"></a>
### PlayerResourcePackStatusEvent

- Java class: `org.bukkit.event.player.PlayerResourcePackStatusEvent`; parent: `org.bukkit.event.player.PlayerEvent`.
- Python subscription: `@bridge.on("PlayerResourcePackStatusEvent")`; `Events.PLAYER_RESOURCE_PACK_STATUS` also works.
- Cancellable: no; player: possible, depending on the runtime object.
- [Official Paper Javadoc](https://jd.papermc.io/paper/1.16.5/org/bukkit/event/player/PlayerResourcePackStatusEvent.html) for meaning, trigger conditions, and Java API.

| `data` field | JSON type | Java getter | Java return type |
| --- | --- | --- | --- |
| `hash` | string | `getHash()` | `java.lang.String` |
| `status` | string | `getStatus()` | `org.bukkit.event.player.PlayerResourcePackStatusEvent$Status` |

<a id="event-org-bukkit-event-player-playerrespawnevent"></a>
### PlayerRespawnEvent

- Java class: `org.bukkit.event.player.PlayerRespawnEvent`; parent: `org.bukkit.event.player.PlayerEvent`.
- Python subscription: `@bridge.on("PlayerRespawnEvent")`; `Events.PLAYER_RESPAWN` also works.
- Cancellable: no; player: possible, depending on the runtime object.
- [Official Paper Javadoc](https://jd.papermc.io/paper/1.16.5/org/bukkit/event/player/PlayerRespawnEvent.html) for meaning, trigger conditions, and Java API.

| `data` field | JSON type | Java getter | Java return type |
| --- | --- | --- | --- |
| `respawnLocation` | location summary | `getRespawnLocation()` | `org.bukkit.Location` |
| `anchorSpawn` | boolean | `isAnchorSpawn()` | `boolean` |
| `bedSpawn` | boolean | `isBedSpawn()` | `boolean` |

<a id="event-org-bukkit-event-player-playerriptideevent"></a>
### PlayerRiptideEvent

- Java class: `org.bukkit.event.player.PlayerRiptideEvent`; parent: `org.bukkit.event.player.PlayerEvent`.
- Python subscription: `@bridge.on("PlayerRiptideEvent")`; `Events.PLAYER_RIPTIDE` also works.
- Cancellable: no; player: possible, depending on the runtime object.
- [Official Paper Javadoc](https://jd.papermc.io/paper/1.16.5/org/bukkit/event/player/PlayerRiptideEvent.html) for meaning, trigger conditions, and Java API.

| `data` field | JSON type | Java getter | Java return type |
| --- | --- | --- | --- |
| `item` | item summary | `getItem()` | `org.bukkit.inventory.ItemStack` |

<a id="event-org-bukkit-event-player-playershearentityevent"></a>
### PlayerShearEntityEvent

- Java class: `org.bukkit.event.player.PlayerShearEntityEvent`; parent: `org.bukkit.event.player.PlayerEvent`.
- Python subscription: `@bridge.on("PlayerShearEntityEvent")`; `Events.PLAYER_SHEAR_ENTITY` also works.
- Cancellable: yes; player: possible, depending on the runtime object.
- [Official Paper Javadoc](https://jd.papermc.io/paper/1.16.5/org/bukkit/event/player/PlayerShearEntityEvent.html) for meaning, trigger conditions, and Java API.

| `data` field | JSON type | Java getter | Java return type |
| --- | --- | --- | --- |
| `entity` | entity summary | `getEntity()` | `org.bukkit.entity.Entity` |
| `hand` | string | `getHand()` | `org.bukkit.inventory.EquipmentSlot` |
| `item` | item summary | `getItem()` | `org.bukkit.inventory.ItemStack` |

<a id="event-io-papermc-paper-event-player-playersigncommandpreprocessevent"></a>
### PlayerSignCommandPreprocessEvent

- Java class: `io.papermc.paper.event.player.PlayerSignCommandPreprocessEvent`; parent: `org.bukkit.event.player.PlayerCommandPreprocessEvent`.
- Python subscription: `@bridge.on("PlayerSignCommandPreprocessEvent")`; `Events.PLAYER_SIGN_COMMAND_PREPROCESS` also works.
- Cancellable: yes; player: possible, depending on the runtime object.
- [Official Paper Javadoc](https://jd.papermc.io/paper/1.16.5/io/papermc/paper/event/player/PlayerSignCommandPreprocessEvent.html) for meaning, trigger conditions, and Java API.

| `data` field | JSON type | Java getter | Java return type |
| --- | --- | --- | --- |
| `message` | string | `getMessage()` | `java.lang.String` |

<a id="event-com-destroystokyo-paper-event-player-playerstartspectatingentityevent"></a>
### PlayerStartSpectatingEntityEvent

- Java class: `com.destroystokyo.paper.event.player.PlayerStartSpectatingEntityEvent`; parent: `org.bukkit.event.player.PlayerEvent`.
- Python subscription: `@bridge.on("PlayerStartSpectatingEntityEvent")`; `Events.PLAYER_START_SPECTATING_ENTITY` also works.
- Cancellable: yes; player: possible, depending on the runtime object.
- [Official Paper Javadoc](https://jd.papermc.io/paper/1.16.5/com/destroystokyo/paper/event/player/PlayerStartSpectatingEntityEvent.html) for meaning, trigger conditions, and Java API.

| `data` field | JSON type | Java getter | Java return type |
| --- | --- | --- | --- |
| `currentSpectatorTarget` | entity summary | `getCurrentSpectatorTarget()` | `org.bukkit.entity.Entity` |
| `newSpectatorTarget` | entity summary | `getNewSpectatorTarget()` | `org.bukkit.entity.Entity` |

<a id="event-org-bukkit-event-player-playerstatisticincrementevent"></a>
### PlayerStatisticIncrementEvent

- Java class: `org.bukkit.event.player.PlayerStatisticIncrementEvent`; parent: `org.bukkit.event.player.PlayerEvent`.
- Python subscription: `@bridge.on("PlayerStatisticIncrementEvent")`; `Events.PLAYER_STATISTIC_INCREMENT` also works.
- Cancellable: yes; player: possible, depending on the runtime object.
- [Official Paper Javadoc](https://jd.papermc.io/paper/1.16.5/org/bukkit/event/player/PlayerStatisticIncrementEvent.html) for meaning, trigger conditions, and Java API.

| `data` field | JSON type | Java getter | Java return type |
| --- | --- | --- | --- |
| `entityType` | string | `getEntityType()` | `org.bukkit.entity.EntityType` |
| `material` | string | `getMaterial()` | `org.bukkit.Material` |
| `newValue` | number | `getNewValue()` | `int` |
| `previousValue` | number | `getPreviousValue()` | `int` |
| `statistic` | string | `getStatistic()` | `org.bukkit.Statistic` |

<a id="event-io-papermc-paper-event-player-playerstonecutterrecipeselectevent"></a>
### PlayerStonecutterRecipeSelectEvent

- Java class: `io.papermc.paper.event.player.PlayerStonecutterRecipeSelectEvent`; parent: `org.bukkit.event.player.PlayerEvent`.
- Python subscription: `@bridge.on("PlayerStonecutterRecipeSelectEvent")`; `Events.PLAYER_STONECUTTER_RECIPE_SELECT` also works.
- Cancellable: yes; player: possible, depending on the runtime object.
- [Official Paper Javadoc](https://jd.papermc.io/paper/1.16.5/io/papermc/paper/event/player/PlayerStonecutterRecipeSelectEvent.html) for meaning, trigger conditions, and Java API.

No serializable possible `data` fields; common event fields are still sent.

<a id="event-com-destroystokyo-paper-event-player-playerstopspectatingentityevent"></a>
### PlayerStopSpectatingEntityEvent

- Java class: `com.destroystokyo.paper.event.player.PlayerStopSpectatingEntityEvent`; parent: `org.bukkit.event.player.PlayerEvent`.
- Python subscription: `@bridge.on("PlayerStopSpectatingEntityEvent")`; `Events.PLAYER_STOP_SPECTATING_ENTITY` also works.
- Cancellable: yes; player: possible, depending on the runtime object.
- [Official Paper Javadoc](https://jd.papermc.io/paper/1.16.5/com/destroystokyo/paper/event/player/PlayerStopSpectatingEntityEvent.html) for meaning, trigger conditions, and Java API.

| `data` field | JSON type | Java getter | Java return type |
| --- | --- | --- | --- |
| `spectatorTarget` | entity summary | `getSpectatorTarget()` | `org.bukkit.entity.Entity` |

<a id="event-org-bukkit-event-player-playerswaphanditemsevent"></a>
### PlayerSwapHandItemsEvent

- Java class: `org.bukkit.event.player.PlayerSwapHandItemsEvent`; parent: `org.bukkit.event.player.PlayerEvent`.
- Python subscription: `@bridge.on("PlayerSwapHandItemsEvent")`; `Events.PLAYER_SWAP_HAND_ITEMS` also works.
- Cancellable: yes; player: possible, depending on the runtime object.
- [Official Paper Javadoc](https://jd.papermc.io/paper/1.16.5/org/bukkit/event/player/PlayerSwapHandItemsEvent.html) for meaning, trigger conditions, and Java API.

| `data` field | JSON type | Java getter | Java return type |
| --- | --- | --- | --- |
| `mainHandItem` | item summary | `getMainHandItem()` | `org.bukkit.inventory.ItemStack` |
| `offHandItem` | item summary | `getOffHandItem()` | `org.bukkit.inventory.ItemStack` |

<a id="event-org-bukkit-event-player-playertakelecternbookevent"></a>
### PlayerTakeLecternBookEvent

- Java class: `org.bukkit.event.player.PlayerTakeLecternBookEvent`; parent: `org.bukkit.event.player.PlayerEvent`.
- Python subscription: `@bridge.on("PlayerTakeLecternBookEvent")`; `Events.PLAYER_TAKE_LECTERN_BOOK` also works.
- Cancellable: yes; player: possible, depending on the runtime object.
- [Official Paper Javadoc](https://jd.papermc.io/paper/1.16.5/org/bukkit/event/player/PlayerTakeLecternBookEvent.html) for meaning, trigger conditions, and Java API.

| `data` field | JSON type | Java getter | Java return type |
| --- | --- | --- | --- |
| `book` | item summary | `getBook()` | `org.bukkit.inventory.ItemStack` |

<a id="event-com-destroystokyo-paper-event-player-playerteleportendgatewayevent"></a>
### PlayerTeleportEndGatewayEvent

- Java class: `com.destroystokyo.paper.event.player.PlayerTeleportEndGatewayEvent`; parent: `org.bukkit.event.player.PlayerTeleportEvent`.
- Python subscription: `@bridge.on("PlayerTeleportEndGatewayEvent")`; `Events.PLAYER_TELEPORT_END_GATEWAY` also works.
- Cancellable: yes; player: possible, depending on the runtime object.
- [Official Paper Javadoc](https://jd.papermc.io/paper/1.16.5/com/destroystokyo/paper/event/player/PlayerTeleportEndGatewayEvent.html) for meaning, trigger conditions, and Java API.

| `data` field | JSON type | Java getter | Java return type |
| --- | --- | --- | --- |
| `cause` | string | `getCause()` | `org.bukkit.event.player.PlayerTeleportEvent$TeleportCause` |
| `from` | location summary | `getFrom()` | `org.bukkit.Location` |
| `to` | location summary | `getTo()` | `org.bukkit.Location` |

<a id="event-org-bukkit-event-player-playerteleportevent"></a>
### PlayerTeleportEvent

- Java class: `org.bukkit.event.player.PlayerTeleportEvent`; parent: `org.bukkit.event.player.PlayerMoveEvent`.
- Python subscription: `@bridge.on("PlayerTeleportEvent")`; `Events.PLAYER_TELEPORT` also works.
- Cancellable: yes; player: possible, depending on the runtime object.
- [Official Paper Javadoc](https://jd.papermc.io/paper/1.16.5/org/bukkit/event/player/PlayerTeleportEvent.html) for meaning, trigger conditions, and Java API.

| `data` field | JSON type | Java getter | Java return type |
| --- | --- | --- | --- |
| `cause` | string | `getCause()` | `org.bukkit.event.player.PlayerTeleportEvent$TeleportCause` |
| `from` | location summary | `getFrom()` | `org.bukkit.Location` |
| `to` | location summary | `getTo()` | `org.bukkit.Location` |

<a id="event-org-bukkit-event-player-playertoggleflightevent"></a>
### PlayerToggleFlightEvent

- Java class: `org.bukkit.event.player.PlayerToggleFlightEvent`; parent: `org.bukkit.event.player.PlayerEvent`.
- Python subscription: `@bridge.on("PlayerToggleFlightEvent")`; `Events.PLAYER_TOGGLE_FLIGHT` also works.
- Cancellable: yes; player: possible, depending on the runtime object.
- [Official Paper Javadoc](https://jd.papermc.io/paper/1.16.5/org/bukkit/event/player/PlayerToggleFlightEvent.html) for meaning, trigger conditions, and Java API.

| `data` field | JSON type | Java getter | Java return type |
| --- | --- | --- | --- |
| `flying` | boolean | `isFlying()` | `boolean` |

<a id="event-org-bukkit-event-player-playertogglesneakevent"></a>
### PlayerToggleSneakEvent

- Java class: `org.bukkit.event.player.PlayerToggleSneakEvent`; parent: `org.bukkit.event.player.PlayerEvent`.
- Python subscription: `@bridge.on("PlayerToggleSneakEvent")`; `Events.PLAYER_TOGGLE_SNEAK` also works.
- Cancellable: yes; player: possible, depending on the runtime object.
- [Official Paper Javadoc](https://jd.papermc.io/paper/1.16.5/org/bukkit/event/player/PlayerToggleSneakEvent.html) for meaning, trigger conditions, and Java API.

| `data` field | JSON type | Java getter | Java return type |
| --- | --- | --- | --- |
| `sneaking` | boolean | `isSneaking()` | `boolean` |

<a id="event-org-bukkit-event-player-playertogglesprintevent"></a>
### PlayerToggleSprintEvent

- Java class: `org.bukkit.event.player.PlayerToggleSprintEvent`; parent: `org.bukkit.event.player.PlayerEvent`.
- Python subscription: `@bridge.on("PlayerToggleSprintEvent")`; `Events.PLAYER_TOGGLE_SPRINT` also works.
- Cancellable: yes; player: possible, depending on the runtime object.
- [Official Paper Javadoc](https://jd.papermc.io/paper/1.16.5/org/bukkit/event/player/PlayerToggleSprintEvent.html) for meaning, trigger conditions, and Java API.

| `data` field | JSON type | Java getter | Java return type |
| --- | --- | --- | --- |
| `sprinting` | boolean | `isSprinting()` | `boolean` |

<a id="event-io-papermc-paper-event-player-playertradeevent"></a>
### PlayerTradeEvent

- Java class: `io.papermc.paper.event.player.PlayerTradeEvent`; parent: `io.papermc.paper.event.player.PlayerPurchaseEvent`.
- Python subscription: `@bridge.on("PlayerTradeEvent")`; `Events.PLAYER_TRADE` also works.
- Cancellable: yes; player: possible, depending on the runtime object.
- [Official Paper Javadoc](https://jd.papermc.io/paper/1.16.5/io/papermc/paper/event/player/PlayerTradeEvent.html) for meaning, trigger conditions, and Java API.

| `data` field | JSON type | Java getter | Java return type |
| --- | --- | --- | --- |
| `villager` | entity summary | `getVillager()` | `org.bukkit.entity.AbstractVillager` |
| `rewardingExp` | boolean | `isRewardingExp()` | `boolean` |

<a id="event-org-bukkit-event-player-playerunleashentityevent"></a>
### PlayerUnleashEntityEvent

- Java class: `org.bukkit.event.player.PlayerUnleashEntityEvent`; parent: `org.bukkit.event.entity.EntityUnleashEvent`.
- Python subscription: `@bridge.on("PlayerUnleashEntityEvent")`; `Events.PLAYER_UNLEASH_ENTITY` also works.
- Cancellable: yes; player: possible, depending on the runtime object.
- [Official Paper Javadoc](https://jd.papermc.io/paper/1.16.5/org/bukkit/event/player/PlayerUnleashEntityEvent.html) for meaning, trigger conditions, and Java API.

| `data` field | JSON type | Java getter | Java return type |
| --- | --- | --- | --- |
| `entity` | entity summary | `getEntity()` | `org.bukkit.entity.Entity` |
| `entityType` | string | `getEntityType()` | `org.bukkit.entity.EntityType` |
| `reason` | string | `getReason()` | `org.bukkit.event.entity.EntityUnleashEvent$UnleashReason` |
| `dropLeash` | boolean | `isDropLeash()` | `boolean` |

<a id="event-org-bukkit-event-player-playerunregisterchannelevent"></a>
### PlayerUnregisterChannelEvent

- Java class: `org.bukkit.event.player.PlayerUnregisterChannelEvent`; parent: `org.bukkit.event.player.PlayerChannelEvent`.
- Python subscription: `@bridge.on("PlayerUnregisterChannelEvent")`; `Events.PLAYER_UNREGISTER_CHANNEL` also works.
- Cancellable: no; player: possible, depending on the runtime object.
- [Official Paper Javadoc](https://jd.papermc.io/paper/1.16.5/org/bukkit/event/player/PlayerUnregisterChannelEvent.html) for meaning, trigger conditions, and Java API.

| `data` field | JSON type | Java getter | Java return type |
| --- | --- | --- | --- |
| `channel` | string | `getChannel()` | `java.lang.String` |

<a id="event-com-destroystokyo-paper-event-player-playeruseunknownentityevent"></a>
### PlayerUseUnknownEntityEvent

- Java class: `com.destroystokyo.paper.event.player.PlayerUseUnknownEntityEvent`; parent: `org.bukkit.event.player.PlayerEvent`.
- Python subscription: `@bridge.on("PlayerUseUnknownEntityEvent")`; `Events.PLAYER_USE_UNKNOWN_ENTITY` also works.
- Cancellable: no; player: possible, depending on the runtime object.
- [Official Paper Javadoc](https://jd.papermc.io/paper/1.16.5/com/destroystokyo/paper/event/player/PlayerUseUnknownEntityEvent.html) for meaning, trigger conditions, and Java API.

| `data` field | JSON type | Java getter | Java return type |
| --- | --- | --- | --- |
| `entityId` | number | `getEntityId()` | `int` |
| `hand` | string | `getHand()` | `org.bukkit.inventory.EquipmentSlot` |
| `attack` | boolean | `isAttack()` | `boolean` |

<a id="event-org-bukkit-event-player-playervelocityevent"></a>
### PlayerVelocityEvent

- Java class: `org.bukkit.event.player.PlayerVelocityEvent`; parent: `org.bukkit.event.player.PlayerEvent`.
- Python subscription: `@bridge.on("PlayerVelocityEvent")`; `Events.PLAYER_VELOCITY` also works.
- Cancellable: yes; player: possible, depending on the runtime object.
- [Official Paper Javadoc](https://jd.papermc.io/paper/1.16.5/org/bukkit/event/player/PlayerVelocityEvent.html) for meaning, trigger conditions, and Java API.

No serializable possible `data` fields; common event fields are still sent.

<a id="category-profile"></a>
## profile

| Event | Python `type` | possible `data` fields | Cancellable |
| --- | --- | ---: | --- |
| [FillProfileEvent](#event-com-destroystokyo-paper-event-profile-fillprofileevent) | `FillProfileEvent` | 0 | No |
| [LookupProfileEvent](#event-com-destroystokyo-paper-event-profile-lookupprofileevent) | `LookupProfileEvent` | 0 | No |
| [PreFillProfileEvent](#event-com-destroystokyo-paper-event-profile-prefillprofileevent) | `PreFillProfileEvent` | 0 | No |
| [PreLookupProfileEvent](#event-com-destroystokyo-paper-event-profile-prelookupprofileevent) | `PreLookupProfileEvent` | 2 | No |
| [ProfileWhitelistVerifyEvent](#event-com-destroystokyo-paper-event-profile-profilewhitelistverifyevent) | `ProfileWhitelistVerifyEvent` | 4 | No |

<a id="event-com-destroystokyo-paper-event-profile-fillprofileevent"></a>
### FillProfileEvent

- Java class: `com.destroystokyo.paper.event.profile.FillProfileEvent`; parent: `org.bukkit.event.Event`.
- Python subscription: `@bridge.on("FillProfileEvent")`; `Events.FILL_PROFILE` also works.
- Cancellable: no; player: no known player getter.
- [Official Paper Javadoc](https://jd.papermc.io/paper/1.16.5/com/destroystokyo/paper/event/profile/FillProfileEvent.html) for meaning, trigger conditions, and Java API.

No serializable possible `data` fields; common event fields are still sent.

<a id="event-com-destroystokyo-paper-event-profile-lookupprofileevent"></a>
### LookupProfileEvent

- Java class: `com.destroystokyo.paper.event.profile.LookupProfileEvent`; parent: `org.bukkit.event.Event`.
- Python subscription: `@bridge.on("LookupProfileEvent")`; `Events.LOOKUP_PROFILE` also works.
- Cancellable: no; player: no known player getter.
- [Official Paper Javadoc](https://jd.papermc.io/paper/1.16.5/com/destroystokyo/paper/event/profile/LookupProfileEvent.html) for meaning, trigger conditions, and Java API.

No serializable possible `data` fields; common event fields are still sent.

<a id="event-com-destroystokyo-paper-event-profile-prefillprofileevent"></a>
### PreFillProfileEvent

- Java class: `com.destroystokyo.paper.event.profile.PreFillProfileEvent`; parent: `org.bukkit.event.Event`.
- Python subscription: `@bridge.on("PreFillProfileEvent")`; `Events.PRE_FILL_PROFILE` also works.
- Cancellable: no; player: no known player getter.
- [Official Paper Javadoc](https://jd.papermc.io/paper/1.16.5/com/destroystokyo/paper/event/profile/PreFillProfileEvent.html) for meaning, trigger conditions, and Java API.

No serializable possible `data` fields; common event fields are still sent.

<a id="event-com-destroystokyo-paper-event-profile-prelookupprofileevent"></a>
### PreLookupProfileEvent

- Java class: `com.destroystokyo.paper.event.profile.PreLookupProfileEvent`; parent: `org.bukkit.event.Event`.
- Python subscription: `@bridge.on("PreLookupProfileEvent")`; `Events.PRE_LOOKUP_PROFILE` also works.
- Cancellable: no; player: no known player getter.
- [Official Paper Javadoc](https://jd.papermc.io/paper/1.16.5/com/destroystokyo/paper/event/profile/PreLookupProfileEvent.html) for meaning, trigger conditions, and Java API.

| `data` field | JSON type | Java getter | Java return type |
| --- | --- | --- | --- |
| `name` | string | `getName()` | `java.lang.String` |
| `uUID` | string | `getUUID()` | `java.util.UUID` |

<a id="event-com-destroystokyo-paper-event-profile-profilewhitelistverifyevent"></a>
### ProfileWhitelistVerifyEvent

- Java class: `com.destroystokyo.paper.event.profile.ProfileWhitelistVerifyEvent`; parent: `org.bukkit.event.Event`.
- Python subscription: `@bridge.on("ProfileWhitelistVerifyEvent")`; `Events.PROFILE_WHITELIST_VERIFY` also works.
- Cancellable: no; player: no known player getter.
- [Official Paper Javadoc](https://jd.papermc.io/paper/1.16.5/com/destroystokyo/paper/event/profile/ProfileWhitelistVerifyEvent.html) for meaning, trigger conditions, and Java API.

| `data` field | JSON type | Java getter | Java return type |
| --- | --- | --- | --- |
| `kickMessage` | string | `getKickMessage()` | `java.lang.String` |
| `op` | boolean | `isOp()` | `boolean` |
| `whitelistEnabled` | boolean | `isWhitelistEnabled()` | `boolean` |
| `whitelisted` | boolean | `isWhitelisted()` | `boolean` |

<a id="category-raid"></a>
## raid

| Event | Python `type` | possible `data` fields | Cancellable |
| --- | --- | ---: | --- |
| [RaidFinishEvent](#event-org-bukkit-event-raid-raidfinishevent) | `RaidFinishEvent` | 1 | No |
| [RaidSpawnWaveEvent](#event-org-bukkit-event-raid-raidspawnwaveevent) | `RaidSpawnWaveEvent` | 2 | No |
| [RaidStopEvent](#event-org-bukkit-event-raid-raidstopevent) | `RaidStopEvent` | 2 | No |
| [RaidTriggerEvent](#event-org-bukkit-event-raid-raidtriggerevent) | `RaidTriggerEvent` | 1 | Yes |

<a id="event-org-bukkit-event-raid-raidfinishevent"></a>
### RaidFinishEvent

- Java class: `org.bukkit.event.raid.RaidFinishEvent`; parent: `org.bukkit.event.raid.RaidEvent`.
- Python subscription: `@bridge.on("RaidFinishEvent")`; `Events.RAID_FINISH` also works.
- Cancellable: no; player: no known player getter.
- [Official Paper Javadoc](https://jd.papermc.io/paper/1.16.5/org/bukkit/event/raid/RaidFinishEvent.html) for meaning, trigger conditions, and Java API.

| `data` field | JSON type | Java getter | Java return type |
| --- | --- | --- | --- |
| `world` | world summary | `getWorld()` | `org.bukkit.World` |

<a id="event-org-bukkit-event-raid-raidspawnwaveevent"></a>
### RaidSpawnWaveEvent

- Java class: `org.bukkit.event.raid.RaidSpawnWaveEvent`; parent: `org.bukkit.event.raid.RaidEvent`.
- Python subscription: `@bridge.on("RaidSpawnWaveEvent")`; `Events.RAID_SPAWN_WAVE` also works.
- Cancellable: no; player: no known player getter.
- [Official Paper Javadoc](https://jd.papermc.io/paper/1.16.5/org/bukkit/event/raid/RaidSpawnWaveEvent.html) for meaning, trigger conditions, and Java API.

| `data` field | JSON type | Java getter | Java return type |
| --- | --- | --- | --- |
| `patrolLeader` | entity summary | `getPatrolLeader()` | `org.bukkit.entity.Raider` |
| `world` | world summary | `getWorld()` | `org.bukkit.World` |

<a id="event-org-bukkit-event-raid-raidstopevent"></a>
### RaidStopEvent

- Java class: `org.bukkit.event.raid.RaidStopEvent`; parent: `org.bukkit.event.raid.RaidEvent`.
- Python subscription: `@bridge.on("RaidStopEvent")`; `Events.RAID_STOP` also works.
- Cancellable: no; player: no known player getter.
- [Official Paper Javadoc](https://jd.papermc.io/paper/1.16.5/org/bukkit/event/raid/RaidStopEvent.html) for meaning, trigger conditions, and Java API.

| `data` field | JSON type | Java getter | Java return type |
| --- | --- | --- | --- |
| `reason` | string | `getReason()` | `org.bukkit.event.raid.RaidStopEvent$Reason` |
| `world` | world summary | `getWorld()` | `org.bukkit.World` |

<a id="event-org-bukkit-event-raid-raidtriggerevent"></a>
### RaidTriggerEvent

- Java class: `org.bukkit.event.raid.RaidTriggerEvent`; parent: `org.bukkit.event.raid.RaidEvent`.
- Python subscription: `@bridge.on("RaidTriggerEvent")`; `Events.RAID_TRIGGER` also works.
- Cancellable: yes; player: possible, depending on the runtime object.
- [Official Paper Javadoc](https://jd.papermc.io/paper/1.16.5/org/bukkit/event/raid/RaidTriggerEvent.html) for meaning, trigger conditions, and Java API.

| `data` field | JSON type | Java getter | Java return type |
| --- | --- | --- | --- |
| `world` | world summary | `getWorld()` | `org.bukkit.World` |

<a id="category-server"></a>
## server

| Event | Python `type` | possible `data` fields | Cancellable |
| --- | --- | ---: | --- |
| [AsyncTabCompleteEvent](#event-com-destroystokyo-paper-event-server-asynctabcompleteevent) | `AsyncTabCompleteEvent` | 4 | Yes |
| [BroadcastMessageEvent](#event-org-bukkit-event-server-broadcastmessageevent) | `BroadcastMessageEvent` | 1 | Yes |
| [GS4QueryEvent](#event-com-destroystokyo-paper-event-server-gs4queryevent) | `GS4QueryEvent` | 1 | No |
| [MapInitializeEvent](#event-org-bukkit-event-server-mapinitializeevent) | `MapInitializeEvent` | 0 | No |
| [PaperServerListPingEvent](#event-com-destroystokyo-paper-event-server-paperserverlistpingevent) | `PaperServerListPingEvent` | 5 | Yes |
| [PluginDisableEvent](#event-org-bukkit-event-server-plugindisableevent) | `PluginDisableEvent` | 0 | No |
| [PluginEnableEvent](#event-org-bukkit-event-server-pluginenableevent) | `PluginEnableEvent` | 0 | No |
| [RemoteServerCommandEvent](#event-org-bukkit-event-server-remoteservercommandevent) | `RemoteServerCommandEvent` | 1 | Yes |
| [ServerCommandEvent](#event-org-bukkit-event-server-servercommandevent) | `ServerCommandEvent` | 1 | Yes |
| [ServerExceptionEvent](#event-com-destroystokyo-paper-event-server-serverexceptionevent) | `ServerExceptionEvent` | 0 | No |
| [ServerListPingEvent](#event-org-bukkit-event-server-serverlistpingevent) | `ServerListPingEvent` | 3 | No |
| [ServerLoadEvent](#event-org-bukkit-event-server-serverloadevent) | `ServerLoadEvent` | 1 | No |
| [ServerResourcesReloadedEvent](#event-io-papermc-paper-event-server-serverresourcesreloadedevent) | `ServerResourcesReloadedEvent` | 1 | No |
| [ServerTickEndEvent](#event-com-destroystokyo-paper-event-server-servertickendevent) | `ServerTickEndEvent` | 3 | No |
| [ServerTickStartEvent](#event-com-destroystokyo-paper-event-server-servertickstartevent) | `ServerTickStartEvent` | 1 | No |
| [ServiceRegisterEvent](#event-org-bukkit-event-server-serviceregisterevent) | `ServiceRegisterEvent` | 0 | No |
| [ServiceUnregisterEvent](#event-org-bukkit-event-server-serviceunregisterevent) | `ServiceUnregisterEvent` | 0 | No |
| [TabCompleteEvent](#event-org-bukkit-event-server-tabcompleteevent) | `TabCompleteEvent` | 3 | Yes |
| [WhitelistToggleEvent](#event-com-destroystokyo-paper-event-server-whitelisttoggleevent) | `WhitelistToggleEvent` | 1 | No |

<a id="event-com-destroystokyo-paper-event-server-asynctabcompleteevent"></a>
### AsyncTabCompleteEvent

- Java class: `com.destroystokyo.paper.event.server.AsyncTabCompleteEvent`; parent: `org.bukkit.event.Event`.
- Python subscription: `@bridge.on("AsyncTabCompleteEvent")`; `Events.ASYNC_TAB_COMPLETE` also works.
- Cancellable: yes; player: no known player getter.
- [Official Paper Javadoc](https://jd.papermc.io/paper/1.16.5/com/destroystokyo/paper/event/server/AsyncTabCompleteEvent.html) for meaning, trigger conditions, and Java API.

| `data` field | JSON type | Java getter | Java return type |
| --- | --- | --- | --- |
| `buffer` | string | `getBuffer()` | `java.lang.String` |
| `location` | location summary | `getLocation()` | `org.bukkit.Location` |
| `command` | boolean | `isCommand()` | `boolean` |
| `handled` | boolean | `isHandled()` | `boolean` |

<a id="event-org-bukkit-event-server-broadcastmessageevent"></a>
### BroadcastMessageEvent

- Java class: `org.bukkit.event.server.BroadcastMessageEvent`; parent: `org.bukkit.event.server.ServerEvent`.
- Python subscription: `@bridge.on("BroadcastMessageEvent")`; `Events.BROADCAST_MESSAGE` also works.
- Cancellable: yes; player: no known player getter.
- [Official Paper Javadoc](https://jd.papermc.io/paper/1.16.5/org/bukkit/event/server/BroadcastMessageEvent.html) for meaning, trigger conditions, and Java API.

| `data` field | JSON type | Java getter | Java return type |
| --- | --- | --- | --- |
| `message` | string | `getMessage()` | `java.lang.String` |

<a id="event-com-destroystokyo-paper-event-server-gs4queryevent"></a>
### GS4QueryEvent

- Java class: `com.destroystokyo.paper.event.server.GS4QueryEvent`; parent: `org.bukkit.event.Event`.
- Python subscription: `@bridge.on("GS4QueryEvent")`; `Events.GS4_QUERY` also works.
- Cancellable: no; player: no known player getter.
- [Official Paper Javadoc](https://jd.papermc.io/paper/1.16.5/com/destroystokyo/paper/event/server/GS4QueryEvent.html) for meaning, trigger conditions, and Java API.

| `data` field | JSON type | Java getter | Java return type |
| --- | --- | --- | --- |
| `queryType` | string | `getQueryType()` | `com.destroystokyo.paper.event.server.GS4QueryEvent$QueryType` |

<a id="event-org-bukkit-event-server-mapinitializeevent"></a>
### MapInitializeEvent

- Java class: `org.bukkit.event.server.MapInitializeEvent`; parent: `org.bukkit.event.server.ServerEvent`.
- Python subscription: `@bridge.on("MapInitializeEvent")`; `Events.MAP_INITIALIZE` also works.
- Cancellable: no; player: no known player getter.
- [Official Paper Javadoc](https://jd.papermc.io/paper/1.16.5/org/bukkit/event/server/MapInitializeEvent.html) for meaning, trigger conditions, and Java API.

No serializable possible `data` fields; common event fields are still sent.

<a id="event-com-destroystokyo-paper-event-server-paperserverlistpingevent"></a>
### PaperServerListPingEvent

- Java class: `com.destroystokyo.paper.event.server.PaperServerListPingEvent`; parent: `org.bukkit.event.server.ServerListPingEvent`.
- Python subscription: `@bridge.on("PaperServerListPingEvent")`; `Events.PAPER_SERVER_LIST_PING` also works.
- Cancellable: yes; player: no known player getter.
- [Official Paper Javadoc](https://jd.papermc.io/paper/1.16.5/com/destroystokyo/paper/event/server/PaperServerListPingEvent.html) for meaning, trigger conditions, and Java API.

| `data` field | JSON type | Java getter | Java return type |
| --- | --- | --- | --- |
| `maxPlayers` | number | `getMaxPlayers()` | `int` |
| `motd` | string | `getMotd()` | `java.lang.String` |
| `numPlayers` | number | `getNumPlayers()` | `int` |
| `protocolVersion` | number | `getProtocolVersion()` | `int` |
| `version` | string | `getVersion()` | `java.lang.String` |

<a id="event-org-bukkit-event-server-plugindisableevent"></a>
### PluginDisableEvent

- Java class: `org.bukkit.event.server.PluginDisableEvent`; parent: `org.bukkit.event.server.PluginEvent`.
- Python subscription: `@bridge.on("PluginDisableEvent")`; `Events.PLUGIN_DISABLE` also works.
- Cancellable: no; player: no known player getter.
- [Official Paper Javadoc](https://jd.papermc.io/paper/1.16.5/org/bukkit/event/server/PluginDisableEvent.html) for meaning, trigger conditions, and Java API.

No serializable possible `data` fields; common event fields are still sent.

<a id="event-org-bukkit-event-server-pluginenableevent"></a>
### PluginEnableEvent

- Java class: `org.bukkit.event.server.PluginEnableEvent`; parent: `org.bukkit.event.server.PluginEvent`.
- Python subscription: `@bridge.on("PluginEnableEvent")`; `Events.PLUGIN_ENABLE` also works.
- Cancellable: no; player: no known player getter.
- [Official Paper Javadoc](https://jd.papermc.io/paper/1.16.5/org/bukkit/event/server/PluginEnableEvent.html) for meaning, trigger conditions, and Java API.

No serializable possible `data` fields; common event fields are still sent.

<a id="event-org-bukkit-event-server-remoteservercommandevent"></a>
### RemoteServerCommandEvent

- Java class: `org.bukkit.event.server.RemoteServerCommandEvent`; parent: `org.bukkit.event.server.ServerCommandEvent`.
- Python subscription: `@bridge.on("RemoteServerCommandEvent")`; `Events.REMOTE_SERVER_COMMAND` also works.
- Cancellable: yes; player: no known player getter.
- [Official Paper Javadoc](https://jd.papermc.io/paper/1.16.5/org/bukkit/event/server/RemoteServerCommandEvent.html) for meaning, trigger conditions, and Java API.

| `data` field | JSON type | Java getter | Java return type |
| --- | --- | --- | --- |
| `command` | string | `getCommand()` | `java.lang.String` |

<a id="event-org-bukkit-event-server-servercommandevent"></a>
### ServerCommandEvent

- Java class: `org.bukkit.event.server.ServerCommandEvent`; parent: `org.bukkit.event.server.ServerEvent`.
- Python subscription: `@bridge.on("ServerCommandEvent")`; `Events.SERVER_COMMAND` also works.
- Cancellable: yes; player: no known player getter.
- [Official Paper Javadoc](https://jd.papermc.io/paper/1.16.5/org/bukkit/event/server/ServerCommandEvent.html) for meaning, trigger conditions, and Java API.

| `data` field | JSON type | Java getter | Java return type |
| --- | --- | --- | --- |
| `command` | string | `getCommand()` | `java.lang.String` |

<a id="event-com-destroystokyo-paper-event-server-serverexceptionevent"></a>
### ServerExceptionEvent

- Java class: `com.destroystokyo.paper.event.server.ServerExceptionEvent`; parent: `org.bukkit.event.Event`.
- Python subscription: `@bridge.on("ServerExceptionEvent")`; `Events.SERVER_EXCEPTION` also works.
- Cancellable: no; player: no known player getter.
- [Official Paper Javadoc](https://jd.papermc.io/paper/1.16.5/com/destroystokyo/paper/event/server/ServerExceptionEvent.html) for meaning, trigger conditions, and Java API.

No serializable possible `data` fields; common event fields are still sent.

<a id="event-org-bukkit-event-server-serverlistpingevent"></a>
### ServerListPingEvent

- Java class: `org.bukkit.event.server.ServerListPingEvent`; parent: `org.bukkit.event.server.ServerEvent`.
- Python subscription: `@bridge.on("ServerListPingEvent")`; `Events.SERVER_LIST_PING` also works.
- Cancellable: no; player: no known player getter.
- [Official Paper Javadoc](https://jd.papermc.io/paper/1.16.5/org/bukkit/event/server/ServerListPingEvent.html) for meaning, trigger conditions, and Java API.

| `data` field | JSON type | Java getter | Java return type |
| --- | --- | --- | --- |
| `maxPlayers` | number | `getMaxPlayers()` | `int` |
| `motd` | string | `getMotd()` | `java.lang.String` |
| `numPlayers` | number | `getNumPlayers()` | `int` |

<a id="event-org-bukkit-event-server-serverloadevent"></a>
### ServerLoadEvent

- Java class: `org.bukkit.event.server.ServerLoadEvent`; parent: `org.bukkit.event.server.ServerEvent`.
- Python subscription: `@bridge.on("ServerLoadEvent")`; `Events.SERVER_LOAD` also works.
- Cancellable: no; player: no known player getter.
- [Official Paper Javadoc](https://jd.papermc.io/paper/1.16.5/org/bukkit/event/server/ServerLoadEvent.html) for meaning, trigger conditions, and Java API.

| `data` field | JSON type | Java getter | Java return type |
| --- | --- | --- | --- |
| `type` | string | `getType()` | `org.bukkit.event.server.ServerLoadEvent$LoadType` |

<a id="event-io-papermc-paper-event-server-serverresourcesreloadedevent"></a>
### ServerResourcesReloadedEvent

- Java class: `io.papermc.paper.event.server.ServerResourcesReloadedEvent`; parent: `org.bukkit.event.server.ServerEvent`.
- Python subscription: `@bridge.on("ServerResourcesReloadedEvent")`; `Events.SERVER_RESOURCES_RELOADED` also works.
- Cancellable: no; player: no known player getter.
- [Official Paper Javadoc](https://jd.papermc.io/paper/1.16.5/io/papermc/paper/event/server/ServerResourcesReloadedEvent.html) for meaning, trigger conditions, and Java API.

| `data` field | JSON type | Java getter | Java return type |
| --- | --- | --- | --- |
| `cause` | string | `getCause()` | `io.papermc.paper.event.server.ServerResourcesReloadedEvent$Cause` |

<a id="event-com-destroystokyo-paper-event-server-servertickendevent"></a>
### ServerTickEndEvent

- Java class: `com.destroystokyo.paper.event.server.ServerTickEndEvent`; parent: `org.bukkit.event.Event`.
- Python subscription: `@bridge.on("ServerTickEndEvent")`; `Events.SERVER_TICK_END` also works.
- Cancellable: no; player: no known player getter.
- [Official Paper Javadoc](https://jd.papermc.io/paper/1.16.5/com/destroystokyo/paper/event/server/ServerTickEndEvent.html) for meaning, trigger conditions, and Java API.

| `data` field | JSON type | Java getter | Java return type |
| --- | --- | --- | --- |
| `tickDuration` | number | `getTickDuration()` | `double` |
| `tickNumber` | number | `getTickNumber()` | `int` |
| `timeRemaining` | number | `getTimeRemaining()` | `long` |

<a id="event-com-destroystokyo-paper-event-server-servertickstartevent"></a>
### ServerTickStartEvent

- Java class: `com.destroystokyo.paper.event.server.ServerTickStartEvent`; parent: `org.bukkit.event.Event`.
- Python subscription: `@bridge.on("ServerTickStartEvent")`; `Events.SERVER_TICK_START` also works.
- Cancellable: no; player: no known player getter.
- [Official Paper Javadoc](https://jd.papermc.io/paper/1.16.5/com/destroystokyo/paper/event/server/ServerTickStartEvent.html) for meaning, trigger conditions, and Java API.

| `data` field | JSON type | Java getter | Java return type |
| --- | --- | --- | --- |
| `tickNumber` | number | `getTickNumber()` | `int` |

<a id="event-org-bukkit-event-server-serviceregisterevent"></a>
### ServiceRegisterEvent

- Java class: `org.bukkit.event.server.ServiceRegisterEvent`; parent: `org.bukkit.event.server.ServiceEvent`.
- Python subscription: `@bridge.on("ServiceRegisterEvent")`; `Events.SERVICE_REGISTER` also works.
- Cancellable: no; player: no known player getter.
- [Official Paper Javadoc](https://jd.papermc.io/paper/1.16.5/org/bukkit/event/server/ServiceRegisterEvent.html) for meaning, trigger conditions, and Java API.

No serializable possible `data` fields; common event fields are still sent.

<a id="event-org-bukkit-event-server-serviceunregisterevent"></a>
### ServiceUnregisterEvent

- Java class: `org.bukkit.event.server.ServiceUnregisterEvent`; parent: `org.bukkit.event.server.ServiceEvent`.
- Python subscription: `@bridge.on("ServiceUnregisterEvent")`; `Events.SERVICE_UNREGISTER` also works.
- Cancellable: no; player: no known player getter.
- [Official Paper Javadoc](https://jd.papermc.io/paper/1.16.5/org/bukkit/event/server/ServiceUnregisterEvent.html) for meaning, trigger conditions, and Java API.

No serializable possible `data` fields; common event fields are still sent.

<a id="event-org-bukkit-event-server-tabcompleteevent"></a>
### TabCompleteEvent

- Java class: `org.bukkit.event.server.TabCompleteEvent`; parent: `org.bukkit.event.Event`.
- Python subscription: `@bridge.on("TabCompleteEvent")`; `Events.TAB_COMPLETE` also works.
- Cancellable: yes; player: no known player getter.
- [Official Paper Javadoc](https://jd.papermc.io/paper/1.16.5/org/bukkit/event/server/TabCompleteEvent.html) for meaning, trigger conditions, and Java API.

| `data` field | JSON type | Java getter | Java return type |
| --- | --- | --- | --- |
| `buffer` | string | `getBuffer()` | `java.lang.String` |
| `location` | location summary | `getLocation()` | `org.bukkit.Location` |
| `command` | boolean | `isCommand()` | `boolean` |

<a id="event-com-destroystokyo-paper-event-server-whitelisttoggleevent"></a>
### WhitelistToggleEvent

- Java class: `com.destroystokyo.paper.event.server.WhitelistToggleEvent`; parent: `org.bukkit.event.Event`.
- Python subscription: `@bridge.on("WhitelistToggleEvent")`; `Events.WHITELIST_TOGGLE` also works.
- Cancellable: no; player: no known player getter.
- [Official Paper Javadoc](https://jd.papermc.io/paper/1.16.5/com/destroystokyo/paper/event/server/WhitelistToggleEvent.html) for meaning, trigger conditions, and Java API.

| `data` field | JSON type | Java getter | Java return type |
| --- | --- | --- | --- |
| `enabled` | boolean | `isEnabled()` | `boolean` |

<a id="category-vehicle"></a>
## vehicle

| Event | Python `type` | possible `data` fields | Cancellable |
| --- | --- | ---: | --- |
| [VehicleBlockCollisionEvent](#event-org-bukkit-event-vehicle-vehicleblockcollisionevent) | `VehicleBlockCollisionEvent` | 2 | No |
| [VehicleCreateEvent](#event-org-bukkit-event-vehicle-vehiclecreateevent) | `VehicleCreateEvent` | 1 | Yes |
| [VehicleDamageEvent](#event-org-bukkit-event-vehicle-vehicledamageevent) | `VehicleDamageEvent` | 3 | Yes |
| [VehicleDestroyEvent](#event-org-bukkit-event-vehicle-vehicledestroyevent) | `VehicleDestroyEvent` | 2 | Yes |
| [VehicleEnterEvent](#event-org-bukkit-event-vehicle-vehicleenterevent) | `VehicleEnterEvent` | 2 | Yes |
| [VehicleEntityCollisionEvent](#event-org-bukkit-event-vehicle-vehicleentitycollisionevent) | `VehicleEntityCollisionEvent` | 4 | Yes |
| [VehicleExitEvent](#event-org-bukkit-event-vehicle-vehicleexitevent) | `VehicleExitEvent` | 3 | Yes |
| [VehicleMoveEvent](#event-org-bukkit-event-vehicle-vehiclemoveevent) | `VehicleMoveEvent` | 3 | No |
| [VehicleUpdateEvent](#event-org-bukkit-event-vehicle-vehicleupdateevent) | `VehicleUpdateEvent` | 1 | No |

<a id="event-org-bukkit-event-vehicle-vehicleblockcollisionevent"></a>
### VehicleBlockCollisionEvent

- Java class: `org.bukkit.event.vehicle.VehicleBlockCollisionEvent`; parent: `org.bukkit.event.vehicle.VehicleCollisionEvent`.
- Python subscription: `@bridge.on("VehicleBlockCollisionEvent")`; `Events.VEHICLE_BLOCK_COLLISION` also works.
- Cancellable: no; player: no known player getter.
- [Official Paper Javadoc](https://jd.papermc.io/paper/1.16.5/org/bukkit/event/vehicle/VehicleBlockCollisionEvent.html) for meaning, trigger conditions, and Java API.

| `data` field | JSON type | Java getter | Java return type |
| --- | --- | --- | --- |
| `block` | block summary | `getBlock()` | `org.bukkit.block.Block` |
| `vehicle` | entity summary | `getVehicle()` | `org.bukkit.entity.Vehicle` |

<a id="event-org-bukkit-event-vehicle-vehiclecreateevent"></a>
### VehicleCreateEvent

- Java class: `org.bukkit.event.vehicle.VehicleCreateEvent`; parent: `org.bukkit.event.vehicle.VehicleEvent`.
- Python subscription: `@bridge.on("VehicleCreateEvent")`; `Events.VEHICLE_CREATE` also works.
- Cancellable: yes; player: no known player getter.
- [Official Paper Javadoc](https://jd.papermc.io/paper/1.16.5/org/bukkit/event/vehicle/VehicleCreateEvent.html) for meaning, trigger conditions, and Java API.

| `data` field | JSON type | Java getter | Java return type |
| --- | --- | --- | --- |
| `vehicle` | entity summary | `getVehicle()` | `org.bukkit.entity.Vehicle` |

<a id="event-org-bukkit-event-vehicle-vehicledamageevent"></a>
### VehicleDamageEvent

- Java class: `org.bukkit.event.vehicle.VehicleDamageEvent`; parent: `org.bukkit.event.vehicle.VehicleEvent`.
- Python subscription: `@bridge.on("VehicleDamageEvent")`; `Events.VEHICLE_DAMAGE` also works.
- Cancellable: yes; player: no known player getter.
- [Official Paper Javadoc](https://jd.papermc.io/paper/1.16.5/org/bukkit/event/vehicle/VehicleDamageEvent.html) for meaning, trigger conditions, and Java API.

| `data` field | JSON type | Java getter | Java return type |
| --- | --- | --- | --- |
| `attacker` | entity summary | `getAttacker()` | `org.bukkit.entity.Entity` |
| `damage` | number | `getDamage()` | `double` |
| `vehicle` | entity summary | `getVehicle()` | `org.bukkit.entity.Vehicle` |

<a id="event-org-bukkit-event-vehicle-vehicledestroyevent"></a>
### VehicleDestroyEvent

- Java class: `org.bukkit.event.vehicle.VehicleDestroyEvent`; parent: `org.bukkit.event.vehicle.VehicleEvent`.
- Python subscription: `@bridge.on("VehicleDestroyEvent")`; `Events.VEHICLE_DESTROY` also works.
- Cancellable: yes; player: no known player getter.
- [Official Paper Javadoc](https://jd.papermc.io/paper/1.16.5/org/bukkit/event/vehicle/VehicleDestroyEvent.html) for meaning, trigger conditions, and Java API.

| `data` field | JSON type | Java getter | Java return type |
| --- | --- | --- | --- |
| `attacker` | entity summary | `getAttacker()` | `org.bukkit.entity.Entity` |
| `vehicle` | entity summary | `getVehicle()` | `org.bukkit.entity.Vehicle` |

<a id="event-org-bukkit-event-vehicle-vehicleenterevent"></a>
### VehicleEnterEvent

- Java class: `org.bukkit.event.vehicle.VehicleEnterEvent`; parent: `org.bukkit.event.vehicle.VehicleEvent`.
- Python subscription: `@bridge.on("VehicleEnterEvent")`; `Events.VEHICLE_ENTER` also works.
- Cancellable: yes; player: no known player getter.
- [Official Paper Javadoc](https://jd.papermc.io/paper/1.16.5/org/bukkit/event/vehicle/VehicleEnterEvent.html) for meaning, trigger conditions, and Java API.

| `data` field | JSON type | Java getter | Java return type |
| --- | --- | --- | --- |
| `entered` | entity summary | `getEntered()` | `org.bukkit.entity.Entity` |
| `vehicle` | entity summary | `getVehicle()` | `org.bukkit.entity.Vehicle` |

<a id="event-org-bukkit-event-vehicle-vehicleentitycollisionevent"></a>
### VehicleEntityCollisionEvent

- Java class: `org.bukkit.event.vehicle.VehicleEntityCollisionEvent`; parent: `org.bukkit.event.vehicle.VehicleCollisionEvent`.
- Python subscription: `@bridge.on("VehicleEntityCollisionEvent")`; `Events.VEHICLE_ENTITY_COLLISION` also works.
- Cancellable: yes; player: possible, depending on the runtime object.
- [Official Paper Javadoc](https://jd.papermc.io/paper/1.16.5/org/bukkit/event/vehicle/VehicleEntityCollisionEvent.html) for meaning, trigger conditions, and Java API.

| `data` field | JSON type | Java getter | Java return type |
| --- | --- | --- | --- |
| `entity` | entity summary | `getEntity()` | `org.bukkit.entity.Entity` |
| `vehicle` | entity summary | `getVehicle()` | `org.bukkit.entity.Vehicle` |
| `collisionCancelled` | boolean | `isCollisionCancelled()` | `boolean` |
| `pickupCancelled` | boolean | `isPickupCancelled()` | `boolean` |

<a id="event-org-bukkit-event-vehicle-vehicleexitevent"></a>
### VehicleExitEvent

- Java class: `org.bukkit.event.vehicle.VehicleExitEvent`; parent: `org.bukkit.event.vehicle.VehicleEvent`.
- Python subscription: `@bridge.on("VehicleExitEvent")`; `Events.VEHICLE_EXIT` also works.
- Cancellable: yes; player: no known player getter.
- [Official Paper Javadoc](https://jd.papermc.io/paper/1.16.5/org/bukkit/event/vehicle/VehicleExitEvent.html) for meaning, trigger conditions, and Java API.

| `data` field | JSON type | Java getter | Java return type |
| --- | --- | --- | --- |
| `exited` | entity summary | `getExited()` | `org.bukkit.entity.LivingEntity` |
| `vehicle` | entity summary | `getVehicle()` | `org.bukkit.entity.Vehicle` |
| `cancellable` | boolean | `isCancellable()` | `boolean` |

<a id="event-org-bukkit-event-vehicle-vehiclemoveevent"></a>
### VehicleMoveEvent

- Java class: `org.bukkit.event.vehicle.VehicleMoveEvent`; parent: `org.bukkit.event.vehicle.VehicleEvent`.
- Python subscription: `@bridge.on("VehicleMoveEvent")`; `Events.VEHICLE_MOVE` also works.
- Cancellable: no; player: no known player getter.
- [Official Paper Javadoc](https://jd.papermc.io/paper/1.16.5/org/bukkit/event/vehicle/VehicleMoveEvent.html) for meaning, trigger conditions, and Java API.

| `data` field | JSON type | Java getter | Java return type |
| --- | --- | --- | --- |
| `from` | location summary | `getFrom()` | `org.bukkit.Location` |
| `to` | location summary | `getTo()` | `org.bukkit.Location` |
| `vehicle` | entity summary | `getVehicle()` | `org.bukkit.entity.Vehicle` |

<a id="event-org-bukkit-event-vehicle-vehicleupdateevent"></a>
### VehicleUpdateEvent

- Java class: `org.bukkit.event.vehicle.VehicleUpdateEvent`; parent: `org.bukkit.event.vehicle.VehicleEvent`.
- Python subscription: `@bridge.on("VehicleUpdateEvent")`; `Events.VEHICLE_UPDATE` also works.
- Cancellable: no; player: no known player getter.
- [Official Paper Javadoc](https://jd.papermc.io/paper/1.16.5/org/bukkit/event/vehicle/VehicleUpdateEvent.html) for meaning, trigger conditions, and Java API.

| `data` field | JSON type | Java getter | Java return type |
| --- | --- | --- | --- |
| `vehicle` | entity summary | `getVehicle()` | `org.bukkit.entity.Vehicle` |

<a id="category-weather"></a>
## weather

| Event | Python `type` | possible `data` fields | Cancellable |
| --- | --- | ---: | --- |
| [LightningStrikeEvent](#event-org-bukkit-event-weather-lightningstrikeevent) | `LightningStrikeEvent` | 3 | Yes |
| [ThunderChangeEvent](#event-org-bukkit-event-weather-thunderchangeevent) | `ThunderChangeEvent` | 2 | Yes |
| [WeatherChangeEvent](#event-org-bukkit-event-weather-weatherchangeevent) | `WeatherChangeEvent` | 2 | Yes |

<a id="event-org-bukkit-event-weather-lightningstrikeevent"></a>
### LightningStrikeEvent

- Java class: `org.bukkit.event.weather.LightningStrikeEvent`; parent: `org.bukkit.event.weather.WeatherEvent`.
- Python subscription: `@bridge.on("LightningStrikeEvent")`; `Events.LIGHTNING_STRIKE` also works.
- Cancellable: yes; player: no known player getter.
- [Official Paper Javadoc](https://jd.papermc.io/paper/1.16.5/org/bukkit/event/weather/LightningStrikeEvent.html) for meaning, trigger conditions, and Java API.

| `data` field | JSON type | Java getter | Java return type |
| --- | --- | --- | --- |
| `cause` | string | `getCause()` | `org.bukkit.event.weather.LightningStrikeEvent$Cause` |
| `lightning` | entity summary | `getLightning()` | `org.bukkit.entity.LightningStrike` |
| `world` | world summary | `getWorld()` | `org.bukkit.World` |

<a id="event-org-bukkit-event-weather-thunderchangeevent"></a>
### ThunderChangeEvent

- Java class: `org.bukkit.event.weather.ThunderChangeEvent`; parent: `org.bukkit.event.weather.WeatherEvent`.
- Python subscription: `@bridge.on("ThunderChangeEvent")`; `Events.THUNDER_CHANGE` also works.
- Cancellable: yes; player: no known player getter.
- [Official Paper Javadoc](https://jd.papermc.io/paper/1.16.5/org/bukkit/event/weather/ThunderChangeEvent.html) for meaning, trigger conditions, and Java API.

| `data` field | JSON type | Java getter | Java return type |
| --- | --- | --- | --- |
| `cause` | string | `getCause()` | `org.bukkit.event.weather.ThunderChangeEvent$Cause` |
| `world` | world summary | `getWorld()` | `org.bukkit.World` |

<a id="event-org-bukkit-event-weather-weatherchangeevent"></a>
### WeatherChangeEvent

- Java class: `org.bukkit.event.weather.WeatherChangeEvent`; parent: `org.bukkit.event.weather.WeatherEvent`.
- Python subscription: `@bridge.on("WeatherChangeEvent")`; `Events.WEATHER_CHANGE` also works.
- Cancellable: yes; player: no known player getter.
- [Official Paper Javadoc](https://jd.papermc.io/paper/1.16.5/org/bukkit/event/weather/WeatherChangeEvent.html) for meaning, trigger conditions, and Java API.

| `data` field | JSON type | Java getter | Java return type |
| --- | --- | --- | --- |
| `cause` | string | `getCause()` | `org.bukkit.event.weather.WeatherChangeEvent$Cause` |
| `world` | world summary | `getWorld()` | `org.bukkit.World` |

<a id="category-world"></a>
## world

| Event | Python `type` | possible `data` fields | Cancellable |
| --- | --- | ---: | --- |
| [ChunkLoadEvent](#event-org-bukkit-event-world-chunkloadevent) | `ChunkLoadEvent` | 2 | No |
| [ChunkPopulateEvent](#event-org-bukkit-event-world-chunkpopulateevent) | `ChunkPopulateEvent` | 1 | No |
| [ChunkUnloadEvent](#event-org-bukkit-event-world-chunkunloadevent) | `ChunkUnloadEvent` | 2 | No |
| [LootGenerateEvent](#event-org-bukkit-event-world-lootgenerateevent) | `LootGenerateEvent` | 3 | Yes |
| [PortalCreateEvent](#event-org-bukkit-event-world-portalcreateevent) | `PortalCreateEvent` | 3 | Yes |
| [SpawnChangeEvent](#event-org-bukkit-event-world-spawnchangeevent) | `SpawnChangeEvent` | 2 | No |
| [StructureGrowEvent](#event-org-bukkit-event-world-structuregrowevent) | `StructureGrowEvent` | 4 | Yes |
| [StructureLocateEvent](#event-io-papermc-paper-event-world-structurelocateevent) | `StructureLocateEvent` | 4 | Yes |
| [TimeSkipEvent](#event-org-bukkit-event-world-timeskipevent) | `TimeSkipEvent` | 3 | Yes |
| [WorldBorderBoundsChangeEvent](#event-io-papermc-paper-event-world-border-worldborderboundschangeevent) | `WorldBorderBoundsChangeEvent` | 5 | Yes |
| [WorldBorderBoundsChangeFinishEvent](#event-io-papermc-paper-event-world-border-worldborderboundschangefinishevent) | `WorldBorderBoundsChangeFinishEvent` | 4 | No |
| [WorldBorderCenterChangeEvent](#event-io-papermc-paper-event-world-border-worldbordercenterchangeevent) | `WorldBorderCenterChangeEvent` | 3 | Yes |
| [WorldGameRuleChangeEvent](#event-io-papermc-paper-event-world-worldgamerulechangeevent) | `WorldGameRuleChangeEvent` | 2 | Yes |
| [WorldInitEvent](#event-org-bukkit-event-world-worldinitevent) | `WorldInitEvent` | 1 | No |
| [WorldLoadEvent](#event-org-bukkit-event-world-worldloadevent) | `WorldLoadEvent` | 1 | No |
| [WorldSaveEvent](#event-org-bukkit-event-world-worldsaveevent) | `WorldSaveEvent` | 1 | No |
| [WorldUnloadEvent](#event-org-bukkit-event-world-worldunloadevent) | `WorldUnloadEvent` | 1 | Yes |

<a id="event-org-bukkit-event-world-chunkloadevent"></a>
### ChunkLoadEvent

- Java class: `org.bukkit.event.world.ChunkLoadEvent`; parent: `org.bukkit.event.world.ChunkEvent`.
- Python subscription: `@bridge.on("ChunkLoadEvent")`; `Events.CHUNK_LOAD` also works.
- Cancellable: no; player: no known player getter.
- [Official Paper Javadoc](https://jd.papermc.io/paper/1.16.5/org/bukkit/event/world/ChunkLoadEvent.html) for meaning, trigger conditions, and Java API.

| `data` field | JSON type | Java getter | Java return type |
| --- | --- | --- | --- |
| `world` | world summary | `getWorld()` | `org.bukkit.World` |
| `newChunk` | boolean | `isNewChunk()` | `boolean` |

<a id="event-org-bukkit-event-world-chunkpopulateevent"></a>
### ChunkPopulateEvent

- Java class: `org.bukkit.event.world.ChunkPopulateEvent`; parent: `org.bukkit.event.world.ChunkEvent`.
- Python subscription: `@bridge.on("ChunkPopulateEvent")`; `Events.CHUNK_POPULATE` also works.
- Cancellable: no; player: no known player getter.
- [Official Paper Javadoc](https://jd.papermc.io/paper/1.16.5/org/bukkit/event/world/ChunkPopulateEvent.html) for meaning, trigger conditions, and Java API.

| `data` field | JSON type | Java getter | Java return type |
| --- | --- | --- | --- |
| `world` | world summary | `getWorld()` | `org.bukkit.World` |

<a id="event-org-bukkit-event-world-chunkunloadevent"></a>
### ChunkUnloadEvent

- Java class: `org.bukkit.event.world.ChunkUnloadEvent`; parent: `org.bukkit.event.world.ChunkEvent`.
- Python subscription: `@bridge.on("ChunkUnloadEvent")`; `Events.CHUNK_UNLOAD` also works.
- Cancellable: no; player: no known player getter.
- [Official Paper Javadoc](https://jd.papermc.io/paper/1.16.5/org/bukkit/event/world/ChunkUnloadEvent.html) for meaning, trigger conditions, and Java API.

| `data` field | JSON type | Java getter | Java return type |
| --- | --- | --- | --- |
| `world` | world summary | `getWorld()` | `org.bukkit.World` |
| `saveChunk` | boolean | `isSaveChunk()` | `boolean` |

<a id="event-org-bukkit-event-world-lootgenerateevent"></a>
### LootGenerateEvent

- Java class: `org.bukkit.event.world.LootGenerateEvent`; parent: `org.bukkit.event.world.WorldEvent`.
- Python subscription: `@bridge.on("LootGenerateEvent")`; `Events.LOOT_GENERATE` also works.
- Cancellable: yes; player: possible, depending on the runtime object.
- [Official Paper Javadoc](https://jd.papermc.io/paper/1.16.5/org/bukkit/event/world/LootGenerateEvent.html) for meaning, trigger conditions, and Java API.

| `data` field | JSON type | Java getter | Java return type |
| --- | --- | --- | --- |
| `entity` | entity summary | `getEntity()` | `org.bukkit.entity.Entity` |
| `world` | world summary | `getWorld()` | `org.bukkit.World` |
| `plugin` | boolean | `isPlugin()` | `boolean` |

<a id="event-org-bukkit-event-world-portalcreateevent"></a>
### PortalCreateEvent

- Java class: `org.bukkit.event.world.PortalCreateEvent`; parent: `org.bukkit.event.world.WorldEvent`.
- Python subscription: `@bridge.on("PortalCreateEvent")`; `Events.PORTAL_CREATE` also works.
- Cancellable: yes; player: possible, depending on the runtime object.
- [Official Paper Javadoc](https://jd.papermc.io/paper/1.16.5/org/bukkit/event/world/PortalCreateEvent.html) for meaning, trigger conditions, and Java API.

| `data` field | JSON type | Java getter | Java return type |
| --- | --- | --- | --- |
| `entity` | entity summary | `getEntity()` | `org.bukkit.entity.Entity` |
| `reason` | string | `getReason()` | `org.bukkit.event.world.PortalCreateEvent$CreateReason` |
| `world` | world summary | `getWorld()` | `org.bukkit.World` |

<a id="event-org-bukkit-event-world-spawnchangeevent"></a>
### SpawnChangeEvent

- Java class: `org.bukkit.event.world.SpawnChangeEvent`; parent: `org.bukkit.event.world.WorldEvent`.
- Python subscription: `@bridge.on("SpawnChangeEvent")`; `Events.SPAWN_CHANGE` also works.
- Cancellable: no; player: no known player getter.
- [Official Paper Javadoc](https://jd.papermc.io/paper/1.16.5/org/bukkit/event/world/SpawnChangeEvent.html) for meaning, trigger conditions, and Java API.

| `data` field | JSON type | Java getter | Java return type |
| --- | --- | --- | --- |
| `previousLocation` | location summary | `getPreviousLocation()` | `org.bukkit.Location` |
| `world` | world summary | `getWorld()` | `org.bukkit.World` |

<a id="event-org-bukkit-event-world-structuregrowevent"></a>
### StructureGrowEvent

- Java class: `org.bukkit.event.world.StructureGrowEvent`; parent: `org.bukkit.event.world.WorldEvent`.
- Python subscription: `@bridge.on("StructureGrowEvent")`; `Events.STRUCTURE_GROW` also works.
- Cancellable: yes; player: possible, depending on the runtime object.
- [Official Paper Javadoc](https://jd.papermc.io/paper/1.16.5/org/bukkit/event/world/StructureGrowEvent.html) for meaning, trigger conditions, and Java API.

| `data` field | JSON type | Java getter | Java return type |
| --- | --- | --- | --- |
| `location` | location summary | `getLocation()` | `org.bukkit.Location` |
| `species` | string | `getSpecies()` | `org.bukkit.TreeType` |
| `world` | world summary | `getWorld()` | `org.bukkit.World` |
| `fromBonemeal` | boolean | `isFromBonemeal()` | `boolean` |

<a id="event-io-papermc-paper-event-world-structurelocateevent"></a>
### StructureLocateEvent

- Java class: `io.papermc.paper.event.world.StructureLocateEvent`; parent: `org.bukkit.event.world.WorldEvent`.
- Python subscription: `@bridge.on("StructureLocateEvent")`; `Events.STRUCTURE_LOCATE` also works.
- Cancellable: yes; player: no known player getter.
- [Official Paper Javadoc](https://jd.papermc.io/paper/1.16.5/io/papermc/paper/event/world/StructureLocateEvent.html) for meaning, trigger conditions, and Java API.

| `data` field | JSON type | Java getter | Java return type |
| --- | --- | --- | --- |
| `origin` | location summary | `getOrigin()` | `org.bukkit.Location` |
| `radius` | number | `getRadius()` | `int` |
| `result` | location summary | `getResult()` | `org.bukkit.Location` |
| `world` | world summary | `getWorld()` | `org.bukkit.World` |

<a id="event-org-bukkit-event-world-timeskipevent"></a>
### TimeSkipEvent

- Java class: `org.bukkit.event.world.TimeSkipEvent`; parent: `org.bukkit.event.world.WorldEvent`.
- Python subscription: `@bridge.on("TimeSkipEvent")`; `Events.TIME_SKIP` also works.
- Cancellable: yes; player: no known player getter.
- [Official Paper Javadoc](https://jd.papermc.io/paper/1.16.5/org/bukkit/event/world/TimeSkipEvent.html) for meaning, trigger conditions, and Java API.

| `data` field | JSON type | Java getter | Java return type |
| --- | --- | --- | --- |
| `skipAmount` | number | `getSkipAmount()` | `long` |
| `skipReason` | string | `getSkipReason()` | `org.bukkit.event.world.TimeSkipEvent$SkipReason` |
| `world` | world summary | `getWorld()` | `org.bukkit.World` |

<a id="event-io-papermc-paper-event-world-border-worldborderboundschangeevent"></a>
### WorldBorderBoundsChangeEvent

- Java class: `io.papermc.paper.event.world.border.WorldBorderBoundsChangeEvent`; parent: `io.papermc.paper.event.world.border.WorldBorderEvent`.
- Python subscription: `@bridge.on("WorldBorderBoundsChangeEvent")`; `Events.WORLD_BORDER_BOUNDS_CHANGE` also works.
- Cancellable: yes; player: no known player getter.
- [Official Paper Javadoc](https://jd.papermc.io/paper/1.16.5/io/papermc/paper/event/world/border/WorldBorderBoundsChangeEvent.html) for meaning, trigger conditions, and Java API.

| `data` field | JSON type | Java getter | Java return type |
| --- | --- | --- | --- |
| `duration` | number | `getDuration()` | `long` |
| `newSize` | number | `getNewSize()` | `double` |
| `oldSize` | number | `getOldSize()` | `double` |
| `type` | string | `getType()` | `io.papermc.paper.event.world.border.WorldBorderBoundsChangeEvent$Type` |
| `world` | world summary | `getWorld()` | `org.bukkit.World` |

<a id="event-io-papermc-paper-event-world-border-worldborderboundschangefinishevent"></a>
### WorldBorderBoundsChangeFinishEvent

- Java class: `io.papermc.paper.event.world.border.WorldBorderBoundsChangeFinishEvent`; parent: `io.papermc.paper.event.world.border.WorldBorderEvent`.
- Python subscription: `@bridge.on("WorldBorderBoundsChangeFinishEvent")`; `Events.WORLD_BORDER_BOUNDS_CHANGE_FINISH` also works.
- Cancellable: no; player: no known player getter.
- [Official Paper Javadoc](https://jd.papermc.io/paper/1.16.5/io/papermc/paper/event/world/border/WorldBorderBoundsChangeFinishEvent.html) for meaning, trigger conditions, and Java API.

| `data` field | JSON type | Java getter | Java return type |
| --- | --- | --- | --- |
| `duration` | number | `getDuration()` | `double` |
| `newSize` | number | `getNewSize()` | `double` |
| `oldSize` | number | `getOldSize()` | `double` |
| `world` | world summary | `getWorld()` | `org.bukkit.World` |

<a id="event-io-papermc-paper-event-world-border-worldbordercenterchangeevent"></a>
### WorldBorderCenterChangeEvent

- Java class: `io.papermc.paper.event.world.border.WorldBorderCenterChangeEvent`; parent: `io.papermc.paper.event.world.border.WorldBorderEvent`.
- Python subscription: `@bridge.on("WorldBorderCenterChangeEvent")`; `Events.WORLD_BORDER_CENTER_CHANGE` also works.
- Cancellable: yes; player: no known player getter.
- [Official Paper Javadoc](https://jd.papermc.io/paper/1.16.5/io/papermc/paper/event/world/border/WorldBorderCenterChangeEvent.html) for meaning, trigger conditions, and Java API.

| `data` field | JSON type | Java getter | Java return type |
| --- | --- | --- | --- |
| `newCenter` | location summary | `getNewCenter()` | `org.bukkit.Location` |
| `oldCenter` | location summary | `getOldCenter()` | `org.bukkit.Location` |
| `world` | world summary | `getWorld()` | `org.bukkit.World` |

<a id="event-io-papermc-paper-event-world-worldgamerulechangeevent"></a>
### WorldGameRuleChangeEvent

- Java class: `io.papermc.paper.event.world.WorldGameRuleChangeEvent`; parent: `org.bukkit.event.world.WorldEvent`.
- Python subscription: `@bridge.on("WorldGameRuleChangeEvent")`; `Events.WORLD_GAME_RULE_CHANGE` also works.
- Cancellable: yes; player: no known player getter.
- [Official Paper Javadoc](https://jd.papermc.io/paper/1.16.5/io/papermc/paper/event/world/WorldGameRuleChangeEvent.html) for meaning, trigger conditions, and Java API.

| `data` field | JSON type | Java getter | Java return type |
| --- | --- | --- | --- |
| `value` | string | `getValue()` | `java.lang.String` |
| `world` | world summary | `getWorld()` | `org.bukkit.World` |

<a id="event-org-bukkit-event-world-worldinitevent"></a>
### WorldInitEvent

- Java class: `org.bukkit.event.world.WorldInitEvent`; parent: `org.bukkit.event.world.WorldEvent`.
- Python subscription: `@bridge.on("WorldInitEvent")`; `Events.WORLD_INIT` also works.
- Cancellable: no; player: no known player getter.
- [Official Paper Javadoc](https://jd.papermc.io/paper/1.16.5/org/bukkit/event/world/WorldInitEvent.html) for meaning, trigger conditions, and Java API.

| `data` field | JSON type | Java getter | Java return type |
| --- | --- | --- | --- |
| `world` | world summary | `getWorld()` | `org.bukkit.World` |

<a id="event-org-bukkit-event-world-worldloadevent"></a>
### WorldLoadEvent

- Java class: `org.bukkit.event.world.WorldLoadEvent`; parent: `org.bukkit.event.world.WorldEvent`.
- Python subscription: `@bridge.on("WorldLoadEvent")`; `Events.WORLD_LOAD` also works.
- Cancellable: no; player: no known player getter.
- [Official Paper Javadoc](https://jd.papermc.io/paper/1.16.5/org/bukkit/event/world/WorldLoadEvent.html) for meaning, trigger conditions, and Java API.

| `data` field | JSON type | Java getter | Java return type |
| --- | --- | --- | --- |
| `world` | world summary | `getWorld()` | `org.bukkit.World` |

<a id="event-org-bukkit-event-world-worldsaveevent"></a>
### WorldSaveEvent

- Java class: `org.bukkit.event.world.WorldSaveEvent`; parent: `org.bukkit.event.world.WorldEvent`.
- Python subscription: `@bridge.on("WorldSaveEvent")`; `Events.WORLD_SAVE` also works.
- Cancellable: no; player: no known player getter.
- [Official Paper Javadoc](https://jd.papermc.io/paper/1.16.5/org/bukkit/event/world/WorldSaveEvent.html) for meaning, trigger conditions, and Java API.

| `data` field | JSON type | Java getter | Java return type |
| --- | --- | --- | --- |
| `world` | world summary | `getWorld()` | `org.bukkit.World` |

<a id="event-org-bukkit-event-world-worldunloadevent"></a>
### WorldUnloadEvent

- Java class: `org.bukkit.event.world.WorldUnloadEvent`; parent: `org.bukkit.event.world.WorldEvent`.
- Python subscription: `@bridge.on("WorldUnloadEvent")`; `Events.WORLD_UNLOAD` also works.
- Cancellable: yes; player: no known player getter.
- [Official Paper Javadoc](https://jd.papermc.io/paper/1.16.5/org/bukkit/event/world/WorldUnloadEvent.html) for meaning, trigger conditions, and Java API.

| `data` field | JSON type | Java getter | Java return type |
| --- | --- | --- | --- |
| `world` | world summary | `getWorld()` | `org.bukkit.World` |
