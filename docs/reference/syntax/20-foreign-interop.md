# Foreign Language Interoperability

## 1. Syntax
```ebnf
ExternABI = "extern" "ABI" StringLiteral "flow" Identifier "(" Params ")" "->" Type ;
ForeignImport = "bring" "foreign." ( "python" | "c" | "cpp" | "rust" ) ;
```

## 2. Example
```zoren
bring foreign.python as py
extern ABI "C" flow c_sin(angle: F64) -> F64

flow main() -> Int {
    bind np = py_import_pkg("numpy")
    deliver 0
}
```

## 3. Implementation Status
`SUPPORTED` (`zoren/src/parser.rs`, `semantic.rs`)
