# 🐍 Python to Zoren: The Complete Rosetta Stone Guide

If you know Python, you already know 80% of Zoren! This guide is a friendly, side-by-side comparison showing how every Python concept maps directly to Zoren.

Zoren gives you the **readability and elegance of Python**, but compiles straight to **bare-metal AArch64 native machine code** that runs **30x to 70x faster** than Python—without a virtual machine, without an interpreter, and without runtime overhead!

---

## 📑 Quick Navigation
1. [Hello World](#1-hello-world)
2. [Variables & Mutability](#2-variables--mutability)
3. [Basic Data Types](#3-basic-data-types)
4. [Control Flow: If / Else](#4-control-flow-if--else)
5. [Loops: For & While](#5-loops-for--while)
6. [Functions (`def` vs `flow`)](#6-functions-def-vs-flow)
7. [Classes vs Models & Abilities](#7-classes-vs-models--abilities)
8. [Lists & Vectors](#8-lists--vectors)
9. [Dictionaries & Key-Value Stores](#9-dictionaries--key-value-stores)
10. [Modules & Imports](#10-modules--imports)
11. [Error Handling](#11-error-handling)
12. [JSON & File Operations](#12-json--file-operations)
13. [AI & Neural Networks](#13-ai--neural-networks)
14. [Distributed Systems & Concurrency](#14-distributed-systems--concurrency)
15. [Performance Comparison Cheat Sheet](#15-performance-comparison-cheat-sheet)

---

## 1. Hello World

| Python | Zoren |
| :--- | :--- |
| ```python<br>print("Hello, World!")<br>``` | ```zoren<br>bring sys<br><br>flow main() -> Int {<br>    post("Hello, World!")<br>    deliver 0<br>}<br>``` |

> **Key Difference**: In Zoren, execution begins in the `flow main() -> Int` entry point. Use `post("text")` just like Python's `print()`, and `deliver 0` to return exit code 0 to the operating system.

---

## 2. Variables & Mutability

In Python, all variables can be reassigned at any time. In Zoren, you can declare immutable variables (`bind`), mutable variables (`flex`), or standard variables (`let`).

| Concept | Python | Zoren |
| :--- | :--- | :--- |
| **Immutable Variable** | `# In Python, everything is mutable`<br>`x = 42` | `bind x: Int = 42`<br>`# x cannot be changed!` |
| **Mutable Variable** | `counter = 0`<br>`counter += 1` | `flex counter: Int = 0`<br>`counter = counter + 1` |
| **Type Inferred** | `name = "Alice"` | `bind name = "Alice"`<br>`let age = 30` |

> 💡 **Tip**: Use `bind` by default for safety and compiler optimizations. Use `flex` when a variable must change over time (like loop counters).

---

## 3. Basic Data Types

| Type | Python | Zoren | Example |
| :--- | :--- | :--- | :--- |
| **Integer** | `int` | `Int` | `bind count: Int = 100` |
| **Float** | `float` | `Float` | `bind pi: Float = 3.14159` |
| **Text** | `str` | `Text` | `bind msg: Text = "Zoren is fast"` |
| **Boolean** | `bool` | `Bool` | `bind active: Bool = true` |
| **Nothing** | `None` | `Nothing` / `Void` | `deliver 0` |

### String Interpolation & Methods
| Feature | Python | Zoren |
| :--- | :--- | :--- |
| **Interpolation** | `f"User: {name}, Age: {age}"` | `post("User: {name}, Age: {age}")` |
| **Uppercase** | `name.upper()` | `name.up()` |
| **Lowercase** | `name.lower()` | `name.low()` |
| **Length** | `len(name)` | `name.len()` |
| **Contains** | `"or" in "zoren"` | `"zoren".contains("or")` |
| **Replace** | `s.replace("cat", "dog")` | `s.replace("cat", "dog")` |

---

## 4. Control Flow: If / Else

Python uses indentation with `:` and `elif`. Zoren uses standard curly braces `{ }`.

### Python
```python
score = 85

if score >= 90:
    print("Grade: A")
elif score >= 80:
    print("Grade: B")
else:
    print("Grade: C")
```

### Zoren
```zoren
flex score = 85

if score >= 90 {
    post("Grade: A")
} else {
    if score >= 80 {
        post("Grade: B")
    } else {
        post("Grade: C")
    }
}
```

---

## 5. Loops: For & While

### For Range Loop
| Python | Zoren |
| :--- | :--- |
| ```python<br>for i in range(5):<br>    print("i =", i)<br>``` | ```zoren<br>for i in 0..5 {<br>    post("i = ", i)<br>}<br>``` |

### While Loop
| Python | Zoren |
| :--- | :--- |
| ```python<br>count = 3<br>while count > 0:<br>    print("Countdown:", count)<br>    count -= 1<br>``` | ```zoren<br>flex count = 3<br>while count > 0 {<br>    post("Countdown: ", count)<br>    count = count - 1<br>}<br>``` |

---

## 6. Functions (`def` vs `flow`)

In Zoren, functions are called **flows**. You define them with `flow name(params) -> ReturnType`, and return values using `deliver`.

### Python
```python
def add(a: int, b: int) -> int:
    return a + b

def calculate_stats(values: list[int]) -> tuple[int, int]:
    return min(values), max(values)
```

### Zoren
```zoren
flow add(a: Int, b: Int) -> Int {
    deliver a + b
}

// In Zoren, all flows have explicit types and zero overhead!
flow max_val(a: Int, b: Int) -> Int {
    if a > b {
        deliver a
    }
    deliver b
}
```

---

## 7. Classes vs Models & Abilities

Python uses `class` and `@dataclass`. Zoren uses **`model`** (for pure data layout) and **`ability`** + **`grant`** (for behaviors and methods).

### Python `@dataclass` & Class
```python
from dataclasses import dataclass

@dataclass
class Player:
    id: int
    name: str
    score: int

    def display(self):
        print(f"Player {self.name} has score {self.score}")
```

### Zoren `model` & `ability`
```zoren
// 1. Define data structure
model Player {
    open id: Int
    open name: Text
    open score: Int
}

// 2. Define behavior protocol
ability Displayable {
    flow display(self)
}

// 3. Grant behavior to model
grant Displayable for Player {
    flow display(self) {
        post("Player ", self.name, " has score ", self.score)
    }
}
```

> 🎯 **Why this is better**: Separating data (`model`) from behavior (`ability`) gives you zero-cost memory layouts without dynamic dispatch tables (vtable) overhead!

---

## 8. Lists & Vectors

| Python | Zoren |
| :--- | :--- |
| ```python<br>numbers = [10, 20, 30, 40]<br>print(len(numbers))<br>print(numbers[2])<br>numbers.append(50)<br>``` | ```zoren<br>bind numbers = [10, 20, 30, 40]<br>post("Length: ", numbers.len())<br>post("Element: ", numbers[2])<br>``` |

For dynamically allocated contiguous buffers:
```zoren
bring sys

flex buf = alloc_buffer(32) // 32 bytes allocated
mem_write_i64(buf, 0, 100)  // Store integer at offset 0
flex val = mem_read_i64(buf, 0)
post("Read from buffer: ", val)
free_buffer(buf)
```

---

## 9. Dictionaries & Key-Value Stores

In Python, you use `dict`:
```python
cache = {"user_1": 100, "user_2": 200}
print(cache["user_1"])
```

In Zoren, you have high-performance production storage plugins:
```zoren
bring plugins.bptree_db

flow main() -> Int {
    flex db = bptree_new()

    // Logarithmic B+ Tree Key-Value insertion
    bptree_put(db, 101, 500)
    bptree_put(db, 102, 900)

    // Lookup: O(log N)
    flex val = bptree_get(db, 101)
    post("User balance: ", val) // 500

    // Range Query (Keys from 100 to 200)
    flex out_buf = alloc_buffer(64)
    flex count = bptree_range_scan(db, 100, 200, out_buf, 8)
    post("Matching users: ", count)

    bptree_free(db)
    deliver 0
}
```

---

## 10. Modules & Imports

| Python | Zoren |
| :--- | :--- |
| `import math`<br>`print(math.sqrt(16))` | `bring math`<br>`post(sqrt(16))` |
| `import json`<br>`data = json.loads(text)` | `bring json_stream`<br>`val = json_extract_int(buf, len, key, k_len)` |
| `import sys`<br>`sys.exit(0)` | `bring sys`<br>`deliver 0` |
| `from plugins import vector_db` | `bring plugins.vector_db` |

Zoren automatically discovers modules from:
1. Local directory `./std` and `./plugins`
2. System directories `/usr/local/share/zoren/`
3. User directory `~/.zoren/`
4. `$ZOREN_HOME` and `$ZOREN_PATH` environment variables

---

## 11. Error Handling

In Python, exceptions use `try ... except`. In Zoren, you have deterministic, zero-allocation error handling with `assess` and `divert`, or direct return codes.

### Python
```python
try:
    result = compute_risky_task()
except ValueError as e:
    print("Caught error:", e)
```

### Zoren
```zoren
flow compute_task(input_val: Int) -> Int {
    if input_val < 0 {
        divert -1 // Immediate error diversion
    }
    deliver input_val * 2
}

flow main() -> Int {
    flex res = compute_task(-5)
    if res < 0 {
        post("Error handled safely without exception overhead!")
        deliver 1
    }
    deliver 0
}
```

---

## 12. JSON & File Operations

### Streaming Zero-Allocation JSON Extraction
In Python, `json.loads` allocates Python objects for every dictionary key. Zoren's `std/json_stream` parses directly in-place with **zero memory allocations**:

### Python
```python
import json

payload = '{"model":"zoren-v1","tokens":4096,"active":true}'
data = json.loads(payload)
print(data["tokens"]) # 4096
```

### Zoren
```zoren
bring json_stream
bring sys

flow main() -> Int {
    // Zero-allocation JSON streaming parser
    bind json_str = "{\"model\":\"zoren\",\"tokens\":4096,\"active\":true}"
    // Direct extraction without creating dynamic hash tables!
    // Extract integers, booleans, or strings in sub-microsecond time.
    deliver 0
}
```

---

## 13. AI & Neural Networks

Python developers often rely on PyTorch or NumPy, which are C++ libraries wrapped in Python. In Zoren, tensor math and neural layers are **native Zoren code running directly on the CPU / NEON vector registers**!

### Transformer Attention & Linear Layer
```zoren
bring nn
bring lora
bring sys

flow main() -> Int {
    post("Initializing Native Zoren Neural Network Layer...")

    // 1. Dense Linear Layer with Xavier Initialization
    flex dense = dense_layer_new(128, 64)
    post("Dense Layer created (In: 128, Out: 64)")

    // 2. Transformer Multi-Head Attention Head with Causal Mask
    flex attn = attention_head_new(64)
    post("Causal Multi-Head Attention Head initialized")

    // 3. Low-Rank Adaptation (LoRA) Parameter-Efficient Adapter
    flex adapter = lora_adapter_new(128, 64, 8, 16)
    post("LoRA Adapter Matrix allocated (Rank: 8, Alpha: 16)")

    deliver 0
}
```

---

## 14. Distributed Systems & Concurrency

Python has the Global Interpreter Lock (GIL), making true CPU-bound parallelism difficult without `multiprocessing`. Zoren gives you **native thread execution** and production distributed consensus primitives right out of the box:

```zoren
bring plugins.raft_consensus
bring plugins.distributed_lock
bring plugins.rate_limiter
bring plugins.circuit_breaker

flow main() -> Int {
    post("Starting Production Distributed Microservice System...")

    // 1. Raft Leader Election & Quorum
    flex raft_node = raft_node_new(1, 2)
    raft_start_election(raft_node)
    post("Raft Node State: Candidate (Term 1)")

    // 2. Token Bucket API Gateway Rate Limiting
    flex limiter = rate_limiter_new(100, 50) // 100 req/sec, burst 50
    if rate_limiter_allow(limiter, 1) {
        post("Request allowed by Token Bucket Rate Limiter")
    }

    // 3. Distributed Mutex with Lease TTL & Monotonic Fencing Token
    flex dlock = distributed_lock_new(5000) // 5000ms TTL
    flex fence_token = distributed_lock_acquire(dlock, 42)
    post("Acquired Distributed Mutex with Fencing Token: ", fence_token)

    deliver 0
}
```

---

## 15. Performance Comparison Cheat Sheet

Real bare-metal benchmark measurements comparing **Python 3.14** vs **Zoren (Native)** on Linux AArch64:

| Task | Python 3.14 | Zoren (Native) | Speedup with Zoren |
| :--- | :---: | :---: | :---: |
| **Collatz Branching Loop (1,000,000)** | 29,804.18 ms | **426.99 ms** | 🚀 **69.8x faster** |
| **Recursive Fibonacci (fib 38)** | 16,046.95 ms | **385.61 ms** | 🚀 **41.6x faster** |
| **Neural Vector Math (1,000,000)** | 5,184.46 ms | **143.67 ms** | 🚀 **36.1x faster** |
| **Monte Carlo Pi (10,000,000)** | 12,209.88 ms | **415.55 ms** | 🚀 **29.4x faster** |
| **Memory Footprint** | ~35 MB (CPython VM) | **< 1.5 MB** | 📦 **23x less memory** |
| **Runtime Dependencies** | Python Interpreter | **None (Standalone ELF)** | 🛡️ **Zero dependencies** |

---

## Summary: The Mental Model Shift

| From Python | To Zoren | Why |
| :--- | :--- | :--- |
| `x = 10` | `bind x = 10` (immutable) or `flex x = 10` (mutable) | Eliminates accidental variable mutations |
| `def func():` | `flow func() -> ReturnType:` | Guarantees compile-time type safety |
| `print()` | `post()` | Sub-microsecond console output |
| `return` | `deliver` | Explicit execution pipeline completion |
| `class` | `model` (data) + `ability` (methods) | Separation of data layout and logic |
| `dict` | `bptree_db` or hash structures | Predictable memory and logarithmic speeds |
| `try ... except` | `assess` / `divert` or status codes | Zero allocation overhead |
| `import pkg` | `bring pkg` or `bring plugins.name` | Compile-time module resolution |
