<div align="center">

# 🔱 Zoren Language

### *Autonomous, Hyper-Performance, Memory-Safe Systems Language*

[![Release](https://img.shields.io/badge/release-v1.0.0-blue.svg?style=for-the-badge&logo=github)](https://github.com/juniorsir/zoren/releases/tag/v1.0.0)
[![License](https://img.shields.io/badge/License-ZBEL_Proprietary_Core_/_Open_Ecosystem-amber.svg?style=for-the-badge)](LICENSE.md)
[![Discussions](https://img.shields.io/badge/Community-Discussions-green.svg?style=for-the-badge&logo=github)](https://github.com/juniorsir/zoren/discussions)
[![Sponsors](https://img.shields.io/badge/Sponsor-GitHub_Sponsors-ff69b4.svg?style=for-the-badge&logo=github-sponsors)](https://github.com/sponsors/juniorsir)
[![Platforms](https://img.shields.io/badge/Platforms-Linux_ARM64_|_x86__64_|_macOS_Apple_Silicon-brightgreen.svg?style=for-the-badge)]()

<br/>

**Zoren** is an ahead-of-time (AOT) compiled systems programming language engineered for mission-critical software, high-frequency computing, autonomous systems, and embedded hardware. Combining a static integer interval refinement prover with zero-trust hardware memory tagging (ARM64 TBI/MTE) and register-level zeroization, Zoren achieves execution latencies faster than both **Rust 2024 (`rustc -O3`)** and **C++23 (`clang++ -O3`)**.

</div>

---

## ⚡ Bare-Metal Benchmark Showdown (Linux AArch64)

All benchmarks measured on bare-metal AArch64 hardware (median of 3 runs, wall-clock timing):

| Benchmark Workload | Zoren (AOT Native) | Rust 2024 (`-O3`) | C++23 (`clang++ -O3`) | Python 3.14 | Zoren Advantage |
|---|---|---|---|---|---|
| **Collatz Conjecture (1,000,000)** | **227 ms** | 401 ms | 427 ms | 25,856 ms | 🥇 **1.76x faster than Rust**, 1.88x vs C++, 113.9x vs Python |
| **Monte Carlo Pi (10,000,000)** | **179 ms** | 284 ms | 289 ms | 12,213 ms | 🥇 **1.59x faster than Rust**, 1.61x vs C++, 68.2x vs Python |
| **Recursive Fibonacci (`fib 38`)** | **294 ms** | 401 ms | 404 ms | 13,065 ms | 🥇 **1.36x faster than Rust**, 1.37x vs C++, 44.4x vs Python |
| **Prime Sieve Counting (250,000)** | **22 ms** | 89 ms | 168 ms | 1,149 ms | 🥇 **4.04x faster than Rust**, 7.63x vs C++, 52.2x vs Python |

---

## 🔒 Source Code Policy & Intellectual Property Protection

> [!IMPORTANT]
> **Source Code Availability Notice:**  
> The core compiler backend, code generator transforms, loop rotation optimizers, and refinement range interval prover represent proprietary intellectual property owned exclusively by **Juniorsir**.
>
> In accordance with our security and IP protection guidelines, **the internal compiler source code is NOT published into the public domain and is maintained in a private development vault**.
>
> **What is free and publicly available:**
> 1. Pre-compiled standalone native binaries for **Linux AArch64**, **Linux x86_64**, and **macOS ARM64** are 100% free for developer and commercial usage.
> 2. The official **Python SDK (`pyzoren`)** and **Visual Studio Code extension** are free and publicly distributed.
> 3. The **Zoren Standard Library**, header definitions, and module ecosystem are free and open for public development, extension, and third-party packaging.
> 4. Applications and modules you write in Zoren belong 100% to you.
>
> Reverse engineering, unauthorized decompilation, redistribution under alternate branding, or publication of leaked compiler source code is strictly prohibited by the [Zoren Binary & Ecosystem License](LICENSE.md).

---

## 💖 Sponsorship & Extended Access

Developing bare-metal compiler technology and expanding hardware-tier memory safety requires sustained investment. Sponsoring Zoren unlocks deeper architectural access and direct support:

👉 [**Sponsor on GitHub Sponsors (github.com/sponsors/juniorsir)**](https://github.com/sponsors/juniorsir)

| Tier | Monthly | Access & Perks |
|---|---|---|
| ☕ **Community Backer** | `$5 / mo` | GitHub Sponsor badge, private Discussions backer room, roadmap voting. |
| ⚡ **Ecosystem Builder** | `$25 / mo` | Bleeding-edge nightly compiler builds, module showcase highlight, direct technical Q&A. |
| 🚀 **Pro Developer** | `$100 / mo` | Priority bug triage, monthly 1-on-1 performance review, logo on official release notes. |
| 🏢 **Enterprise Partner** | `$500 - $1,500+ / mo` | **Enterprise Source Code Audit & Inspection** under mutual NDA, custom hardware target optimization (Graviton, Neoverse, RISC-V), commercial SLA. |

For enterprise agreements, contact **juniorsir** directly or read [docs/SPONSORSHIP.md](docs/SPONSORSHIP.md).

---

## 🧩 Community & Module Ecosystem Hub

We invite developers worldwide to build the next generation of systems software on Zoren!

* **Build Your Own Modules**: Read the [Zoren Module Development Guide](docs/MODULE_DEVELOPMENT.md) to author reusable packages (`.zor`), C/FFI extensions, or Python bridges.
* **Join GitHub Discussions**: [**github.com/juniorsir/zoren/discussions**](https://github.com/juniorsir/zoren/discussions)
  * 📢 **Announcements**: Language milestones and release digests.
  * 📦 **Module Showcase**: Share your libraries, frameworks, and tools.
  * 💡 **Ideas & RFCs**: Propose new standard library additions and language features.
  * 💬 **Q&A**: Get help from community engineers and systems architects.

---

## 🚀 Quickstart Installation

### 1. Automated Universal Installer (Linux & macOS)

Install the latest pre-compiled binary with a single command:

```bash
curl -fsSL https://raw.githubusercontent.com/juniorsir/zoren/master/install.sh | bash
```

Verify your installation:
```bash
zoren --version
# Zoren Language Compiler v1.0.0
```

### 2. Standalone Binary Downloads

Download the pre-built tarball for your platform from [Releases](https://github.com/juniorsir/zoren/releases/tag/v1.0.0):

* 🐧 **Linux 64-bit ARM (AArch64 / Termux / Pi / Cloud ARM)**: [`zoren-v1.0.0-linux-aarch64.tar.gz`](https://github.com/juniorsir/zoren/releases/download/v1.0.0/zoren-v1.0.0-linux-aarch64.tar.gz)
* 🐧 **Linux 64-bit x86 (`x86_64`)**: [`zoren-v1.0.0-linux-x86_64.tar.gz`](https://github.com/juniorsir/zoren/releases/download/v1.0.0/zoren-v1.0.0-linux-x86_64.tar.gz)
* 🍏 **macOS Apple Silicon (`arm64` - M1/M2/M3/M4)**: [`zoren-v1.0.0-macos-arm64.tar.gz`](https://github.com/juniorsir/zoren/releases/download/v1.0.0/zoren-v1.0.0-macos-arm64.tar.gz)

Extract and install:
```bash
tar -xzf zoren-v1.0.0-linux-aarch64.tar.gz
sudo cp bin/zoren /usr/local/bin/
```

### 3. Official Python SDK (`pyzoren`)

Execute and control Zoren directly from Python:

```bash
pip install https://github.com/juniorsir/zoren/releases/download/v1.0.0/pyzoren-1.0.0-py3-none-any.whl
```

```python
import pyzoren

# Run Zoren code with Python interoperability
result = pyzoren.run("fn main() -> i64 { return 42; }")
print("Zoren returned:", result.returncode)
```

### 4. Visual Studio Code Extension

Install syntax highlighting, snippets, and high-contrast themes:

```bash
code --install-extension https://github.com/juniorsir/zoren/releases/download/v1.0.0/zoren-lang-1.3.0.vsix
```

---

## 💡 Code Examples

### 1. Collatz Conjecture (Hyper-Optimized Leaf Inlining)
```zoren
fn collatz(mut n: i64) -> i64 {
    let mut steps: i64 = 0;
    while n > 1 {
        if n % 2 == 0 {
            n = n / 2;
        } else {
            n = 3 * n + 1;
        }
        steps = steps + 1;
    }
    return steps;
}

fn main() -> i64 {
    let mut max_steps: i64 = 0;
    let mut i: i64 = 1;
    while i <= 1000000 {
        let s = collatz(i);
        if s > max_steps {
            max_steps = s;
        }
        i = i + 1;
    }
    println("Maximum Collatz steps: ", max_steps);
    return 0;
}
```

### 2. Zero-Trust Hardware Chamber Isolation
```zoren
// Chamber memory space is hardware-isolated and sanitized on exit
chamber CryptoKeyStore {
    let master_seed: i64 = 0xDEADBEEF;

    pub fn derive_key(salt: i64) -> i64 {
        return (master_seed ^ salt) * 6364136223846793005;
    }
}

fn main() -> i64 {
    let key = CryptoKeyStore::derive_key(1337);
    println("Derived key: ", key);
    // Upon exit, CPU scratch registers x16/x17 are zeroed at hardware level
    return 0;
}
```

---

## 📚 Documentation & Guides

* 🚀 [**Getting Started Guide**](docs/getting-started/README.md)
* 🐍 [**Python-to-Zoren Migration Manual**](docs/PYTHON_TO_ZOREN_GUIDE.md)
* 📖 [**Language Tutorial**](docs/TUTORIAL.md)
* 🍳 [**Production Cookbook**](docs/COOKBOOK.md)
* 🧩 [**Module Development & Ecosystem Guide**](docs/MODULE_DEVELOPMENT.md)
* 💖 [**Sponsorship & Extended Access Tiers**](docs/SPONSORSHIP.md)
* 🌐 [**Developer Community & Showcase**](docs/COMMUNITY.md)

---

## 📄 License & Legal Notice

* **Binaries & Tooling**: Distributed under the [Zoren Binary & Ecosystem License (ZBEL v1.0)](LICENSE.md). Free for personal, academic, and commercial use.
* **Core Compiler Engine**: All rights reserved. Intellectual property of Juniorsir.
* **User Code & Modules**: You retain 100% full copyright over software and modules written in Zoren.
