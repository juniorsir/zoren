# 15 - Next Steps and Advanced Tooling

## What you'll learn
Where to go next: advanced toolchain commands, building applications, and exploring the Zoren ecosystem.

## Basic example
```shell
# Audit package capabilities
zoren audit .

# Run static linter
zoren check .

# Generate HTML documentation
zoren doc .

# Forge binary executable
zoren forge .
```

## How it works
- `zoren audit` verifies package security contracts.
- `zoren check` runs static code quality analysis.
- `zoren forge` compiles and materializes capability-bound binaries into `~/.zoren/bin/`.

## More examples
```zoren
# Complete Application Template
bring math
bring text

flow main() -> Int {
    post("Zoren Application Ready for Production!")
    deliver 0
}
```

## Common mistakes
```shell
# Incorrect: forgetting to format before forging
zoren forge .

# Correct workflow: format, audit, then forge
zoren fmt src/main.zor
zoren audit .
zoren forge .
```

## Try it yourself
Run `zoren audit .` and `zoren check .` on your current Zoren project.

## Related topics
- [Documentation Index](../README.md)
