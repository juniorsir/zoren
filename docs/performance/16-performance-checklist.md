# Pre-Optimization Checklist

## 1. Language Guarantee
1. Measure baseline median execution time.
2. Confirm bottleneck using `--dump-allocations` or profiler.
3. Build with `-O3 --lto` release flags.
4. Re-measure and verify correctness.

## 2. Current Implementation Details
Follows systematic 4-step performance verification methodology.

## 3. Optimization Opportunities
Iterative benchmark validation.
