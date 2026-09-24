# PaperPyBridge

[English](README.md) · [更新记录](CHANGELOG.zh-CN.md) · 版本 **0.1.0** · Paper **1.16.5**

PaperPyBridge 由一个可安装的 Python package 和一个轻量的 Paper 1.16.5 插件组成。Python 开发者通过 `import paperpybridge` 订阅 MC 事件、向玩家发消息，不必自己处理 HTTP、令牌鉴权和 JSON 格式。Paper 不直接连接 NapCat；QQ 机器人可以同时使用这个 package 和自己的 OneBot 客户端。

```text
Minecraft/Paper -- 选中的事件 --> Python package / QQ 机器人
Minecraft/Paper <-- 消息、查询、命令 -- Python package
```

## 环境要求

- Paper 1.16.5 服务器。Paper 对此版本推荐 Java 16；插件 JAR 编译为 Java 8 字节码，以便兼容旧运行环境。
- Maven，用于构建插件。
- Python 3.9 或更高版本，用于运行无第三方依赖的 package。

## 快速开始

1. 在本目录运行 `mvn package`，把 `target/paper-py-bridge-0.1.0.jar` 复制到 Paper 服务器的 `plugins` 目录。
2. 启动一次服务器，让它生成 `plugins/PaperPyBridge/config.yml`，然后停止服务器。把 `change-this-secret` 换成私密令牌。未修改占位令牌时，插件会拒绝启动。
3. 运行 `python -m pip install -e .`，把 Python package 安装到本地环境。示例脚本优先读取 `PAPERPY_TOKEN` 环境变量；未设置时读取本项目本地服务端的配置文件。
4. 运行 `python python/example.py`，再启动 Paper。两者在同一台机器时保留默认的本机地址即可。如果分处不同机器，需要配置互相可达的私有地址和 `PAPERPY_TOKEN`；不要将接口直接暴露到公网。
5. 进入服务器发送聊天消息，Python 终端会持续打印聊天事件，游戏里会收到 `Hello from Python!` 回复。

默认只有聊天、玩家进入和离开事件会交给 Python。示例处理聊天事件。如果 Python 未运行，游戏内原有行为仍照常进行，插件会记录投递错误。

## Python package 的用法

```python
from paperpybridge import Bridge, Events

bridge = Bridge(token="你的私密令牌")

@bridge.on(Events.ASYNC_PLAYER_CHAT)
def on_chat(event):
    if event.message == "!py ping":
        return event.reply("[Python] pong")

bridge.start()  # 后台接收事件；关闭时调用 bridge.close()
bridge.broadcast("来自 Python 的消息")
# 在异步 QQ 机器人处理函数中：await bridge.abroadcast("来自 QQ 的消息")
```

独立脚本可用 `bridge.serve_forever()` 代替 `start()`。注册的回调是同步函数，会在接收服务的工作线程中运行。如果你的机器人已有 HTTP 服务，可调用 `bridge.handle(data)` 处理解码后的事件并取得响应字典。主动发消息可用 `bridge.broadcast(text)` 或 `bridge.tell(player_uuid, text)`；`abroadcast` 和 `atell` 是供异步程序调用的封装。

### Python → MC 查询和操作

```python
players = bridge.online_players()  # 返回 Player(uuid, name) 列表
if players:
    result = bridge.send_title(players[0].uuid, "欢迎", "来自 Python")
    print(result.ok, result.error)

result = bridge.run_command("list")
print(result.ok, result.error)
```

`online_players()` 在 Paper 主线程获取在线玩家快照；请求失败会抛出 `BridgeError`。`send_title()` 和 `run_command()` 返回 `OperationResult(ok, error)`；例如玩家离线时 `error` 为 `player_offline`，命令不在白名单时为 `command_not_allowed`。`ok=True` 对命令表示 Paper 已接受并分发命令，不保证命令产生了预期游戏效果。异步 QQ 机器人可用 `aonline_players()`、`asend_title()` 和 `arun_command()`。

命令白名单在 `server/plugins/PaperPyBridge/config.yml` 的 `actions.allowed-commands` 中配置，默认仅允许 `list`。例如要执行 `time set day`，先加入 `time` 并重启 Paper。命令以控制台身份执行，不能带前导 `/`；标题只会发送给在线玩家。

package 接收的第 1 版事件格式如下：

```json
{"protocol_version":1,"type":"chat","server":"survival","player":{"uuid":"...","name":"Steve"},"message":"Hello"}
```

插件默认只注册聊天、玩家加入和退出事件；Wiki 收录所有可按需启用的事件。`Events` 常量使用完整 Java 类名，例如 `Events.ASYNC_PLAYER_CHAT`。`chat`、`join`、`quit` 仍是兼容旧代码的别名。处理函数可以返回 `event.reply(text)`、`Broadcast(text)`、`PlayerMessage(uuid, text)`、动作列表或 `None`。动作在线路上的格式为：

```json
{"type":"player_message","player_uuid":"...","text":"单独回复"}
{"type":"broadcast","text":"发送给全部在线玩家"}
```

