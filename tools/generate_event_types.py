"""Generate typed Python event constants from the Paper 1.16.5 catalog."""

import argparse
from collections import defaultdict
from pathlib import Path

import generate_event_docs as docs


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--paper-jar", type=Path, default=docs.DEFAULT_PAPER_JAR)
    parser.add_argument("--java-home", type=Path)
    args = parser.parse_args()
    data = docs.extract(args.paper_jar, docs.java_home(args.java_home))
    groups = defaultdict(list)
    for event in data["events"]:
        groups[docs.category(event)].append(event)
    names = [docs.constant_name(event) for event in data["events"]]
    if len(names) != len(set(names)):
        raise SystemExit("Event constant names collide")
    lines = [
        '"""Paper 1.16.5 event names for ``Bridge.on`` and server configuration.',
        "",
        "Generated from the same event catalog as the Wiki. A constant names an event;",
        "it does not enable forwarding. Configure events.include on the Paper server.",
        '"""', "",
        "", "class Events:",
        '    """Fully qualified Java event class names."""', "",
    ]
    for group, events in sorted(groups.items()):
        lines.append(f"    # {group}")
        for event in sorted(events, key=lambda item: docs.constant_name(item)):
            lines.append(f'    {docs.constant_name(event)} = "{event["class"]}"')
        lines.append("")
    target = docs.ROOT / "python/paperpybridge/events.py"
    target.write_text("\n".join(lines).rstrip() + "\n", encoding="utf-8", newline="\n")
    print(f"Generated {len(names)} Python event constants in {target}")


if __name__ == "__main__":
    main()
