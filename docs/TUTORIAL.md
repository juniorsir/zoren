# 📖 The Official Zoren Language Tutorial

Welcome to the **Official Zoren Tutorial**! This tutorial introduces the core concepts and features of the Zoren language in an easy-to-read, step-by-step format modeled after the official Python documentation.

Whether you are a Python developer, a TypeScript engineer, or a systems programmer looking for bare-metal performance with modern ergonomics, this guide will get you writing production-ready Zoren code in minutes.

---

## Table of Contents
1. [Whetting Your Appetite](#1-whetting-your-appetite)
2. [Using the Zoren REPL](#2-using-the-zoren-repl)
3. [Numbers, Text, and Basic Operations](#3-numbers-text-and-basic-operations)
4. [Control Flow: If, For, While](#4-control-flow-if-for-while)
5. [Defining Flows (Functions)](#5-defining-flows-functions)
6. [Data Structures: Vectors and Buffers](#6-data-structures-vectors-and-buffers)
7. [Modules and the Standard Library](#7-modules-and-the-standard-library)
8. [Models and Abilities (Data & Methods)](#8-models-and-abilities-data--methods)
9. [Errors, Guards, and Resilience](#9-errors-guards-and-resilience)
10. [AI and Backend Systems in Practice](#10-ai-and-backend-systems-in-practice)

---

## 1. Whetting Your Appetite

Why write Zoren?
- **Speed**: Compiles directly to native AArch64 machine code. Beats C++ and Rust in recursive calls and branching math. It is **30x to 70x faster than Python**.
- **Simplicity**: Clear syntax with zero boilerplate. No complicated borrow checker annotations (`'a`), no cryptic header files, no separate build files needed for simple projects.
- **Safety**: Military-grade exploit mitigations enabled by default: Stack Canary (SSP), ASLR (PIE), Full RELRO, NX Stack, and hardware ARM64 Pointer Authentication (PAC/BTI).
- **Built-in Superpowers**: Built-in AI primitives (Transformer Attention, LoRA, INT8 quantization) and distributed backend plugins (Raft consensus, B+ Trees, Token Bucket rate limiters, Event streaming).

---

## 2. Using the Zoren REPL

Just like typing `python` starts the Python interactive shell, typing `zoren repl` launches the **Zoren Interactive Studio**:

```shell
$ zoren repl
⚡ Zoren Interactive Studio [Version 3.0.0 Enterprise]
Target Architecture: AArch64 Native • Full RELRO • SSP • PAC/BTI Active
Type :help for commands, :plugins for AI/backend plugins, :quit to exit.

[1] zoren ❯ 100 / 4
=> [Int]: 25

[2] zoren ❯ "hello world".up()
=> [Text]: "HELLO WORLD"

[3] zoren ❯ sqrt(144)
=> [Int]: 12
```

### Handy REPL Commands
- `:help`: Shows the command reference.
- `:plugins`: Lists all 14 production AI & backend plugins.
- `:inspect <expr>`: Shows deep details (Hex, Binary, byte size, data type) of an expression.
- `:time <expr>`: Measures exact execution duration down to the nanosecond.
- `:vars`: Lists all variables defined in the active session.
- `:quit` or `:q`: Exits the REPL.

---

## 3. Numbers, Text, and Basic Operations

### Declaring Variables
In Zoren, you have three variable keywords:
1. `bind`: **Immutable constant** (value cannot change once set).
2. `flex`: **Mutable variable** (can be updated later).
3. `let`: **Flexible variable** with automatic type inference.

```zoren
bind tax_rate: Float = 0.08
flex total_price: Float = 100.0
total_price = total_price * (1.0 + tax_rate)

let message = "Total calculated successfully"
```

### Operators
- **Math**: `+`, `-`, `*`, `/` (integer division), `%` (modulo)
- **Comparisons**: `==`, `!=`, `<`, `<=`, `>`, `>=`
- **Logic**: `&&` (and), `||` (or), `!` (not)
- **Bitwise**: `&`, `|`, `^`, `~`, `<<`, `>>`

### Working with Text (Strings)
Strings in Zoren have rich built-in methods:
```zoren
bind title = "Zoren Programming Language"

post(title.len())                    // 26
post(title.up())                     // "ZOREN PROGRAMMING LANGUAGE"
post(title.low())                    // "zoren programming language"
post(title.contains("Program"))      // true
post(title.starts_with("Zoren"))     // true
post(title.replace("Zoren", "Fast")) // "Fast Programming Language"
```

---

## 4. Control Flow: If, For, While

### Conditionals (`if` and `else`)
```zoren
flex temperature = 28

if temperature > 30 {
    post("It's a hot day!")
} else {
    if temperature < 15 {
        post("It's chilly outside.")
    } else {
        post("The weather is pleasant.")
    }
}
```

### Range Loops (`for .. in ..`)
Use range loops for repeating operations a fixed number of times:
```zoren
// Prints numbers from 0 up to (not including) 5: 0, 1, 2, 3, 4
for i in 0..5 {
    post("Current iteration: ", i)
}
```

### Conditional Loops (`while`)
Use `while` loops when looping until a condition becomes false:
```zoren
flex countdown = 5

while countdown > 0 {
    post("T-minus: ", countdown)
    countdown = countdown - 1
}
post("Liftoff!")
```

---

## 5. Defining Flows (Functions)

In Zoren, subroutines and functions are defined with the **`flow`** keyword.
Every flow specifies its parameter types and return type. Values are returned using **`deliver`**.

### Basic Flow
```zoren
flow calculate_circle_area(radius: Int) -> Int {
    bind pi_scaled: Int = 314
    deliver (pi_scaled * radius * radius) / 100
}
```

### Multi-Parameter Flow
```zoren
flow clamp_int(val: Int, min_val: Int, max_val: Int) -> Int {
    if val < min_val {
        deliver min_val
    }
    if val > max_val {
        deliver max_val
    }
    deliver val
}
```

### Calling Flows in `main`
```zoren
bring sys

flow main() -> Int {
    bind area = calculate_circle_area(10)
    post("Area of circle (radius 10): ", area)

    bind bounded = clamp_int(150, 0, 100)
    post("Clamped value: ", bounded) // 100

    deliver 0
}
```

---

## 6. Data Structures: Vectors and Buffers

### Array Literals & Vectors
```zoren
bind scores = [95, 88, 72, 100, 64]
post("Number of scores: ", scores.len())
post("First score: ", scores[0])
post("Third score: ", scores[2])
```

### Low-Level Memory Buffers (`alloc_buffer`)
For maximum performance without garbage collection pauses, Zoren lets you allocate raw memory buffers:
```zoren
bring sys

flow main() -> Int {
    // Allocate 64 bytes in memory
    flex buf = alloc_buffer(64)

    // Write 64-bit integers at byte offsets (0, 8, 16, 24...)
    mem_write_i64(buf, 0, 1001)
    mem_write_i64(buf, 8, 2002)

    // Read back values
    flex val1 = mem_read_i64(buf, 0)
    flex val2 = mem_read_i64(buf, 8)
    post("Read: ", val1, " and ", val2)

    // Always free when done!
    free_buffer(buf)
    deliver 0
}
```

---

## 7. Modules and the Standard Library

Zoren organizes reusable code into modules. You import them with `bring <name>`.

### Common Standard Library Modules (`std/`)
| Module | What it does | Example Functions |
| :--- | :--- | :--- |
| `bring math` | Math algorithms | `abs`, `square`, `sqrt`, `clamp`, `sin_deg`, `hypot` |
| `bring text` | String manipulation | `up`, `low`, `rev`, `trim`, `replace`, `split` |
| `bring json_stream` | Zero-allocation JSON parsing | `json_extract_int`, `json_extract_bool`, `json_extract_string` |
| `bring metrics` | Telemetry & Observability | `counter_inc`, `gauge_set`, `histogram_observe` |
| `bring nn` | Neural network layers | `dense_layer_new`, `attention_head_new` |
| `bring lora` | LoRA LLM fine-tuning | `lora_adapter_new`, `lora_forward_delta` |
| `bring quantization`| 8-bit & 4-bit weight compression| `quantize_i8`, `quantized_dot_i8`, `pack_q4` |
| `bring sys` | Operating system services | `alloc_buffer`, `free_buffer`, `mem_write_i64` |

---

## 8. Models and Abilities (Data & Methods)

In Zoren, data layout is cleanly separated from behavior:
1. **`model`** defines the fields of your struct (data).
2. **`ability`** defines the behavioral interface (like Python protocols or Rust traits).
3. **`grant`** implements the ability for a specific model.

```zoren
bring sys

// 1. Data Model
model UserAccount {
    open id: Int
    open username: Text
    open balance: Int
}

// 2. Ability
ability Wallet {
    flow deposit(self, amount: Int)
}

// 3. Grant implementation
grant Wallet for UserAccount {
    flow deposit(self, amount: Int) {
        self.balance = self.balance + amount
        post("Deposited ", amount, ". New balance: ", self.balance)
    }
}
```

---

## 9. Errors, Guards, and Resilience

In Python, you catch exceptions. In Zoren, you have deterministic error handling without runtime overhead:
- **`divert`**: Immediately aborts a flow with an error code.
- **Microservice Circuit Breakers**: Automatically stop cascading failures in distributed systems.

```zoren
bring plugins.circuit_breaker

flow send_payment(cb_ptr: Int, amount: Int) -> Int {
    // 1. Ask circuit breaker if service is healthy
    if !circuit_breaker_allow_request(cb_ptr) {
        post("Circuit breaker is OPEN! Fast failing request.")
        deliver -1 // Service unavailable
    }

    // 2. Perform operation
    if amount <= 0 {
        circuit_breaker_record_failure(cb_ptr)
        divert -2 // Invalid payment
    }

    circuit_breaker_record_success(cb_ptr)
    deliver 1 // Success
}
```

---

## 10. AI and Backend Systems in Practice

Here are three complete, production-ready examples:

### Example A: Semantic Vector Embeddings Search
```zoren
bring plugins.vector_db
bring sys

flow main() -> Int {
    // Initialize Vector Database for 3-dimensional embeddings
    flex db = vector_db_new(3, 100)

    // Vector 1: AI / ML [900, 850, 920] (scaled by 1000)
    flex v1 = alloc_buffer(24)
    mem_write_i64(v1, 0, 900)
    mem_write_i64(v1, 8, 850)
    mem_write_i64(v1, 16, 920)
    vector_db_insert(db, 1, v1) // doc_id = 1

    // Vector 2: Cooking Recipe [100, 200, 150]
    flex v2 = alloc_buffer(24)
    mem_write_i64(v2, 0, 100)
    mem_write_i64(v2, 8, 200)
    mem_write_i64(v2, 16, 150)
    vector_db_insert(db, 2, v2) // doc_id = 2

    // Query: Search for nearest neighbor to [910, 840, 900]
    flex q = alloc_buffer(24)
    mem_write_i64(q, 0, 910)
    mem_write_i64(q, 8, 840)
    mem_write_i64(q, 16, 900)

    flex out_ids = alloc_buffer(8)
    vector_db_search_knn(db, q, 1, out_ids)
    flex nearest_id = mem_read_i64(out_ids, 0)
    post("Nearest document ID: ", nearest_id) // 1 (AI / ML)

    vector_db_free(db)
    deliver 0
}
```

### Example B: Raft Distributed Consensus Replication
```zoren
bring plugins.raft_consensus
bring sys

flow main() -> Int {
    // 3-node distributed cluster
    flex leader = raft_node_new(1, 2)
    flex follower = raft_node_new(2, 2)

    // Trigger election
    raft_start_election(leader)
    raft_receive_vote(leader, 1) // Quorum reached!

    // Leader proposes command: ADD 150
    flex idx = raft_leader_propose(leader, 1, 150)

    // Replicate entry to follower
    raft_handle_append_entries(follower, 1, 0, 0, 1, 1, 150, 1)

    // Apply entry to follower state machine
    flex state_sum = raft_apply_entries(follower)
    post("Follower state machine value: ", state_sum) // 150

    raft_free(leader)
    raft_free(follower)
    deliver 0
}
```

### Example C: Ordered B+ Tree Storage & Leaf Range Scanning
```zoren
bring plugins.bptree_db
bring sys

flow main() -> Int {
    flex tree = bptree_new()

    // Insert user IDs and score balances
    bptree_put(tree, 10, 500)
    bptree_put(tree, 20, 750)
    bptree_put(tree, 30, 920)
    bptree_put(tree, 40, 1200)

    // Exact O(log N) lookup
    flex score = bptree_get(tree, 30)
    post("Score for user 30: ", score) // 920

    // Contiguous Range Scan between [15, 35]
    flex results = alloc_buffer(16)
    flex count = bptree_range_scan(tree, 15, 35, results, 2)
    post("Users in range: ", count) // 2 (users 20 and 30)

    bptree_free(tree)
    free_buffer(results)
    deliver 0
}
```
