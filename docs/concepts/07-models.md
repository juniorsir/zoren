# Data Models

## What is it?
Models (`model`) define composite data structures with named, typed fields.

## Why does Zoren have it?
Groups related state data into contiguous memory layouts.

## Mental model
Think of a model as a blueprint for a contiguous binary memory block.

## Basic example
```zoren
model Point {
    open x: Int
    open y: Int
}

flow main() -> Int {
    bind p = Point(10, 20)
    deliver 0
}
```

## How it works
Field values are laid out contiguously in memory matching target alignment rules.

## Common mistakes
```zoren
model Point { x: Int } // Error: missing open modifier for public field access
```

## When should I use it?
Use models for grouping application state, game entities, and network headers.

## When should I avoid it?
Avoid deeply nested model hierarchies when flat memory arrays are sufficient.

## Performance implications
Language Guarantee: Memory layout matches target architecture alignment boundaries.

## Related concepts
- [Abilities](./08-abilities.md)
