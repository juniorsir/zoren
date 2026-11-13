# Creating Modules and Plugins in Zoren

This guide explains the Zoren module architecture, how modules and plugins compare, how to combine them, and how you can create and publish your own custom modules and plugins.

---

## 1. Modules vs. Plugins: The Quick Summary

In Zoren, **modules and plugins are powered by the exact same engine under the hood**. Every module or plugin is a native `.zor` file that exports flows and data structures using the `open` keyword.

| Feature | Standard Modules (`std/*`) | Enterprise Plugins (`plugins/*`) | User / Community (`community/*`) |
| :--- | :--- | :--- | :--- |
| **Primary Scope** | Foundational computer science building blocks | Specialized, high-performance distributed systems | Custom user domain logic, proprietary extensions |
| **Examples** | `math`, `fs`, `json`, `rope`, `van_emde_boas` | `jwt_auth`, `raft_consensus`, `vector_hnsw` | `billing_engine`, `custom_metrics` |
| **Typical Size** | Lightweight, zero external dependencies | Enterprise-grade, domain-optimized algorithms | Any size |
| **Import Syntax** | `bring math`<br>`bring rope` | `bring plugins.jwt_auth`<br>`bring plugins.vector_hnsw` | `bring community.my_pkg`<br>`bring my_module` |
| **Storage Location** | `~/.zoren/std/`<br>`/usr/local/share/zoren/std/` | `~/.zoren/plugins/`<br>`/usr/local/share/zoren/plugins/` | `~/.zoren/community/`<br>Local project directory `./` |

---

## 2. Can You Combine Modules and Plugins?

**Yes, completely!** 

Because both modules and plugins compile to the same abstract syntax tree (AST) and machine code:
1. **Plugins can import Modules:** A plugin like `plugins.vector_hnsw` can internally import `bring math` or `bring rope`.
2. **Modules can import other Modules:** `std/wavelet_matrix` can import `bring bitwise`.
3. **User applications can combine both freely:** Your application can import standard library modules, plugins, and your own custom modules all in the same file:

```zoren
// Combining std, plugins, and custom local modules in one application
bring math
bring plugins.jwt_auth
bring plugins.rate_limiter
bring my_custom_service

flow main() -> Int {
    echo("All modules combined and ready!")
    deliver 0
}
```

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
