# Toolchain Architecture Overview

```
Zoren Source (.zor) ──> zoren / zorenv1 ──> SSA IR / AArch64 Assembly (.s) ──> gcc / ld.lld ──> Executable Binary
                                    │
                                    └──> Direct ELF Encoder (elf.rs) ──────────> Executable Binary (0 External Tools)
```
