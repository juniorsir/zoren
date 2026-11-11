# Package Use Blocks

# Problem
You want to import multiple Python packages in a single block.

# Solution
Use `bring foreign.python use { pkg1 as alias1, pkg2 }`.

# Code
```zoren
bring foreign.python use {
    numpy as np,
    pandas as pd
}

flow main() -> Int {
    post("Imported NumPy and Pandas via Enclave.")
    deliver 0
}
```

# Related
- [Language Reference — Modules](../../reference/syntax/17-modules.md)
