# Concurrency and Async Spindles

## What is it?
Zoren uses lightweight green tasks (**Spindles**) scheduled across M:N work-stealing queues.

## Why does Zoren have it?
Allows running millions of concurrent tasks with minimal memory footprint.

## Mental model
Think of a Spindle as an ultra-lightweight worker thread with a 128-byte initial stack.

## Basic example
```zoren
async flow worker_task(id: Int) -> Int {
    deliver id * 10
}

flow main() -> Int {
    spawn worker_task(1)
    bind res = await worker_task(2)
    deliver 0
}
```

## How it works
`spawn` dispatches tasks to the lock-free Spindle scheduler; `await` yields task resolution.

## Common mistakes
```zoren
bind val = await regular_sync_function() // Compiler Error: await requires async flow
```

## When should I use it?
Use Spindles for concurrent web servers, background workers, and event streams.

## When should I avoid it?
Avoid blocking Spindles with synchronous infinite loops.

## Performance implications
Language Guarantee: Spindle context switches execute in ~2ns in CPU registers.

## Related concepts
- [Functions and Composition](./05-functions-and-composition.md)
