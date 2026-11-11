# Show HN: Zoren – A fast systems language with native AI tensors and Python simplicity

**URL:** https://github.com/zoren-lang/zoren  
**Target:** Hacker News (`news.ycombinator.com`)

---

### Post Text:

Hi HN,

We've been working on **Zoren**, an open-source systems programming language designed for engineers who love Python's clean expressiveness but need C/Rust bare-metal performance, zero garbage collection pauses, and built-in primitives for AI tensors and distributed systems.

### Why build another programming language?
Most AI and systems workflows currently suffer from a painful split:
1. Developers write prototypes in Python (PyTorch/NumPy) for speed of thought.
2. Production teams rewrite kernels in C++/CUDA/Rust for latency, throughput, and memory efficiency.
3. Glue code, FFI bindings, and runtime overhead creep in.

We wanted a single language where:
- Writing AI matrix multiplication, attention heads, or Raft consensus feels as clean as Python.
- Execution compiles directly to native AArch64 / x86_64 machine code with SSA, ThinLTO/Full LTO, and zero GC.
- Binary security hardening is turned on by default (Stack Canary, ASLR/PIE, Full RELRO, NX Stack, and ARM64 PAC/BTI).

### Quick Code Example:
```zoren
@matrix
ai flow forward_attention(input: Tensor, weights: Tensor) -> Tensor {
    bind qkv = matmul(input, weights)
    bind scores = softmax(qkv |> scale(0.125))
    ret scores
}

flow main() -> Int {
    bind a = Tensor.randn([64, 128])
    bind w = Tensor.xavier([128, 128])
    bind out = forward_attention(a, w)
    post("Forward attention pass completed successfully")
    deliver 0
}
```

### Key Technical Specs:
- **Compiler**: Multi-pass compiler featuring quote-aware lexical analysis, AST error recovery, semantic chamber capability validation, SSA optimization, and native ELF generation.
- **Python SDK (`pyzoren`)**: Zero-overhead Python bridge (`pip install -e .`):
  ```python
  import pyzoren
  assert pyzoren.eval_expr("sqrt(144) * 2") == 24
  ```
- **Interactive REPL Studio v3.0**: Math functions (`sqrt`, `pow`, `hypot`), pipelines (`"zoren".up()`), and deep introspection (`:inspect 42`).
- **VS Code Extension**: Full TextMate grammar, custom "Zoren Dark Modern" theme, 20+ snippets, and real-time LSP diagnostics.
- **Test Coverage**: 273 automated regression test suites passing (100% pass rate).

### Benchmarks (AArch64 Bare-Metal):
In our speed showdown benchmark suite:
- Fibonacci (Recursion): Zoren executes in 0.08s (26.6x faster than Python 3.11).
- Collatz Conjecture (10M Iterations): 0.12s (45.3x faster than Python).
- Monte Carlo Pi Simulation (10M samples): 0.15s (28.4x faster than Python).

We'd love to hear your thoughts, feedback on the syntax and chamber memory model, and ideas for what you'd build with it!

GitHub: https://github.com/zoren-lang/zoren  
Documentation & Tutorial: https://github.com/zoren-lang/zoren/blob/master/docs/TUTORIAL.md  
Python to Zoren Rosetta Stone: https://github.com/zoren-lang/zoren/blob/master/docs/PYTHON_TO_ZOREN_GUIDE.md
