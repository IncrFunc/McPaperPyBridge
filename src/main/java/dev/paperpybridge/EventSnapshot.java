package dev.paperpybridge;

import com.google.gson.JsonElement;
import com.google.gson.JsonNull;
import com.google.gson.JsonObject;
import com.google.gson.JsonPrimitive;
import java.lang.reflect.Method;
import java.lang.reflect.Modifier;
import java.nio.charset.StandardCharsets;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.Comparator;
import java.util.List;
import java.util.Map;
import java.util.UUID;
import java.util.concurrent.ConcurrentHashMap;
import org.bukkit.Location;
import org.bukkit.World;
import org.bukkit.block.Block;
import org.bukkit.entity.Entity;
import org.bukkit.entity.Player;
import org.bukkit.event.Cancellable;
import org.bukkit.event.Event;
import org.bukkit.inventory.ItemStack;

/** A bounded, immutable JSON snapshot; Bukkit objects never cross worker threads. */
final class EventSnapshot {
    private static final int MAX_EVENT_BYTES = 4096;
    private static final int MAX_PROPERTIES = 24;
    private static final int MAX_STRING_LENGTH = 512;
    private static final Map<Class<?>, List<Method>> GETTERS = new ConcurrentHashMap<>();

    private EventSnapshot() {}

    static JsonObject capture(Event event, String serverId) {
        Class<?> eventClass = event.getClass();
        String name = eventClass.getSimpleName();
        JsonObject result = new JsonObject();
        result.addProperty("protocol_version", 1);
        result.addProperty("type", legacyType(name));
        result.addProperty("event", eventClass.getName());
        result.addProperty("name", name);
        result.addProperty("server", serverId);
        result.addProperty("asynchronous", event.isAsynchronous());
        result.addProperty("timestamp_ms", System.currentTimeMillis());
        if (event instanceof Cancellable) result.addProperty("cancelled", ((Cancellable) event).isCancelled());
        Player player = findPlayer(event);
        if (player != null) {
            JsonObject identity = new JsonObject();
            identity.addProperty("uuid", player.getUniqueId().toString());
            identity.addProperty("name", player.getName());
            result.add("player", identity);
        }
        JsonObject data = new JsonObject();
        for (Method getter : GETTERS.computeIfAbsent(eventClass, EventSnapshot::getters)) {
            if (data.entrySet().size() >= MAX_PROPERTIES) break;
            try {
                Object value = getter.invoke(event);
                if (value == null) continue;
                JsonElement encoded = encode(value);
                if (encoded == null) continue;
                String property = propertyName(getter.getName());
                data.add(property, encoded);
                if ("message".equals(property) && value instanceof String) {
                    result.addProperty("message", truncate((String) value));
                }
            } catch (ReflectiveOperationException | RuntimeException ignored) {
                // A getter may be unavailable for a particular event state.
            }
        }
        result.add("data", data);
        while (result.toString().getBytes(StandardCharsets.UTF_8).length > MAX_EVENT_BYTES
                && !data.entrySet().isEmpty()) {
            String last = null;
            for (Map.Entry<String, JsonElement> entry : data.entrySet()) last = entry.getKey();
            data.remove(last);
        }
        return result;
    }

    static String legacyType(String name) {
        if ("AsyncPlayerChatEvent".equals(name)) return "chat";
        if ("PlayerJoinEvent".equals(name)) return "join";
        if ("PlayerQuitEvent".equals(name)) return "quit";
        return name;
    }

    private static Player findPlayer(Event event) {
        for (String getterName : new String[] {"getPlayer", "getEntity", "getWhoClicked"}) {
            try {
                Method getter = event.getClass().getMethod(getterName);
                if (Player.class.isAssignableFrom(getter.getReturnType())) {
                    return (Player) getter.invoke(event);
                }
                Object value = getter.invoke(event);
                if (value instanceof Player) return (Player) value;
            } catch (ReflectiveOperationException | RuntimeException ignored) {
                // Most events do not have a player.
            }
        }
        return null;
    }

