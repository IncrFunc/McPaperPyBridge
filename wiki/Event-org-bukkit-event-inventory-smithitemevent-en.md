# SmithItemEvent

[[Home-en|Home]] / [[Category-inventory-en|inventory]]

- Java class: `org.bukkit.event.inventory.SmithItemEvent`
- Parent class: `org.bukkit.event.inventory.InventoryClickEvent`
- Python subscription: `SmithItemEvent`
- Python constant: `Events.SMITH_ITEM`
- Cancellable: Yes
- Player available: Possible at runtime
- HandlerList owner: `org.bukkit.event.inventory.InventoryClickEvent`
- [Official Paper Javadoc](https://jd.papermc.io/paper/1.16.5/org/bukkit/event/inventory/SmithItemEvent.html)

## Python example

```python
from paperpybridge import Events

@bridge.on(Events.SMITH_ITEM)
def on_event(event):
    print(event.event, event.data)
```

## `data` fields

| Field | JSON type | Java getter | Java return type | Declared in |
| --- | --- | --- | --- | --- |
| `action` | string | `getAction()` | `org.bukkit.event.inventory.InventoryAction` | `org.bukkit.event.inventory.InventoryClickEvent` |
| `click` | string | `getClick()` | `org.bukkit.event.inventory.ClickType` | `org.bukkit.event.inventory.InventoryClickEvent` |
| `currentItem` | item summary | `getCurrentItem()` | `org.bukkit.inventory.ItemStack` | `org.bukkit.event.inventory.InventoryClickEvent` |
| `cursor` | item summary | `getCursor()` | `org.bukkit.inventory.ItemStack` | `org.bukkit.event.inventory.InventoryClickEvent` |
| `hotbarButton` | number | `getHotbarButton()` | `int` | `org.bukkit.event.inventory.InventoryClickEvent` |
| `rawSlot` | number | `getRawSlot()` | `int` | `org.bukkit.event.inventory.InventoryClickEvent` |
| `result` | string | `getResult()` | `org.bukkit.event.Event$Result` | `org.bukkit.event.inventory.InventoryInteractEvent` |
| `slot` | number | `getSlot()` | `int` | `org.bukkit.event.inventory.InventoryClickEvent` |
| `slotType` | string | `getSlotType()` | `org.bukkit.event.inventory.InventoryType$SlotType` | `org.bukkit.event.inventory.InventoryClickEvent` |
| `whoClicked` | entity summary | `getWhoClicked()` | `org.bukkit.entity.HumanEntity` | `org.bukkit.event.inventory.InventoryInteractEvent` |
| `leftClick` | boolean | `isLeftClick()` | `boolean` | `org.bukkit.event.inventory.InventoryClickEvent` |
| `rightClick` | boolean | `isRightClick()` | `boolean` | `org.bukkit.event.inventory.InventoryClickEvent` |
| `shiftClick` | boolean | `isShiftClick()` | `boolean` | `org.bukkit.event.inventory.InventoryClickEvent` |

[[Data-Format-en|Wire format and limits]] · [[Event-org-bukkit-event-inventory-smithitemevent|中文]]

If this event is not enabled, add its Java class or simple name to `events.include` in the Paper plugin configuration.
