# Migrating from Python to Zoren

## 1. If you already know Python
Zoren offers clean readability similar to Python, but compiles to bare-metal native machine code with static type safety.

## 2. Basic syntax mapping

| Concept | Python | Zoren |
| :--- | :--- | :--- |
| **Immutable Value** | `x = 10` (convention) | `bind x: Int = 10` |
| **Mutable Value** | `x = 10` | `flex x: Int = 10` |
| **Function** | `def add(a, b): return a + b` | `flow add(a: Int, b: Int) -> Int { deliver a + b }` |
| **Data Struct** | `class Point:` / `@dataclass` | `model Point { open x: Int, open y: Int }` |
| **Print Output** | `print(f"Val: {x}")` | `post("Val: {x}")` |
| **Python Interop** | `import numpy as np` | `bring foreign.python use { numpy as np }` |

## 3. Variables and mutability
Zoren requires explicit `bind` (immutable constant) or `flex` (mutable variable) declarations.

## 4. Functions
Python functions use `def` and `return`. Zoren uses `flow` and `deliver`.

## 5. Types
Python is dynamically typed. Zoren is strictly statically typed (`Int`, `Float`, `Bool`, `Text`).

## 6. Collections
Python lists map to Zoren `Vector[T]` (`create_vector[T]()`).

## 7. Models vs Classes
Zoren `model` structures store field data only; methods are attached via `grant`.

## 8. Abilities vs Interfaces
Zoren `ability` contracts replace Python abstract base classes.

## 9. Generics
Python uses dynamic duck typing. Zoren monomorphizes generic functions (`[T]`) at build time.

## 10. Modules
Python `import math` maps to Zoren `bring math`.

## 11. Errors
Python uses `try`/`except`. Zoren uses `diverges`, `divert`, and `catch`.

## 12. Concurrency
Python uses asyncio / threads. Zoren uses lightweight Spindles (`async flow`, `spawn`, `await`).

## 13. Foreign Interoperability
Zoren can load Python packages directly via `bring foreign.python use { numpy as np }`.

## 14. Performance mindset
Zoren compiles directly to native AArch64/x86_64 machine code without GIL locks or interpreter overhead.

## 15. Common migration mistakes
```zoren
// Incorrect Python-style dynamic assignment
x = 10 // Compiler Error Z1001

// Correct Zoren assignment
bind x: Int = 10
```
