# 03 - Variables and Mutability

## What you'll learn
How to declare immutable constants with `bind` and mutable variables with `flex`.

## Basic example
```zoren
flow main() -> Int {
    bind age: Int = 25
    flex score: Int = 100
    score = score + 5
    post("Score: ", score)
    deliver 0
}
```

## How it works
- `bind` creates an immutable constant that cannot be reassigned.
- `flex` creates a mutable variable that can be modified later.

## More examples
```zoren
flow main() -> Int {
    bind birth_year = 1995
    flex current_year = 2026
    bind age = current_year - birth_year
    post("Age: ", age)
    deliver 0
}
```

## Common mistakes
```zoren
// Incorrect: attempting to reassign a bind constant
bind x: Int = 10
x = 20 // Compiler Error Z4003

// Correct: use flex for mutable values
flex x: Int = 10
x = 20
```

## Try it yourself
Declare a `bind` constant for your birth year and a `flex` variable for your current score.

## Related topics
- [Types](./04-types.md)
