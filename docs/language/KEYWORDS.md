# Official Zoren Reserved Keywords

The following keywords are reserved by the active Zoren compiler implementation (`lexer.rs`):

| Keyword | Category | Active Compiler Role | Status |
| :--- | :--- | :--- | :--- |
| `flow` | Subroutines | Subroutine / function definition | `SUPPORTED` |
| `bind` | Declarations | Immutable constant binding | `SUPPORTED` |
| `flex` | Declarations | Mutable variable declaration | `SUPPORTED` |
| `deliver` | Control Flow | Subroutine return statement | `SUPPORTED` |
| `assess` | Pattern Matching | Multi-branch pattern match expression | `SUPPORTED` |
| `case` | Pattern Matching | Pattern match branch arm | `SUPPORTED` |
| `repeat` | Control Flow | Loop construct | `SUPPORTED` |
| `while` | Control Flow | Conditional loop predicate | `SUPPORTED` |
| `for` | Control Flow | Range iteration construct | `SUPPORTED` |
| `in` | Control Flow | Iterator bounds predicate | `SUPPORTED` |
| `if` | Control Flow | Conditional branch predicate | `SUPPORTED` |
| `else` | Control Flow | Alternative branch predicate | `SUPPORTED` |
| `break` | Control Flow | Loop break statement | `SUPPORTED` |
| `continue` | Control Flow | Loop iteration skip statement | `SUPPORTED` |
| `model` | Types | Composite struct data model definition | `SUPPORTED` |
| `open` | Exports | Public export modifier | `SUPPORTED` |
| `ability` | Traits | Interface contract definition | `SUPPORTED` |
| `grant` | Traits | Interface implementation block | `SUPPORTED` |
| `enum` | Types | Enumerated type definition | `SUPPORTED` |
| `divert` | Error Contracts | Error raise / throw statement | `SUPPORTED` |
| `diverges` | Error Contracts | Error signature contract declaration | `SUPPORTED` |
| `catch` | Error Contracts | Error handling block | `SUPPORTED` |
| `ensure` | Scope Cleanup | LIFO scope exit cleanup handler | `SUPPORTED` |
| `bring` | Modules | Module import statement | `SUPPORTED` |
| `as` | Modules | Module / symbol aliasing keyword | `SUPPORTED` |
| `use` | Modules | Package import block specifier | `SUPPORTED` |
| `extern` | Interop | Foreign function declaration | `SUPPORTED` |
| `ABI` | Interop | Target register calling convention specifier | `SUPPORTED` |
| `async` | Concurrency | Asynchronous flow modifier | `SUPPORTED` |
| `await` | Concurrency | Asynchronous task resolution | `SUPPORTED` |
| `spawn` | Concurrency | Concurrent Spindle task creation | `SUPPORTED` |
| `comptime` | Metaprogramming | Build-time subroutine evaluation | `SUPPORTED` |
| `compute_kernel` | Graphics / GPU | GPU shader kernel subroutine modifier | `SUPPORTED` |
| `accel` | Hardware AI | NPU hardware acceleration subroutine modifier | `SUPPORTED` |
| `actor` | Distributed | Distributed Actor model modifier | `SUPPORTED` |
| `chamber` | Memory | Bounded memory arena pool keyword | `SUPPORTED` |
| `true` | Literals | Boolean true literal | `SUPPORTED` |
| `false` | Literals | Boolean false literal | `SUPPORTED` |
| `null` | Literals | Null reference literal | `SUPPORTED` |
| `escape` | Memory | Escape analysis annotation | `SUPPORTED` |
| `skip` | Optimizations | Optimization bypass annotation | `SUPPORTED` |
