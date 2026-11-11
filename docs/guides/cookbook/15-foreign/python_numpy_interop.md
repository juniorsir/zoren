# Python NumPy Interop

# Problem
You want to execute NumPy matrix operations inside Zoren.

# Solution
Import `foreign.python` and call `py_import_pkg` / `py_call`.

# Code
```zoren
bring foreign.python as py

flow main() -> Int {
    bind np = py_import_pkg("numpy")
    bind arr = py_call(np, "zeros", 100)
    post("NumPy Array Created via Enclave: ", arr)
    deliver 0
}
```

# Related
- [Standard Library — std/python](../../standard-library/python.md)
