# Zoren Official Documentation Policy

This document establishes the binding quality, accuracy, and operational standards for all official Zoren documentation.

---

## Core Documentation Principles

1. **Implementation Authoritativeness:**
   - The **CURRENT** compiler implementation (`zoren` / `zorenv1` / `zorenv2`) is the authoritative source of truth.
   - Documentation must accurately reflect actual compiler behavior. If documentation conflicts with the implementation, the conflict must be reported and resolved explicitly.

2. **No Undocumented Behavior Allowed:**
   - No feature may be presented as supported unless it is fully implemented and tested in the active compiler codebase.

3. **Compilable Code Examples:**
   - All code examples marked as executable must be valid, compilable Zoren programs verified by the automated test harness (`test_runner.py`).

4. **Syntax Precision:**
   - All documented syntax rules, keywords, and grammar constructs must match the active parser implementation exactly.

5. **Explicit Stability Identification:**
   - Every API, library function, and compiler directive must explicitly state its stability status:
     - `SUPPORTED` — Production-ready, fully implemented, and verified by test suites.
     - `PARTIAL` — Implemented in compiler pipeline, with specific known limitations.
     - `EXPERIMENTAL` — Opt-in or prototype feature subject to evolution.
     - `PLANNED` — Approved for future release roadmap.
     - `UNIMPLEMENTED` — Specified in design, but not yet present in compiler backend.

6. **Explicit Deprecation & Experimental Marking:**
   - Deprecated or experimental features must be prominently flagged with clear notices and recommended alternatives.

7. **Benchmark-Backed Performance Claims:**
   - All performance claims, speedup ratios, and memory footprints must be backed by reproducible benchmark results.

8. **Diagnostic Code Accuracy:**
   - Every documented compiler diagnostic must use its official diagnostic code (e.g., `Z1001`, `Z2001`, `Z3001`, `Z4006`, `Z8001`, `Z9001`).

9. **Clear Structural Separation:**
   - Documentation must rigorously distinguish between **Syntax** (grammar rules), **Semantics** (type checking and runtime behavior), and **API Contracts** (library functions and capability parameters).
