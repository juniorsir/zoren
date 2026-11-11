# Benchmarking Best Practices

## 1. Language Guarantee
Benchmarks MUST use release compilation flags (`-O3 --lto`) and record median execution times.

## 2. Current Implementation Details
`live_performance_test.py` provides the standard timing harness.

## 3. Optimization Opportunities
Avoid running benchmarks on power-throttled battery profiles.
