# PaperPyBridge 事件 Wiki

这里收录 Paper 1.16.5 中 **333 个可转发的具体事件类**，共使用 **292 组 HandlerList**。每个事件单独成页，列出 Python 订阅名、实际转出的字段和官方 Javadoc。

[[Home-en|English]] · [[Data-Format|通用字段、数据格式和限制]] · [[Python-to-MC|Python → MC 操作]]

默认只启用聊天、玩家加入和退出事件。要接收其他事件，先将其加入 `events.include`。

## 快速上手

```python
from paperpybridge import Events

@bridge.on(Events.ASYNC_PLAYER_CHAT)
def on_chat(event):
    print(event.message)
```

也可以用 Java 完整类名订阅，或用 `@bridge.on("*")` 订阅全部事件。原有 `chat`、`join`、`quit` 别名继续有效。

## 按类别浏览

| 分类 | 事件数 |
| --- | ---: |
| [[Category-block|方块]] | 45 |
| [[Category-command|命令]] | 1 |
| [[Category-enchantment|附魔]] | 2 |
| [[Category-entity|实体]] | 107 |
| [[Category-hanging|悬挂实体]] | 3 |
| [[Category-inventory|物品栏]] | 21 |
| [[Category-packet|网络包]] | 2 |
| [[Category-player|玩家]] | 95 |
| [[Category-profile|玩家资料]] | 5 |
| [[Category-raid|袭击]] | 4 |
| [[Category-server|服务端]] | 19 |
| [[Category-vehicle|载具]] | 9 |
| [[Category-weather|天气]] | 3 |
| [[Category-world|世界]] | 17 |

## 阅读说明

本 Wiki 描述 PaperPyBridge 实际转出的字段。事件触发条件和 Java 行为请看各页的官方 Javadoc。Python 收到的是快照，不能同步取消或修改原事件。
