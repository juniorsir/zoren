# 🧩 Zoren Unified Module Architecture

In Zoren, **everything is a Module**. All standard utilities, distributed algorithms, data structures, and enterprise engines are native `.zor` files imported directly by name with `bring <module_name>`.

---

## 1. Unified Design Philosophy

Zoren eliminates the artificial split between "modules" and "plugins". Everything is part of the unified **Zoren Module Ecosystem**:

- **Direct Imports:** Import every module directly by its simple name:
  ```zoren
  bring math
  bring rope
  bring jwt_auth
  bring raft_consensus
  bring vector_hnsw
  bring cuckoo_hash_map
  ```
- **Zero Configuration:** Every module compiles directly to native AArch64 machine code with full RELRO, PAC/BTI, and stack canary protection.

| Category | Typical Scope | Direct Import |
| :--- | :--- | :--- |
| **Core Primitives** | Math, Text, File System, Network | `bring math`<br>`bring fs` |
| **Data Structures** | Rope, Van Emde Boas, Wavelet Matrix, Heaps | `bring rope`<br>`bring van_emde_boas` |
| **Enterprise Subsystems** | Raft Consensus, JWT Auth, Vector HNSW, B+ Tree | `bring jwt_auth`<br>`bring raft_consensus` |
| **Serialization** | Snappy, Zstandard, Parquet, Arrow, Cap'n Proto | `bring zstandard_frame`<br>`bring snappy_framed` |
| **Custom User Modules** | Project services, domain business logic | `bring string_utils`<br>`bring my_service` |

---

## 2. Using Modules in the Interactive REPL

The Zoren REPL (`zoren repl`) fully reflects this unified architecture:

1. **View the Catalog:** Type `:modules` to inspect the categorized catalog of all available data structures, security modules, distributed consensus engines, and AI indices.
2. **Auto-Importing by Name:** Simply type any module's name directly in the REPL session:
   ```zoren
   [1] zoren ❯ jwt_auth
   ✓ Module `jwt_auth` imported successfully.
     Tip: in Zoren source files, load modules directly using `bring jwt_auth`.

   [2] zoren ❯ rope
   ✓ Module `rope` imported successfully.
     Tip: in Zoren source files, load modules directly using `bring rope`.
   ```
3. **No More Bind Errors:** If you enter a module name, Zoren recognizes it immediately as a module rather than giving an undeclared identifier error.

---

## 3. How Zoren Resolves `bring` Imports

When you write `bring <module_name>`:

Zoren searches the following paths in order:
1. **Current project directory:** `./<module_name>.zor`
2. **Relative parent directories:** `../<module_name>.zor`
3. **Global Standard Library:** `~/.zoren/std/<module_name>.zor` or `std/<module_name>.zor`
4. **Global Enterprise Modules:** `~/.zoren/plugins/<module_name>.zor` or `plugins/<module_name>.zor`
5. **Global Community Packages:** `~/.zoren/community/<module_name>.zor`
6. **System share directories:** `/usr/local/share/zoren/std/` and `/usr/local/share/zoren/plugins/`

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
    post(result) // Outputs: Hello Zoren!!!
    deliver 0
}
```

Run your application:
```bash
zoren app.zor -o app && ./app
```

---

## 5. Making Your Module Available Globally (System-Wide)

To make your custom module usable from **any directory** on your machine or inside the interactive REPL without copying files around:

Copy it to your user module cache:
```bash
mkdir -p ~/.zoren/std
cp string_utils.zor ~/.zoren/std/
```

Now, from any project directory or inside the REPL, simply write:
```zoren
bring string_utils
```

---

## 6. Best Practices for Authoring Zoren Modules

1. **Use `open` for Public API:** Mark all functions and models intended for external use with `open flow` and `open model`.
2. **Explicit Type Signatures:** Always specify input and output types (`flow calculate(x: Int) -> Int`).
3. **Explicit Deliver:** Ensure every code path exits with `deliver <val>`.
4. **Memory Hygiene:** If your module allocates native memory buffers using `alloc_buffer(size)`, always provide a corresponding cleanup flow (e.g. `destroy(ptr)` calling `free_buffer(ptr)`).
5. **No Global State Leakage:** Encapsulate state inside models or allocated structures rather than relying on uncontained mutable globals.

---

## 7. Distributing Modules with ZorPack

Ready to share your module with the world? Check out the **[ZorPack Package Management Guide](./package_management.md)** to learn how to:
- Publish cryptographically sealed `.zpkg` bundles using `zoren publish`.
- Install registry and Git packages with `zoren add <pkg>`.
- Leverage zero-bloat caching and capability security graphs.
