# 🧩 Zoren Module Development & Ecosystem Guide

Welcome to the **Zoren Module Ecosystem**! This guide walks you through creating, testing, packaging, and publishing custom modules and libraries for Zoren.

Whether you are building high-performance numerical algorithms, networking clients, game engines, cryptography utilities, or embedded drivers, this guide provides the standard conventions and tooling needed to share your work with the global Zoren community.

---

## 1. What is a Zoren Module?

In Zoren, a module is a reusable package of:
* Functions and algorithms
* Custom data types and `struct` definitions
* Zero-trust security chambers (`chamber`)
* Refinement contracts and assertions
* Native C/FFI bindings or hardware primitives

Modules can be distributed as:
1. **Source Modules (`.zor`)**: Native Zoren files that can be imported directly using `import module_name;`.
2. **Pre-compiled Libraries (`.a` / `.so` / `.dylib`)**: Binary modules linked using Zoren's native linker.
3. **Python Bridge Extensions**: Hybrid packages allowing Python developers to call Zoren routines seamlessly via `pyzoren`.

---

## 2. Creating Your First Module

Let's build a sample module named `fast_math`.

### Step 1: Create the Module Directory Structure

```bash
fast_math/
├── zoren.mod.json          # Module manifest & metadata
├── README.md               # Documentation and usage guide
├── LICENSE                 # Choose your preferred license (e.g. MIT / Apache 2.0)
├── src/
│   ├── mod.zor             # Module entry point
│   ├── matrix.zor          # Matrix math submodule
│   └── statistics.zor      # Statistical algorithms
└── tests/
    └── test_fast_math.zor  # Unit test suite
```

### Step 2: Define `zoren.mod.json`

Create the metadata manifest file:

```json
{
  "name": "fast_math",
  "version": "0.1.0",
  "description": "Hyper-fast linear algebra and numerical routines for Zoren",
  "author": "Your Name <you@example.com>",
  "license": "MIT",
  "entry": "src/mod.zor",
  "dependencies": {},
  "targets": ["linux-aarch64", "linux-x86_64", "macos-arm64"]
}
```

### Step 3: Implement the Module Logic (`src/mod.zor`)

```zoren
// src/mod.zor - Module Entry Point
module fast_math;

pub struct Vector2 {
    pub x: f64,
    pub y: f64,
}

pub fn vector_add(a: Vector2, b: Vector2) -> Vector2 {
    return Vector2 {
        x: a.x + b.x,
        y: a.y + b.y,
    };
}

pub fn dot_product(a: Vector2, b: Vector2) -> f64 {
    return (a.x * b.x) + (a.y * b.y);
}

// Zero-trust chamber for sensitive mathematical transformations
pub chamber SecureStats {
    pub fn variance(values: [f64], mean: f64) -> f64 {
        let mut sum_sq: f64 = 0.0;
        let n: i64 = len(values);
        if n <= 1 {
            return 0.0;
        }
        
        let mut i: i64 = 0;
        while i < n {
            let diff: f64 = values[i] - mean;
            sum_sq = sum_sq + (diff * diff);
            i = i + 1;
        }
        
        return sum_sq / (n - 1) as f64;
    }
}
```

### Step 4: Write Unit Tests (`tests/test_fast_math.zor`)

```zoren
import fast_math;

fn main() -> i64 {
    let v1 = fast_math::Vector2 { x: 3.0, y: 4.0 };
    let v2 = fast_math::Vector2 { x: 1.0, y: 2.0 };

    let sum = fast_math::vector_add(v1, v2);
    assert(sum.x == 4.0);
    assert(sum.y == 6.0);

    let dot = fast_math::dot_product(v1, v2);
    assert(dot == 11.0);

    println("All fast_math tests passed successfully!");
    return 0;
}
```

Run tests with the Zoren compiler:

```bash
zoren test tests/test_fast_math.zor
```

---

## 3. Best Practices for Zoren Modules

1. **Leverage Zero-Trust Chambers**:
   Wrap stateful operations, file parsing, or network packet handlers inside `chamber <Name> { ... }` blocks so callers benefit from hardware memory scrubbing and isolation.
2. **Encourage Static Range Invariants**:
   Use bounded integer types or assertions so the Zoren Refinement Prover can statically eliminate runtime bounds checks and division-by-zero checks.
3. **Include Multi-Architecture Support**:
   Test on both AArch64 and x86_64 to ensure seamless performance portability.
4. **Retain Full Ownership**:
   All modules you author belong 100% to you. Choose an open license like MIT or Apache 2.0 if you want maximum adoption, or commercial terms if you distribute proprietary plugins.

---

## 4. Publishing & Sharing Your Module

To share your module with the community:

1. **Host on GitHub**: Push your module repository (e.g., `https://github.com/your-username/zoren-fast-math`).
2. **Showcase on GitHub Discussions**:
   Submit a post under the [**Module Showcase**](https://github.com/juniorsir/zoren/discussions/categories/module-showcase) category on `juniorsir/zoren`.
3. **List in Awesome Zoren**:
   Open a Pull Request on [`juniorsir/zoren`](https://github.com/juniorsir/zoren) to add your package to `AWESOME_ZOREN.md`.
4. **Tag Your Repository**:
   Add the GitHub repository topics `zoren-module`, `zoren`, `systems-programming` so developers can discover it.

Together, we are building the fastest and safest systems software ecosystem in the world!
