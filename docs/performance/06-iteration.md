# Loop Iteration Throughput

## 1. Language Guarantee
Tight loops (`repeat while`) compile to direct CPU branch instructions (`b.lt`, `b.ge`).

## 2. Current Implementation Details
`codegen.rs` pins loop counters to high-speed registers (`x19`, `x20`) without stack memory spills.

## 3. Optimization Opportunities
Unrolling short constant loops increases instruction pipeline throughput.
