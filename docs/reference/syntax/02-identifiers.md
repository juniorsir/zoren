# Identifiers

## 1. Syntax
```ebnf
Identifier = ( Letter | "_" ) { Letter | Digit | "_" } ;
```

## 2. Rules
Identifiers start with an ASCII letter or underscore, followed by alphanumeric characters or underscores. Keywords cannot be used as identifiers.

## 3. Valid Examples
```zoren
bind user_age: Int = 20
bind _internal_flag: Bool = true
```

## 4. Implementation Status
`SUPPORTED` (`zoren/src/lexer.rs`)
