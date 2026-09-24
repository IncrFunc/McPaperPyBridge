"""Generate bilingual bridge event reference from the exact Paper 1.16.5 API."""

import argparse
import json
import os
import re
import subprocess
import tempfile
from collections import defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
EVENT_LIST = ROOT / "src/main/resources/paper-events.txt"
JAVA_SOURCE = ROOT / "tools/EventDocExtractor.java"
CLASSES = ROOT / "target/classes"
DEFAULT_PAPER_JAR = ROOT / "server/cache/patched_1.16.5.jar"
CATEGORIES_ZH = {
    "block": "方块", "command": "命令", "enchantment": "附魔", "entity": "实体",
    "hanging": "悬挂实体", "inventory": "物品栏", "packet": "网络包", "player": "玩家",
    "profile": "玩家资料", "raid": "袭击", "server": "服务端", "vehicle": "载具",
    "weather": "天气", "world": "世界",
}
SHAPES_ZH = {
    "string": "字符串", "number": "数字", "boolean": "布尔值", "world": "世界摘要",
    "location": "位置摘要", "block": "方块摘要", "entity": "实体摘要", "item": "物品摘要",
}
SHAPES_EN = {
    "string": "string", "number": "number", "boolean": "boolean", "world": "world summary",
    "location": "location summary", "block": "block summary", "entity": "entity summary", "item": "item summary",
}


def java_home(explicit):
    if explicit:
        return Path(explicit)
    runtime = ROOT / "server/runtime"
    for candidate in sorted(runtime.glob("*/bin/javac.exe")):
        return candidate.parent.parent
    if os.environ.get("JAVA_HOME"):
        return Path(os.environ["JAVA_HOME"])
    raise SystemExit("Java JDK not found; pass --java-home")


def extract(paper_jar, home):
    if not paper_jar.is_file():
        raise SystemExit(f"Paper JAR not found: {paper_jar}")
    if not CLASSES.is_dir():
        raise SystemExit("Build the plugin first with mvn package")
    executable = ".exe" if os.name == "nt" else ""
    javac = home / "bin" / f"javac{executable}"
    java = home / "bin" / f"java{executable}"
    with tempfile.TemporaryDirectory(prefix="paper-event-docs-") as temporary:
        classpath = os.pathsep.join((str(paper_jar), str(CLASSES)))
        subprocess.run([str(javac), "-cp", classpath, "-d", temporary, str(JAVA_SOURCE)], check=True)
        runtime_classpath = os.pathsep.join((temporary, classpath))
        result = subprocess.run(
            [str(java), "-cp", runtime_classpath, "dev.paperpybridge.EventDocExtractor", str(EVENT_LIST)],
            check=True, capture_output=True, text=True, encoding="utf-8",
        )
    data = json.loads(result.stdout)
    if data["skipped"]:
        raise SystemExit(f"Event extraction skipped classes: {data['skipped']}")
    if data["candidate_count"] != 353 or len(data["events"]) < 300:
        raise SystemExit("Unexpected Paper 1.16.5 event catalog; check the API version")
    return data


def category(event):
    return event["class"].split(".event.", 1)[1].split(".", 1)[0]


def event_anchor(event):
    return "event-" + event["class"].lower().replace(".", "-")


def javadoc_url(event):
    return "https://jd.papermc.io/paper/1.16.5/" + event["class"].replace(".", "/") + ".html"


def constant_name(event):
    """Stable Python identifier for a fully qualified Paper event class."""
    name = event["name"].removesuffix("Event")
    name = re.sub(r"(.)([A-Z][a-z]+)", r"\1_\2", name)
    name = re.sub(r"([a-z0-9])([A-Z])", r"\1_\2", name).upper()
    if event["class"] == "com.destroystokyo.paper.event.player.PlayerLocaleChangeEvent":
        name = "PAPER_" + name
    return name


