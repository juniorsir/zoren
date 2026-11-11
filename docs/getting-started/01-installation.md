# 01 - Installing Zoren

## What you'll learn
How to set up the Zoren toolchain, verify your compiler binary, and scaffold a new workspace.

## Basic example
```shell
# Verify compiler platform
zoren --version
```

## How it works
Running `zoren` invokes the Zoren compiler engine (`zorenv1` or `zorenv2`).

## More examples
```shell
# Scaffold a new workspace
zoren new my_project

# Format source files
zoren fmt src/main.zor
```

## Common mistakes
```shell
# Incorrect: invoking obsolete internal paths directly
./zoren/target/release/zorenv1 src/main.zor

# Correct: use official CLI command
zoren src/main.zor
```

## Try it yourself
Run `zoren new my_app` and navigate into the `my_app` directory.

## Related topics
- [Hello World](./02-hello-zoren.md)
