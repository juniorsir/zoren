# 📦 ZorPack: Package Management & Distribution in Zoren

**ZorPack** is Zoren's native package and module distribution system. It provides the frictionless simplicity of Python (`pip`) and JavaScript (`npm`), while completely redesigning package architecture to eliminate supply chain vulnerabilities, dependency bloat, and untrusted execution.

---

## 1. The Vision: Easy Like Python & npm, Unique to Zoren

Developers love the speed of `pip install` and `npm install`. However, traditional package managers suffer from critical architectural flaws:
- **`node_modules` Bloat:** Every project duplicates hundreds of megabytes of identical dependencies on disk.
- **Supply-Chain Malware:** Unverified `postinstall` or `setup.py` scripts execute arbitrary code during installation, stealing environment variables and SSH keys.
- **Untracked Provenance:** Binaries have no verifiable proof of which libraries or author identities were compiled into them.

**ZorPack re-engineers package distribution around Zoren's core strengths:**

| Feature | npm (`npm i`) | Python (`pip`) | Zoren (`zoren add / publish`) |
| :--- | :--- | :--- | :--- |
| **Command Simplicity** | `npm i <pkg>` | `pip install <pkg>` | `zoren add <pkg>` |
| **Publishing** | `npm publish` | `twine upload` | `zoren publish` |
| **Disk Storage** | Duplicated per project (`node_modules`) | Shared or virtualenvs | **Zero-Bloat Global Content Store** (Merkle hashed) |
| **Pre-Install Scripts** | Executes arbitrary shell scripts | Executes arbitrary Python | **Zero Arbitrary Execution** (pure static analysis) |
| **Security Auditing** | Manual (`npm audit` ad-hoc) | Third-party scanners | **Native Capability Graph** (statically verified sandbox) |
| **Signatures & Identity** | Optional / external | Rarely signed | **Built-in Ed25519 Signing + Merkle Root** |
| **Binary Provenance** | None | None | **Immutable `.note.zoren.credit` in ELF binaries** |

---

## 2. Developer Experience: Fast, Clean, Frictionless

### Adding a Dependency
To add any module—from the registry or directly from GitHub:

```bash
# From the Zoren Module Registry:
zoren add jwt_auth

# Directly from a Git repository:
zoren add github.com/community/hyper_vector

# Or local package:
zoren add ./libs/custom_engine
```

**What happens behind the scenes:**
1. ZorPack fetches the package into the global content-addressed store (`~/.zoren/community/`).
2. Runs the **Zoren Capability Audit** (checks network access, filesystem writes, and memory bounds).
3. Records the dependency cleanly into your project's `manifest.zor`.

Now, simply bring it into your code:
```zoren
bring jwt_auth
bring hyper_vector

flow main() -> Int {
    post("Dependencies loaded securely!")
    deliver 0
}
```

---

### Removing a Dependency
```bash
zoren remove jwt_auth
```
ZorPack cleanly removes the entry from `manifest.zor` and unlinks it from your active workspace.

---

### Creating and Publishing Your Own Module

Distributing your module to other developers takes a single command:

#### Step 1: Initialize or Structure Your Module
Create a folder with your module code and a `manifest.zor`:

```
my_vector_tool/
├── manifest.zor
└── my_vector_tool.zor
```

Example `manifest.zor`:
```zoren
# Package Manifest
package <- "zoren::community::my_vector_tool"
version <- "1.2.0"
license <- "MIT"
description <- "High-speed SIMD vector math module"

capabilities {
    pure: true
    network: false
    filesystem: false
}
```

Example `my_vector_tool.zor`:
```zoren
// 'open' exports the flow to callers
open flow dot_product_2d(x1: Int, y1: Int, x2: Int, y2: Int) -> Int {
    deliver (x1 * x2) + (y1 * y2)
}
```

#### Step 2: Publish with `zoren publish`
Run the publisher:
```bash
zoren publish .
```

Output:
```text
==================================================
⚡ ZOREN CRYPTOGRAPHIC PACKAGE PUBLISHER
==================================================
Publishing workspace: 'my_vector_tool' (v1.2.0)
1. Validating package source syntax & abilities...
2. Verifying developer Ed25519 identity key (~/.zoren/identity.key)...
3. Computing SHA-256 Merkle Root Hash...
4. Packaging sealed distribution bundle: release/my_vector_tool_v1.2.0_aarch64.zpkg
==================================================
✓ Package `my_vector_tool` v1.2.0 successfully forged and published!
  ├── Merkle Root: sha256:4f8a...c912
  ├── Identity Key: ed25519:pub:00a1b2c3...
  └── Distributable: release/my_vector_tool_v1.2.0_aarch64.zpkg
==================================================
```

---

## 3. The 3 Architectural Pillars of ZorPack

### 1. Zero Disk Bloat (Global Content Store)
Unlike `node_modules` which can swallow gigabytes across several local projects:
- ZorPack caches modules centrally at `~/.zoren/community/` and `~/.zoren/packages/`.
- Projects reference packages by Merkle hash. If 20 projects use `vector_hnsw`, exactly **one copy** exists on your machine.
- Zero copy time, zero duplicate storage, instant project cloning.

### 2. The Capability Security Graph (Zero Supply-Chain Attacks)
In npm and Python, malicious packages frequently inject obfuscated curl commands or cryptominers into install scripts.

**Zoren makes this physically impossible:**
- Modules have **no lifecycle install scripts**.
- During compilation, Zoren statically audits the Abstract Syntax Tree (AST):
  ```bash
  zoren audit ./my_module
  ```
  If a package claims to be a `json_parser` but attempts socket access, the compiler flags capability violation `[Z5001]` and halts compilation.

### 3. Cryptographic Provenance & Binary Attribution
When compiling a Zoren project with external dependencies:
1. Every module is verified against its Ed25519 author signature.
2. The compiler embeds an immutable ELF note section (`.note.zoren.credit`) directly into the final AArch64 executable:
   - Contains author public key, Merkle root hash, and build timestamp.
   - Provides unforgeable software bill of materials (SBOM) built directly into the binary!

---

## 4. Quick CLI Reference

| Command | Action |
| :--- | :--- |
| `zoren new <name>` | Scaffold a new project or module with standard layout |
| `zoren add <pkg>` | Resolve, audit, and install a package dependency |
| `zoren remove <pkg>` | Remove a dependency from manifest and workspace |
| `zoren publish [path]` | Cryptographically seal, sign, and build a `.zpkg` bundle |
| `zoren audit [path]` | Inspect the capability graph (pure, network, filesystem) |
| `zoren repl` | Interactive shell (`:modules` to inspect installed modules) |
