# 13 - Modules and Imports

## What you'll learn
Importing packages with `bring`, symbol aliasing with `as`, and package use blocks.

## Basic example
```zoren
bring math
bring text as txt

flow main() -> Int {
    bind val = abs(-42)
    post("Absolute Value: ", val)
    deliver 0
}
```

## How it works
- `bring math` imports standard math utilities (`abs`, `square`, `max`).
- `bring text as txt` imports `text` with local alias `txt`.

## More examples
```zoren
bring foreign.python use {
    numpy as np
}

flow main() -> Int {
    post("Imported NumPy package via Python enclave bridge.")
    deliver 0
}
```

## Common mistakes
```zoren
// Incorrect: importing non-existent module name
bring unknown_mod // Compiler Error Z2001

// Correct:
bring math
```

## Try it yourself
Import `math` and `text` packages and call `square(5)` and `upper("zoren")`.

## Related topics
- [Error Handling](./14-error-handling.md)
