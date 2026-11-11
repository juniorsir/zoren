# Error Contracts and Diversion

# Problem
You want to raise, propagate, and handle errors deterministically.

# Solution
Use `diverges`, `divert`, `catch`, and `ensure`.

# Code
```zoren
model CustomErr { open code: Int }

flow risky(x: Int) -> Int diverges CustomErr {
    ensure { post("Cleanup Executed") }
    if x < 0 { divert CustomErr(500) }
    deliver x * 2
}

flow main() -> Int {
    bind res = risky(10) catch err { deliver 0 }
    post("Result: ", res)
    deliver 0
}
```

# Related
- [Language Reference — Error Handling](../../reference/syntax/18-error-handling.md)
