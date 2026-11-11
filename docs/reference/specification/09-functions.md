# Subroutines (Flows)

## SYNTAX
`flow name(param: Type) -> RetType { ... }`

## SEMANTICS
Subroutines MUST return a value matching `RetType` via `deliver`. `flow main()` MUST return integer status code `0` on clean exit.
