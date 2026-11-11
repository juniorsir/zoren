# Concurrency (Async & Spindles)

## 1. Syntax
```ebnf
AsyncFlow = "async" "flow" Identifier "(" Params ")" "->" Type Block ;
AwaitExpr = "await" CallExpr ;
SpawnStmt = "spawn" CallExpr ;
```

## 2. Example
```zoren
async flow task() -> Int { deliver 42 }

flow main() -> Int {
    spawn task()
    bind val = await task()
    deliver 0
}
```

## 3. Implementation Status
`SUPPORTED` (`zoren/src/parser.rs`, `std/async.zor`)
