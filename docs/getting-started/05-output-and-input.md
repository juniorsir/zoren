# 05 - Output and Input

## What you'll learn
How to print formatted messages with `post(...)` and read user input with `pull[T]()`.

## Basic example
```zoren
flow main() -> Int {
    post("Enter your age: ")
    bind age = pull[Int]()
    post("Your age is {age}")
    deliver 0
}
```

## How it works
- `post(...)` prints items to stdout with string placeholder interpolation (`{age}`).
- `pull[Int]()` reads a typed integer from stdin.

## More examples
```zoren
flow main() -> Int {
    post("Enter your name: ")
    bind name = pull[Text]()
    post("Hello, {name}!")
    deliver 0
}
```

## Common mistakes
```zoren
// Incorrect: using quotes inside pull generic bracket
bind val = pull["Int"]() // Error Z4006

// Correct: use unquoted type identifier
bind val = pull[Int]()
```

## Try it yourself
Write a program that prompts for your favorite number and prints double its value.

## Related topics
- [Expressions](./06-expressions.md)
