# Types

## 1. Syntax
```ebnf
Type = PrimitiveType | TypeAlias | ModelType | GenericType | OptionalType ;
```

## 2. Supported Primitives
`i8`, `i16`, `i32`, `i64`, `u8`, `u16`, `u32`, `u64`, `f32`, `f64`, `iptr`, `uptr`, `byte`, `rune`, `bool`, `text`, `void`.

## 3. Aliases
`Int` (`i64`), `UInt` (`u64`), `Float` (`f64`), `Bool` (`bool`), `Char` (`rune`), `Text` (`text`), `Nothing` (`void`).

## 4. Implementation Status
`SUPPORTED` (`zoren/src/types.rs`, `parser.rs`)
