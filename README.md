<div align="center">

# ⚡ Zoren Programming Language

### *Autonomous, Bare-Metal Systems Language with Native AI Autograd & Zero-GC Chamber Memory*

[![CI](https://github.com/zoren-lang/zoren/actions/workflows/ci.yml/badge.svg)](https://github.com/zoren-lang/zoren/actions/workflows/ci.yml)
[![Version](https://img.shields.io/badge/version-1.0.0-blue.svg)](https://github.com/zoren-lang/zoren/releases)
[![Platform](https://img.shields.io/badge/arch-AArch64%20Linux-green.svg)](https://github.com/zoren-lang/zoren)
[![Tests](https://img.shields.io/badge/tests-295%20passed%20%28100%25%29-brightgreen.svg)](file:///root/Zoren_lang/test_runner.py)
[![Python SDK](https://img.shields.io/badge/python%20sdk-pyzoren%20v1.0-3776AB.svg?logo=python&logoColor=white)](pyzoren)
[![VS Code](https://img.shields.io/badge/vscode-extension%20v1.3.0-007ACC.svg?logo=visualstudiocode&logoColor=white)](dist/zoren-lang-1.3.0.vsix)
[![Discord](https://img.shields.io/badge/discord-join%20community-5865F2.svg?logo=discord&logoColor=white)](https://discord.gg/zoren-lang)
[![License](https://img.shields.io/badge/license-MIT-purple.svg)](LICENSE)

[**Quickstart**](#-zoren-in-60-seconds) •
[**Quick Reference**](docs/QUICK_REFERENCE.md) •
[**Python to Zoren Guide**](docs/PYTHON_TO_ZOREN_GUIDE.md) •
[**Standard Library Catalog**](docs/standard-library/README.md) •
[**Tutorial**](docs/TUTORIAL.md) •
[**Cookbook**](docs/COOKBOOK.md) •
[**Benchmarks**](#-bare-metal-performance-showdown-aarch64-linux) •
[**Roadmap**](ROADMAP.md) •
[**Awesome Zoren**](AWESOME_ZOREN.md)

</div>

---

## 💡 Why Zoren?

Modern software architectures face an acute split: developers write prototypes in **Python** for expressive elegance, then rewrite critical backend pipelines in **C++ or Rust** for bare-metal latency and memory density.

**Zoren bridges this divide directly:**
1. **Pythonic Readability**: Clean, indentation-aware syntax, first-class pipelines (`|>`), pattern matching, and straightforward error recovery (`maybe`/`err`).
2. **Bare-Metal Native Speed**: Compiles directly to hardened AArch64 machine code via SSA, peephole optimization, and Link-Time Optimization (LTO). Zero tracing GC pauses.
3. **Chamber Arena Isolation**: Bounded memory enclaves execute bump-pointer allocations with $O(1)$ batch resets and compiler-enforced capability boundaries.
4. **Native AI Tensors & SIMD**: Accelerated `@matrix` kernels, transformer multi-head attention (`std/nn`), parameter-efficient fine-tuning (`std/lora`), and INT8 quantization (`std/quantization`) built into the grammar.
5. **Military-Grade Security Hardening**: Stack Canary (SSP), ASLR (PIE), Full RELRO, NX Stack, and ARM64 PAC/BTI active by default on production binaries.

---

## ⚡ Zoren in 60 Seconds

```zoren
bring math
bring text
bring sys

// Struct Data Model
model ServerMetrics {
    open requests: Int
    open latency_us: Int
}

// Flow Subroutine with Vector Pipeline
flow process_stream(data: [Int]) -> Int {
    flex sum: Int = 0
    for val in data {
        sum = sum + val
    }
    deliver sum
}

flow main() -> Int {
    post("⚡ Welcome to Zoren Platform v1.0!")

    // 1. Immutable Bindings & Mutable Flex Variables
    bind language: Text = "Zoren"
    flex counter: Int = 0

    // 2. Loop & Mathematical Operations
    for i in 0..5 {
        counter = counter + (i * i)
    }
    post("Sum of squares: ", counter) // 30

    // 3. String Method Pipelines
    post(language.up()) // "ZOREN"

    deliver 0
}
```

Compile and run natively:
```bash
zoren run main.zor
```

---

## 📊 Bare-Metal Performance Showdown (AArch64 Linux)

Measured on bare-metal Linux AArch64 with `-O3` maximum optimization against standard production runtimes:

| Benchmark | **Zoren (Native)** | **Rust (`-O3`)** | **C++ (Clang `-O3`)** | **Node.js (V8)** | **Python 3.14** | Speedup vs Python |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Recursive Fibonacci (fib 38)** | **385.61 ms** | 406.82 ms | 507.86 ms | 2,288.48 ms | 16,046.95 ms | 🥇 **41.6x faster** |
| **Collatz Conjecture (1,000,000)** | **426.99 ms** | 445.81 ms | 501.43 ms | 3,677.20 ms | 29,804.18 ms | 🥇 **69.8x faster** |
| **Monte Carlo Pi (10,000,000)** | **415.55 ms** | 418.46 ms | 466.41 ms | 2,193.38 ms | 12,209.88 ms | 🥇 **29.4x faster** |
| **Neural Vector Math (1,000,000)** | **143.67 ms** | 136.42 ms | 161.17 ms | 783.63 ms | 5,184.46 ms | 🥈 **36.1x faster** |
| **Prime Sieve (250,000)** | **165.08 ms** | 135.23 ms | 93.57 ms | 911.71 ms | 879.22 ms | 🥉 **5.5x faster** |

---

## 🛠️ Installation

### Quick Automated Installer
```bash
curl -sSL https://raw.githubusercontent.com/zoren-lang/zoren/master/install.sh | bash
# Or locally:
./install.sh
```

Installs the compiler binary to `/usr/local/bin/zoren`, plus standard library modules and plugins to `/usr/local/share/zoren/`.

### From Source (Makefile)
```bash
# Build production compiler with LTO
make build

# Install system-wide and to user home
make install

# Run complete 273-test automated regression suite
make test

# Package standalone distribution archive (.tar.gz)
make dist
```

---

## 🐍 Official Python SDK: `pyzoren`

Adopt Zoren incrementally in existing Python projects:

```bash
pip install -e .
```

```python
import pyzoren

# Evaluate Zoren expressions in microseconds
assert pyzoren.eval_expr("100 / 4") == 25
assert pyzoren.eval_expr("sqrt(144) * 2") == 24
assert pyzoren.eval_expr('"zoren".up()') == "ZOREN"

# Run Zoren script files or inline code
res = pyzoren.run("kernel.zor")
print("Native execution time:", res.duration_ms, "ms")
```

---

## 🎨 Visual Studio Code Extension & Editor Support

Zoren provides first-class developer tooling for **VS Code**, **Vim/Neovim**, **Helix**, and **Sublime Text**:

- **Official Extension**: [`dist/zoren-lang-1.3.0.vsix`](dist/zoren-lang-1.3.0.vsix)
- **Install in VS Code**:
  ```bash
  code --install-extension dist/zoren-lang-1.3.0.vsix
  ```
- **Features**:
  - 🎨 **Full Syntax Coloring**: Granular TextMate tokens for flows, models, decorators (`@matrix`, `@simd`, `@inline`), pipelines, template expressions, and types.
  - 🌌 **Zoren Dark Modern Theme**: Hand-crafted high-contrast dark theme calibrated for both Zoren and Python syntax.
  - ⚡ **LSP Integration**: Inline real-time compiler diagnostics, hover type inspection, and auto-formatting (`Shift+Alt+F`).
  - 📝 **Python & Zoren Snippets**: Instant scaffolding for `pyzoren.run()`, `eval_expr()`, FastAPI routes, NumPy bridges, and Python aliases (`def`, `class`, `import`, `try`).
  - 🚀 **Integrated Shortcuts**: Run (`Alt+R`), Doctor (`Alt+D`), and REPL (`Alt+Z`).

See [**docs/tooling/VSCODE.md**](docs/tooling/VSCODE.md) and [**docs/tooling/PYTHON_VSCODE_INTEGRATION.md**](docs/tooling/PYTHON_VSCODE_INTEGRATION.md).

---

## 💻 Zoren Interactive Studio REPL (v3.0)

Launch the interactive evaluation environment:
```bash
zoren repl
```

```text
⚡ Zoren Interactive Studio [Version 3.0.0 Enterprise]
Target Architecture: AArch64 Native • Full RELRO • SSP • PAC/BTI Active
Type :help for commands, :plugins for AI/backend plugins, :quit to exit.

[1] zoren ❯ 100 / 4
=> [Int]: 25

[2] zoren ❯ "zoren".up()
=> [Text]: "ZOREN"

[3] zoren ❯ sqrt(144)
=> [Int]: 12

[4] zoren ❯ :inspect 42
Expression Introspection:
  Expression : 42
  Type       : Int
  Value      : 42
  Size       : 2 bytes
  Hex Value  : 0x000000000000002A
  Binary     : 0b0000000000000000000000000000000000000000000000000000000000101010
```

---

## 🧠 Standard Library & Enterprise Plugin Ecosystem

Zoren features a comprehensive, zero-dependency ecosystem of **78 native production modules** categorized across systems programming, high-performance data structures, distributed consensus, serialization, and native AI:

### 🌲 High-Performance Data Structures & Algorithms
- **[`std/rope.zor`](file:///root/Zoren_lang/std/rope.zor)**: Binary tree for large texts: $O(\log N)$ concatenation, slicing, insertion, and deletion.
- **[`std/fenwick_tree_2d.zor`](file:///root/Zoren_lang/std/fenwick_tree_2d.zor)**: 2D Binary Indexed Tree for dynamic point updates and 2D range sum queries.
- **[`std/van_emde_boas.zor`](file:///root/Zoren_lang/std/van_emde_boas.zor)**: $O(\log \log U)$ integer priority queue: min, max, predecessor, successor.
- **[`std/wavelet_matrix.zor`](file:///root/Zoren_lang/std/wavelet_matrix.zor)**: Succinct Wavelet Matrix for $O(\log \Sigma)$ rank queries and range quantile selection.
- **[`std/b_plus_tree.zor`](file:///root/Zoren_lang/std/b_plus_tree.zor)** & **[`std/red_black_tree.zor`](file:///root/Zoren_lang/std/red_black_tree.zor)**: Self-balancing search trees for embedded storage engines.
- **[`plugins/cuckoo_hash_map.zor`](file:///root/Zoren_lang/plugins/cuckoo_hash_map.zor)**: Guaranteed $O(1)$ worst-case lookup dual-hash map with kick-out displacement and stash.
- **[`plugins/vector_hnsw.zor`](file:///root/Zoren_lang/plugins/vector_hnsw.zor)**: Hierarchical Navigable Small World (HNSW) proximity graph for ANN vector search.

### 🌐 Distributed Systems & Consensus
- **[`plugins/raft_joint_consensus.zor`](file:///root/Zoren_lang/plugins/raft_joint_consensus.zor)** & **[`plugins/raft_log_compaction.zor`](file:///root/Zoren_lang/plugins/raft_log_compaction.zor)**: Raft cluster reconfiguration and log snapshot compaction.
- **[`plugins/paxos_multidecree.zor`](file:///root/Zoren_lang/plugins/paxos_multidecree.zor)**: Multi-instance Paxos consensus engine with phase 1/2 slot proposals.
- **[`plugins/chandy_lamport_snapshot.zor`](file:///root/Zoren_lang/plugins/chandy_lamport_snapshot.zor)**: Distributed global state snapshot capturing process & in-flight channel states.
- **[`plugins/distributed_barrier.zor`](file:///root/Zoren_lang/plugins/distributed_barrier.zor)**: Multi-stage cyclic barrier with dynamic generation rolling and arrival synchronization.
- **[`plugins/consistent_ring_vnodes.zor`](file:///root/Zoren_lang/plugins/consistent_ring_vnodes.zor)** & **[`plugins/consistent_ring_maglev.zor`](file:///root/Zoren_lang/plugins/consistent_ring_maglev.zor)**: High-speed packet & partition routing rings.

### 📦 Modern Serialization & Framing
- **[`std/json.zor`](file:///root/Zoren_lang/std/json.zor)** & **[`std/csv.zor`](file:///root/Zoren_lang/std/csv.zor)**: Zero-copy JSON and CSV tabular data parsers.
- **[`plugins/zstandard_frame.zor`](file:///root/Zoren_lang/plugins/zstandard_frame.zor)** & **[`plugins/snappy_framed.zor`](file:///root/Zoren_lang/plugins/snappy_framed.zor)**: Official RFC 8878 Zstandard and Google Snappy framed streaming codecs.
- **[`plugins/parquet_metadata.zor`](file:///root/Zoren_lang/plugins/parquet_metadata.zor)** & **[`plugins/arrow_ipc_frame.zor`](file:///root/Zoren_lang/plugins/arrow_ipc_frame.zor)**: Apache Parquet and Arrow columnar format inspectors.
- **[`plugins/flatbuffers_verifier.zor`](file:///root/Zoren_lang/plugins/flatbuffers_verifier.zor)** & **[`plugins/capnproto_frame.zor`](file:///root/Zoren_lang/plugins/capnproto_frame.zor)**: Zero-copy binary serialization verifiers.

### 🤖 Native AI & Machine Learning
- **[`std/nn.zor`](file:///root/Zoren_lang/std/nn.zor)**: Transformer Multi-Head Attention, LayerNorm, Dense layers, and GELU activation.
- **[`std/lora.zor`](file:///root/Zoren_lang/std/lora.zor)**: Parameter-Efficient Fine-Tuning LoRA adapter projections ($W_0 + \frac{\alpha}{r}AB$).
- **[`std/quantization.zor`](file:///root/Zoren_lang/std/quantization.zor)**: Symmetric INT8 quantization, fast integer dot products, and 4-bit packed weights.

👉 **[Browse the Full Standard Library Catalog (All 78 Modules)](docs/standard-library/README.md)**

---

## 🤝 Community & Contributing

We welcome contributions from developers, researchers, and systems enthusiasts of all skill levels:

- **[Contributing Guide](CONTRIBUTING.md)**: Architecture walk-through, local development, and PR instructions.
- **[Code of Conduct](CODE_OF_CONDUCT.md)**: Contributor Covenant v2.1.
- **[Security Policy](SECURITY.md)**: Vulnerability disclosure and exploit mitigation guarantees.
- **[Support & Channels](SUPPORT.md)**: GitHub Discussions, Discord, and FAQs.
- **[Roadmap](ROADMAP.md)**: Forward-looking milestones and feature timeline.
- **[Awesome Zoren](AWESOME_ZOREN.md)**: Curated showcase of projects, plugins, and guides.

### Stay Connected:
- 💬 **GitHub Discussions**: [github.com/zoren-lang/zoren/discussions](https://github.com/zoren-lang/zoren/discussions)
- 🎮 **Discord Community**: [discord.gg/zoren-lang](https://discord.gg/zoren-lang)
- 🐦 **Twitter / X**: [@zorenlang](https://twitter.com/zorenlang)

---

## 📄 License
Zoren is distributed under the terms of the **MIT License**. See [LICENSE](LICENSE) for details.
