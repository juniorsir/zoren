# Foreign Interoperability Overhead

## 1. Language Guarantee
`extern ABI "C"` subroutines map directly to CPU registers with 0.00ns calling overhead.

## 2. Current Implementation Details
Foreign C/C++ shared objects link directly via target registers.

## 3. Optimization Opportunities
Python calls (`py_call`) execute via CPython Enclave Bridge.
