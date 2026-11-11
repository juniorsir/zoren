# Functions (Flows)

## 1. Syntax
```ebnf
FlowDecl = [ "open" | "async" | "comptime" | "accel" ] "flow" Identifier "(" [ ParameterList ] ")" [ "->" Type ] [ "diverges" Type ] Block ;
```

## 2. Examples
```zoren
open flow square(n: Int) -> Int {
    deliver n * n
}
```

## 3. Implementation Status
`SUPPORTED` (`zoren/src/parser.rs`, `codegen.rs`)
