package dev.paperpybridge;

import com.google.gson.JsonArray;
import com.google.gson.JsonElement;
import com.google.gson.JsonObject;
import com.google.gson.JsonParser;
import com.sun.net.httpserver.HttpExchange;
import com.sun.net.httpserver.HttpServer;
import java.io.ByteArrayOutputStream;
import java.io.IOException;
import java.io.InputStream;
import java.io.OutputStream;
import java.net.HttpURLConnection;
import java.net.InetSocketAddress;
import java.net.URL;
import java.nio.charset.StandardCharsets;
import java.security.MessageDigest;
import java.util.ArrayList;
import java.util.Comparator;
import java.util.HashSet;
import java.util.Locale;
import java.util.UUID;
import java.util.List;
import java.util.Set;
import java.util.concurrent.ExecutionException;
import java.util.concurrent.Future;
import java.util.concurrent.TimeoutException;
import java.util.concurrent.BlockingQueue;
import java.util.concurrent.ArrayBlockingQueue;
import java.util.concurrent.atomic.AtomicLong;
import java.util.concurrent.ExecutorService;
import java.util.concurrent.Executors;
import java.util.concurrent.TimeUnit;
import org.bukkit.Bukkit;
import org.bukkit.entity.Player;
import org.bukkit.event.Event;
import org.bukkit.event.Listener;
import org.bukkit.plugin.java.JavaPlugin;

public final class PaperPyBridgePlugin extends JavaPlugin implements Listener {
    private static final int MAX_BODY_BYTES = 16384;
    private static final int MAX_ACTIONS = 20;
    private ExecutorService outboundWorkers;
    private BlockingQueue<JsonObject> eventQueue;
    private final AtomicLong lastWarningMs = new AtomicLong();
    private List<String> includedEvents;
    private List<String> excludedEvents;
    private Set<String> allowedCommands;
    private ExecutorService inboundWorkers;
    private HttpServer actionServer;
    private volatile boolean stopping;
    private String token;
    private String serverId;
    private String pythonUrl;
    private int connectTimeoutMs;
    private int readTimeoutMs;

    @Override
    public void onEnable() {
        saveDefaultConfig();
        token = getConfig().getString("token", "");
        if (token == null || token.isEmpty() || "change-this-secret".equals(token)) {
            getLogger().severe("Set a private token in plugins/PaperPyBridge/config.yml before starting.");
            Bukkit.getPluginManager().disablePlugin(this);
            return;
        }
        serverId = getConfig().getString("server-id", "survival");
        pythonUrl = getConfig().getString("python-url", "http://127.0.0.1:8765/minecraft/events");
        connectTimeoutMs = getConfig().getInt("connect-timeout-ms", 2000);
        readTimeoutMs = getConfig().getInt("read-timeout-ms", 3000);

        includedEvents = getConfig().getStringList("events.include");
        excludedEvents = getConfig().getStringList("events.exclude");
        allowedCommands = new HashSet<>();
        for (String command : getConfig().getStringList("actions.allowed-commands")) {
            if (command.matches("[A-Za-z0-9_:-]+")) {
                allowedCommands.add(command.toLowerCase(Locale.ROOT));
            } else {
                getLogger().warning("Ignoring invalid allowed command name: " + command);
            }
        }
        eventQueue = new ArrayBlockingQueue<>(2048);
        outboundWorkers = Executors.newSingleThreadExecutor();
        outboundWorkers.execute(this::runEventPump);
        inboundWorkers = Executors.newFixedThreadPool(2);
        try {
            String host = getConfig().getString("action-server.host", "127.0.0.1");
            int port = getConfig().getInt("action-server.port", 8766);
            actionServer = HttpServer.create(new InetSocketAddress(host, port), 0);
            actionServer.createContext("/actions", this::handleActions);
            actionServer.createContext("/rpc", this::handleRpc);
            actionServer.setExecutor(inboundWorkers);
            actionServer.start();
        } catch (IOException error) {
            getLogger().severe("Cannot start action server: " + error.getMessage());
            Bukkit.getPluginManager().disablePlugin(this);
            return;
        }
        try {
            int count = EventCatalog.register(this, this, this::queueEvent,
                    includedEvents, excludedEvents);
            getLogger().info("Registered " + count + " Paper event handler lists.");
        } catch (IOException error) {
            getLogger().severe("Cannot register Paper events: " + error.getMessage());
            Bukkit.getPluginManager().disablePlugin(this);
            return;
        }
        getLogger().info("Python action endpoint listening on "
                + actionServer.getAddress().getHostString() + ":" + actionServer.getAddress().getPort());
    }

