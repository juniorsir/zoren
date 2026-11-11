# 🗺️ Zoren Language Roadmap

This document outlines the strategic engineering roadmap and vision for the **Zoren Programming Language** and platform.

---

## 🟢 Phase 1: Foundation & Production Readiness (v1.0.0) — *Current*
- [x] Native AArch64 bare-metal compiler engine with SSA and Link-Time Optimization (LTO).
- [x] Military-grade binary hardening: Full RELRO, Stack Canary (SSP), ASLR (PIE), NX Stack, and ARM64 PAC/BTI.
- [x] Quote-aware Interactive Studio REPL v3.0 Enterprise with mathematical builtins and introspection (`:inspect`, `:plugins`, `:models`).
- [x] Standard library: Neural Networks (`std/nn`), LoRA PEFT (`std/lora`), INT8 Quantization (`std/quantization`), JSON streaming (`std/json_stream`), Metrics (`std/metrics`), Bloom filters (`std/bloom_filter`).
- [x] Production plugins: Raft Consensus (`plugins/raft_consensus`), B+ Tree Database (`plugins/bptree_db`).
- [x] Comprehensive 10-chapter tutorial, Rosetta Stone guide, and 10-recipe production cookbook.
- [x] Official VS Code extension (`zoren-lang-1.3.0.vsix`), Zoren Dark Modern theme, 20+ snippets.
- [x] Official Python SDK (`pyzoren`) with `eval_expr()`, `run()`, and persistent sessions.
- [x] 100% automated regression test suite pass rate (273/273 tests).

---

## 🟡 Phase 2: Hardware Acceleration & Cloud Native (v1.2 - v1.5)
- [ ] **CUDA & ROCm Native Backend**: Direct PTX / GCN code emission for GPU tensor forward passes without external drivers.
- [ ] **Apple Silicon AMX / Metal Acceleration**: Native hooks into Apple Neural Engine and Matrix Coprocessor.
- [ ] **WebAssembly DOM & WebGPU Bindings**: Full browser client-side execution with direct canvas and WebGPU rendering.
- [ ] **Zero-Allocation gRPC / Protobuf Generator**: Automatic compile-time protobuf wire format generation.
- [ ] **Native Async Event Loop**: Epoll / io_uring asynchronous runtime integration with green spindle threads.

---

## 🟣 Phase 3: Self-Hosting & Ecosystem Maturity (v2.0)
- [ ] **Self-Hosting Compiler**: Re-implementing the Zoren compiler in pure Zoren.
- [ ] **`zpm` Package Registry**: Decentralized, cryptographically-signed package manager for Zoren packages.
- [ ] **Formal Verification Engine**: SMT-solver-backed formal verification of chamber enclave invariants.
- [ ] **Language Server Protocol (LSP) v2**: Jump-to-definition, find references, and automated refactoring inside VS Code.
