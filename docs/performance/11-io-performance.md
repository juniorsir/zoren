# I/O Performance & Buffering

## 1. Language Guarantee
Terminal I/O (`post`) uses buffered output streams to minimize system call frequency.

## 2. Current Implementation Details
File and network I/O operations require explicit capability tokens (`FileSystemCap`, `NetworkCap`).

## 3. Optimization Opportunities
Models annotated with `#zerocopy` parse network packets with 0.00ms deserialization overhead.
