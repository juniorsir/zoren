# 14 - Error Handling and Cleanup

## What you'll learn
Linear error contracts (`diverges`), raise (`divert`), handling (`catch`), and LIFO cleanup (`ensure`).

## Basic example
```zoren
model CustomErr {
    open msg: Text
}

flow risky_action(flag: Bool) -> Int diverges CustomErr {
    ensure {
        post("Scope Cleanup Executed")
    }
    if !flag {
        divert CustomErr("Action Failed")
    }
    deliver 100
}

flow main() -> Int {
    bind res = risky_action(false) catch err {
        post("Handled Error Safely")
        deliver 0
    }
    deliver 0
}
```

## How it works
- `diverges CustomErr` declares the error contract in the subroutine signature.
- `divert` raises the error value.
- `catch err { ... }` handles the diverted error value.
- `ensure { ... }` guarantees cleanup code runs when exiting the scope.

## More examples
```zoren
flow main() -> Int {
    ensure {
        post("Cleanup Handler Finished")
    }
    post("Main Task Execution")
    deliver 0
}
```

## Common mistakes
```zoren
// Incorrect: calling a diverging function without catch
bind res = risky_action(false) // Compiler Error Z4006

// Correct: handle with catch
bind res = risky_action(false) catch err { deliver 0 }
```

## Try it yourself
Write a flow that uses an `ensure` block to print a cleanup message on scope exit.

## Related topics
- [Next Steps](./15-next-steps.md)
