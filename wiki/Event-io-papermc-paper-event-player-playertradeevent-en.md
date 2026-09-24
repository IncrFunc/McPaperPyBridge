# PlayerTradeEvent

[[Home-en|Home]] / [[Category-player-en|player]]

- Java class: `io.papermc.paper.event.player.PlayerTradeEvent`
- Parent class: `io.papermc.paper.event.player.PlayerPurchaseEvent`
- Python subscription: `PlayerTradeEvent`
- Python constant: `Events.PLAYER_TRADE`
- Cancellable: Yes
- Player available: Possible at runtime
- HandlerList owner: `io.papermc.paper.event.player.PlayerPurchaseEvent`
- [Official Paper Javadoc](https://jd.papermc.io/paper/1.16.5/io/papermc/paper/event/player/PlayerTradeEvent.html)

## Python example

```python
from paperpybridge import Events

@bridge.on(Events.PLAYER_TRADE)
def on_event(event):
    print(event.event, event.data)
```

## `data` fields

| Field | JSON type | Java getter | Java return type | Declared in |
| --- | --- | --- | --- | --- |
| `villager` | entity summary | `getVillager()` | `org.bukkit.entity.AbstractVillager` | `io.papermc.paper.event.player.PlayerTradeEvent` |
| `rewardingExp` | boolean | `isRewardingExp()` | `boolean` | `io.papermc.paper.event.player.PlayerPurchaseEvent` |

[[Data-Format-en|Wire format and limits]] · [[Event-io-papermc-paper-event-player-playertradeevent|中文]]

If this event is not enabled, add its Java class or simple name to `events.include` in the Paper plugin configuration.
