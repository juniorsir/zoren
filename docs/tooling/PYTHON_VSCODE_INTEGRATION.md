# Python & Visual Studio Code Integration Manual

This guide covers the **PyZoren** production Python SDK, VS Code workspace configurations, Python-to-Zoren snippets, and polyglot Python/Zoren development workflows.

---

## 🐍 1. Official Python SDK: `pyzoren`

The `pyzoren` package provides a high-performance Python bridge to the native Zoren platform.

### Installation
From the root repository:
```bash
pip install -e .
```
Or build standard wheels:
```bash
python3 -m build
pip install dist/pyzoren-1.0.0-py3-none-any.whl
```

### Core API Reference

#### A. Execute Scripts or Inline Code (`pyzoren.run`)
```python
import pyzoren

# Run inline code
result = pyzoren.run("""
flow main() -> Int {
    post("Hello from Zoren via Python!")
    deliver 0
}
""")

print("Stdout:", result.stdout)
print("Exit Code:", result.exit_code)
print(f"Executed in: {result.duration_ms:.2f} ms")
```

#### B. Dynamic Expression Evaluation (`pyzoren.eval_expr`)
Evaluates Zoren math, string transformations, and builtins in microseconds using the REPL engine:
```python
import pyzoren

# Math operations
assert pyzoren.eval_expr("100 / 4") == 25
assert pyzoren.eval_expr("sqrt(144)") == 12

# String pipelines
assert pyzoren.eval_expr('"zoren".up()') == "ZOREN"

# Booleans
assert pyzoren.eval_expr("10 > 5") is True
```

#### C. Persistent REPL Session (`pyzoren.ZorenSession`)
Maintain state across multiple Python calls:
```python
import pyzoren

with pyzoren.ZorenSession() as session:
    session.execute("flex counter: int = 10")
    session.execute("counter += 5")
    val = session.execute("counter * 2")
    print("Result:", val)
```

#### D. PyZoren CLI Tool
```bash
# Run script
pyzoren run script.zor

# Evaluate expression
pyzoren eval "sqrt(256) * 4"

# Run Doctor diagnostics
pyzoren doctor script.zor

# Auto-format
pyzoren fmt script.zor
```

---

## 💻 2. VS Code Python Snippets (`snippets/python.json`)

When writing `.py` files in VS Code with the Zoren extension installed, the following snippets are immediately available:

| Prefix | Description | Generated Code |
|---|---|---|
| `zor_run` | Run Zoren script from Python | Executes `pyzoren.run(path)` and handles results |
| `zor_eval` | Evaluate Zoren expression | `pyzoren.eval_expr("sqrt(144) * 2")` |
| `zor_session` | Persistent interactive session | `with pyzoren.ZorenSession() as zor:` block |
| `zor_fastapi` | High-throughput FastAPI route | Endpoint delegating compute to native Zoren |
| `zor_bench` | Microsecond benchmark showdown | Benchmark loop comparing Python vs native Zoren |
| `zor_numpy` | NumPy zero-copy tensor bridge | Connect NumPy arrays to Zoren AI enclave |
| `zor_ctypes` | Call compiled `.so` via ctypes | Load Zoren shared object using `ctypes.CDLL` |

---

## 🔁 3. Python Developer Aliases in Zoren (`snippets/zoren.json`)

For Python developers writing `.zor` files, familiar Python syntax expands directly into idiomatic Zoren constructs:

| Python Keyword | Expands To Zoren Equivalent |
|---|---|
| `def` | `flow function_name(param: int) -> int { ... deliver 0 }` |
| `class` | `model ClassName { open field: str }` |
| `import` | `use package as alias` |
| `from` | `use package.submodule as alias` |
| `try` | `maybe res = op() { err(e) -> ..., ok(val) -> ... }` |
| `print` | `post("...")` or `println("...")` |
| `dataclass` | `model RecordName { open id: int }` |

---

## ⚙️ 4. VS Code Polyglot Workspace Configuration (`.vscode/`)

The repository includes ready-to-use VS Code configurations:

### `.vscode/settings.json`
- Configures file associations for `*.zor` and `*.zoren`.
- Enables bracket pair colorization and semantic syntax highlighting.
- Activates the custom **Zoren Dark Modern** color theme with dedicated Python scopes.
- Sets auto-formatting on save for both Python and Zoren.

### `.vscode/tasks.json`
- `Ctrl+Shift+B`: Builds the release Zoren compiler (`make build`).
- Run Tests: Runs the full 273-file test runner (`python3 test_runner.py`).
- Run Benchmarks: Executes the multi-language speed showdown (`python3 benchmarks/speed_showdown/run_suite.py`).
- Package Extension: Packages the VS Code extension (`make vsix`).

### `.vscode/launch.json`
- `F5` on any `.py` file launches Python debugging with debugpy.
- `F5` on `test_runner.py` launches the test suite in debug mode.
- `F5` on `.zor` files executes the file with native AArch64 runner.

---

## 🎨 5. Python Syntax Coloring in "Zoren Dark Modern" Theme

The included VS Code theme formats Python syntax with distinctive, eye-friendly tones:
- **`def` / Functions**: Electric Cyan (`#61AFEF`, Bold)
- **`class` / Types**: Mint Gold (`#E5C07B`, Bold)
- **`self`**: Coral Red (`#E06C75`, Italic)
- **Decorators (`@dataclass`, `@staticmethod`)**: Warm Amber (`#D19A66`, Bold)
- **Builtins (`print`, `len`, `range`)**: Bright Teal (`#56B6C2`, Bold)
- **Docstrings (`"""..."""`)**: Slate Grey (`#7F848E`, Italic)
