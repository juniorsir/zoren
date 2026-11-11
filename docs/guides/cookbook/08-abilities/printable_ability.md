# Ability Contracts

# Problem
You want to define an interface contract and implement it for a model.

# Solution
Use `ability` and `grant ... for`.

# Code
```zoren
ability Printable {
    flow print_summary() -> Nothing
}

model Person {
    open name: Text
}

grant Printable for Person {
    print_summary {
        post("Person Name: ", self.name)
    }
}

flow main() -> Int {
    bind p = Person("Alice")
    p.print_summary()
    deliver 0
}
```

# Related
- [Language Reference — Abilities](../../reference/syntax/13-abilities.md)
