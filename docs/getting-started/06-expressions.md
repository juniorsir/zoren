# 06 - Expressions and Operators

## What you'll learn
Arithmetic, comparison, logical operators, and the null-coalescing operator (`??`).

## Basic example
```zoren
flow main() -> Int {
    bind a = 10 + 5 * 2
    bind is_greater = a > 15
    bind name_opt: Text = null
    bind active_name = name_opt ?? "Default User"
    post("Active Name: ", active_name)
    deliver 0
}
```

## How it works
- Standard arithmetic follows operator precedence (`*` before `+`).
- `??` evaluates to the left operand if non-null, else the fallback right operand.

## More examples
```zoren
flow main() -> Int {
    flex score = 10
    score += 5
    bind is_valid = (score >= 15) && (score <= 100)
    post("Score Valid: ", is_valid)
    deliver 0
}
```

## Common mistakes
```zoren
// Incorrect: mixing incompatible types in arithmetic
bind res = 10 + "5" // Compiler Error Z3001

// Correct:
bind res = 10 + 5
```

## Try it yourself
Create an expression using addition, multiplication, and a null-coalescing fallback.

## Related topics
- [Functions](./07-functions.md)