现有的异步 QQ 机器人收到指令时，可调用 `await bridge.abroadcast(text)`。NapCat/OneBot 连接始终由 Python 管理。

插件在 Paper 主线程之外发送 HTTP 请求，收到 Python 的动作后切回主线程执行。事件、动作和查询接口都要求共享令牌。内部通信格式带有版本号 `protocol_version: 1`；单次消息上限为 16 KiB，每个事件响应最多执行 20 个动作，每个动作的文字不超过 512 字符。发送队列有容量限制，避免 Python 处理缓慢时无限积压。

## 检查

```sh
mvn package
python -m pip wheel --no-deps -w dist .
python -m unittest discover -s python -v
```

构建和 Python 测试覆盖编译、package 安装元数据及 HTTP 接口约定，但不能代替真实 Paper 1.16.5 服务器上的验证。正式使用前，请按快速开始在你的服务器里试运行。

## 项目结构

- `src/main/java/dev/paperpybridge/PaperPyBridgePlugin.java`：Paper 事件监听、HTTP 客户端和动作接口。
- `src/main/resources/config.yml`：地址、令牌、超时和服务器标识。
- `python/paperpybridge/`：可复用的 Python package。
- `python/example.py`：可直接运行的示例。
- `python/test_bridge.py`：行为与 HTTP 鉴权测试。


## 本地 Paper 1.16.5 服务端

`server/` 目录被 Git 忽略，**不会随仓库上传**。本地测试时请自行创建该目录，放入名为 `paper-1.16.5-794.jar` 的 Paper 1.16.5 JAR。安装 Java 16 并加入 `PATH`，或者把便携版 JDK 放入 `server/runtime/`。首次启动前请阅读并接受 [Minecraft EULA](https://aka.ms/MinecraftEULA)，然后将 `server/eula.txt` 设置为 `eula=true`。

在项目根目录运行 `./start-server.ps1`。脚本会以 1–2 GiB 内存启动服务端。进入游戏时连接 `localhost:25565`，在服务端控制台输入 `stop` 可正常关闭。


## 事件订阅

插件启动时扫描随 JAR 附带的 Paper 1.16.5 事件清单，但只注册 `events.include` 选中的事件。默认选中 `AsyncPlayerChatEvent`、`PlayerJoinEvent`、`PlayerQuitEvent`。要增加事件，在 `server/plugins/PaperPyBridge/config.yml` 的 `events.include` 中加入简单类名或完整类名；`"*"` 表示全部事件，`events.exclude` 可排除指定事件。修改配置后重启 Paper。Python 常量只是事件名称，不会自动启用服务端转发。

事件会先在触发线程上生成 JSON 快照，再由后台按最多 32 条一批发送到 Python。非玩家事件没有 `player`；每条包含 `type`（聊天等旧别名或简单类名）、`event`（完整类名）、`name`、`server`、`timestamp_ms`、`asynchronous`、可选 `cancelled`、`player`、`message` 和 `data`。`data` 只包含安全、有限大小的基础字段及方块、实体、位置等摘要，不是 Bukkit 对象的完整复制。事件无法在 Python 侧同步取消或修改。发送队列有容量上限；Python 跟不上时会丢弃事件并在日志中提示。

```python
from paperpybridge import Events

@bridge.on(Events.PLAYER_MOVE)  # 先在 events.include 中启用 PlayerMoveEvent
def on_move(event):
    print(event.player.name if event.player else None, event.data.get("to"))

@bridge.on("*")
def on_any_event(event):
    print(event.event, event.data)
```

本地运行 `python python/example.py` 会持续打印收到的聊天事件。

`bridge.on()` 也接受完整类名和 `Events` 常量，例如 `Events.PLAYER_MOVE`。旧的 `@bridge.on("chat")` 不用改。`@bridge.on("*")` 只接收服务端已启用的事件。高频事件（移动、方块物理等）会产生大量消息，建议按需配置 `events.include`。

## 事件参考文档

[事件 Wiki 首页](wiki/Home.md)提供分类目录和 333 个事件的独立页面，也有英文版、通用数据格式页、侧边栏和页脚。版本化的 `wiki/` 目录还收录了 [Python → MC 操作指南](wiki/Python-to-MC.md)。

[Paper 1.16.5 全部可转发事件与 Python 字段](docs/events.zh-CN.md)按类别列出 333 个具体事件类。每项包含完整类名、Python 常量、可取消状态、实际 `data` 字段与 Paper 官方 Javadoc 链接。全量启用时这些事件共使用 292 组处理器列表；当前默认配置只注册 3 组。

修改 `EventSnapshot` 或升级 Paper API 后，先运行 `mvn package`，再运行 `python tools/generate_event_types.py`、`python tools/generate_event_docs.py` 和 `python tools/generate_wiki.py` 重建事件常量、中英文文档及 Wiki。生成器需要本地 `server/cache/patched_1.16.5.jar` 和 `server/runtime` 的 Java 16；也可显式传入 `--paper-jar`、`--java-home`。
