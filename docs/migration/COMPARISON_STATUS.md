# Migration Guide Audit Status

| Source Language | Guide Status | Verified Zoren Mapping | Unsupported Features Documented |
| :--- | :--- | :--- | :--- |
| **Python** | `COMPLETE` | `bind`/`flex`, `flow`, `model`, `ability`, `foreign.python` | Dynamic typing, GIL, GC |
| **Rust** | `COMPLETE` | `bind`/`flex`, `flow`, `model`, `ability`, `grant`, `[T]` | Borrow checker lifetime annotations (`'a`), macros |
| **C++** | `COMPLETE` | `bind`/`flex`, `flow`, `model`, `extern ABI "C"`, Chamber arenas | Virtual inheritance, header files, preprocessor |
| **C** | `COMPLETE` | `bind`/`flex`, `flow`, `model`, `extern ABI "C"`, `diverges` | Manual `free()`, uninitialized pointers |
| **Go** | `COMPLETE` | `bind`/`flex`, `flow`, `model`, `ability`, `async`/`spawn` | Garbage Collector (GC), `interface{}` dynamic boxed types |
| **JavaScript** | `COMPLETE` | `bind`/`flex`, `flow`, `model`, `async`/`await` | Prototype chains, dynamic event loop queues |
| **Java** | `COMPLETE` | `bind`/`flex`, `flow`, `model`, `ability`, `grant` | JVM bytecode, class inheritance, GC |
