# Error Handling

## 1. Syntax
```ebnf
DivergeContract = "diverges" ErrorType ;
DivertStmt = "divert" Expression ;
CatchExpr = Expression "catch" Identifier Block ;
EnsureBlock = "ensure" Block ;
```

## 2. Example
```zoren
flow risky() -> Int diverges CustomErr {
    ensure { post("Cleanup") }
    divert CustomErr("Failed")
}

bind res = risky() catch err { deliver 0 }
```

## 3. Implementation Status
`SUPPORTED` (`zoren/src/parser.rs`, `codegen.rs`)
