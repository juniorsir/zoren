# Zoren Performance Model

## 1. Language Guarantee
Zoren guarantees 0.00ms Garbage Collection pause latency. All memory is allocated on stack frames or bounded Chamber memory arenas.

## 2. Current Implementation Details
`zorenv1` and `zorenv2` compile Zoren source code directly into AArch64/x86_64 target machine assembly (`.s`) or freestanding ELF binaries (`elf.rs`).

## 3. Optimization Opportunities
Compiling with `-O3 --lto` enables whole-program Link-Time Optimization and dead code elimination.
