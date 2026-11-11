# Zoren Ecosystem and Governance Specification
## Version 1.0 — Ecosystem & Operational Blueprint

---

## 1. Governance Model & Community Structure

Zoren is governed by an independent, multi-stakeholder framework designed to guarantee technical stability, transparent evolution, and long-term ecosystem viability.

```
                  +-----------------------------------+
                  |   Technical Steering Committee    |
                  |     (TSC - Final Design Arbiter)  |
                  +-----------------------------------+
                                    |
            +-----------------------+-----------------------+
            |                       |                       |
            v                       v                       v
+-----------------------+ +-----------------------+ +-----------------------+
|  Language & Compiler  | |   Standard Library    | |  Security & Registry  |
|     Working Group     | |     Working Group     | |     Working Group     |
+-----------------------+ +-----------------------+ +-----------------------+
```

### 1.1 Technical Steering Committee (TSC)
*   **Composition:** A panel of seven (7) members drawn from core compiler engineers, principal standard library architects, and major enterprise contributors.
*   **Term Limits:** Members serve staggered two-year terms, with empty seats filled by nomination and voting from the active contributor pool.
*   **Responsibilities:** 
    *   Acts as the final arbiter for language design decisions.
    *   Approves or rejects RFCs that have passed through the working groups.
    *   Establishes standard security response protocols and manages release timelines.

### 1.2 The RFC (Request for Comments) Process
Every language modification, syntax update, standard library API expansion, or tooling change must proceed through the formal RFC process.

#### RFC States:
1.  **Draft:** A preliminary proposal undergoing discussion in the relevant Working Group (WG).
2.  **Proposed:** The WG promotes the draft to a formal proposal, establishing a mandatory 30-day community review phase.
3.  **Active:** The TSC approves the RFC. Implementers are cleared to write code for the reference compiler (`zoren`).
4.  **Completed:** The feature is fully implemented, verified, tested, and shipped in a stable compiler release.
5.  **Rejected / Withdrawn:** The proposal is retired and archived to prevent design duplicates.

---

## 2. Package Ecosystem & Supply Chain Security

Zoren’s package manager uses a decentralized, content-addressed, and cryptographically verified design to prevent dependency confusion, registry hijacking, and supply chain vulnerabilities.

### 2.1 Content-Addressable Registry Layout
Packages are not indexed by subjective names alone. Instead, a package reference in `manifest.zor` consists of a cryptographically signed source URL combined with a SHA-256 hash of its contents:

```zoren
package <- "zoren::org::networking"
dependency "std::net" {:
    source <- "https://registry.zoren.org/std/net-v1.2.4.tar.gz",
    sha256 <- "e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855"
:}
```

### 2.2 Secure Package Manifests & Lockfiles
*   **Verification:** The package manager shall verify package hashes against `lock.zor` on every build. If any downloaded package hash deviates from the recorded lockfile entry, compilation halts immediately with a supply chain compromise error.
*   **Air-Gapped Mirroring:** Enterprise networks can mirror packages locally. By changing the source host mapping in the registry config while preserving SHA-256 hashes, builds remain deterministic and secure in air-gapped environments.

---

## 3. Release Lifecycle & Compatibility Guarantees

Zoren protects software investments by separating language updates into distinct cadences, backed by strict semantic versioning (SemVer) and Epoch transitions.

```
[ Stable Releases (Every 6 Months) ] ---------> [ Minor Patches / Bugfixes ]
  |
  +---> [ LTS Releases (Every 2 Years) ] ------> Supported for 5 Years
  |
  +---> [ Epoch Shift (Every 5 Years) ] --------> Controlled deprecation & migration
```

### 3.1 Release Cadences
*   **Stable Releases:** Occur every six (6) months, incrementing the minor version (e.g., `v1.1.0` $\rightarrow$ `v1.2.0`). Includes backward-compatible API additions.
*   **LTS Releases (Long-Term Support):** Occur every two (2) years, establishing a five-year support horizon for enterprise security and stability patches.
*   **Epoch Shifts:** Occur every five (5) years. An Epoch allows the language to deprecate old APIs or syntax structures. Codebases targeting older Epochs are guaranteed to compile alongside modern modules using the same compiler binary.

### 3.2 Backward Compatibility Matrix

| Transition | Source Compatibility | Binary Compatibility | Standard Library APIs |
| :--- | :--- | :--- | :--- |
| **Patch Release** | Guaranteed | Guaranteed | Immutable |
| **Minor Release** | Guaranteed | Guaranteed | Opt-in additions only |
| **Major Release** | Guaranteed | Evaluated by case | Deprecated APIs marked |
| **Epoch Shift** | Checked via compiler migration tools | Resolved at module boundaries | Outdated APIs removed |

---

## 4. Continuous Quality Assurance (QA) & Verification

The compiler and runtime are validated using automated testing to catch regressions and verify language invariants.

### 4.1 Automated QA Test Suite
*   **Performance Regression Testing:** Runs daily benchmarks of compiled programs against target hardware profiles to monitor and prevent execution time regressions.
*   **Compatibility Matrix Testing:** Every compiler commit is built and tested across all supported platforms (AArch64 Linux, x86-64 Linux, RISC-V macOS, etc.) via CI.
*   **Fuzz Testing:** Employs grammar-based fuzzer loops that generate thousands of random, malformed Zoren files to verify that the compiler parser handles unexpected inputs gracefully without crashing.

---

## 5. Ecosystem Roadmap (10-Year Vision)

This roadmap outlines Zoren’s long-term design objectives and technical milestones.

### 5.1 One-Year Horizon: Compiler and Ecosystem Maturation
*   **Objective:** Optimize the Stage 1 self-hosting compiler to match the performance of the Stage 0 bootstrap compiler.
*   **Milestones:** Implement the standard `std::collections` memory-pooling passes and achieve fully integrated DWARF/PDB debugging output.

### 5.2 Three-Year Horizon: Platform Expansion and Tooling Integration
*   **Objective:** Establish WebAssembly (WASM/WASI) as a first-class compiler target and standard library platform.
*   **Milestones:** Ship the offical Zoren Language Server Protocol (LSP) and launch the decentralized package registry index.

### 5.3 Five-Year Horizon: The First Epoch Transition (Epoch 2031)
*   **Objective:** Execute the first language Epoch transition to deprecate early bootstrap APIs and integrate lessons learned from production.
*   **Milestones:** Release the automated syntax migration tool `zoren migrate` to rewrite codebases safely.

### 5.4 Ten-Year Vision: The Safe Systems Standard
*   **Objective:** Establish Zoren as a preferred language for mission-critical software, operating systems, cloud systems, and high-performance embedded networks.
*   **Milestones:** Formalize the Zoren Language Specification through an international standards body (such as ISO) to ensure long-term stability and platform independence.

---

## 6. Success Metrics & Quality Indicators

The health and adoption of the Zoren ecosystem are tracked using clear, measurable indicators:

1.  **Compiler Defect Density:** Measured by the number of critical compiler bugs reported per 10,000 lines of standard library code, targeting a standard of `< 0.1` bugs.
2.  **Bootstrap Build Times:** The self-hosted compiler must compile its own complete codebase in under ten (10) seconds on standard target hardware, preserving developer productivity.
3.  **Zero-Overhead Abstractions:** Aspect devirtualization passes must achieve a 100% static dispatch resolution rate across the standard library, verifying our performance guarantees.
4.  **Ecosystem Growth Rate:** Evaluated by the number of verified, cryptographically signed libraries published in the decentralized package ecosystem.

