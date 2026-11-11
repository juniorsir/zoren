# Unsupported Features in Zoren Version 1.0

The following features commonly found in other languages are **NOT** present in Zoren's current implementation:

1. **Class Inheritance & Virtual Tables (`class Child extends Parent`):**
   - Zoren uses data models (`model`) and devirtualized interface contracts (`ability` / `grant`).
2. **Automatic Garbage Collection (GC):**
   - Zoren uses stack frame allocation and bounded Chamber arenas (`Chamber[T]`).
3. **Rust-Style Borrow-Checker Lifetime Parameters (`'a`):**
   - Zoren uses single-use linear liveness contracts (`#linear`) without lifetime parameter syntax.
4. **C Pre-Processor Macros (`#define`):**
   - Zoren uses build-time subroutine evaluation (`comptime flow`).
5. **Dynamic Reflection & Runtime Type Mutation:**
   - Zoren uses compile-time monomorphization and static type queries (`type_of(val)`).
