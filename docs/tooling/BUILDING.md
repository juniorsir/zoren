# Building Applications

## Build Modes
- **Development Build:** `zoren src/main.zor -o app` (Fast compilation speed).
- **Release Build:** `zoren src/main.zor -O3 --lto -o app` (Maximum machine performance).
- **Direct Freestanding ELF Build:** `zoren src/main.zor --direct-elf -o app` (0 external compiler dependencies).
