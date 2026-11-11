# Contributing to Zoren

Thank you for your interest in contributing to **Zoren**! Zoren is a high-performance, military-hardened programming language with native AI tensor autograd, zero-GC chamber memory, and bare-metal AArch64 speed.

We welcome contributions from compiler engineers, systems programmers, AI researchers, and technical writers!

---

## 🛠️ Setting Up Your Local Environment

### Prerequisites
- **Rust Toolchain**: `rustup` with stable Rust (`rustc 1.75+`, `cargo`).
- **Python 3.8+**: Used by the automated regression test harness and `pyzoren`.
- **Node.js 18+** (Optional): Only needed for packaging the VS Code extension.

### Clone and Build
```bash
git clone https://github.com/zoren-lang/zoren.git
cd zoren

# Compile the release compiler binary
make build

# Verify build
./bin/zoren --version
```

---

## 🧪 Running the Test Suite

Zoren features a comprehensive regression test harness covering all 273 language, semantic, parsing, optimization, and AI test cases.

```bash
# Run full automated regression suite
python3 test_runner.py

# Run Python SDK tests
python3 tests/test_pyzoren.py

# Run bare-metal speed showdown benchmarks
python3 benchmarks/speed_showdown/run_suite.py
```

All 273 tests must pass before submitting a Pull Request.

---

## 🏗️ Compiler Architecture Overview

The Zoren compiler (`zoren/src/`) is structured into decoupled, modular passes:

```
Source (.zor) 
      │
      ▼
lexer.rs          Tokenization & Quote-Aware Parsing
      │
      ▼
parser.rs         Abstract Syntax Tree (AST) Generation & Error Recovery
      │
      ▼
semantic.rs       Scope Resolution, Ability Tables & Chamber Enclave Validation
      │
      ▼
hir.rs / ssa.rs   High-Level IR & Static Single Assignment Transform
      │
      ▼
optimize.rs       Constant Folding, Inlining & Dead-Code Elimination
      │
      ▼
codegen.rs        Native AArch64 Machine Code / WAT Emission
      │
      ▼
elf.rs            Hardened ELF Binary Emission (Full RELRO, SSP, PAC/BTI)
```

---

## 📐 Adding a New Standard Library Module or Plugin

1. Standard library files belong in `std/` (e.g. `std/my_module.zor`).
2. High-performance plugins belong in `plugins/` (e.g. `plugins/my_plugin.zor`).
3. Add corresponding regression tests in `tests/` with the metadata header:
   ```zoren
   # EXPECT: SUCCESS
   // your test code here
   ```
4. Verify using `python3 test_runner.py`.

---

## 🎨 Code Style & Formatting

- **Zoren Code**: Format using `./bin/zoren fmt <file.zor>`.
- **Rust Code**: Follow `cargo fmt` and `cargo clippy`.
- **Python Code**: Adhere to PEP 8.

---

## 🚀 Submitting a Pull Request

1. Fork the repository and create your branch from `master`:
   ```bash
   git checkout -b feat/my-new-feature
   ```
2. Write clear, descriptive commit messages:
   ```
   feat(parser): add support for range pattern matching
   fix(repl): prevent quote splitting on division slashes
   docs(tutorial): add section on chamber memory allocation
   ```
3. Push to your fork and submit a Pull Request using the provided PR template.
4. Engage with reviewer feedback in a friendly, constructive manner.

---

## 💬 Community Channels
- **GitHub Discussions**: [github.com/zoren-lang/zoren/discussions](https://github.com/zoren-lang/zoren/discussions)
- **Discord Server**: [discord.gg/zoren-lang](https://discord.gg/zoren-lang)
- **Twitter / X**: [@zorenlang](https://twitter.com/zorenlang)
