# Mutability (bind vs flex)

## What is it?
Zoren explicitly separates immutable constant bindings (`bind`) from mutable variables (`flex`).

## Why does Zoren have it?
Prevents accidental variable mutation bugs in concurrent systems.

## Mental model
Think of 'bind' as a permanently sealed vault value, and 'flex' as a mutable whiteboard.

## Basic example
```zoren
flow main() -> Int {
    bind pi = 3.14159
    flex count = 0
    count = count + 1
    deliver 0
}
```

## How it works
`bind` declarations cannot be reassigned; attempting reassignment triggers compiler error Z4003.

## Common mistakes
```zoren
bind age = 20
age = 21 // Compiler Error Z4003
```

## When should I use it?
Default to `bind` for all values unless mutation is explicitly required.

## When should I avoid it?
Avoid overusing `flex` across multi-threaded Spindle boundaries.

## Performance implications
Language Guarantee: Immutable `bind` values permit aggressive compiler optimization.

## Related concepts
- [Values and Types](./02-values-and-types.md)
