# Compiler Optimization Pipeline

## 1. Language Guarantee
Optimization levels `-O1`, `-O2`, `-O3` execute constant propagation, CSE, DCE, and function inlining.

## 2. Current Implementation Details
`optimize.rs` runs constant folding and dead statement elimination passes.

## 3. Optimization Opportunities
Using `--pgo-use profile.zprof` guides function inlining using execution profile statistics.
