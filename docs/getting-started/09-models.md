# 09 - Data Models (Structs)

## What you'll learn
How to define composite data models (`model`) and access fields with dot notation.

## Basic example
```zoren
model User {
    open id: Int
    open name: Text
}

flow main() -> Int {
    bind user = User(101, "Alice")
    post("User ID: {user.id}, Name: {user.name}")
    deliver 0
}
```

## How it works
- `model ModelName` defines a composite struct type.
- `open field: Type` declares a public model field.
- `User(101, "Alice")` instantiates the model.

## More examples
```zoren
model Point {
    open x: Int
    open y: Int
}

flow main() -> Int {
    bind p = Point(10, 20)
    post("Point Coordinates: ({p.x}, {p.y})")
    deliver 0
}
```

## Common mistakes
```zoren
// Incorrect: missing 'open' modifier on fields needed publicly
model Item {
    cost: Int
}

// Correct:
model Item {
    open cost: Int
}
```

## Try it yourself
Create a `Rectangle` model with `width` and `height` fields, instantiate it, and print its dimensions.

## Related topics
- [Abilities](./10-abilities.md)
