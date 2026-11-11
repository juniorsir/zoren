# Concurrency (Async Spindles)

## RUNTIME BEHAVIOR
`async flow` subroutines execute as lightweight Spindle tasks scheduled across lock-free M:N work-stealing queues (`spawn`, `await`).
