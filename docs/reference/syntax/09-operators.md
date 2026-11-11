# Operators and Precedence

## Precedence Table

| Level | Operator | Description | Associativity |
| :---: | :--- | :--- | :---: |
| 1 | `.`, `()`, `[]` | Member access, call, indexing | Left-to-Right |
| 2 | `-`, `!`, `?` | Unary minus, logical NOT, optional | Right-to-Left |
| 3 | `*`, `/`, `%` | Multiplicative | Left-to-Right |
| 4 | `+`, `-` | Additive / String Concatenation | Left-to-Right |
| 5 | `<<`, `>>` | Bitwise Left Shift, Bitwise Right Shift | Left-to-Right |
| 6 | `&`, `|`, `^` | Bitwise AND, Bitwise OR, Bitwise XOR | Left-to-Right |
| 7 | `==`, `!=`, `<`, `<=`, `>`, `>=` | Relational Comparisons | Left-to-Right |
| 8 | `&&` | Logical AND | Left-to-Right |
| 9 | `||` | Logical OR | Left-to-Right |
| 10 | `??` | Null-coalescing | Left-to-Right |
| 11 | `=`, `+=`, `-=`, `*=` | Assignment & Mutation | Right-to-Left |

## Implementation Status
`SUPPORTED` (`zoren/src/parser.rs`, `codegen.rs`)
