"""Generate the bilingual GitHub Wiki from the Paper 1.16.5 event catalog."""

import argparse
import re
from collections import defaultdict
from pathlib import Path

import generate_event_docs as docs

WIKI = docs.ROOT / "wiki"


def event_page(event, english=False):
    return "Event-" + event["class"].lower().replace(".", "-") + ("-en" if english else "") + ".md"


def category_page(group, english=False):
    return "Category-" + group + ("-en" if english else "") + ".md"


def link(label, target):
    if target.endswith(".md"):
        return f"[[{target[:-3]}|{label}]]"
    return f"[{label}]({target})"


def write(name, lines):
    (WIKI / name).write_text("\n".join(lines).rstrip() + "\n", encoding="utf-8", newline="\n")


def render_event(event, english):
    group = docs.category(event)
    label = group if english else docs.CATEGORIES_ZH.get(group, group)
    yes_no = ("Yes" if event["cancellable"] else "No") if english else ("是" if event["cancellable"] else "否")
    player = (("Possible at runtime" if event["player_possible"] else "No known player getter") if english else
              ("取决于实际对象" if event["player_possible"] else "没有已知玩家 getter"))
    lines = [
        f"# {event['name']}", "",
        link("Home" if english else "首页", "Home-en.md" if english else "Home.md") + " / " +
        link(label, category_page(group, english)), "",
        f"- {'Java class' if english else 'Java 类'}: `{event['class']}`",
        f"- {'Parent class' if english else '父类'}: `{event['parent']}`",
        f"- {'Python subscription' if english else 'Python 订阅名'}: `{event['type']}`",
        f"- {'Python constant' if english else 'Python 常量'}: `Events.{docs.constant_name(event)}`",
        f"- {'Cancellable' if english else '可取消'}: {yes_no}",
        f"- {'Player available' if english else '可能关联玩家'}: {player}",
        f"- {'HandlerList owner' if english else '处理器列表定义于'}: `{event['handler_list_owner']}`",
        "- " + link("Official Paper Javadoc" if english else "Paper 官方 Javadoc", docs.javadoc_url(event)), "",
        "## Python example" if english else "## Python 示例", "", "```python",
        "from paperpybridge import Events", "",
        f'@bridge.on(Events.{docs.constant_name(event)})',
        "def on_event(event):", "    print(event.event, event.data)", "```", "",
        "## `data` fields" if english else "## `data` 字段", "",
    ]
    if event["fields"]:
        lines.extend([
            "| Field | JSON type | Java getter | Java return type | Declared in |" if english else
            "| 字段 | JSON 类型 | Java getter | Java 返回类型 | 定义于 |",
            "| --- | --- | --- | --- | --- |",
        ])
        shapes = docs.SHAPES_EN if english else docs.SHAPES_ZH
        for field in event["fields"]:
            shape = shapes.get(field["json_type"], field["json_type"])
            lines.append(f"| `{field['name']}` | {shape} | `{field['getter']}` | "
                         f"`{field['java_type']}` | `{field['declared_in']}` |")
    else:
        lines.append("No supported serializable fields; common event fields are still sent." if english else
                     "没有可序列化的字段，仍会收到通用事件字段。")
    lines.extend(["", link("Wire format and limits" if english else "通用字段、数据格式和限制",
                           "Data-Format-en.md" if english else "Data-Format.md") + " · " +
                  link("中文" if english else "English", event_page(event, not english)), ""])
    lines.extend([
        "If this event is not enabled, add its Java class or simple name to `events.include` in the Paper plugin configuration."
        if english else
        "若此事件尚未启用，请将其 Java 完整类名或简单类名加入 Paper 插件配置的 `events.include`。", "",
    ])
    return lines


def render_category(group, events, english):
    label = group if english else docs.CATEGORIES_ZH.get(group, group)
    lines = [f"# {label} {'events' if english else '事件'} (`{group}`)", "",
             link("Home" if english else "首页", "Home-en.md" if english else "Home.md") + " · " +
             link("中文" if english else "English", category_page(group, not english)), "",
             f"{len(events)} {'forwardable event classes' if english else '个可转发事件类'}。", "",
             "| Event | Python `type` | `data` fields | Cancellable |" if english else
             "| 事件 | Python `type` | `data` 字段数 | 可取消 |", "| --- | --- | ---: | --- |"]
    for event in events:
        flag = ("Yes" if event["cancellable"] else "No") if english else ("是" if event["cancellable"] else "否")
        lines.append(f"| {link(event['name'], event_page(event, english))} | "
                     f"`{event['type']}` | {len(event['fields'])} | {flag} |")
    return lines + [""]


