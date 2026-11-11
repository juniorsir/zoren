# Data Models

# Problem
You want to define a structured data model with typed fields.

# Solution
Use `model ModelName { open field: Type }`.

# Code
```zoren
model User {
    open id: Int
    open name: Text
}

flow main() -> Int {
    bind u = User(101, "Alice")
    post("User ID: {u.id}, Name: {u.name}")
    deliver 0
}
```

# Related
- [Language Reference — Models](../../reference/syntax/12-models.md)
