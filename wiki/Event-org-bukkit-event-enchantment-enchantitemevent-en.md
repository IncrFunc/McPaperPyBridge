# EnchantItemEvent

[[Home-en|Home]] / [[Category-enchantment-en|enchantment]]

- Java class: `org.bukkit.event.enchantment.EnchantItemEvent`
- Parent class: `org.bukkit.event.inventory.InventoryEvent`
- Python subscription: `EnchantItemEvent`
- Python constant: `Events.ENCHANT_ITEM`
- Cancellable: Yes
- Player available: No known player getter
- HandlerList owner: `org.bukkit.event.enchantment.EnchantItemEvent`
- [Official Paper Javadoc](https://jd.papermc.io/paper/1.16.5/org/bukkit/event/enchantment/EnchantItemEvent.html)

## Python example

```python
from paperpybridge import Events

@bridge.on(Events.ENCHANT_ITEM)
def on_event(event):
    print(event.event, event.data)
```

## `data` fields

| Field | JSON type | Java getter | Java return type | Declared in |
| --- | --- | --- | --- | --- |
| `enchantBlock` | block summary | `getEnchantBlock()` | `org.bukkit.block.Block` | `org.bukkit.event.enchantment.EnchantItemEvent` |
| `enchanter` | entity summary | `getEnchanter()` | `org.bukkit.entity.Player` | `org.bukkit.event.enchantment.EnchantItemEvent` |
| `expLevelCost` | number | `getExpLevelCost()` | `int` | `org.bukkit.event.enchantment.EnchantItemEvent` |
| `item` | item summary | `getItem()` | `org.bukkit.inventory.ItemStack` | `org.bukkit.event.enchantment.EnchantItemEvent` |

[[Data-Format-en|Wire format and limits]] · [[Event-org-bukkit-event-enchantment-enchantitemevent|中文]]

If this event is not enabled, add its Java class or simple name to `events.include` in the Paper plugin configuration.
