# 10 - Abilities and Grants

## What you'll learn
Interface contracts (`ability`) and compile-time devirtualized implementations (`grant ... for`).

## Basic example
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

## How it works
- `ability` defines an interface contract.
- `grant Ability for Model` implements the ability for a specific model.
- `self` refers to the active model instance.

## More examples
```zoren
ability Speaker {
    flow speak() -> Nothing
}

model Dog {}

grant Speaker for Dog {
    speak { post("Woof!") }
}

flow main() -> Int {
    bind d = Dog()
    d.speak()
    deliver 0
}
```

## Common mistakes
```zoren
// Incorrect: duplicate grant block
grant Speaker for Dog { ... }
grant Speaker for Dog { ... } // Compiler Error Z4002

// Correct: define grant once
```

## Try it yourself
Create an `Area` ability with an `area()` subroutine and implement it for a `Square` model.

## Related topics
- [Collections](./11-collections.md)
