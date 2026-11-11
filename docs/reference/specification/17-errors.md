# Error Contracts and Cleanup

## SEMANTICS
Functions raising errors MUST declare `diverges ErrorType` contracts. Errors MUST be raised via `divert` and handled via `catch`. `ensure` blocks MUST execute on scope exit in LIFO order.
