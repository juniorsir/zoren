# General Migration Philosophy: Don't Translate Literally

Translating code line-by-line from another language to Zoren often results in un-idiomatic or inefficient code.

## Key Architectural Shift:
- **Data vs. Behavior:** Separate state into `model` and behavior into `ability`/`grant`.
- **Explicit Mutability:** Use `bind` by default; use `flex` only when mutation is necessary.
- **Deterministic Memory:** Use stack frames and Chamber arenas instead of manual heap pointers or garbage collectors.
- **Capability Contracts:** Explicitly pass capability tokens (`FileSystemCap`, `NetworkCap`) for I/O operations.
