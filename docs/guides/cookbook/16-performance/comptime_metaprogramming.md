# Build-Time Metaprogramming

# Problem
You want to compute values at build-time with zero runtime overhead.

# Solution
Use `comptime flow`.

# Code
```zoren
comptime flow build_time_const() -> Int {
    deliver 65536
}

flow main() -> Int {
    bind val = build_time_const()
    post("Pre-Computed Constant: ", val)
    deliver 0
}
```

# Related
- [Language Reference — Generics](../../reference/syntax/15-generics.md)