def render_home(data, groups, english):
    count = len(data["events"])
    if english:
        lines = ["# PaperPyBridge Event Wiki", "",
                 f"Reference for **{count} forwardable event classes** in Paper 1.16.5. "
                 f"They use **{data['handler_list_count']} distinct HandlerLists**. "
                 "Each event page lists the Python subscription name and the fields this bridge sends.", "",
                 link("中文版", "Home.md") + " · " + link("Wire format and limits", "Data-Format-en.md")
                 + " · " + link("Python → MC", "Python-to-MC-en.md"), "",
                 "Only chat, player join, and player quit are enabled by default. "
                 "Add other events to `events.include` before subscribing to them.", "",
                 "## Start here", "", "```python", "from paperpybridge import Events", "",
                 '@bridge.on(Events.ASYNC_PLAYER_CHAT)',
                 "def on_chat(event):", '    print(event.message)', "```", "",
                 'You can also subscribe by fully qualified Java class name or use `@bridge.on("*")`. '
                 'The existing `chat`, `join`, and `quit` aliases continue to work.', "",
                 "## Browse by category", "", "| Category | Events |", "| --- | ---: |"]
    else:
        lines = ["# PaperPyBridge 事件 Wiki", "",
                 f"这里收录 Paper 1.16.5 中 **{count} 个可转发的具体事件类**，共使用 "
                 f"**{data['handler_list_count']} 组 HandlerList**。每个事件单独成页，"
                 "列出 Python 订阅名、实际转出的字段和官方 Javadoc。", "",
                 link("English", "Home-en.md") + " · " + link("通用字段、数据格式和限制", "Data-Format.md")
                 + " · " + link("Python → MC 操作", "Python-to-MC.md"), "",
                 "默认只启用聊天、玩家加入和退出事件。要接收其他事件，先将其加入 `events.include`。", "",
                 "## 快速上手", "", "```python", "from paperpybridge import Events", "",
                 '@bridge.on(Events.ASYNC_PLAYER_CHAT)',
                 "def on_chat(event):", '    print(event.message)', "```", "",
                 '也可以用 Java 完整类名订阅，或用 `@bridge.on("*")` 订阅全部事件。'
                 '原有 `chat`、`join`、`quit` 别名继续有效。', "",
                 "## 按类别浏览", "", "| 分类 | 事件数 |", "| --- | ---: |"]
    for group, events in groups.items():
        label = group if english else docs.CATEGORIES_ZH.get(group, group)
        lines.append(f"| {link(label, category_page(group, english))} | {len(events)} |")
    lines.extend(["", "## Notes" if english else "## 阅读说明", "",
                  "This wiki describes the fields emitted by PaperPyBridge. Follow each event page's "
                  "official Javadoc link for trigger conditions and Java behavior. Python receives a "
                  "snapshot and cannot synchronously cancel or modify the original event."
                  if english else
                  "本 Wiki 描述 PaperPyBridge 实际转出的字段。事件触发条件和 Java 行为请看各页的"
                  "官方 Javadoc。Python 收到的是快照，不能同步取消或修改原事件。", ""])
    return lines


