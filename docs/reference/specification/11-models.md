# Data Models (Structs)

## SYNTAX
`[#align(N) | #soa | #zerocopy | #linear] [actor] model Name { open field: Type }`

## MEMORY SEMANTICS
Field layouts MUST be laid out contiguously in memory matching target platform alignment rules.
