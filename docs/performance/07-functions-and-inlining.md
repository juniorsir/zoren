# Functions and Inlining

## 1. Language Guarantee
Subroutine calls follow standard target ABI calling conventions.

## 2. Current Implementation Details
At `-O3`, `optimize.rs` automatically inlines small leaf functions (<25 statements).

## 3. Optimization Opportunities
Functions marked `comptime flow` evaluate during compilation with zero runtime call cost.
