# Copying and Value Moves

## 1. Language Guarantee
Primitive scalar values pass by value in target registers (`x0`–`x7`).

## 2. Current Implementation Details
Model structures pass via stack pointers or register pairs depending on field count.

## 3. Optimization Opportunities
Models annotated with `#linear` enforce single-use move liveness contracts without copying.
