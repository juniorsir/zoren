# Zoren Interactive Studio REPL Manual [Version 3.0]

The **Zoren Interactive Studio REPL (v3.0)** is an enterprise interactive evaluation shell featuring real-time syntax highlighting, multi-line block continuation, live expression evaluation, math and string method pipelines, session persistence, and instant access to Zoren's 14 production AI & distributed backend plugins.

---

## 1. Launching the REPL

Start the interactive shell from any terminal:

```shell
zoren repl
```

```text
⚡ Zoren Interactive Studio [Version 3.0.0 Enterprise]
Target Architecture: AArch64 Native • Full RELRO • SSP • PAC/BTI Active
Type :help for commands, :plugins for AI/backend plugins, :quit to exit.

[1] zoren ❯
```

---

## 2. Interactive Directives & Meta Commands

| Directive | Description | Example |
| :--- | :--- | :--- |
| **`:help [topic]`** | Command reference and topic guidance (`math`, `plugins`, `sys`) | `:help plugins` |
| **`:plugins`** | Catalog of all 14 production plugins with one-line descriptions | `:plugins` |
| **`:flows` / `:fns`** | Lists all custom user-defined flows in the session | `:flows` |
| **`:models`** | Lists all custom models, fields, and ability grants | `:models` |
| **`:vars` / `:env [prefix]`** | Displays all active variables with types and current values | `:vars` |
| **`:inspect <expr>`** | Deep introspection (Type, Value, Byte Size, Hex, Binary) | `:inspect 42` |
| **`:type <expr>`** | Prints the inferred or evaluated type of an expression | `:type "hello"` |
| **`:time <expr>`** | High-resolution nanosecond benchmarking of an expression | `:time fib(20)` |
| **`:compare <e1> vs <e2>`** | Side-by-side benchmark comparison between two expressions | `:compare abs(-42) vs 42` |
| **`:load <file.zor>`** | Ingests and executes definitions from an external Zoren file | `:load test.zor` |
| **`:save <file.zor>`** | Exports all active session variables and flows to a script | `:save session.zor` |
| **`:undo`** | Removes the most recently bound variable from the session | `:undo` |
| **`:sys` / `:perf`** | Displays hardware architecture, security engines, and memory | `:sys` |
| **`:history`** | Displays previous command execution history | `:history` |
| **`:clear` / `:cls`** | Clears the terminal screen | `:clear` |
| **`:reset`** | Clears all session definitions with confirmation | `:reset` |
| **`:quit` / `:q`** | Exits the interactive REPL session | `:quit` |
| **`!cmd` / `:sh cmd`** | Executes an operating system shell command | `!ls -la` |

---

## 3. Mathematical & Bitwise Expression Evaluation

### Operators
- **Arithmetic**: `+`, `-`, `*`, `/` (integer division), `%` (modulo)
- **Logical**: `&&` (AND), `||` (OR), `!` (NOT)
- **Bitwise**: `&` (AND), `|` (OR), `^` (XOR), `~` (NOT), `<<` (left shift), `>>` (right shift)
- **Relational**: `==`, `!=`, `<`, `<=`, `>`, `>=`
- **Compound Assignment**: `+=`, `-=`, `*=`, `/=`, `%=`

### Built-in Mathematical Functions
- `sqrt(x)`: Integer square root (`sqrt(144) => 12`)
- `min(a, b)`, `max(a, b)`: Extrema calculation (`min(15, 42) => 15`)
- `pow(b, e)`: Exponentiation (`pow(2, 8) => 256`)
- `hypot(a, b)`: Euclidean distance $\sqrt{a^2 + b^2}$ (`hypot(3, 4) => 5`)
- `abs(x)`, `square(x)`, `clamp(val, min, max)`
- `PI`, `TAU`, `E` constants

---

## 4. String & Vector Operations

### String Method Chaining
```zoren
[1] zoren ❯ "zoren language".up()
=> [Text]: "ZOREN LANGUAGE"

[2] zoren ❯ "HELLO".low()
=> [Text]: "hello"

[3] zoren ❯ "deep learning".len()
=> [Int]: 13

[4] zoren ❯ "autonomous".contains("auto")
=> [Bool]: true

[5] zoren ❯ "fast runtime".starts_with("fast")
=> [Bool]: true

[6] zoren ❯ "hello world".replace("world", "zoren")
=> [Text]: "hello zoren"
```

### Vector Indexing & Length
```zoren
[7] zoren ❯ bind arr = [10, 20, 30, 40]
✓ bind arr: Vector[Int] = [10, 20, 30, 40]

[8] zoren ❯ arr.len()
=> [Int]: 4

[9] zoren ❯ arr[2]
=> [Int]: 30
```

---

## 5. Control Flow in REPL

### Top-Level and Flow Loops
```zoren
[10] zoren ❯ for i in 0..5 { post("i = ", i) }
i = 0
i = 1
i = 2
i = 3
i = 4

[11] zoren ❯ flex counter = 3
✓ flex counter: Int = 3

[12] zoren ❯ while counter > 0 { post("count: ", counter) counter -= 1 }
count: 3
count: 2
count: 1
```

---

## 6. Accessing AI & Backend Plugins from REPL

All 14 production plugins can be imported interactively:
```zoren
[13] zoren ❯ bring plugins.raft_consensus
✓ Module `plugins.raft_consensus` imported successfully.

[14] zoren ❯ bring plugins.bptree_db
✓ Module `plugins.bptree_db` imported successfully.

[15] zoren ❯ :plugins
Zoren Production Plugins Catalog (plugins/*):
  ├── plugins.agent_swarm      : Multi-agent state consensus & quorum evaluation
  ├── plugins.bptree_db        : High-performance ordered B+ Tree storage & range index
  ├── plugins.circuit_breaker  : Resilience4j/Hystrix fault tolerance state machine
  ...
```
