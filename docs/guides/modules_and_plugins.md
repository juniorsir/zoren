# 🧩 Zoren Unified Module Architecture

In Zoren, **everything is a Module**. All standard library components and enterprise subsystems are built using the exact same native `.zor` format and can be imported directly and interchangeably.

---

## 1. Unified Design Philosophy

Rather than treating "plugins" as a separate, complex foreign system, Zoren unifies all standard library utilities, distributed algorithms, security mechanisms, and user packages under a **single cohesive module system**:

- **Direct Imports:** You can import any module directly by name:
  ```zoren
  bring math
  bring rope
  bring jwt_auth
  bring raft_consensus
  bring vector_hnsw
  ```
- **Namespaced Aliases (Optional):** If you prefer to explicitly categorize imports in your codebase, namespaced paths like `bring plugins.jwt_auth` and `bring std.rope` are fully supported aliases.
- **Zero Configuration:** Every module compiles directly to native AArch64 machine code with full RELRO, PAC/BTI, and stack protection.

| Category | Typical Scope | Direct Import | Namespaced Alias |
| :--- | :--- | :--- | :--- |
| **Core Utilities** | Math, Strings, File System, Networking, Ropes | `bring math`<br>`bring rope` | `bring std.math`<br>`bring std.rope` |
| **Enterprise Subsystems** | Raft Consensus, JWT Auth, Vector HNSW, B+ Tree | `bring jwt_auth`<br>`bring raft_consensus` | `bring plugins.jwt_auth`<br>`bring plugins.raft_consensus` |
| **Custom User Modules** | Project services, domain business logic | `bring my_service` | `bring components.my_service` |

---

## 2. Using Modules in the Interactive REPL

The Zoren REPL (`zoren repl`) fully reflects this unified architecture:

1. **View the Catalog:** Type `:modules` (or `:plugins`) to inspect the catalog of available data structures, security modules, distributed consensus engines, and AI indices.
2. **Auto-Importing by Name:** Simply type any module's name directly in the REPL session:
   ```zoren
   [1] zoren ❯ jwt_auth
   ✓ Module `jwt_auth` imported successfully.
     Tip: in Zoren source files, load modules using `bring jwt_auth`.

   [2] zoren ❯ rope
   ✓ Module `rope` imported successfully.
     Tip: in Zoren source files, load modules using `bring rope`.
   ```
3. **No More False Bind Errors:** If you enter a module name, Zoren recognizes it immediately as a module rather than giving an undeclared identifier error.

---

## 3. How Zoren Resolves `bring` Imports

When you write `bring <target>`:

- Dots (`.`) in the module name are translated into directory separators (`/`). For example, `bring plugins.jwt_auth` looks for `plugins/jwt_auth.zor`.
- Zoren searches the following paths in order:
  1. **Current project directory:** `./<target>.zor` (e.g. `./my_module.zor` or `./plugins/my_plugin.zor`)
  2. **Relative parent directories:** `../<target>.zor`
  3. **User global plugins directory:** `~/.zoren/plugins/<name>.zor`
  4. **System plugins directory:** `/usr/local/share/zoren/plugins/<name>.zor`
  5. **User global stdlib directory:** `~/.zoren/std/<name>.zor`
  6. **System stdlib directory:** `/usr/local/share/zoren/std/<name>.zor`
  7. **User community directory:** `~/.zoren/community/<name>.zor`

---

## 4. Step-by-Step: Creating Your Own Custom Module

Creating a module in Zoren takes less than 30 seconds.

### Step 1: Create the Module File
Create a new file called `string_utils.zor`:

```zoren
// string_utils.zor - Custom Module

// 'open' exports this flow so other files can call it
open flow shout(msg: Text) -> Text {
    deliver str_concat(msg, "!!!")
}

open flow repeat_twice(msg: Text) -> Text {
    deliver str_concat(msg, msg)
}

// Private helper: flows without 'open' are internal to this file
flow secret_salt() -> Text {
    deliver "secret_key_999"
}
```

### Step 2: Import and Use It
In your main application file (`app.zor` in the same directory):

```zoren
// app.zor
bring string_utils

flow main() -> Int {
    bind result = shout("Hello Zoren")
    echo(result) // Outputs: Hello Zoren!!!
    deliver 0
}
```

Run your application:
```bash
zoren app.zor
```

---

## 5. Step-by-Step: Creating a Reusable Plugin

A plugin is simply a module organized under the `plugins/` namespace or directory.

### Step 1: Create the Plugin in a `plugins/` folder
Create `plugins/metrics_collector.zor`:

```zoren
// plugins/metrics_collector.zor - Custom Plugin

open flow create_counter(initial_value: Int) -> Int {
    deliver initial_value
}

open flow increment_counter(current: Int, step: Int) -> Int {
    deliver current + step
}
```

### Step 2: Import It via the `plugins.` Namespace

```zoren
// service.zor
bring plugins.metrics_collector

flow main() -> Int {
    bind counter = create_counter(100)
    bind updated = increment_counter(counter, 5)
    echo("Counter value:")
    echo(updated) // Outputs: 105
    deliver 0
}
```

---

## 6. Making Your Module/Plugin Available Globally (System-Wide)

If you want your custom module or plugin to be usable from **any directory** on your machine or inside the interactive REPL without copying files around:

### For a Custom Standard Library Module:
Copy it to your user stdlib cache:
```bash
mkdir -p ~/.zoren/std
cp my_custom_module.zor ~/.zoren/std/
```
Now, in any folder on your machine, simply write:
```zoren
bring my_custom_module
```

### For a Custom Plugin:
Copy it to your user plugins cache:
```bash
mkdir -p ~/.zoren/plugins
cp my_plugin.zor ~/.zoren/plugins/
```
Now, from any folder or project:
```zoren
bring plugins.my_plugin
```

---

## 7. Using Custom Modules & Plugins in the Interactive REPL

Start the Zoren REPL:
```bash
zoren repl
```

To load any custom or built-in plugin directly into the REPL session:
```zoren
[1] zoren ❯ plugins.jwt_auth
⚡ Loaded plugin `plugins.jwt_auth` into session.

[2] zoren ❯ bring plugins.metrics_collector
✔ Module `plugins.metrics_collector` imported successfully.
```

---

## 8. Best Practices for Authoring Zoren Modules

1. **Use `open` for Public API:** Mark all functions and models intended for external use with `open flow` and `open model`.
2. **Explicit Type Signatures:** Always specify input and output types (`flow calculate(x: Int) -> Int`).
3. **Explicit Deliver:** Ensure every code path exits with `deliver <val>`.
4. **Memory Hygiene:** If your module allocates native memory buffers using `alloc_buffer(size)`, always provide a corresponding cleanup flow (e.g. `destroy(ptr)` calling `free_buffer(ptr)`).
5. **No Global State Leakage:** Encapsulate state inside models or allocated structures rather than relying on uncontained mutable globals.
