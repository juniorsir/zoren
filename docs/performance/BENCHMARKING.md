# Official Benchmarking Methodology

To obtain accurate, reproducible performance measurements in Zoren, benchmarks MUST follow these standards:

## 1. Environment Controls
- **Warm-Up Runs:** Execute 3 warm-up runs to stabilize CPU branch predictors and hardware caches before recording.
- **Repeated Sample Runs:** Collect a minimum of 10 timing iterations and report median wall-clock execution time.
- **CPU Frequency Pinning:** Set target CPU governor to performance mode where available.

## 2. Compiler Configuration
- Benchmarks MUST be built using release compilation flags (`-O3 --lto`). Debug builds (`-O0`) MUST NOT be used for performance comparison.

## 3. Allocation & Memory Measurement
- Measure resident set size (RSS) memory footprint using process stats or Chamber arena allocation counters (`--dump-allocations`).
