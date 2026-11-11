# Compiler Intrinsics & Builtins Reference

These functions are provided directly by the compiler engine (`zoren` / `zorenv1` / `zorenv2`).

## 1. Unified I/O Intrinsics

### `post(...)`
- **Kind:** Compiler Intrinsic
- **Signature:** `post(args...) -> Nothing`
- **Purpose:** Prints formatted values and string placeholders (`"{val}"`) to stdout with a newline.
- **Example:** `post("Score: {score}")`

### `pull[T]()`
- **Kind:** Compiler Intrinsic
- **Signature:** `pull[T](prompt: Text? = null) -> T`
- **Purpose:** Reads a typed input value from stdin.
- **Example:** `bind age = pull[Int]()`

## 2. Type Inspection Intrinsics

### `type_of(val)`
- **Kind:** Compiler Intrinsic / Runtime Query
- **Signature:** `type_of(val: Any) -> Text`
- **Purpose:** Returns the string representation of an expression's type at runtime.
- **Example:** `post(type_of(42))` // Output: "Int"

### `type_name[T]()`
- **Kind:** Compiler Intrinsic
- **Signature:** `type_name[T]() -> Text`
- **Purpose:** Returns the compile-time type string.
- **Example:** `post(type_name[Float]())` // Output: "Float"
