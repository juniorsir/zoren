# Zoren Philosophy

## What is it?
Zoren is an original systems programming language built for correctness, performance, capability security, and long-term evolution.

## Why does Zoren have it?
Eliminates garbage collection pauses and C-style memory unsafety without requiring complex lifetime annotations.

## Mental model
Think of Zoren as a bare-metal native machine code generator with capability security guardrails.

## Basic example
```zoren
flow main() -> Int {
    post("Zoren Philosophy")
    deliver 0
}
```

## How it works
Compiles directly to AArch64/x86_64 machine code via direct ELF encoding or assembly lowering.

## Common mistakes
```zoren
// Incorrect: trying to write C-style un-typed code
x = 10
```

## When should I use it?
Use Zoren for game engines, AI pipelines, cloud microservices, and bare-metal kernels.

## When should I avoid it?
Do not use Zoren if you require dynamic scripting languages with dynamic reflection.

## Performance implications
Language Guarantee: 0.00ms startup latency and zero GC pause spikes.

## Related concepts
- [Design Principles](./DESIGN_PRINCIPLES.md)
