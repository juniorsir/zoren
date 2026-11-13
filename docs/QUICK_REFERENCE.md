# ⚡ Zoren Quick Reference & Cheat Sheet

A concise 1-page reference for developers writing code in the **Zoren Programming Language**.

---

## 🔑 Keywords & Syntax

| Keyword | Purpose | Example |
|---|---|---|
| `bind` | Declare an **immutable** value | `bind max_retries = 3` |
| `flex` | Declare a **mutable** variable | `flex counter = 0` |
| `flow` | Define a subroutine or function | `flow add(a: Int, b: Int) -> Int { deliver a + b }` |
| `open` | Mark flow or model field as **public / exported** | `open flow main() -> Int { ... }` |
| `deliver` | Return an expression from a flow | `deliver true` |
| `model` | Define a composite data model / struct | `model Point { open x: Int; open y: Int }` |
| `bring` | Import a module from standard library | `bring math` or `bring vector_hnsw` |
| `if` / `else` | Conditional branching | `if x > 0 { deliver 1 } else { deliver 0 }` |
| `while` | Condition-controlled loop | `while i < 10 { i = i + 1 }` |
| `for` | Iterator-controlled loop | `for item in list { post(item) }` |

---

## 📦 Data Types

| Type | Description | Literal Examples |
|---|---|---|
| `Int` | 64-bit signed integer | `0`, `42`, `-100`, `2147483647` |
| `Bool` | Boolean truth value | `true`, `false` |
| `Text` | UTF-8 string | `"hello"`, `"Zoren 1.0\n"` |
| `[T]` | Bounded array / list of type `T` | `[1, 2, 3]` |

---

## 🧵 Functions & Subroutines

```zoren
// Function with parameters and explicit return type
flow multiply(a: Int, b: Int) -> Int {
    deliver a * b
}

// Public entrypoint
open flow main() -> Int {
    flex result = multiply(6, 7)
    post(result) // prints 42
    deliver 0    // exit code 0
}
```

---

## 💾 Direct Memory Management Primitives

For high-performance data structures, zero-copy buffers, and embedded records:

```zoren
// 1. Allocate a raw memory block (in bytes):
flex buf = alloc_buffer(64)

// 2. Zero-fill memory: mem_fill(ptr, byte_val, size_in_bytes)
mem_fill(buf, 0, 64)

// 3. 64-bit integer read/write (offset in bytes):
mem_write_i64(buf, 0, 100)      // write 100 at byte offset 0
flex val = mem_read_i64(buf, 0) // reads 100

// 4. Single byte read/write (0..255):
mem_write_byte(buf, 8, 42)      // write byte 42 at offset 8
flex b = mem_read_byte(buf, 8)  // reads byte 42

// 5. Memory copy: mem_copy(dst, src, bytes)
mem_copy(dst_buf, src_buf, 32)

// 6. Free buffer when done:
free_buffer(buf)
```

---

## 🔤 Built-in String Functions

| Function | Signature | Description |
|---|---|---|
| `length` | `length(s: Text) -> Int` | Returns string character count. |
| `str_concat` | `str_concat(s1: Text, s2: Text) -> Text` | Concatenates two strings together. |
| `str_slice` | `str_slice(s: Text, start: Int, len: Int) -> Text` | Extracts substring of length `len` starting at `start`. |
| `str_find` | `str_find(haystack: Text, needle: Text) -> Int` | Returns 0-based index of needle, or `-1` if not found. |
| `str_upper` | `str_upper(s: Text) -> Text` | Converts ASCII characters to uppercase. |
| `str_lower` | `str_lower(s: Text) -> Text` | Converts ASCII characters to lowercase. |
| `str_trim` | `str_trim(s: Text) -> Text` | Strips leading and trailing whitespace. |
| `constant_time_compare` | `constant_time_compare(a: Text, b: Text) -> Bool` | Timing-safe string content comparison. |
| `int_to_str` | `int_to_str(val: Int) -> Text` | Converts integer to string representation. |
| `hex_encode` | `hex_encode(s: Text) -> Text` | Converts string bytes to hexadecimal string. |
| `hex_decode` | `hex_decode(hex: Text) -> Text` | Decodes hexadecimal string back to text. |

---

## 🛠️ Compiler Commands & Flags

```bash
# Compile and link:
zoren main.zor -o main

# Compile and immediately run:
zoren main.zor -o /tmp/run && /tmp/run

# Run full compiler regression test suite:
python3 test_runner.py

# Format or inspect binary protections:
readelf -l main | grep -i stack
```

---

## 📚 Common Idioms & Best Practices

### 1. Loop Over a Bounded Range
```zoren
flex i = 0
flex limit = 10
while i < limit {
    // perform work
    i = i + 1
}
```

### 2. Guard Clauses with Early Deliver
```zoren
flow safe_divide(numerator: Int, denominator: Int) -> Int {
    if denominator == 0 {
        deliver 0 // guard against division by zero
    }
    deliver numerator / denominator
}
```

### 3. Safe Large Modulo Constants
```zoren
// Bind large constants to variables before arithmetic in AArch64:
flex mod_val = 2147483647
flex result = (val + mod_val) % mod_val
```