def render(data, chinese):
    groups = defaultdict(list)
    for event in data["events"]:
        groups[category(event)].append(event)
    for values in groups.values():
        values.sort(key=lambda event: (event["name"].lower(), event["class"]))
    total = len(data["events"])
    if chinese:
        lines = [
            "# PaperPyBridge 事件参考：Paper 1.16.5", "",
            f"本页列出 **{total} 个可转发的具体事件类**，来自插件内的 `paper-events.txt` 和当前 `EventSnapshot` 序列化规则。",
            f"它们共使用 **{data['handler_list_count']} 组 HandlerList**；共享 HandlerList 的事件类只注册一次监听器，因此这个数字小于事件类数量。",
            "默认仅转发聊天、玩家加入和退出事件；其他事件需要加入 Paper 插件配置的 `events.include`。Wiki 中列出某事件不代表已启用。",
            "事件含义和触发时机请查看每项的 Paper 官方 Javadoc；本页重点说明 Python 实际接收的字段。", "",
            "## 通用事件格式", "",
            "```json", '{"protocol_version":1,"type":"PlayerMoveEvent","event":"org.bukkit.event.player.PlayerMoveEvent","name":"PlayerMoveEvent","server":"survival","asynchronous":false,"timestamp_ms":1234567890000,"cancelled":false,"player":{"uuid":"...","name":"Steve"},"data":{"from":{"world":"world","x":1,"y":64,"z":2,"yaw":0,"pitch":0},"to":{"world":"world","x":2,"y":64,"z":2,"yaw":0,"pitch":0}}}', "```", "",
            "- `protocol_version`、`type`、`event`、`name`、`server`、`asynchronous`、`timestamp_ms` 和 `data` 总会生成。",
            "- `cancelled` 仅对实现 `Cancellable` 的事件生成；`player` 只有实际关联到玩家时生成；字符串 `data.message` 还会复制到顶层 `message`。",
            "- `type` 是 Python 订阅名。聊天、加入、退出仍使用 `chat`、`join`、`quit`；其他事件使用简单类名。也可用完整类名或 `*` 订阅。",
            "- `data` 字段来自公开、无参数、返回受支持类型的 `get...()`/`is...()` 方法。getter 返回 `null` 或抛错时字段缺失。每条最多 24 个字段、4096 字节；字符串最多 512 字符，超限时删减末尾字段。",
            "- 世界、位置、方块、实体和物品是**摘要对象**，不是完整 Bukkit 对象。Python 不能同步取消或修改已经转发的事件。", "",
            "| 摘要类型 | JSON 属性 |", "| --- | --- |",
            "| `world` | `name`, `uuid` |",
            "| `location` | `world`（可选）, `x`, `y`, `z`, `yaw`, `pitch` |",
            "| `block` | `world`, `x`, `y`, `z`, `type` |",
            "| `entity` | `uuid`, `type`, `name`（玩家时） |",
            "| `item` | `type`, `amount` |", "",
            "## 分类索引", "", "| 分类 | 事件数 |", "| --- | ---: |",
        ]
    else:
        lines = [
            "# PaperPyBridge Event Reference: Paper 1.16.5", "",
            f"This page lists **{total} concrete event classes** that the plugin can forward, based on its `paper-events.txt` catalog and current `EventSnapshot` serialization rules.",
            f"They share **{data['handler_list_count']} HandlerLists**. Classes sharing a list need only one listener registration, so this count is smaller than the class count.",
            "Only chat, player join, and player quit are forwarded by default. Add other events to the Paper plugin's `events.include`; listing an event here does not enable it.",
            "Follow each event's official Paper Javadoc link for its meaning and trigger conditions. This page documents what Python actually receives.", "",
            "## Common event format", "",
            "```json", '{"protocol_version":1,"type":"PlayerMoveEvent","event":"org.bukkit.event.player.PlayerMoveEvent","name":"PlayerMoveEvent","server":"survival","asynchronous":false,"timestamp_ms":1234567890000,"cancelled":false,"player":{"uuid":"...","name":"Steve"},"data":{"from":{"world":"world","x":1,"y":64,"z":2,"yaw":0,"pitch":0},"to":{"world":"world","x":2,"y":64,"z":2,"yaw":0,"pitch":0}}}', "```", "",
            "- `protocol_version`, `type`, `event`, `name`, `server`, `asynchronous`, `timestamp_ms`, and `data` are always produced.",
            "- `cancelled` appears only for `Cancellable` events; `player` appears only when a player is actually associated. String `data.message` is also copied to top-level `message`.",
            "- `type` is the Python subscription name. Chat, join, and quit keep the aliases `chat`, `join`, and `quit`; other events use the simple class name. You can also subscribe by full class name or `*`.",
            "- `data` comes from public zero-argument `get...()`/`is...()` methods with supported return types. Null or failing getters are omitted. A snapshot has at most 24 fields and 4096 bytes; strings are limited to 512 characters, and trailing fields are removed if needed.",
            "- Worlds, locations, blocks, entities, and items become **summary objects**, not live Bukkit objects. Python cannot synchronously cancel or mutate a forwarded event.", "",
            "| Summary type | JSON properties |", "| --- | --- |",
            "| `world` | `name`, `uuid` |",
            "| `location` | optional `world`, `x`, `y`, `z`, `yaw`, `pitch` |",
            "| `block` | `world`, `x`, `y`, `z`, `type` |",
            "| `entity` | `uuid`, `type`, optional player `name` |",
            "| `item` | `type`, `amount` |", "",
            "## Package index", "", "| Package category | Events |", "| --- | ---: |",
        ]
    for group in sorted(groups):
        label = CATEGORIES_ZH.get(group, group) + f" (`{group}`)" if chinese else f"`{group}`"
        lines.append(f"| [{label}](#category-{group}) | {len(groups[group])} |")
    for group in sorted(groups):
        label = CATEGORIES_ZH.get(group, group) + f" / {group}" if chinese else group
        lines.extend(["", f'<a id="category-{group}"></a>', f"## {label}", ""])
        if chinese:
            lines.extend(["| 事件 | Python `type` | `data` 候选字段数 | 可取消 |", "| --- | --- | ---: | --- |"])
        else:
            lines.extend(["| Event | Python `type` | possible `data` fields | Cancellable |", "| --- | --- | ---: | --- |"])
        for event in groups[group]:
            yes = "是" if chinese else "Yes"
            no = "否" if chinese else "No"
            lines.append(f"| [{event['name']}](#{event_anchor(event)}) | `{event['type']}` | {len(event['fields'])} | {yes if event['cancellable'] else no} |")
        for event in groups[group]:
            full = event["class"]
            link = javadoc_url(event)
            lines.extend(["", f'<a id="{event_anchor(event)}"></a>', f"### {event['name']}", ""])
            if chinese:
                lines.extend([
                    f"- Java 类：`{full}`；父类：`{event['parent']}`。",
                    f"- Python 订阅：`@bridge.on(\"{event['type']}\")`；也可使用 `Events.{constant_name(event)}`。",
                    f"- 可取消：{'是' if event['cancellable'] else '否'}；关联玩家：{'可能有，取决于实际对象' if event['player_possible'] else '无已知玩家 getter'}。",
                    f"- [Paper 官方 Javadoc]({link})：事件含义、触发条件和 Java API。",
                ])
            else:
                lines.extend([
                    f"- Java class: `{full}`; parent: `{event['parent']}`.",
                    f"- Python subscription: `@bridge.on(\"{event['type']}\")`; `Events.{constant_name(event)}` also works.",
                    f"- Cancellable: {'yes' if event['cancellable'] else 'no'}; player: {'possible, depending on the runtime object' if event['player_possible'] else 'no known player getter'}.",
                    f"- [Official Paper Javadoc]({link}) for meaning, trigger conditions, and Java API.",
                ])
            lines.append("")
            if event["fields"]:
                if chinese:
                    lines.extend(["| `data` 字段 | JSON 类型 | Java getter | Java 返回类型 |", "| --- | --- | --- | --- |"])
                else:
                    lines.extend(["| `data` field | JSON type | Java getter | Java return type |", "| --- | --- | --- | --- |"])
                for field in event["fields"]:
                    shape = (SHAPES_ZH if chinese else SHAPES_EN).get(field["json_type"], field["json_type"])
                    lines.append(f"| `{field['name']}` | {shape} | `{field['getter']}` | `{field['java_type']}` |")
            else:
                lines.append("没有可序列化的 `data` 字段；仍会收到通用事件字段。" if chinese else "No serializable possible `data` fields; common event fields are still sent.")
    lines.append("")
    return "\n".join(lines)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--paper-jar", type=Path, default=DEFAULT_PAPER_JAR)
    parser.add_argument("--java-home", type=Path)
    args = parser.parse_args()
    data = extract(args.paper_jar, java_home(args.java_home))
    docs = ROOT / "docs"
    docs.mkdir(exist_ok=True)
    for filename, chinese in (("events.zh-CN.md", True), ("events.md", False)):
        with (docs / filename).open("w", encoding="utf-8", newline="\n") as stream:
            stream.write(render(data, chinese))
    print(f"Generated {len(data['events'])} event pages in each language; "
          f"{data['handler_list_count']} HandlerLists, {data['candidate_count']} candidates")


if __name__ == "__main__":
    main()
