# Generics

## 1. Syntax
```ebnf
GenericFlow = "flow" Identifier "[" GenericParams "]" "(" Params ")" "->" Type Block ;
```

## 2. Example
```zoren
flow max[T](a: T, b: T) -> T {
    if a > b { deliver a }
    deliver b
}
```

## 3. Implementation Status
`SUPPORTED` (`zoren/src/semantic.rs` monomorphization pass)
