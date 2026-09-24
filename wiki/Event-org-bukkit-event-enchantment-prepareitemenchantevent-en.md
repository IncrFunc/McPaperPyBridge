# PrepareItemEnchantEvent

[[Home-en|Home]] / [[Category-enchantment-en|enchantment]]

- Java class: `org.bukkit.event.enchantment.PrepareItemEnchantEvent`
- Parent class: `org.bukkit.event.inventory.InventoryEvent`
- Python subscription: `PrepareItemEnchantEvent`
- Python constant: `Events.PREPARE_ITEM_ENCHANT`
- Cancellable: Yes
- Player available: No known player getter
- HandlerList owner: `org.bukkit.event.enchantment.PrepareItemEnchantEvent`
- [Official Paper Javadoc](https://jd.papermc.io/paper/1.16.5/org/bukkit/event/enchantment/PrepareItemEnchantEvent.html)

## Python example

```python
from paperpybridge import Events

@bridge.on(Events.PREPARE_ITEM_ENCHANT)
def on_event(event):
    print(event.event, event.data)
```

## `data` fields

| Field | JSON type | Java getter | Java return type | Declared in |
| --- | --- | --- | --- | --- |
| `enchantBlock` | block summary | `getEnchantBlock()` | `org.bukkit.block.Block` | `org.bukkit.event.enchantment.PrepareItemEnchantEvent` |
| `enchanter` | entity summary | `getEnchanter()` | `org.bukkit.entity.Player` | `org.bukkit.event.enchantment.PrepareItemEnchantEvent` |
| `enchantmentBonus` | number | `getEnchantmentBonus()` | `int` | `org.bukkit.event.enchantment.PrepareItemEnchantEvent` |
| `item` | item summary | `getItem()` | `org.bukkit.inventory.ItemStack` | `org.bukkit.event.enchantment.PrepareItemEnchantEvent` |

[[Data-Format-en|Wire format and limits]] · [[Event-org-bukkit-event-enchantment-prepareitemenchantevent|中文]]

If this event is not enabled, add its Java class or simple name to `events.include` in the Paper plugin configuration.
