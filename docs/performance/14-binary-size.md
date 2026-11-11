# Binary Size Optimization

## 1. Language Guarantee
`--direct-elf` builds standalone 64-bit ELF binaries without external GCC or C library overhead.

## 2. Current Implementation Details
Cargo release profiles enable `strip = true` to strip debug symbol tables.

## 3. Optimization Opportunities
Unreferenced functions in imported modules are pruned before code generation.
