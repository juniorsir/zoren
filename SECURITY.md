# Security Policy

The **Zoren Programming Language** is built with military-grade memory safety and binary exploit mitigations as first-class architectural constraints.

---

## 🛡️ Built-in Exploit Mitigations

Every binary produced with `zoren --secure` or `make build` enforces:

1. **Stack Smashing Protection (SSP / Canary)**:
   - `-fstack-protector-strong` protects every stack frame against buffer overwrites.
2. **Address Space Layout Randomization (ASLR / PIE)**:
   - Position Independent Executable (`-fPIE -pie`) randomizes code and data segments in memory.
3. **Full RELRO (Read-Only Relocations)**:
   - `-Wl,-z,relro,-z,now` resolves all symbols during loader initialization and marks Global Offset Tables (GOT) strictly read-only, neutralizing GOT overwrite exploits.
4. **Non-Executable Stack (NX Stack)**:
   - `-Wl,-z,noexecstack` guarantees execution denial on stack buffers.
5. **ARM64 Pointer Authentication & Branch Target Identification (PAC/BTI)**:
   - `-mbranch-protection=standard` hardware-level return address signing and branch target validation preventing Jump-Oriented Programming (JOP) and Return-Oriented Programming (ROP) attacks.
6. **Zero-Trust Chamber Enclaves**:
   - Compiler-enforced capability barriers isolating sensitive memory zones.

---

## 🚨 Reporting a Vulnerability

If you discover a security vulnerability, compiler exploit vector, or chamber isolation bypass in Zoren, please do **NOT** open a public issue.

Instead, please send a responsible disclosure report to:

📧 **security@zoren-lang.org**

### Information to Include:
- Description of the vulnerability and attack vector.
- Minimal reproducible proof of concept (`.zor` or assembly trace).
- Affected architectures (AArch64, x86_64, WebAssembly) and OS versions.
- Potential impact and suggested mitigations.

### Response Timeline:
- **Initial Response**: Within 24 hours.
- **Triage & Reproduction**: Within 72 hours.
- **Patch & Advisory Release**: Coordinated with the reporter, typically within 14 days.

We credit all responsible security researchers in our security advisories and release notes.
