# Official Zoren Type System Inventory

The active compiler (`parser.rs`, `types.rs`, `semantic.rs`) supports the following primitive and composite types:

## 1. Low-Level Primitive Types

| Type Identifier | Size | Alignment | Description | Status |
| :--- | :--- | :--- | :--- | :--- |
| `i8` | 1 byte | 1 byte | Signed 8-bit integer | `SUPPORTED` |
| `i16` | 2 bytes | 2 bytes | Signed 16-bit integer | `SUPPORTED` |
| `i32` | 4 bytes | 4 bytes | Signed 32-bit integer | `SUPPORTED` |
| `i64` | 8 bytes | 8 bytes | Signed 64-bit integer | `SUPPORTED` |
| `u8` | 1 byte | 1 byte | Unsigned 8-bit integer | `SUPPORTED` |
| `u16` | 2 bytes | 2 bytes | Unsigned 16-bit integer | `SUPPORTED` |
| `u32` | 4 bytes | 4 bytes | Unsigned 32-bit integer | `SUPPORTED` |
| `u64` | 8 bytes | 8 bytes | Unsigned 64-bit integer | `SUPPORTED` |
| `iptr` | 8 bytes | 8 bytes | Architecture-sized signed pointer | `SUPPORTED` |
| `uptr` | 8 bytes | 8 bytes | Architecture-sized unsigned pointer | `SUPPORTED` |
| `f32` | 4 bytes | 4 bytes | Single-precision 32-bit float | `SUPPORTED` |
| `f64` | 8 bytes | 8 bytes | Double-precision 64-bit float | `SUPPORTED` |
| `byte` | 1 byte | 1 byte | Raw byte scalar | `SUPPORTED` |
| `rune` | 4 bytes | 4 bytes | Unicode scalar character | `SUPPORTED` |
| `bool` | 1 byte | 1 byte | Boolean value (`true` / `false`) | `SUPPORTED` |
| `text` | 16 bytes | 8 bytes | UTF-8 string slice fat pointer | `SUPPORTED` |
| `void` | 0 bytes | 0 bytes | Unit / empty type | `SUPPORTED` |

## 2. High-Level Type Aliases

| Alias Identifier | Canonical Primitive Type | Status |
| :--- | :--- | :--- |
| `Int` | `i64` | `SUPPORTED` |
| `UInt` | `u64` | `SUPPORTED` |
| `Float` | `f64` | `SUPPORTED` |
| `Bool` | `bool` | `SUPPORTED` |
| `Char` | `rune` | `SUPPORTED` |
| `Text` | `text` | `SUPPORTED` |
| `Nothing` | `void` | `SUPPORTED` |

## 3. Composite & Extended Types

- **`model` (Struct):** Composite data structures with named, typed fields (`SUPPORTED`).
- **`actor model`:** Distributed Actor data models (`SUPPORTED`).
- **`enum`:** Enumerated tagged union types (`SUPPORTED`).
- **Generic Types `[T]`:** Monomorphized compile-time template types (`SUPPORTED`).
- **Optional Types `T?`:** Nullable types handled safely via `??` or pattern matching (`SUPPORTED`).
