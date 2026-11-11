# Awesome Zoren [![Awesome](https://awesome.re/badge.svg)](https://awesome.re)

> A curated list of awesome Zoren frameworks, libraries, tools, plugins, learning resources, and community projects.

---

## 🌟 Official Ecosystem
- [Zoren Compiler Toolchain](https://github.com/zoren-lang/zoren) — Native AArch64/Linux compiler engine with SSA, LTO, and military-grade exploit mitigations.
- [PyZoren](https://github.com/zoren-lang/zoren/tree/master/pyzoren) — Official Python SDK and native runtime bridge.
- [VS Code Extension](https://github.com/zoren-lang/zoren/tree/master/tools/vscode-zoren) — Syntax highlighting, dark theme, snippets, and LSP client.
- [Interactive Studio REPL](https://github.com/zoren-lang/zoren/blob/master/docs/tooling/REPL.md) — Enterprise interactive evaluation environment.

---

## 🧠 AI, ML & Tensor Computing
- **`std/nn.zor`** — Transformer Attention Heads (`Scaled Dot-Product`), Multi-Head Attention, Xavier Initialization, GELU, and Dense layers.
- **`std/lora.zor`** — Parameter-Efficient Fine-Tuning LoRA adapter projections with forward matrix scaling.
- **`std/quantization.zor`** — Symmetric INT8 quantization and fast integer dot products.
- **`projects/zoren_ai`** — End-to-end vision and language autograd tensor inference pipeline.

---

## 🌐 Distributed Systems & Databases
- **`plugins/raft_consensus.zor`** — Production Raft distributed consensus state machine with leader leases and log replication.
- **`plugins/bptree_db.zor`** — High-performance ordered B+ Tree database engine with contiguous leaf range scanning.
- **`std/bloom_filter.zor`** — Probabilistic double-hashing filter with zero false negatives.
- **`std/json_stream.zor`** — Zero-allocation streaming JSON tokenizer and extractor for high-throughput LLM tool calling.
- **`std/metrics.zor`** — Prometheus / OpenMetrics compatible counters, gauges, and histograms.

---

## 🛠️ Editor Integrations
- [Visual Studio Code](docs/tooling/VSCODE.md) — First-class extension with TextMate grammar and theme.
- [Vim / Neovim](tools/vim-zoren/syntax/zoren.vim) — Syntax definitions and filetype detection.
- [Helix](tools/editors/helix_languages.toml) — Helix language configuration with LSP auto-launch.
- [Sublime Text](tools/editors/zoren.sublime-syntax) — Syntax specification for Sublime Text 3 & 4.

---

## 📚 Learning Resources
- [Official Zoren Tutorial](docs/TUTORIAL.md) — 10-chapter comprehensive tutorial.
- [Python to Zoren Rosetta Stone](docs/PYTHON_TO_ZOREN_GUIDE.md) — 15 side-by-side comparison sections for Python developers.
- [The Zoren Cookbook](docs/COOKBOOK.md) — 10 production-ready recipes (APIs, Raft, vector search, LLM serving).
- [Production Deployment Guide](PRODUCTION_DEPLOYMENT.md) — Enterprise bare-metal and container ops.

---

## 👥 Community
- [GitHub Discussions](https://github.com/zoren-lang/zoren/discussions)
- [Discord Server](https://discord.gg/zoren-lang)
- [Twitter / X](https://twitter.com/zorenlang)
