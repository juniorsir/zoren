# Benchmarking Best Practices

Refer to [Performance Guide — BENCHMARKING](../performance/BENCHMARKING.md) for full methodology.

```shell
# Compile with maximum optimization
zoren benchmark_suite.zor -O3 --lto -o bench_app
./bench_app
```
