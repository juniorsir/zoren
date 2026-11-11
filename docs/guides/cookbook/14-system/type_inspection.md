# Runtime Type Inspection

# Problem
You want to query the data type of a variable at runtime.

# Solution
Import `std/system` and call `type_of(var)`.

# Code
```zoren
bring system

flow main() -> Int {
    bind name: Text = "Alice"
    post("Name Type: ", type_of(name))
    deliver 0
}
```

# Related
- [Standard Library — std/system](../../standard-library/system.md)
