# Zoren Executable Documentation Verification Engine

This directory contains the automated verification engine (`verify_examples.py`) for testing all code examples embedded in Zoren documentation.

## Usage

```shell
# Run verification on all documentation examples
python3 Zoren_lang/docs/examples/verify_examples.py

# Run verification in verbose mode
python3 Zoren_lang/docs/examples/verify_examples.py --verbose

# Run verification displaying live output for passing examples
python3 Zoren_lang/docs/examples/verify_examples.py --show-output

# Filter verification by category or substring
python3 Zoren_lang/docs/examples/verify_examples.py --filter "getting-started"
```

## Documentation Index & Status

- [INDEX — Complete Documentation Example Index](./INDEX.md)
- [STATUS — Documentation Verification Audit Status](./STATUS.md)
