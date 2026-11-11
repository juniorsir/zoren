# Async Spindle Tasks

# Problem
You want to run asynchronous background tasks cleanly.

# Solution
Use `async flow`, `spawn`, and `await`.

# Code
```zoren
async flow async_task(id: Int) -> Int {
    deliver id * 10
}

flow main() -> Int {
    spawn async_task(1)
    bind val = await async_task(2)
    post("Task Result: ", val)
    deliver 0
}
```

# Related
- [Language Reference — Concurrency](../../reference/syntax/19-concurrency.md)
