# Expressions

## 1. Syntax
```ebnf
Expression = CoalescingExpr ;
CoalescingExpr = LogicalOrExpr { "??" LogicalOrExpr } ;
```

## 2. Examples
```zoren
bind total = (10 + 5) * 2
bind active_name = name_opt ?? "Default Guest"
```

## 3. Implementation Status
`SUPPORTED` (`zoren/src/parser.rs`)
