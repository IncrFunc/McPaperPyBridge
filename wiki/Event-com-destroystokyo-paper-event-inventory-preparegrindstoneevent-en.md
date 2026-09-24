# PrepareGrindstoneEvent

[[Home-en|Home]] / [[Category-inventory-en|inventory]]

- Java class: `com.destroystokyo.paper.event.inventory.PrepareGrindstoneEvent`
- Parent class: `com.destroystokyo.paper.event.inventory.PrepareResultEvent`
- Python subscription: `PrepareGrindstoneEvent`
- Python constant: `Events.PREPARE_GRINDSTONE`
- Cancellable: No
- Player available: No known player getter
- HandlerList owner: `com.destroystokyo.paper.event.inventory.PrepareResultEvent`
- [Official Paper Javadoc](https://jd.papermc.io/paper/1.16.5/com/destroystokyo/paper/event/inventory/PrepareGrindstoneEvent.html)

## Python example

```python
from paperpybridge import Events

@bridge.on(Events.PREPARE_GRINDSTONE)
def on_event(event):
    print(event.event, event.data)
```

## `data` fields

| Field | JSON type | Java getter | Java return type | Declared in |
| --- | --- | --- | --- | --- |
| `result` | item summary | `getResult()` | `org.bukkit.inventory.ItemStack` | `com.destroystokyo.paper.event.inventory.PrepareResultEvent` |

[[Data-Format-en|Wire format and limits]] · [[Event-com-destroystokyo-paper-event-inventory-preparegrindstoneevent|中文]]

If this event is not enabled, add its Java class or simple name to `events.include` in the Paper plugin configuration.
