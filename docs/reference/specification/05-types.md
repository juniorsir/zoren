# Type System

## SYNTAX
Primitive type identifiers (`i8`–`i64`, `u8`–`u64`, `f32`, `f64`, `iptr`, `uptr`, `byte`, `rune`, `bool`, `text`, `void`) and aliases (`Int`, `UInt`, `Float`, `Bool`, `Char`, `Text`, `Nothing`).

## TYPE RULES
Zoren enforces Strict Type Isolation. Implicit type widening or lossy coercions MUST NOT occur.
