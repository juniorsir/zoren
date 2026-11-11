# Tooling & CLI Implementation Status Audit

| Tooling Subsystem | Status | Implementation Source |
| :--- | :--- | :--- |
| **CLI Commands (`new`, `fmt`, `forge`, `audit`, `check`, `doc`, `repl`)** | `SUPPORTED` | `zoren/src/main.rs` |
| **Direct ELF Binary Writer (`--direct-elf`)** | `SUPPORTED` | `zoren/src/elf.rs` |
| **Code Formatter (`zoren fmt`)** | `SUPPORTED` | `zoren/src/fmt.rs` |
| **Automated Test Harness (`test_runner.py`)** | `SUPPORTED` | `Zoren_lang/test_runner.py` |
| **Security Capability Auditor (`zoren audit`)** | `SUPPORTED` | `zoren/src/main.rs` |
| **Static Linter (`zoren check`)** | `SUPPORTED` | `zoren/src/main.rs` |
| **Documentation Generator (`zoren doc`)** | `SUPPORTED` | `zoren/src/main.rs` |
| **Language Server Protocol (`zoren lsp`)** | `PARTIAL` | `zoren/src/lsp.rs` |
| **Registry Publishing (`zoren publish`)** | `PLANNED` | Pending domain registry endpoint |
