# Official Zoren Operator Inventory

The following operators are implemented in the active compiler pipeline (`lexer.rs`, `parser.rs`, `codegen.rs`):

## 1. Arithmetic Operators
- `+` (Addition / String Concatenation) — `SUPPORTED`
- `-` (Subtraction / Unary Negation) — `SUPPORTED`
- `*` (Multiplication) — `SUPPORTED`
- `/` (Division) — `SUPPORTED`
- `%` (Modulo) — `SUPPORTED`
- `+=`, `-=`, `*=`, `/=`, `%=` (Compound Assignment) — `SUPPORTED`
- `++`, `--` (Postfix Increment / Decrement) — `SUPPORTED`

## 2. Relational Operators
- `==` (Equal) — `SUPPORTED`
- `!=` (Not Equal) — `SUPPORTED`
- `<` (Less Than) — `SUPPORTED`
- `<=` (Less Than or Equal) — `SUPPORTED`
- `>` (Greater Than) — `SUPPORTED`
- `>=` (Greater Than or Equal) — `SUPPORTED`

## 3. Logical Operators
- `&&` (Logical AND) — `SUPPORTED`
- `||` (Logical OR) — `SUPPORTED`
- `!` (Logical NOT) — `SUPPORTED`

## 4. Null Safety & Assignment Operators
- `=` (Variable Assignment) — `SUPPORTED`
- `??` (Null-Coalescing Operator) — `SUPPORTED`
- `!` (Postfix Error / Optional Unwrap) — `SUPPORTED`

## 5. Path, Access & Arrow Operators
- `.` (Field Access / UFCS Dot Call) — `SUPPORTED`
- `::` (Selective Symbol Extraction) — `SUPPORTED`
- `->` (Subroutine Return / Match Arm Arrow) — `SUPPORTED`
- `|>` (Pipeline Composition Operator) — `PARTIAL`

## 6. Syntactic Delimiters
- `{`, `}` (Block Braces) — `SUPPORTED`
- `[`, `]` (Generic Brackets / Collection Brackets) — `SUPPORTED`
- `(`, `)` (Parameter Parentheses) — `SUPPORTED`
- `:` (Type Specifier) — `SUPPORTED`
- `,` (Element Separator) — `SUPPORTED`
