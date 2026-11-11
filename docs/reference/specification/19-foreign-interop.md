# Foreign Interoperability

## RUNTIME BEHAVIOR
`extern ABI "C"` subroutines MUST map directly to AArch64/x86_64 target calling registers (`x0`–`x7`) with 0.00ns FFI overhead.
