# Variable Bindings

## SYNTAX
`bind name: Type = expr` (Immutable Constant)
`flex name: Type = expr` (Mutable Variable)

## SEMANTICS
Re-assigning a `bind` constant MUST trigger a build-time error (`Z4003`). `flex` variables MAY be mutated.
