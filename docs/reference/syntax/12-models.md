# Models (Structs)

## 1. Syntax
```ebnf
ModelDecl = [ "#align(" Int ")" | "#soa" | "#zerocopy" | "#linear" ] [ "actor" ] "model" Identifier "{" { FieldDecl } "}" ;
FieldDecl = [ "open" ] Identifier ":" Type ;
```

## 2. Examples
```zoren
model User {
    open id: Int
    open name: Text
}

bind u = User(101, "Alice")
```

## 3. Implementation Status
`SUPPORTED` (`zoren/src/parser.rs`, `semantic.rs`)
