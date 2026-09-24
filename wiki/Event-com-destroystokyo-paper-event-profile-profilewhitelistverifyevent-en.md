# ProfileWhitelistVerifyEvent

[[Home-en|Home]] / [[Category-profile-en|profile]]

- Java class: `com.destroystokyo.paper.event.profile.ProfileWhitelistVerifyEvent`
- Parent class: `org.bukkit.event.Event`
- Python subscription: `ProfileWhitelistVerifyEvent`
- Python constant: `Events.PROFILE_WHITELIST_VERIFY`
- Cancellable: No
- Player available: No known player getter
- HandlerList owner: `com.destroystokyo.paper.event.profile.ProfileWhitelistVerifyEvent`
- [Official Paper Javadoc](https://jd.papermc.io/paper/1.16.5/com/destroystokyo/paper/event/profile/ProfileWhitelistVerifyEvent.html)

## Python example

```python
from paperpybridge import Events

@bridge.on(Events.PROFILE_WHITELIST_VERIFY)
def on_event(event):
    print(event.event, event.data)
```

## `data` fields

| Field | JSON type | Java getter | Java return type | Declared in |
| --- | --- | --- | --- | --- |
| `kickMessage` | string | `getKickMessage()` | `java.lang.String` | `com.destroystokyo.paper.event.profile.ProfileWhitelistVerifyEvent` |
| `op` | boolean | `isOp()` | `boolean` | `com.destroystokyo.paper.event.profile.ProfileWhitelistVerifyEvent` |
| `whitelistEnabled` | boolean | `isWhitelistEnabled()` | `boolean` | `com.destroystokyo.paper.event.profile.ProfileWhitelistVerifyEvent` |
| `whitelisted` | boolean | `isWhitelisted()` | `boolean` | `com.destroystokyo.paper.event.profile.ProfileWhitelistVerifyEvent` |

[[Data-Format-en|Wire format and limits]] · [[Event-com-destroystokyo-paper-event-profile-profilewhitelistverifyevent|中文]]

If this event is not enabled, add its Java class or simple name to `events.include` in the Paper plugin configuration.
