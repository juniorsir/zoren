# Zoren Command Line Interface (CLI) Reference

The `zoren` CLI platform provides project management, code formatting, security auditing, binary materialization, interactive evaluation, static analysis, and native compilation.

---

## 1. Primary Toolchain Commands

### `zoren new <project_name>`
- **Purpose:** Scaffolds a standard Zoren workspace with `manifest.zor` and `src/main.zor`.
- **Example:** `zoren new my_app`

### `zoren repl`
- **Purpose:** Starts the live Interactive Studio REPL v2.0 with real-time syntax highlighting, tab-completion, and live expression evaluation.
- **Example:** `zoren repl`

### `zoren doctor [path] [--json] [--color|--no-color]`
- **Purpose:** Runs Zoren Doctor static analysis for type narrowing, memory allocation hoisting, security taint analysis, and circular dependency detection.
- **Example:** `zoren doctor .`

### `zoren fmt <file.zor>`
- **Purpose:** Deterministically formats Zoren source code in-place.
- **Example:** `zoren fmt src/main.zor`

### `zoren audit [path]` / `zoren audit --credits`
- **Purpose:** Audits security capability flow graphs (`SystemCap`, `NetworkCap`) and verifies Ed25519 authorship signatures (`--credits`).
- **Example:** `zoren audit --credits ~/.zoren/bin/zsentinel`

### `zoren check [path]`
- **Purpose:** Runs static linter rule analysis (`Z6xxx`) and naming convention checks.
- **Example:** `zoren check .`

### `zoren doc [path]`
- **Purpose:** Generates HTML and Markdown API documentation from source doc comments (`##!`).
- **Example:** `zoren doc .`

### `zoren forge [path|package]`
- **Purpose:** Compiles, Merkle-verifies, and materializes capability-bound native binaries into `~/.zoren/bin/`.
- **Example:** `zoren forge .`

### `zoren web <file.zor> [options]`
- **Purpose:** Compiles Zoren source code directly into WebAssembly (`.wasm`), generates WebAssembly Text (`.wat`), modern HTML5 runner page, and JavaScript bridge (`zoren_web.js`).
- **Flags:**
  - `-o <out.wasm>`: Output WebAssembly binary path
  - `--serve`: Automatically starts local HTTP web server after compilation
  - `--port <number>`: Port for HTTP server (default: `8080`)
- **Example:** `zoren web src/main.zor --serve --port 8080`

### `zoren serve [dir] [--port 8080]`
- **Purpose:** Starts an embedded high-speed HTTP development server with automatic MIME-type detection (`application/wasm`, `text/html`, `application/javascript`) and CORS support.
- **Example:** `zoren serve projects/zoren_web/dist --port 8080`

### `zoren lsp`
- **Purpose:** Starts the background Language Server Protocol (LSP) daemon for IDE editor intelligence (VS Code, Neovim, Helix).
- **Example:** `zoren lsp`

---

## 2. Interactive Studio REPL Directives (`:command`)

| Directive | Purpose | Example |
| :--- | :--- | :--- |
| **`:type <expr>`** | Inspect expression type and memory layout. | `:type 42` $ightarrow$ `Int (8 bytes)` |
| **`:time <expr>`** | Benchmark expression execution latency ($\mu$s/ns). | `:time square(100)` |
| **`:time --repeat N <expr>`** | Run benchmark N times and calculate min/max/avg. | `:time --repeat 1000 15 * 8` |
| **`:vars [filter]`** / **`:env`** | Inspect active session variables and types. | `:vars` or `:vars p1` |
| **`:modules`** / **`:mods`** | List all available standard library modules. | `:modules` |
| **`:doc <symbol>`** | View built-in documentation for functions and types. | `:doc abs` |
| **`:undo`** | Revert the last variable binding. | `:undo` |
| **`:ast <expr>`** | Display Abstract Syntax Tree for an expression. | `:ast 10 + 20` |
| **`:asm <expr>`** | Display target AArch64 machine assembly. | `:asm 15 * 8` |
| **`:history`** | Show session command history. | `:history` |
| **`:save <file.zor>`** | Export active session variables to a `.zor` script. | `:save session.zor` |
| **`:load <file.zor>`** | Load and execute an external `.zor` script atomically. | `:load math.zor` |
| **`:clear`** / **`:cls`** | Clear terminal screen without resetting variables. | `:clear` |
| **`:reset`** | Reset session variables. | `:reset` |
| **`! <cmd>`** / **`:sh <cmd>`** | Execute a terminal shell command. | `! ls` or `! git status` |
| **`:quit`** / **`:q`** | Exit the REPL. | `:q` |
| **`? <symbol>`** / **`<symbol>?`** | Quick docstring lookup. | `?square` |

---

## 3. Compiler Compilation Options (`zoren <file.zor>`)

| Option Flag | Purpose | Example |
| :--- | :--- | :--- |
| `-o <output>` | Output executable name. | `zoren main.zor -o app` |
| `-O1`, `-O2`, `-O3` | Set optimization pass levels. | `zoren main.zor -O3` |
| `--target <triple>` | Cross-compilation target (`wasm32-unknown-wasi`, `aarch64-unknown-linux`). | `zoren main.zor --target wasm32-unknown-wasi` |
| `--web` | Target WebAssembly and web browser environment. | `zoren main.zor --web -o app.wasm` |
| `--emit-wat` | Emit human-readable WebAssembly Text representation (`.wat`). | `zoren main.zor --emit-wat` |
| `--direct-elf` | Direct 64-bit ELF binary writer (0 external linkers). | `zoren main.zor --direct-elf -o app` |
| `--thin-lto` / `--lto` | Link-Time Optimization (ThinLTO / Full LTO). | `zoren main.zor -O3 --lto` |
| `--pgo-use <file>` | Profile-Guided Optimization using `.zprof` profile data. | `zoren main.zor --pgo-use profile.zprof` |
| `--emit-hir` / `--dump-cfg` / `--dump-ssa` | Intermediate Representation debugging dumps. | `zoren main.zor --dump-ssa` |
| `--dump-allocations` | Print detailed Chamber memory allocation traces. | `zoren main.zor --dump-allocations` |
