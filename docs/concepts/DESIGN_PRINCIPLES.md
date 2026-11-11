# Zoren Design Principles

1. **Readability Over Cleverness:** Non-abbreviated, explicit English keywords (`bind`, `flex`, `flow`, `deliver`, `ensure`).
2. **Explicitness:** Zero implicit type widening or hidden memory allocations.
3. **Predictable Performance:** 0.00ms startup latency and zero Garbage Collection pause spikes.
4. **Capability-Based Security:** Systems access requires explicit capability tokens (`FileSystemCap`, `NetworkCap`).
5. **Compile-Time Devirtualization:** Interfaces (`ability`/`grant`) and generics (`[T]`) resolve at build time with 0 vtable overhead.
