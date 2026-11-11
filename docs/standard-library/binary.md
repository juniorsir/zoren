# std/binary Reference

Binary analysis, ELF header inspection, and disassembly.

- `parse_elf(path: Text) -> Int` — Parses 64-bit ELF header entrypoint.
- `disassemble_bytes(b: Text) -> Int` — Disassembles machine code instruction stream.
