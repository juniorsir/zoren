# Variable Bindings

## 1. Syntax
```ebnf
BindDecl = "bind" Identifier [ ":" Type ] "=" Expression ;
FlexDecl = "flex" Identifier [ ":" Type ] "=" Expression ;
```

## 2. Rules
- `bind` creates an immutable constant.
- `flex` creates a mutable variable.

## 3. Examples
```zoren
bind pi: Float = 3.14159
flex count: Int = 0
count = count + 1
```

## 4. Implementation Status
`SUPPORTED` (`zoren/src/parser.rs`, `semantic.rs`)
