# 11 - Collections and Vectors

## What you'll learn
Dynamic resizable arrays using `Vector[T]`.

## Basic example
```zoren
bring collections

flow main() -> Int {
    bind numbers = create_vector[Int]()
    post("Vector initialized cleanly.")
    deliver 0
}
```

## How it works
- `bring collections` imports the standard vector package.
- `create_vector[T]()` instantiates a typed dynamic array.

## More examples
```zoren
bring collections

flow main() -> Int {
    bind vec = create_vector[Text]()
    post("Vector created with 0 heap overhead.")
    deliver 0
}
```

## Common mistakes
```zoren
// Incorrect: calling create_vector without type parameter
bind vec = create_vector() // Compiler Error Z4006

// Correct:
bind vec = create_vector[Int]()
```

## Try it yourself
Create a `Vector[Text]` collection and print a confirmation message.

## Related topics
- [Generics](./12-generics.md)
