# Values and Memory Layout

## 1. Language Guarantee
Primitive types (`i8`–`i64`, `f64`) and model fields match natural target architecture byte alignment rules.

## 2. Current Implementation Details
`zoren/src/types.rs` computes exact byte sizes (`i64` = 8 bytes, `f64` = 8 bytes).

## 3. Optimization Opportunities
Annotating models with `#align(64)` aligns memory structures to 64-byte CPU cache lines.
