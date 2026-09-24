# PlayerHandshakeEvent

[[Home-en|Home]] / [[Category-player-en|player]]

- Java class: `com.destroystokyo.paper.event.player.PlayerHandshakeEvent`
- Parent class: `org.bukkit.event.Event`
- Python subscription: `PlayerHandshakeEvent`
- Python constant: `Events.PLAYER_HANDSHAKE`
- Cancellable: Yes
- Player available: No known player getter
- HandlerList owner: `com.destroystokyo.paper.event.player.PlayerHandshakeEvent`
- [Official Paper Javadoc](https://jd.papermc.io/paper/1.16.5/com/destroystokyo/paper/event/player/PlayerHandshakeEvent.html)

## Python example

```python
from paperpybridge import Events

@bridge.on(Events.PLAYER_HANDSHAKE)
def on_event(event):
    print(event.event, event.data)
```

## `data` fields

| Field | JSON type | Java getter | Java return type | Declared in |
| --- | --- | --- | --- | --- |
| `failMessage` | string | `getFailMessage()` | `java.lang.String` | `com.destroystokyo.paper.event.player.PlayerHandshakeEvent` |
| `originalHandshake` | string | `getOriginalHandshake()` | `java.lang.String` | `com.destroystokyo.paper.event.player.PlayerHandshakeEvent` |
| `originalSocketAddressHostname` | string | `getOriginalSocketAddressHostname()` | `java.lang.String` | `com.destroystokyo.paper.event.player.PlayerHandshakeEvent` |
| `propertiesJson` | string | `getPropertiesJson()` | `java.lang.String` | `com.destroystokyo.paper.event.player.PlayerHandshakeEvent` |
| `serverHostname` | string | `getServerHostname()` | `java.lang.String` | `com.destroystokyo.paper.event.player.PlayerHandshakeEvent` |
| `socketAddressHostname` | string | `getSocketAddressHostname()` | `java.lang.String` | `com.destroystokyo.paper.event.player.PlayerHandshakeEvent` |
| `uniqueId` | string | `getUniqueId()` | `java.util.UUID` | `com.destroystokyo.paper.event.player.PlayerHandshakeEvent` |
| `failed` | boolean | `isFailed()` | `boolean` | `com.destroystokyo.paper.event.player.PlayerHandshakeEvent` |

[[Data-Format-en|Wire format and limits]] · [[Event-com-destroystokyo-paper-event-player-playerhandshakeevent|中文]]

If this event is not enabled, add its Java class or simple name to `events.include` in the Paper plugin configuration.
