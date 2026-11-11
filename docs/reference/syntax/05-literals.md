# Literals

## 1. Syntax
```ebnf
Literal = IntLiteral | HexLiteral | BinLiteral | FloatLiteral | CharLiteral | StringLiteral | BoolLiteral | NullLiteral ;
```

## 2. Examples
```zoren
bind count = 100            // Decimal Integer
bind hex_val = 0xFF         // Hexadecimal (255)
bind bin_val = 0b1010       // Binary (10)
bind ratio = 3.14           // Float
bind letter = 'A'           // Char
bind name = "Alice"         // String
bind flag = true            // Bool
bind empty: Text = null     // Null
```

## 3. Implementation Status
`SUPPORTED` (`zoren/src/lexer.rs`, `parser.rs`)
