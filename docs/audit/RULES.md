# Zoren Documentation Audit Rules

| Rule ID | Name | Severity | Description |
| :--- | :--- | :---: | :--- |
| **DOC001** | Directory & File Existence | `ERROR` | Verifies existence of required documentation directories and index files. |
| **DOC002** | Link Integrity | `ERROR` | Verifies all internal Markdown links (`.md`) resolve to existing files. |
| **DOC003** | Keyword Alignment | `ERROR` | Compares reserved keywords in `lexer.rs` against `KEYWORDS.md`. |
| **DOC004** | Type System Alignment | `ERROR` | Compares compiler primitive types against `TYPES.md`. |
| **DOC005** | Operator Alignment | `ERROR` | Compares active compiler operators against `OPERATORS.md`. |
| **DOC006** | Standard Library API Coverage | `ERROR` | Verifies documented public APIs against `std/*.zor` declarations. |
| **DOC007** | Diagnostic Error Code Audit | `ERROR` | Verifies diagnostic error codes (`Zxxxx`) against compiler source. |
| **DOC008** | Executable Example Audit | `ERROR` | Compiles and executes code examples using `verify_examples.py`. |
| **DOC009** | Status Term Consistency | `WARNING` | Checks for status term contradictions across documentation phases. |
| **DOC010** | Performance Claim Evidence | `WARNING` | Checks that strong performance claims have corresponding evidence in `CLAIMS.md`. |