    @Override
    public void onDisable() {
        stopping = true;
        if (actionServer != null) actionServer.stop(0);
        if (inboundWorkers != null) inboundWorkers.shutdownNow();
        if (outboundWorkers != null) outboundWorkers.shutdownNow();
    }

    private void queueEvent(Event event) {
        if (stopping || eventQueue == null || !shouldForward(event)) return;
        JsonObject snapshot = EventSnapshot.capture(event, serverId);
        if (!eventQueue.offer(snapshot)) warnThrottled("Python event queue is full; events were dropped.");
    }

    private boolean shouldForward(Event event) {
        String name = event.getClass().getSimpleName();
        String qualified = event.getClass().getName();
        String alias = EventSnapshot.legacyType(name);
        boolean included = EventCatalog.matches(includedEvents, name, qualified, alias);
        return included && !EventCatalog.matches(excludedEvents, name, qualified, alias);
    }

    private void runEventPump() {
        JsonObject pending = null;
        while (!stopping) {
            try {
                JsonObject first = pending != null ? pending : eventQueue.poll(100, TimeUnit.MILLISECONDS);
                pending = null;
                if (first == null) continue;
                JsonArray batch = new JsonArray();
                batch.add(first);
                Thread.sleep(15); // Coalesce bursts without blocking a Paper event thread.
                while (batch.size() < 32) {
                    JsonObject next = eventQueue.poll();
                    if (next == null) break;
                    batch.add(next);
                    if (batchRequest(batch).toString().getBytes(StandardCharsets.UTF_8).length > MAX_BODY_BYTES) {
                        batch.remove(batch.size() - 1);
                        pending = next;
                        break;
                    }
                }
                postEvent(batchRequest(batch));
            } catch (InterruptedException error) {
                Thread.currentThread().interrupt();
                return;
            }
        }
    }

    private static JsonObject batchRequest(JsonArray events) {
        JsonObject payload = new JsonObject();
        payload.addProperty("protocol_version", 1);
        payload.add("events", events);
        return payload;
    }

    private void warnThrottled(String message) {
        long now = System.currentTimeMillis();
        long previous = lastWarningMs.get();
        if (now - previous >= 10000 && lastWarningMs.compareAndSet(previous, now)) {
            getLogger().warning(message);
        }
    }

    private void postEvent(JsonObject payload) {
        HttpURLConnection connection = null;
        try {
            connection = (HttpURLConnection) new URL(pythonUrl).openConnection();
            connection.setRequestMethod("POST");
            connection.setDoOutput(true);
            connection.setConnectTimeout(connectTimeoutMs);
            connection.setReadTimeout(readTimeoutMs);
            connection.setRequestProperty("Content-Type", "application/json; charset=utf-8");
            connection.setRequestProperty("Authorization", "Bearer " + token);
            byte[] bytes = payload.toString().getBytes(StandardCharsets.UTF_8);
            try (OutputStream output = connection.getOutputStream()) {
                output.write(bytes);
            }
            if (connection.getResponseCode() != 200) {
                warnThrottled("Python returned HTTP " + connection.getResponseCode());
                return;
            }
            JsonObject response = parseObject(readLimited(connection.getInputStream()));
            if (!isProtocolV1(response)) {
                getLogger().warning("Python returned an unsupported protocol version.");
                return;
            }
            scheduleActions(response);
        } catch (Exception error) {
            if (!stopping) warnThrottled("Cannot deliver events to Python: " + error.getMessage());
        } finally {
            if (connection != null) connection.disconnect();
        }
    }

