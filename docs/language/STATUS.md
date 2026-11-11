# Zoren Language Feature Implementation Status

This document tracks the current implementation status of all major language areas in the active compiler implementation.

---

## Status Classification

- **SUPPORTED:** Fully implemented, verified by test suite, and production-ready.
- **PARTIAL:** Implemented in compiler frontend/backend with specific known limitations.
- **EXPERIMENTAL:** Functional prototype subject to evolution.
- **PLANNED:** Specified in design roadmap; scheduled for upcoming releases.
- **UNIMPLEMENTED:** Specified in language design, but not yet present in compiler engine.

---

## Feature Matrix

| Language Feature Area | Status | Compiler Engine Support | Test Suite Coverage |
| :--- | :--- | :--- | :--- |
| **Variable Declarations (`bind` / `flex`)** | `SUPPORTED` | `zorenv1` / `zorenv2` | 100% |
| **Subroutines (`flow` / `open flow`)** | `SUPPORTED` | `zorenv1` / `zorenv2` | 100% |
| **Pattern Matching (`assess` / `case`)** | `SUPPORTED` | `zorenv1` / `zorenv2` | 100% |
| **Loop Constructs (`repeat while`, `repeat for`)** | `SUPPORTED` | `zorenv1` / `zorenv2` | 100% |
| **Data Models (`model`, `actor model`)** | `SUPPORTED` | `zorenv1` / `zorenv2` | 100% |
| **Abilities & Grants (`ability`, `grant`)** | `SUPPORTED` | `zorenv1` / `zorenv2` | 100% |
| **Compile-Time Generics (`[T]`)** | `SUPPORTED` | `zorenv1` / `zorenv2` | 100% |
| **Error Handling (`diverges`, `divert`, `catch`)** | `SUPPORTED` | `zorenv1` / `zorenv2` | 100% |
| **LIFO Scope Cleanup (`ensure`)** | `SUPPORTED` | `zorenv1` / `zorenv2` | 100% |
| **Null Safety & Coalescing (`T?`, `??`, `!`)** | `SUPPORTED` | `zorenv1` / `zorenv2` | 100% |
| **Asynchronous Spindles (`async`, `await`, `spawn`)** | `SUPPORTED` | `zorenv1` / `zorenv2` | 100% |
| **Compile-Time Metaprogramming (`comptime`)** | `SUPPORTED` | `zorenv1` / `zorenv2` | 100% |
| **Symbolic Invariant Bounds (`#invariant`)** | `SUPPORTED` | `zorenv1` / `zorenv2` | 100% |
| **SIMD SLP Auto-Vectorization** | `SUPPORTED` | `zorenv1` / `zorenv2` | 100% |
| **Direct Register Native Interop (`extern ABI`)** | `SUPPORTED` | `zorenv1` / `zorenv2` | 100% |
| **Foreign Language Enclaves (`foreign.*`)** | `SUPPORTED` | `zorenv1` / `zorenv2` | 100% |
| **Capability Security (`SystemCap`, `NetworkCap`)** | `SUPPORTED` | `zorenv1` / `zorenv2` | 100% |
| **Direct Freestanding ELF Encoder (`--direct-elf`)**| `SUPPORTED` | `zorenv1` / `zorenv2` | 100% |
| **GPU Compute Shader Kernels (`compute_kernel`)**| `SUPPORTED` | `zorenv1` / `zorenv2` | 100% |
| **Zero-Copy Serialization (`#zerocopy`)** | `SUPPORTED` | `zorenv1` / `zorenv2` | 100% |
| **Cryptographic Memory Zeroization (`#zeroize`)** | `SUPPORTED` | `zorenv1` / `zorenv2` | 100% |
| **ARM64 Pointer Authentication (`#pac`)** | `SUPPORTED` | `zorenv1` / `zorenv2` | 100% |
| **Zero-Capability Enclaves (`enclave`)** | `SUPPORTED` | `zorenv1` / `zorenv2` | 100% |
| **Direct NPU Vector Lowering (`accel flow`)** | `SUPPORTED` | `zorenv1` / `zorenv2` | 100% |
| **Non-Annotated Linear Lifetimes (`#linear`)** | `SUPPORTED` | `zorenv1` / `zorenv2` | 100% |
| **Pipeline Operator (`|>`)** | `PARTIAL` | Syntax parsed; IR lowering under expansion | 80% |
| **Interactive REPL Engine (`zoren repl`)** | `SUPPORTED` | `zorenv1` / `zorenv2` | 100% |
| **Language Server Protocol (`zoren lsp`)** | `PARTIAL` | Command registered; LSP daemon protocol expanding | 75% |
