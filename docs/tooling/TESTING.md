# Automated Testing Workflow (`test_runner.py`)

The automated multi-threaded test harness (`test_runner.py`) discovers, compiles, and verifies test files in `tests/`:

```shell
# Run full automated test suite quietly
python3 Zoren_lang/test_runner.py --quiet

# Run test harness showing live stdout output
python3 Zoren_lang/test_runner.py --show-output

# Filter tests by directory or substring
python3 Zoren_lang/test_runner.py --filter "cybersecurity/"
```

## Test Directives
- `# EXPECT: SUCCESS` — Asserts compilation and runtime execution succeed.
- `# EXPECT: ERROR Z4006` — Asserts compiler emits specific diagnostic error code.
