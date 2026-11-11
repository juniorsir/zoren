# Abilities

## What is it?
Abilities (`ability`) define interface contracts specifying subroutine signatures.

## Why does Zoren have it?
Separates data model state from interface behavior.

## Mental model
Think of an ability as a job contract that data models agree to satisfy.

## Basic example
```zoren
ability Printable {
    flow print_summary() -> Nothing
}
```

## How it works
Abilities contain subroutine signatures without implementation bodies.

## Common mistakes
```zoren
ability P { flow print() { post("Bad") } } // Error: ability signatures cannot have bodies
```

## When should I use it?
Use abilities to define shared behaviors across distinct data models.

## When should I avoid it?
Avoid defining single-use abilities when direct model functions suffice.

## Performance implications
Language Guarantee: Ability calls resolve at compile time with 0 vtable lookup overhead.

## Related concepts
- [Grants](./09-grants.md)
