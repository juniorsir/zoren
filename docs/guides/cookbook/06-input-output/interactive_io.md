# Interactive I/O

# Problem
You want to print formatted messages and prompt the user for input.

# Solution
Use `post(...)` and `pull[T]()`.

# Code
```zoren
flow main() -> Int {
    post("Enter your name: ")
    bind name = pull[Text]()
    post("Hello, {name}!")
    deliver 0
}
```

# Related
- [Standard Library — BUILTINS](../../standard-library/BUILTINS.md)
