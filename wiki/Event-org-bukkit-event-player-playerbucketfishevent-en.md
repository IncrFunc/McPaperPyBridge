# PlayerBucketFishEvent

[[Home-en|Home]] / [[Category-player-en|player]]

- Java class: `org.bukkit.event.player.PlayerBucketFishEvent`
- Parent class: `org.bukkit.event.player.PlayerBucketEntityEvent`
- Python subscription: `PlayerBucketFishEvent`
- Python constant: `Events.PLAYER_BUCKET_FISH`
- Cancellable: Yes
- Player available: Possible at runtime
- HandlerList owner: `org.bukkit.event.player.PlayerBucketEntityEvent`
- [Official Paper Javadoc](https://jd.papermc.io/paper/1.16.5/org/bukkit/event/player/PlayerBucketFishEvent.html)

## Python example

```python
from paperpybridge import Events

@bridge.on(Events.PLAYER_BUCKET_FISH)
def on_event(event):
    print(event.event, event.data)
```

## `data` fields

| Field | JSON type | Java getter | Java return type | Declared in |
| --- | --- | --- | --- | --- |
| `entity` | entity summary | `getEntity()` | `org.bukkit.entity.Fish` | `org.bukkit.event.player.PlayerBucketFishEvent` |
| `entityBucket` | item summary | `getEntityBucket()` | `org.bukkit.inventory.ItemStack` | `org.bukkit.event.player.PlayerBucketEntityEvent` |
| `fishBucket` | item summary | `getFishBucket()` | `org.bukkit.inventory.ItemStack` | `org.bukkit.event.player.PlayerBucketFishEvent` |
| `originalBucket` | item summary | `getOriginalBucket()` | `org.bukkit.inventory.ItemStack` | `org.bukkit.event.player.PlayerBucketEntityEvent` |
| `waterBucket` | item summary | `getWaterBucket()` | `org.bukkit.inventory.ItemStack` | `org.bukkit.event.player.PlayerBucketFishEvent` |

[[Data-Format-en|Wire format and limits]] · [[Event-org-bukkit-event-player-playerbucketfishevent|中文]]

If this event is not enabled, add its Java class or simple name to `events.include` in the Paper plugin configuration.
