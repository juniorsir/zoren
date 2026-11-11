# Allocation and Chamber Arenas

## 1. Language Guarantee
Zoren provides bounded Chamber memory arenas (`Chamber[T]`) for microsecond allocation throughput.

## 2. Current Implementation Details
Chamber allocations use a linear bump-pointer (`allocated_bytes += size`). Resetting an arena resets a single offset pointer in 0.00ms.

## 3. Optimization Opportunities
Pre-allocating Chamber capacity (`create_frame_chamber(1048576)`) eliminates mid-loop buffer expansion.
