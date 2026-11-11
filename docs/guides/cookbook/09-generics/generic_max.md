# Generic Functions

# Problem
You want to write a single subroutine that operates on multiple types.

# Solution
Use generic parameter brackets `[T]`.

# Code
```zoren
flow max[T](a: T, b: T) -> T {
    if a > b { deliver a }
    deliver b
}

flow main() -> Int {
    bind m = max(15, 30)
    post("Max Value: ", m)
    deliver 0
}
```

# Related
- [Language Reference — Generics](../../reference/syntax/15-generics.md)
