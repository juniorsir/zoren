# Migrating from Rust to Zoren

## 1. If you already know Rust
Zoren shares static typing, zero-cost abstractions, and devirtualized traits, but eliminates lifetime parameter syntax (`'a`).

## 2. Basic syntax mapping

| Concept | Rust | Zoren |
| :--- | :--- | :--- |
| **Immutable Value** | `let x = 10;` | `bind x: Int = 10` |
| **Mutable Value** | `let mut x = 10;` | `flex x: Int = 10` |
| **Function** | `fn add(a: i64, b: i64) -> i64` | `flow add(a: Int, b: Int) -> Int` |
| **Struct** | `struct Point { x: i64 }` | `model Point { open x: Int }` |
| **Trait / Impl** | `trait P {} impl P for Point {}` | `ability P {} grant P for Point {}` |
| **Return** | `return val;` / `val` | `deliver val` |

## 3. Variables and mutability
Rust uses `let` and `let mut`. Zoren uses `bind` and `flex`.

## 4. Functions
Rust uses `fn`. Zoren uses `flow`. Return values are returned via `deliver`.

## 5. Types
Rust `i64` maps to Zoren `Int` (`i64`), `f64` maps to `Float` (`f64`), `String`/`&str` maps to `Text`.

## 6. Collections
Rust `Vec<T>` maps to Zoren `Vector[T]`.

## 7. Models and Structs
Rust `struct` maps to Zoren `model`.

## 8. Abilities and Traits
Rust `trait` maps to Zoren `ability`. Rust `impl Trait for Struct` maps to Zoren `grant Ability for Model`.

## 9. Generics
Both Rust and Zoren monomorphize generic templates at compile time with 0 runtime penalty.

## 10. Modules
Rust `use crate::module;` maps to Zoren `bring module`.

## 11. Errors
Rust uses `Result<T, E>` and `?`. Zoren uses `diverges`, `divert`, and `catch`.

## 12. Concurrency
Rust uses `async`/`await` with executors like tokio. Zoren uses built-in Spindle tasks (`spawn`, `await`).

## 13. Foreign Interoperability
Rust C-ABI functions (`extern "C"`) link cleanly with Zoren `extern ABI "C" flow`.

## 14. Performance mindset
Both languages produce bare-metal machine code with whole-program LTO.

## 15. Common migration mistakes
```zoren
// Incorrect Rust-style fn syntax
fn main() -> i64 { return 0; } // Compiler Error Z1001

// Correct Zoren syntax
flow main() -> Int { deliver 0 }
```
