# 04 - Data Types

## What you'll learn
Zoren's core primitive types (`Int`, `Float`, `Bool`, `Text`, `Char`).

## Basic example
```zoren
flow main() -> Int {
    bind count: Int = 42
    bind ratio: Float = 3.14159
    bind active: Bool = true
    bind name: Text = "Zoren"
    post("Name: ", name)
    deliver 0
}
```

## How it works
- `Int` is a signed 64-bit integer (`i64`).
- `Float` is a 64-bit floating point number (`f64`).
- `Bool` is boolean `true` or `false`.
- `Text` is a UTF-8 string.

## More examples
```zoren
flow main() -> Int {
    bind pi: F64 = 3.14
    bind is_ready: bool = true
    post("PI: ", pi)
    deliver 0
}
```

## Common mistakes
```zoren
// Incorrect: mismatched type assignment
bind age: Int = "Twenty" // Compiler Error Z3001

// Correct:
bind age: Int = 20
```

## Try it yourself
Declare variables for a temperature (`Float`), city name (`Text`), and online status (`Bool`).

## Related topics
- [Output and Input](./05-output-and-input.md)
