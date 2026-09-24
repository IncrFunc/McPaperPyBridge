# PrepareAnvilEvent

[[Home-en|Home]] / [[Category-inventory-en|inventory]]

- Java class: `org.bukkit.event.inventory.PrepareAnvilEvent`
- Parent class: `com.destroystokyo.paper.event.inventory.PrepareResultEvent`
- Python subscription: `PrepareAnvilEvent`
- Python constant: `Events.PREPARE_ANVIL`
- Cancellable: No
- Player available: No known player getter
- HandlerList owner: `com.destroystokyo.paper.event.inventory.PrepareResultEvent`
- [Official Paper Javadoc](https://jd.papermc.io/paper/1.16.5/org/bukkit/event/inventory/PrepareAnvilEvent.html)

## Python example

```python
from paperpybridge import Events

@bridge.on(Events.PREPARE_ANVIL)
def on_event(event):
    print(event.event, event.data)
```

## `data` fields

| Field | JSON type | Java getter | Java return type | Declared in |
| --- | --- | --- | --- | --- |
| `result` | item summary | `getResult()` | `org.bukkit.inventory.ItemStack` | `org.bukkit.event.inventory.PrepareAnvilEvent` |

[[Data-Format-en|Wire format and limits]] · [[Event-org-bukkit-event-inventory-prepareanvilevent|中文]]

If this event is not enabled, add its Java class or simple name to `events.include` in the Paper plugin configuration.
