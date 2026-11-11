# 02 - Hello World in Zoren

## What you'll learn
How to write, compile, and run your first Zoren program using subroutines and output statements.

## Basic example
```zoren
flow main() -> Int {
    post("Hello, Zoren!")
    deliver 0
}
```

## How it works
- `flow main()` defines the entrypoint subroutine.
- `post("Hello, Zoren!")` prints text to stdout with a newline.
- `deliver 0` returns integer status code 0.

## More examples
```zoren
flow main() -> Int {
    post("Welcome to Zoren Version 1.0")
    post("Line 2 Execution")
    deliver 0
}
```

## Common mistakes
```zoren
// Incorrect: missing flow keyword
main() -> Int { deliver 0 }

// Correct:
flow main() -> Int { deliver 0 }
```

## Try it yourself
Modify the program to print your name on stdout.

## Related topics
- [Variables](./03-variables.md)
