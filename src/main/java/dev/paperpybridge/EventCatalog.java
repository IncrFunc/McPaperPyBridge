package dev.paperpybridge;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStream;
import java.io.InputStreamReader;
import java.lang.reflect.Modifier;
import java.nio.charset.StandardCharsets;
import java.util.Collections;
import java.util.IdentityHashMap;
import java.util.List;
import java.util.Set;
import org.bukkit.Bukkit;
import org.bukkit.event.Event;
import org.bukkit.event.EventPriority;
import org.bukkit.event.HandlerList;
import org.bukkit.event.Listener;
import org.bukkit.plugin.EventExecutor;
import org.bukkit.plugin.java.JavaPlugin;

/** Registers only the concrete Paper events selected in the plugin configuration. */
final class EventCatalog {
    interface Sink {
        void accept(Event event);
    }

    private EventCatalog() {}

    static int register(JavaPlugin plugin, Listener listener, Sink sink,
                        List<String> included, List<String> excluded) throws IOException {
        InputStream resource = plugin.getResource("paper-events.txt");
        if (resource == null) throw new IOException("paper-events.txt is missing from the plugin JAR");
        Set<HandlerList> registered = Collections.newSetFromMap(new IdentityHashMap<HandlerList, Boolean>());
        EventExecutor executor = (ignored, event) -> sink.accept(event);
        int count = 0;
        try (BufferedReader reader = new BufferedReader(new InputStreamReader(resource, StandardCharsets.UTF_8))) {
            String name;
            while ((name = reader.readLine()) != null) {
                if (name.isEmpty() || name.startsWith("#")) continue;
                try {
                    Class<?> candidate = Class.forName(name, false, Event.class.getClassLoader());
                    if (!Event.class.isAssignableFrom(candidate) || Modifier.isAbstract(candidate.getModifiers())) continue;
                    String simple = candidate.getSimpleName();
                    String alias = EventSnapshot.legacyType(simple);
                    if (!matches(included, simple, name, alias)
                            || matches(excluded, simple, name, alias)) continue;
                    HandlerList handlers = (HandlerList) candidate.getMethod("getHandlerList").invoke(null);
                    if (!registered.add(handlers)) continue;
                    @SuppressWarnings("unchecked")
                    Class<? extends Event> eventClass = (Class<? extends Event>) candidate;
                    Bukkit.getPluginManager().registerEvent(eventClass, listener, EventPriority.MONITOR,
                            executor, plugin, false);
                    count++;
                } catch (ReflectiveOperationException | LinkageError | RuntimeException error) {
                    plugin.getLogger().warning("Skipping event " + name + ": " + error.getClass().getSimpleName());
                }
            }
        }
        return count;
    }

    static boolean matches(List<String> patterns, String simple, String qualified, String alias) {
        return patterns.contains("*") || patterns.contains(simple)
                || patterns.contains(qualified) || patterns.contains(alias);
    }
}
