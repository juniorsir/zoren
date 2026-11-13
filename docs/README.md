# 📖 Welcome to Zoren Documentation

> **Fast like C, Readable like Python, Built for Systems & AI.**

Welcome to the official documentation for the **Zoren Programming Language**. Whether you are writing high-throughput distributed microservices, AI inference pipelines, or embedded low-level algorithms, Zoren is engineered to be approachable, expressive, and bare-metal fast.

---

## ⚡ Zoren in 3 Minutes

If you know Python, TypeScript, or Go, you already know 90% of Zoren!

### 1. Variables & Mutability
```zoren
// Immutable value by default:
bind name = "Antigravity"
bind max_connections = 1000

// Mutable variable using 'flex':
flex counter = 0
counter = counter + 1
```

### 2. Subroutines (`flow`) & Returns (`deliver`)
```zoren
// Subroutines are defined with 'flow'
// Returns are explicitly dispatched with 'deliver'
flow calculate_tax(amount: Int, rate: Int) -> Int {
    if amount <= 0 {
        deliver 0
    }
    deliver (amount * rate) / 100
}
```

### 3. Data Models (`model`)
```zoren
// Define clean data models / structs
model ServerConfig {
    open host: Text
    open port: Int
    open secure: Bool
}
```

### 4. Loops & Control Flow
```zoren
flow print_even_numbers(limit: Int) -> Int {
    flex i = 0
    while i <= limit {
        if (i % 2) == 0 {
            post(i) // prints to console
        }
        i = i + 1
    }
    deliver 0
}
```

### 5. Bringing Modules
```zoren
bring math
bring json
bring fs
bring plugins.cuckoo_hash_map
```

---

## 🧭 Documentation Map

Find exactly what you need quickly:

| Guide | Description | Best For |
|---|---|---|
| **[⚡ Quick Reference Cheat Sheet](./QUICK_REFERENCE.md)** | 1-page complete cheat sheet of all keywords, types, and compiler commands. | Everyday coding |
| **[🧩 Creating Modules & Plugins](./guides/modules_and_plugins.md)** | Guide to creating custom modules & plugins, combining them, and global setup. | Custom packages |
| **[🐍 Python to Zoren Guide](./PYTHON_TO_ZOREN_GUIDE.md)** | Side-by-side Rosetta Stone comparing Python idioms directly to Zoren. | Python developers |
| **[🎓 15-Lesson Tutorial Series](./getting-started/01-installation.md)** | Step-by-step beginner journey from installation to advanced abilities. | Beginners |
| **[🍲 Production Cookbook](./COOKBOOK.md)** | Real-world recipes: HTTP servers, Raft consensus, vector search, and tokenizers. | Backend engineers |
| **[📚 Standard Library & Plugin Index](./standard-library/README.md)** | Complete reference of all 78 native modules (Data structures, Networking, AI). | All developers |
| **[💻 VS Code & Editor Setup](./tooling/VSCODE.md)** | Syntax highlighting, LSP autocomplete, formatting, and dark neon themes. | Tooling setup |
| **[🚀 Production Deployment](../PRODUCTION_DEPLOYMENT.md)** | Bare-metal compile flags, security hardening, and deployment pipelines. | DevOps & SREs |

---

## 🛠️ The 3 Essential CLI Commands

```bash
# 1. Compile and link a Zoren program into a native binary:
zoren main.zor -o main

# 2. Run the compiled binary:
./main

# 3. Run the full automated test suite:
python3 test_runner.py
```

---

## 💡 Top 5 Tips for Clean Zoren Code

1. **Explicit Return Types:** Always annotate flow return types (`-> Int`, `-> Bool`, `-> Text`).
2. **Every Deliver Returns an Expression:** Write `deliver 0` or `deliver true` for clean control flow.
3. **String Comparison:** Use `constant_time_compare(str1, str2)` or `sys_constant_time_compare` for bulletproof content equality checks.
4. **String Concatenation:** Combine strings with `str_concat(s1, s2)` for maximum performance.
5. **Zero Memory Leaks:** If you allocate buffers with `alloc_buffer(size)`, release them with `free_buffer(ptr)` when done.

---

## 🤝 Community & Contributing

- **Issue Tracker:** [GitHub Issues](https://github.com/juniorsir/zoren/issues)
- **Discussion Board:** [GitHub Discussions](https://github.com/juniorsir/zoren/discussions)
- **Contribution Guide:** [`CONTRIBUTING.md`](../CONTRIBUTING.md)
