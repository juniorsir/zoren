# Comments

## 1. Syntax
```ebnf
Comment = "//" { Character - "
" } "
" ;
```

## 2. Rules
Single-line comments start with `//` and extend to the end of the line.

## 3. Valid Example
```zoren
// This is a single-line comment in Zoren
bind active: Bool = true
```

## 4. Implementation Status
`SUPPORTED` (`zoren/src/lexer.rs`)
