# Hello World Program

# Problem
You want to write, compile, and execute a minimal Zoren application.

# Solution
Write a `flow main() -> Int` subroutine returning status code `0`.

# Code
```zoren
flow main() -> Int {
    post("Hello, Zoren!")
    deliver 0
}
```

# Explanation
- `flow main()` defines the entrypoint subroutine.
- `post(...)` prints text to stdout with a newline.
- `deliver 0` returns integer status code 0.

# Why this works
Zoren applications require an entrypoint named `main`.

# Variations
```zoren
# Short main without return arrow (implicitly defaults to Int)
flow main() {
    post("Short Main Syntax")
}
```

# Performance
Compiles directly to AArch64/x86_64 native machine code in <0.01s.

# Common mistakes
```zoren
// Incorrect: missing flow keyword
main() -> Int { deliver 0 }
```

# Related
- [Language Reference — Functions](../../reference/syntax/10-functions.md)
- [Standard Library — BUILTINS](../../standard-library/BUILTINS.md)
