# IllegalPacketEvent

[[Home-en|Home]] / [[Category-player-en|player]]

- Java class: `com.destroystokyo.paper.event.player.IllegalPacketEvent`
- Parent class: `org.bukkit.event.player.PlayerEvent`
- Python subscription: `IllegalPacketEvent`
- Python constant: `Events.ILLEGAL_PACKET`
- Cancellable: No
- Player available: Possible at runtime
- HandlerList owner: `com.destroystokyo.paper.event.player.IllegalPacketEvent`
- [Official Paper Javadoc](https://jd.papermc.io/paper/1.16.5/com/destroystokyo/paper/event/player/IllegalPacketEvent.html)

## Python example

```python
from paperpybridge import Events

@bridge.on(Events.ILLEGAL_PACKET)
def on_event(event):
    print(event.event, event.data)
```

## `data` fields

| Field | JSON type | Java getter | Java return type | Declared in |
| --- | --- | --- | --- | --- |
| `exceptionMessage` | string | `getExceptionMessage()` | `java.lang.String` | `com.destroystokyo.paper.event.player.IllegalPacketEvent` |
| `kickMessage` | string | `getKickMessage()` | `java.lang.String` | `com.destroystokyo.paper.event.player.IllegalPacketEvent` |
| `type` | string | `getType()` | `java.lang.String` | `com.destroystokyo.paper.event.player.IllegalPacketEvent` |
| `shouldKick` | boolean | `isShouldKick()` | `boolean` | `com.destroystokyo.paper.event.player.IllegalPacketEvent` |

[[Data-Format-en|Wire format and limits]] · [[Event-com-destroystokyo-paper-event-player-illegalpacketevent|中文]]

If this event is not enabled, add its Java class or simple name to `events.include` in the Paper plugin configuration.
