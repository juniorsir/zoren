# Concurrency & Spindle Tasks

## 1. Language Guarantee
Async Spindles (`async flow`) initialize with a 128-byte stack frame scheduled across lock-free M:N work-stealing queues.

## 2. Current Implementation Details
Spindle task context switches execute in ~2ns in CPU registers without kernel mode transitions.

## 3. Optimization Opportunities
Spawning millions of Spindles allows massive concurrent task parallelism.
