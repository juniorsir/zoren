# Memory Model and Chamber Arenas

## What is it?
Zoren manages memory using stack frames and Chamber arena pools (`Chamber[T]`).

## Why does Zoren have it?
Eliminates dynamic garbage collection pauses and manual pointer freeing.

## Mental model
Think of a Chamber as a fixed workspace whiteboard that is wiped clean all at once.

## Basic example
```zoren
bring game

flow main() -> Int {
    bind ch = create_frame_chamber(1048576)
    reset_frame_chamber(ch)
    deliver 0
}
```

## How it works
Allocations occur on stack frames or bounded Chamber memory pools. Resetting a Chamber resets an offset pointer in 0.00ms.

## Common mistakes
```zoren
// Incorrect: expecting automatic background GC
flex data = malloc(1000)
```

## When should I use it?
Use Chamber arenas for per-frame game allocations and high-frequency network buffers.

## When should I avoid it?
Avoid infinite allocations without resetting the Chamber arena.

## Performance implications
Language Guarantee: Zero Garbage Collection pause latency.

## Related concepts
- [Collections](./11-collections.md)
