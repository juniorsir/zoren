# Abilities (Interfaces)

## 1. Syntax
```ebnf
AbilityDecl = "ability" Identifier "{" { FlowSignature } "}" ;
```

## 2. Example
```zoren
ability Printable {
    flow print_summary() -> Nothing
}
```

## 3. Implementation Status
`SUPPORTED` (`zoren/src/parser.rs`, `semantic.rs`)
