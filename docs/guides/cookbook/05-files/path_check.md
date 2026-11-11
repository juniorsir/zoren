# File Path Validation

# Problem
You want to validate a file path using capability-bound file APIs.

# Solution
Import `std/fs` and call `check_file_path(path)`.

# Code
```zoren
bring fs

flow main() -> Int {
    bind valid = check_file_path("config.json")
    post("Path Check Result: ", valid)
    deliver 0
}
```

# Related
- [Standard Library — std/fs](../../standard-library/fs.md)
