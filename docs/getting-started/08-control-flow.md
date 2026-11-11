# 08 - Control Flow and Loops

## What you'll learn
Decision making with `if`/`else`, pattern matching with `assess`/`case`, and loops with `repeat while`.

## Basic example
```zoren
flow main() -> Int {
    flex counter = 1
    repeat while (counter <= 3) {
        post("Counter: ", counter)
        counter = counter + 1
    }

    bind number = 0
    assess number {
        case 0 -> { post("Zero") }
        case _ -> { post("Other") }
    }
    deliver 0
}
```

## How it works
- `repeat while (cond)` loops while predicate evaluates `true`.
- `assess expr { case pat -> { ... } }` performs pattern matching.

## More examples
```zoren
flow main() -> Int {
    bind score = 85
    if score >= 90 {
        post("Grade A")
    } else if score >= 80 {
        post("Grade B")
    } else {
        post("Grade C")
    }
    deliver 0
}
```

## Common mistakes
```zoren
// Incorrect: using 'while' without 'repeat'
while (x < 10) { ... } // Compiler Error Z1001

// Correct:
repeat while (x < 10) { ... }
```

## Try it yourself
Write a loop that prints numbers from 1 to 5 using `repeat while`.

## Related topics
- [Models](./09-models.md)