    private void handleActions(HttpExchange exchange) throws IOException {
        try {
            if (!"POST".equals(exchange.getRequestMethod())) {
                respond(exchange, 405, "Method not allowed");
                return;
            }
            String provided = exchange.getRequestHeaders().getFirst("Authorization");
            String expected = "Bearer " + token;
            if (provided == null || !MessageDigest.isEqual(
                    provided.getBytes(StandardCharsets.UTF_8), expected.getBytes(StandardCharsets.UTF_8))) {
                respond(exchange, 401, "Unauthorized");
                return;
            }
            JsonObject body = parseObject(readLimited(exchange.getRequestBody()));
            if (!isProtocolV1(body) || !body.has("actions") || !body.get("actions").isJsonArray()) {
                respond(exchange, 400, "Expected protocol version 1 and actions array");
                return;
            }
            scheduleActions(body);
            respond(exchange, 202, "Accepted");
        } catch (Exception error) {
            respond(exchange, 400, "Invalid request");
        } finally {
            exchange.close();
        }
    }

    private void handleRpc(HttpExchange exchange) throws IOException {
        try {
            if (!"POST".equals(exchange.getRequestMethod())) {
                respond(exchange, 405, "Method not allowed");
                return;
            }
            String provided = exchange.getRequestHeaders().getFirst("Authorization");
            String expected = "Bearer " + token;
            if (provided == null || !MessageDigest.isEqual(
                    provided.getBytes(StandardCharsets.UTF_8), expected.getBytes(StandardCharsets.UTF_8))) {
                respond(exchange, 401, "Unauthorized");
                return;
            }
            JsonObject request;
            try {
                request = parseObject(readLimited(exchange.getRequestBody()));
            } catch (IOException | RuntimeException error) {
                respondJson(exchange, 400, rpcError("invalid_request"));
                return;
            }
            if (!isProtocolV1(request)) {
                respondJson(exchange, 400, rpcError("unsupported_protocol"));
                return;
            }
            Future<JsonObject> task;
            try {
                task = Bukkit.getScheduler().callSyncMethod(this, () -> executeRpc(request));
            } catch (IllegalStateException error) {
                respondJson(exchange, 503, rpcError("server_stopping"));
                return;
            }
            try {
                respondJson(exchange, 200, task.get(5, TimeUnit.SECONDS));
            } catch (TimeoutException error) {
                task.cancel(false);
                respondJson(exchange, 503, rpcError("server_busy"));
            } catch (InterruptedException error) {
                task.cancel(false);
                Thread.currentThread().interrupt();
                respondJson(exchange, 503, rpcError("server_stopping"));
            } catch (ExecutionException error) {
                getLogger().warning("Python RPC failed: " + error.getCause());
                respondJson(exchange, 500, rpcError("internal_error"));
            }
        } finally {
            exchange.close();
        }
    }

    private JsonObject executeRpc(JsonObject request) {
        try {
            String operation = requiredString(request, "operation", 40, false);
            if ("online_players".equals(operation)) {
                JsonObject result = rpcSuccess();
                JsonArray players = new JsonArray();
                List<Player> online = new ArrayList<>(Bukkit.getOnlinePlayers());
                online.sort(Comparator.comparing(Player::getName, String.CASE_INSENSITIVE_ORDER));
                for (Player player : online) {
                    JsonObject item = new JsonObject();
                    item.addProperty("uuid", player.getUniqueId().toString());
                    item.addProperty("name", player.getName());
                    players.add(item);
                }
                result.add("players", players);
                return result;
            }
            if ("send_title".equals(operation)) {
                UUID id = UUID.fromString(requiredString(request, "player_uuid", 36, false));
                String title = requiredString(request, "title", 128, false);
                String subtitle = request.has("subtitle")
                        ? requiredString(request, "subtitle", 128, true) : "";
                Player player = Bukkit.getPlayer(id);
                if (player == null || !player.isOnline()) return rpcError("player_offline");
                player.sendTitle(title, subtitle, 10, 70, 20);
                return rpcSuccess();
            }
            if ("run_command".equals(operation)) {
                String command = requiredString(request, "command", 256, false).trim();
                if (command.startsWith("/") || command.matches(".*[\\r\\n\\t\\x00-\\x1F].*")) {
                    return rpcError("invalid_command");
                }
                String root = command.split(" ", 2)[0].toLowerCase(Locale.ROOT);
                if (!allowedCommands.contains(root)) return rpcError("command_not_allowed");
                try {
                    return Bukkit.dispatchCommand(Bukkit.getConsoleSender(), command)
                            ? rpcSuccess() : rpcError("command_not_found");
                } catch (RuntimeException error) {
                    getLogger().warning("Whitelisted command failed: " + root);
                    return rpcError("command_failed");
                }
            }
            return rpcError("unknown_operation");
        } catch (IllegalArgumentException | IllegalStateException error) {
            return rpcError("invalid_arguments");
        }
    }

