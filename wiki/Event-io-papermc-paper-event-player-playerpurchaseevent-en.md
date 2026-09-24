# PlayerPurchaseEvent

[[Home-en|Home]] / [[Category-player-en|player]]

- Java class: `io.papermc.paper.event.player.PlayerPurchaseEvent`
- Parent class: `org.bukkit.event.player.PlayerEvent`
- Python subscription: `PlayerPurchaseEvent`
- Python constant: `Events.PLAYER_PURCHASE`
- Cancellable: Yes
- Player available: Possible at runtime
- HandlerList owner: `io.papermc.paper.event.player.PlayerPurchaseEvent`
- [Official Paper Javadoc](https://jd.papermc.io/paper/1.16.5/io/papermc/paper/event/player/PlayerPurchaseEvent.html)

## Python example

```python
from paperpybridge import Events

@bridge.on(Events.PLAYER_PURCHASE)
def on_event(event):
    print(event.event, event.data)
```

## `data` fields

| Field | JSON type | Java getter | Java return type | Declared in |
| --- | --- | --- | --- | --- |
| `rewardingExp` | boolean | `isRewardingExp()` | `boolean` | `io.papermc.paper.event.player.PlayerPurchaseEvent` |

[[Data-Format-en|Wire format and limits]] · [[Event-io-papermc-paper-event-player-playerpurchaseevent|中文]]

If this event is not enabled, add its Java class or simple name to `events.include` in the Paper plugin configuration.