def render_format(english):
    lines = ["# Wire format and limits" if english else "# 通用字段、数据格式和限制", "",
             link("Home" if english else "首页", "Home-en.md" if english else "Home.md") + " · " +
             link("中文" if english else "English", "Data-Format.md" if english else "Data-Format-en.md"), "",
             "## Example" if english else "## 示例", "", "```json",
             '{"protocol_version":1,"type":"PlayerMoveEvent","event":"org.bukkit.event.player.PlayerMoveEvent","name":"PlayerMoveEvent","server":"survival","asynchronous":false,"timestamp_ms":1234567890000,"cancelled":false,"player":{"uuid":"...","name":"Steve"},"data":{"from":{"world":"world","x":1,"y":64,"z":2,"yaw":0,"pitch":0}}}',
             "```", ""]
    if english:
        lines.extend([
            "- Always present: `protocol_version`, `type`, `event`, `name`, `server`, `asynchronous`, `timestamp_ms`, `data`.",
            "- `cancelled` appears for cancellable events; `player` appears only when a player is identified.",
            "- A string `data.message` is also copied to top-level `message`.",
            "- `data` comes from supported public no-argument getters. Null or failed getters are omitted.",
            "- At most 24 `data` fields and 4096 bytes; strings are at most 512 characters. Excess tail fields are omitted.",
            "- World, location, block, entity, and item values are summaries, not Bukkit objects.",
            "- The bridge queues events and sends batches of up to 32. Events may be dropped if Python falls behind.",
            "- Python cannot synchronously cancel or modify an event.", "", "## Summary shapes", "",
            "| Type | JSON properties |", "| --- | --- |",
        ])
    else:
        lines.extend([
            "- 总会出现：`protocol_version`、`type`、`event`、`name`、`server`、`asynchronous`、`timestamp_ms`、`data`。",
            "- `cancelled` 仅在可取消事件中出现；`player` 仅在识别到玩家时出现。",
            "- 字符串 `data.message` 还会复制到顶层 `message`。",
            "- `data` 来自受支持的公开无参数 getter；返回空值或调用失败时，该字段缺失。",
            "- `data` 最多 24 个字段、4096 字节；字符串最多 512 字符，超限时删减末尾字段。",
            "- 世界、位置、方块、实体和物品会转成摘要，不是完整 Bukkit 对象。",
            "- 插件将事件排队，每批最多发送 32 条；Python 跟不上时可能丢弃事件。",
            "- Python 不能同步取消或修改原事件。", "", "## 摘要对象", "",
            "| 类型 | JSON 属性 |", "| --- | --- |",
        ])
    lines.extend(["| `world` | `name`, `uuid` |",
                  "| `location` | `world` (optional), `x`, `y`, `z`, `yaw`, `pitch` |" if english else
                  "| `location` | `world`（可选）, `x`, `y`, `z`, `yaw`, `pitch` |",
                  "| `block` | `world`, `x`, `y`, `z`, `type` |",
                  "| `entity` | `uuid`, `type`, `name` (for players) |" if english else
                  "| `entity` | `uuid`, `type`, `name`（玩家时） |",
                  "| `item` | `type`, `amount` |", ""])
    return lines


def render_actions(english):
    if english:
        return [
            "# Python → MC operations", "",
            link("Home", "Home-en.md") + " · " + link("中文", "Python-to-MC.md"), "",
            "The Paper plugin serves authenticated requests at `/rpc`. These methods can be called "
            "without starting the Python event receiver.", "", "```python",
            "from paperpybridge import Bridge", "",
            'bridge = Bridge(token="your-private-token")',
            "players = bridge.online_players()  # list[Player] with uuid and name",
            'title = bridge.send_title(players[0].uuid, "Welcome", "From Python") if players else None',
            'command = bridge.run_command("list")', "```", "",
            "| Method | Return value | Notes |", "| --- | --- | --- |",
            "| `online_players()` | `list[Player]` | Raises `BridgeError` on query failure. |",
            "| `send_title(uuid, title, subtitle="" )` | `OperationResult` | Target must be online; `player_offline` otherwise. |",
            "| `run_command(command)` | `OperationResult` | Console dispatch only for allowed command roots. |", "",
            "`OperationResult.ok` is a boolean; `error` is a code such as `command_not_allowed`. "
            "A successful command result means Paper dispatched it, not that its intended game effect occurred. "
            "Async variants: `aonline_players`, `asend_title`, and `arun_command`.", "",
            "## Command allowlist", "", "```yaml", "actions:", "  allowed-commands:", '    - "list"', "```", "",
            "Add `time` before calling `run_command(\"time set day\")`. Restart Paper after editing its config. "
            "Commands run as the console and must not start with `/`.", "",
        ]
    return [
        "# Python → MC 操作", "",
        link("首页", "Home.md") + " · " + link("English", "Python-to-MC-en.md"), "",
        "Paper 插件通过需要令牌的 `/rpc` 接口处理请求。直接调用这些方法时，不必先启动 Python 事件接收服务。", "",
        "```python", "from paperpybridge import Bridge", "",
        'bridge = Bridge(token="你的私密令牌")',
        "players = bridge.online_players()  # Player(uuid, name) 列表",
        'title = bridge.send_title(players[0].uuid, "欢迎", "来自 Python") if players else None',
        'command = bridge.run_command("list")', "```", "",
        "| 方法 | 返回值 | 说明 |", "| --- | --- | --- |",
        "| `online_players()` | `list[Player]` | 查询失败抛出 `BridgeError`。 |",
        "| `send_title(uuid, title, subtitle="" )` | `OperationResult` | 玩家必须在线，否则返回 `player_offline`。 |",
        "| `run_command(command)` | `OperationResult` | 仅以控制台身份分发白名单中的命令。 |", "",
        "`OperationResult.ok` 是布尔值，`error` 是 `command_not_allowed` 等错误码。"
        "命令返回成功表示 Paper 已分发，不能证明游戏效果符合预期。异步版本为 "
        "`aonline_players`、`asend_title`、`arun_command`。", "",
        "## 命令白名单", "", "```yaml", "actions:", "  allowed-commands:", '    - "list"', "```", "",
        "要调用 `run_command(\"time set day\")`，先加入 `time` 并重启 Paper。"
        "命令以控制台身份执行，不能带前导 `/`。", "",
    ]


