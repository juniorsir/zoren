# 07 - Subroutines and Functions

## What you'll learn
How to define flows, pass parameters, and return values with `deliver`.

## Basic example
```zoren
flow add_numbers(a: Int, b: Int) -> Int {
    deliver a + b
}

flow main() -> Int {
    bind sum = add_numbers(15, 30)
    post("Sum: ", sum)
    deliver 0
}
```

## How it works
- `flow` declares a subroutine.
- `(a: Int, b: Int)` defines parameter names and types.
- `-> Int` specifies return type.
- `deliver` returns an expression result.

## More examples
```zoren
flow square(n: Int) -> Int {
    deliver n * n
}

flow main() -> Int {
    post("4 Squared = ", square(4))
    deliver 0
}
```

## Common mistakes
```zoren
// Incorrect: returning mismatched type
flow get_value() -> Int {
    deliver "NotAnInt" // Compiler Error Z4006
}

// Correct:
flow get_value() -> Int {
    deliver 42
}
```

## Try it yourself
Write a subroutine `multiply(a: Int, b: Int) -> Int` and call it from `main`.

## Related topics
- [Control Flow](./08-control-flow.md)