    private static String requiredString(JsonObject object, String key, int maxLength, boolean allowEmpty) {
        if (!object.has(key) || !object.get(key).isJsonPrimitive()
                || !object.getAsJsonPrimitive(key).isString()) {
            throw new IllegalArgumentException(key);
        }
        String value = object.get(key).getAsString();
        if (value.length() > maxLength || (!allowEmpty && value.trim().isEmpty())) {
            throw new IllegalArgumentException(key);
        }
        return value;
    }

    private static JsonObject rpcSuccess() {
        JsonObject result = new JsonObject();
        result.addProperty("protocol_version", 1);
        result.addProperty("ok", true);
        return result;
    }

    private static JsonObject rpcError(String code) {
        JsonObject result = new JsonObject();
        result.addProperty("protocol_version", 1);
        result.addProperty("ok", false);
        result.addProperty("error", code);
        return result;
    }

    private static void respondJson(HttpExchange exchange, int status, JsonObject body) throws IOException {
        byte[] bytes = body.toString().getBytes(StandardCharsets.UTF_8);
        exchange.getResponseHeaders().set("Content-Type", "application/json; charset=utf-8");
        exchange.sendResponseHeaders(status, bytes.length);
        try (OutputStream output = exchange.getResponseBody()) {
            output.write(bytes);
        }
    }

    private void scheduleActions(JsonObject body) {
        if (stopping || !isEnabled()) return;
        if (!body.has("actions") || !body.get("actions").isJsonArray()) return;
        JsonArray actions = body.getAsJsonArray("actions");
        int count = Math.min(actions.size(), MAX_ACTIONS);
        for (int index = 0; index < count; index++) {
            JsonElement element = actions.get(index);
            if (!element.isJsonObject()) continue;
            JsonObject action = element.getAsJsonObject();
            try {
                Bukkit.getScheduler().runTask(this, () -> applyAction(action));
            } catch (IllegalStateException error) {
                return;
            }
        }
    }

    private void applyAction(JsonObject action) {
        try {
            String type = action.get("type").getAsString();
            String text = action.get("text").getAsString();
            if (text.length() > 512) return;
            if ("broadcast".equals(type)) {
                Bukkit.broadcastMessage(text);
            } else if ("player_message".equals(type)) {
                UUID id = UUID.fromString(action.get("player_uuid").getAsString());
                Player player = Bukkit.getPlayer(id);
                if (player != null) player.sendMessage(text);
            }
        } catch (RuntimeException error) {
            getLogger().warning("Ignoring invalid action from Python.");
        }
    }

    private static JsonObject parseObject(byte[] bytes) {
        JsonElement value = new JsonParser().parse(new String(bytes, StandardCharsets.UTF_8));
        if (!value.isJsonObject()) throw new IllegalArgumentException("Expected JSON object");
        return value.getAsJsonObject();
    }

    private static boolean isProtocolV1(JsonObject body) {
        try {
            return body.get("protocol_version").getAsInt() == 1;
        } catch (RuntimeException error) {
            return false;
        }
    }

    private static byte[] readLimited(InputStream input) throws IOException {
        ByteArrayOutputStream output = new ByteArrayOutputStream();
        byte[] buffer = new byte[4096];
        int total = 0;
        int count;
        while ((count = input.read(buffer)) != -1) {
            total += count;
            if (total > MAX_BODY_BYTES) throw new IOException("Request body too large");
            output.write(buffer, 0, count);
        }
        return output.toByteArray();
    }

    private static void respond(HttpExchange exchange, int status, String body) throws IOException {
        byte[] bytes = body.getBytes(StandardCharsets.UTF_8);
        exchange.getResponseHeaders().set("Content-Type", "text/plain; charset=utf-8");
        exchange.sendResponseHeaders(status, bytes.length);
        try (OutputStream output = exchange.getResponseBody()) {
            output.write(bytes);
        }
    }
}