def validate(expected):
    actual = {p.name for p in WIKI.glob("*.md")}
    if expected - actual:
        raise SystemExit(f"Missing Wiki pages: {sorted(expected - actual)[:5]}")
    broken = []
    for name in expected:
        page = (WIKI / name).read_text(encoding="utf-8")
        for target in re.findall(r"\[\[([^]|]+)\|[^]]+\]\]", page):
            if target + ".md" not in actual:
                broken.append((name, target))
    if broken:
        raise SystemExit(f"Broken Wiki links: {broken[:5]}")


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--paper-jar", type=Path, default=docs.DEFAULT_PAPER_JAR)
    parser.add_argument("--java-home", type=Path)
    args = parser.parse_args()
    data = docs.extract(args.paper_jar, docs.java_home(args.java_home))
    groups = defaultdict(list)
    for event in data["events"]:
        groups[docs.category(event)].append(event)
    groups = dict(sorted(groups.items()))
    for events in groups.values():
        events.sort(key=lambda event: (event["name"].lower(), event["class"]))
    WIKI.mkdir(exist_ok=True)
    expected = set()
    for english in (False, True):
        home = "Home-en.md" if english else "Home.md"
        fmt = "Data-Format-en.md" if english else "Data-Format.md"
        write(home, render_home(data, groups, english))
        write(fmt, render_format(english))
        actions = "Python-to-MC-en.md" if english else "Python-to-MC.md"
        write(actions, render_actions(english))
        expected.update((home, fmt, actions))
        for group, events in groups.items():
            name = category_page(group, english)
            write(name, render_category(group, events, english))
            expected.add(name)
            for event in events:
                name = event_page(event, english)
                write(name, render_event(event, english))
                expected.add(name)
    sidebar = ["**PaperPyBridge Wiki**", "",
               link("首页", "Home.md") + " · " + link("English", "Home-en.md"), "",
               link("数据格式 / Wire format", "Data-Format.md"), "",
               link("Python → MC 操作 / Operations", "Python-to-MC.md"), "",
               "**事件分类 / Categories**", ""]
    for group in groups:
        sidebar.append("- " + link(docs.CATEGORIES_ZH.get(group, group) + f" / {group}", category_page(group)))
    write("_Sidebar.md", sidebar)
    write("_Footer.md", [f"Paper 1.16.5 · {len(data['events'])} events · " +
                         link("Home", "Home.md") + " · " +
                         link("官方 Javadoc", "https://jd.papermc.io/paper/1.16.5/"), ""])
    expected.update(("_Sidebar.md", "_Footer.md"))
    for name in ({p.name for p in WIKI.glob("Event-*.md")} |
                 {p.name for p in WIKI.glob("Category-*.md")}) - expected:
        (WIKI / name).unlink()
    validate(expected)
    print(f"Generated {len(expected)} Wiki pages: {len(data['events'])} events x 2 languages, "
          f"{len(groups)} categories x 2 languages; links verified")


if __name__ == "__main__":
    main()
