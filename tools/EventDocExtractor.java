package dev.paperpybridge;

import com.google.gson.JsonArray;
import com.google.gson.JsonObject;
import java.io.BufferedReader;
import java.lang.reflect.Method;
import java.lang.reflect.Modifier;
import java.nio.charset.StandardCharsets;
import java.nio.file.Files;
import java.nio.file.Paths;
import java.util.Collections;
import java.util.IdentityHashMap;
import java.util.LinkedHashMap;
import java.util.List;
import java.util.Map;
import java.util.Set;
import org.bukkit.block.Block;
import org.bukkit.entity.Entity;
import org.bukkit.event.Cancellable;
import org.bukkit.event.Event;
import org.bukkit.event.HandlerList;
import org.bukkit.inventory.ItemStack;
import org.bukkit.Location;
import org.bukkit.World;

/** Reflects the same Paper API and getter selection used by the plugin. */
public final class EventDocExtractor {
    private EventDocExtractor() {}

    public static void main(String[] args) throws Exception {
        Method selectGetters = EventSnapshot.class.getDeclaredMethod("getters", Class.class);
        selectGetters.setAccessible(true);
        JsonArray events = new JsonArray();
        JsonArray skipped = new JsonArray();
        Set<HandlerList> lists = Collections.newSetFromMap(new IdentityHashMap<HandlerList, Boolean>());
        int candidates = 0;
        try (BufferedReader reader = Files.newBufferedReader(Paths.get(args[0]), StandardCharsets.UTF_8)) {
            String className;
            while ((className = reader.readLine()) != null) {
                if (className.isEmpty() || className.startsWith("#")) continue;
                candidates++;
                try {
                    Class<?> type = Class.forName(className, false, Event.class.getClassLoader());
                    if (!Event.class.isAssignableFrom(type) || Modifier.isAbstract(type.getModifiers())) continue;
                    HandlerList handlers = (HandlerList) type.getMethod("getHandlerList").invoke(null);
                    lists.add(handlers);
                    JsonObject item = new JsonObject();
                    String simpleName = type.getSimpleName();
                    item.addProperty("name", simpleName);
                    item.addProperty("class", type.getName());
                    item.addProperty("type", EventSnapshot.legacyType(simpleName));
                    item.addProperty("parent", type.getSuperclass().getName());
                    item.addProperty("cancellable", Cancellable.class.isAssignableFrom(type));
                    item.addProperty("player_possible", hasAccessor(type, "getPlayer")
                            || hasAccessor(type, "getEntity") || hasAccessor(type, "getWhoClicked"));
                    item.addProperty("handler_list_owner", type.getMethod("getHandlerList").getDeclaringClass().getName());
                    JsonArray fields = new JsonArray();
                    @SuppressWarnings("unchecked")
                    List<Method> getters = (List<Method>) selectGetters.invoke(null, type);
                    Map<String, Method> unique = new LinkedHashMap<>();
                    for (Method getter : getters) {
                        String methodName = getter.getName();
                        String stem = methodName.startsWith("is") ? methodName.substring(2) : methodName.substring(3);
                        String field = Character.toLowerCase(stem.charAt(0)) + stem.substring(1);
                        unique.put(field, getter);
                    }
                    for (Map.Entry<String, Method> entry : unique.entrySet()) {
                        Method getter = entry.getValue();
                        JsonObject field = new JsonObject();
                        field.addProperty("name", entry.getKey());
                        field.addProperty("getter", getter.getName() + "()");
                        field.addProperty("java_type", getter.getReturnType().getTypeName());
                        field.addProperty("json_type", jsonType(getter.getReturnType()));
                        field.addProperty("declared_in", getter.getDeclaringClass().getName());
                        fields.add(field);
                    }
                    item.add("fields", fields);
                    events.add(item);
                } catch (ReflectiveOperationException | LinkageError | RuntimeException error) {
                    JsonObject failure = new JsonObject();
                    failure.addProperty("class", className);
                    failure.addProperty("reason", error.getClass().getSimpleName());
                    skipped.add(failure);
                }
            }
        }
        JsonObject result = new JsonObject();
        result.addProperty("api", "Paper 1.16.5");
        result.addProperty("candidate_count", candidates);
        result.addProperty("handler_list_count", lists.size());
        result.add("events", events);
        result.add("skipped", skipped);
        System.out.println(result);
    }

    private static boolean hasAccessor(Class<?> type, String name) {
        try {
            type.getMethod(name);
            return true;
        } catch (NoSuchMethodException error) {
            return false;
        }
    }

    private static String jsonType(Class<?> type) {
        if (type == String.class || type == java.util.UUID.class || type == Character.class
                || type == char.class || type.isEnum()) return "string";
        if (type == boolean.class || type == Boolean.class) return "boolean";
        if (type.isPrimitive() || Number.class.isAssignableFrom(type)) return "number";
        if (World.class.isAssignableFrom(type)) return "world";
        if (Location.class.isAssignableFrom(type)) return "location";
        if (Block.class.isAssignableFrom(type)) return "block";
        if (Entity.class.isAssignableFrom(type)) return "entity";
        if (ItemStack.class.isAssignableFrom(type)) return "item";
        return "unknown";
    }
}
