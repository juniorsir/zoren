# Debugging and Diagnostics

- **Compiler Diagnostics:** Detailed error locations with line, column, snippet pointers, and quick-fix hints.
- **IR Inspection Dumps:**
  - `zoren main.zor --dump-cfg` (Control Flow Graphs)
  - `zoren main.zor --dump-ssa` (Static Single Assignment IR)
  - `zoren main.zor --dump-escape` (Escape Analysis Decisions)
