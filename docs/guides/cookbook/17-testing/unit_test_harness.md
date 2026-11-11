# Unit Testing Directives

# Problem
You want to write automated unit test files for the test runner.

# Solution
Add `# EXPECT: SUCCESS` header directives.

# Code
```zoren
# EXPECT: SUCCESS
flow main() -> Int {
    post("Automated Test Verification Passed")
    deliver 0
}
```

# Related
- [Tooling — Test Runner](../../tooling/README.md)
