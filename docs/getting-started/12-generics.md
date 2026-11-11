# 12 - Compile-Time Generics

## What you'll learn
Monomorphized generic functions and models `[T]`.

## Basic example
```zoren
flow max[T](a: T, b: T) -> T {
    if a > b {
        deliver a
    }
    deliver b
}

flow main() -> Int {
    bind int_max = max(15, 30)
    post("Max Int: ", int_max)
    deliver 0
}
```

## How it works
- `[T]` declares a generic type parameter.
- The compiler monomorphizes `max[T]` at compile time into concrete specialized subroutines (`max_i64`) with 0 runtime penalty.

## More examples
```zoren
model Box[T] {
    open value: T
}

flow main() -> Int {
    bind b = Box(100)
    post("Box Value: ", b.value)
    deliver 0
}
```

## Common mistakes
```zoren
// Incorrect: passing mismatched argument types to generic function
bind res = max(10, "Twenty") // Compiler Error Z3001

// Correct:
bind res = max(10, 20)
```

## Try it yourself
Write a generic `identity[T](val: T) -> T` function and test it with an `Int` and a `Text`.

## Related topics
- [Modules](./13-modules.md)
