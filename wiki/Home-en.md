# PaperPyBridge Event Wiki

Reference for **333 forwardable event classes** in Paper 1.16.5. They use **292 distinct HandlerLists**. Each event page lists the Python subscription name and the fields this bridge sends.

[[Home|中文版]] · [[Data-Format-en|Wire format and limits]] · [[Python-to-MC-en|Python → MC]]

Only chat, player join, and player quit are enabled by default. Add other events to `events.include` before subscribing to them.

## Start here

```python
from paperpybridge import Events

@bridge.on(Events.ASYNC_PLAYER_CHAT)
def on_chat(event):
    print(event.message)
```

You can also subscribe by fully qualified Java class name or use `@bridge.on("*")`. The existing `chat`, `join`, and `quit` aliases continue to work.

## Browse by category

| Category | Events |
| --- | ---: |
| [[Category-block-en|block]] | 45 |
| [[Category-command-en|command]] | 1 |
| [[Category-enchantment-en|enchantment]] | 2 |
| [[Category-entity-en|entity]] | 107 |
| [[Category-hanging-en|hanging]] | 3 |
| [[Category-inventory-en|inventory]] | 21 |
| [[Category-packet-en|packet]] | 2 |
| [[Category-player-en|player]] | 95 |
| [[Category-profile-en|profile]] | 5 |
| [[Category-raid-en|raid]] | 4 |
| [[Category-server-en|server]] | 19 |
| [[Category-vehicle-en|vehicle]] | 9 |
| [[Category-weather-en|weather]] | 3 |
| [[Category-world-en|world]] | 17 |

## Notes

This wiki describes the fields emitted by PaperPyBridge. Follow each event page's official Javadoc link for trigger conditions and Java behavior. Python receives a snapshot and cannot synchronously cancel or modify the original event.
