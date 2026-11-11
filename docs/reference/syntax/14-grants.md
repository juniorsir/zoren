# Grants (Trait Implementations)

## 1. Syntax
```ebnf
GrantDecl = "grant" AbilityName "for" ModelName "{" { MethodImpl } "}" ;
```

## 2. Example
```zoren
grant Printable for User {
    print_summary {
        post("User Name: ", self.name)
    }
}
```

## 3. Implementation Status
`SUPPORTED` (`zoren/src/parser.rs`, `codegen.rs`)
