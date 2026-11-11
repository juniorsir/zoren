# Zoren Source Files

## 1. Name
Zoren Source File (`.zor` / `.zoren`)

## 2. Purpose
Defines the top-level compilation unit containing module imports, model definitions, abilities, grants, and subroutines.

## 3. Formal Syntax
```ebnf
SourceFile = { ImportDirective | ModelDecl | AbilityDecl | GrantDecl | FlowDecl } ;
```

## 4. Valid Example
```zoren
bring math

flow main() -> Int {
    deliver 0
}
```

## 5. Implementation Status
`SUPPORTED` (`zoren/src/parser.rs`)
