# Lexical Structure

## SYNTAX
Source files MUST be encoded in valid UTF-8 text.

## SEMANTICS
Lexical tokens MUST be scanned sequentially according to longest-match rules.

## TYPE RULES
Lexical analysis produces token streams (`TokenKind`) consumed by the parser.

## COMPILER REQUIREMENTS
Compilers MUST reject invalid UTF-8 byte sequences with diagnostic `Z1001`.