    private static List<Method> getters(Class<?> eventClass) {
        Method[] methods = eventClass.getMethods();
        Arrays.sort(methods, Comparator.comparing(Method::getName));
        List<Method> selected = new ArrayList<>();
        for (Method method : methods) {
            String name = method.getName();
            if (method.getParameterCount() != 0 || Modifier.isStatic(method.getModifiers())) continue;
            if (!(name.startsWith("get") && name.length() > 3)
                    && !(name.startsWith("is") && name.length() > 2)) continue;
            if ("getClass".equals(name) || "getHandlers".equals(name)
                    || "getEventName".equals(name) || "isAsynchronous".equals(name)
                    || "isCancelled".equals(name) || "getPlayer".equals(name)) continue;
            if (!supported(method.getReturnType())) continue;
            selected.add(method);
        }
        return selected;
    }

    private static boolean supported(Class<?> type) {
        return type.isPrimitive() || Number.class.isAssignableFrom(type)
                || type == Boolean.class || type == Character.class || type == String.class
                || type == UUID.class || type.isEnum() || Entity.class.isAssignableFrom(type)
                || Block.class.isAssignableFrom(type) || World.class.isAssignableFrom(type)
                || Location.class.isAssignableFrom(type) || ItemStack.class.isAssignableFrom(type);
    }

    private static String propertyName(String getter) {
        String stem = getter.startsWith("is") ? getter.substring(2) : getter.substring(3);
        return Character.toLowerCase(stem.charAt(0)) + stem.substring(1);
    }

    private static JsonElement encode(Object value) {
        if (value instanceof String) return new JsonPrimitive(truncate((String) value));
        if (value instanceof Number) return new JsonPrimitive((Number) value);
        if (value instanceof Boolean) return new JsonPrimitive((Boolean) value);
        if (value instanceof Character) return new JsonPrimitive((Character) value);
        if (value instanceof UUID) return new JsonPrimitive(value.toString());
        if (value instanceof Enum<?>) return new JsonPrimitive(((Enum<?>) value).name());
        if (value instanceof World) {
            World world = (World) value;
            JsonObject result = new JsonObject();
            result.addProperty("name", world.getName());
            result.addProperty("uuid", world.getUID().toString());
            return result;
        }
        if (value instanceof Location) {
            Location location = (Location) value;
            JsonObject result = new JsonObject();
            if (location.getWorld() != null) result.addProperty("world", location.getWorld().getName());
            result.addProperty("x", location.getX());
            result.addProperty("y", location.getY());
            result.addProperty("z", location.getZ());
            result.addProperty("yaw", location.getYaw());
            result.addProperty("pitch", location.getPitch());
            return result;
        }
        if (value instanceof Block) {
            Block block = (Block) value;
            JsonObject result = new JsonObject();
            result.addProperty("world", block.getWorld().getName());
            result.addProperty("x", block.getX());
            result.addProperty("y", block.getY());
            result.addProperty("z", block.getZ());
            result.addProperty("type", block.getType().name());
            return result;
        }
        if (value instanceof Entity) {
            Entity entity = (Entity) value;
            JsonObject result = new JsonObject();
            result.addProperty("uuid", entity.getUniqueId().toString());
            result.addProperty("type", entity.getType().name());
            if (entity instanceof Player) result.addProperty("name", ((Player) entity).getName());
            return result;
        }
        if (value instanceof ItemStack) {
            ItemStack item = (ItemStack) value;
            JsonObject result = new JsonObject();
            result.addProperty("type", item.getType().name());
            result.addProperty("amount", item.getAmount());
            return result;
        }
        return JsonNull.INSTANCE;
    }

    private static String truncate(String text) {
        return text.length() <= MAX_STRING_LENGTH ? text : text.substring(0, MAX_STRING_LENGTH);
    }
}

