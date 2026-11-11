# Performance Pitfalls

## 1. Language Guarantee
Avoid re-allocating Chamber arenas inside tight loops without calling `reset_frame_chamber`.

## 2. Current Implementation Details
Avoid un-buffered single-byte I/O operations.

## 3. Optimization Opportunities
Avoid building performance benchmarks in debug mode (`-O0`).
