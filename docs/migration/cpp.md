# Migrating from C++ to Zoren

## 1. If you already know C++
C++ developers map `struct` to `model`, `template<typename T>` to `[T]`, and `std::vector` to `Vector[T]`.

## 2. Basic syntax mapping

| Concept | C++ | Zoren |
| :--- | :--- | :--- |
| **Immutable Value** | Constant Declaration | `bind x: Int = 10` |
| **Mutable Value** | Variable Declaration | `flex x: Int = 10` |
| **Subroutine** | Function / Method | `flow name() -> Int` |
| **Data Struct** | Class / Struct | `model Name { open field: Int }` |
| **Interface** | Interface / Trait | `ability Name { flow method() -> Int }` |

## 3. Variables and mutability
Zoren requires `bind` for constants and `flex` for mutable variables.

## 4. Functions
Subroutines use `flow` and return values via `deliver`.

## 5. Types
Strict static typing (`Int`, `Float`, `Bool`, `Text`).

## 6. Collections
`Vector[T]` provides dynamic array storage.

## 7. Models
Zoren `model` structures hold state fields; methods are implemented via `grant`.

## 8. Abilities
Zoren `ability` contracts replace interfaces.

## 9. Generics
Compile-time monomorphization (`[T]`).

## 10. Modules
Import packages using `bring module`.

## 11. Errors
Structured error contracts (`diverges`, `divert`, `catch`) and LIFO scope cleanup (`ensure`).

## 12. Concurrency
Lightweight Spindle green tasks (`async flow`, `spawn`, `await`).

## 13. Foreign Interoperability
C-ABI direct register linkage (`extern ABI "C"`).

## 14. Performance mindset
Bare-metal AArch64/x86_64 machine code execution.

## 15. Common migration mistakes
```zoren
// Incorrect C++-style declaration syntax
bind x = 10
```
