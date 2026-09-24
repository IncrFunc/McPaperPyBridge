# Changelog

[简体中文](CHANGELOG.zh-CN.md)

## v0.1.0

- Added a Paper 1.16.5 plugin and Python package for authenticated, versioned communication.
- Forwarded selected Paper events to Python; chat, join, and quit are enabled by default. The event catalog and constants cover 333 event classes.
- Added player messages, broadcasts, online-player queries, titles, and allowlisted console command dispatch from Python.
- Added bilingual README files and event Wiki pages.

Python receives event snapshots and cannot synchronously cancel or change the original Paper event. Command success means Paper accepted the dispatch; it does not guarantee the command's intended effect.
