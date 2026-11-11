# Profiling Tools and Hotspots

## 1. Language Guarantee
`--dump-allocations` prints detailed compile-time Chamber memory allocation traces.

## 2. Current Implementation Details
`--dump-cfg` and `--dump-ssa` emit control flow graphs and SSA IR for inspection.

## 3. Optimization Opportunities
Using `--pgo-generate` builds instrumented binaries to collect execution profiles (`.zprof`).
