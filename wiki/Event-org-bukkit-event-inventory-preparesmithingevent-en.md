# PrepareSmithingEvent

[[Home-en|Home]] / [[Category-inventory-en|inventory]]

- Java class: `org.bukkit.event.inventory.PrepareSmithingEvent`
- Parent class: `com.destroystokyo.paper.event.inventory.PrepareResultEvent`
- Python subscription: `PrepareSmithingEvent`
- Python constant: `Events.PREPARE_SMITHING`
- Cancellable: No
- Player available: No known player getter
- HandlerList owner: `com.destroystokyo.paper.event.inventory.PrepareResultEvent`
- [Official Paper Javadoc](https://jd.papermc.io/paper/1.16.5/org/bukkit/event/inventory/PrepareSmithingEvent.html)

## Python example

```python
from paperpybridge import Events

@bridge.on(Events.PREPARE_SMITHING)
def on_event(event):
    print(event.event, event.data)
```

## `data` fields

| Field | JSON type | Java getter | Java return type | Declared in |
| --- | --- | --- | --- | --- |
| `result` | item summary | `getResult()` | `org.bukkit.inventory.ItemStack` | `org.bukkit.event.inventory.PrepareSmithingEvent` |

[[Data-Format-en|Wire format and limits]] · [[Event-org-bukkit-event-inventory-preparesmithingevent|中文]]

If this event is not enabled, add its Java class or simple name to `events.include` in the Paper plugin configuration.
