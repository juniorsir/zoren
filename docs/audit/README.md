# Zoren Automated Documentation Audit System

This directory contains the automated documentation audit system (`audit_docs.py`), rule reference (`RULES.md`), and audit reports (`REPORT.md`, `report.json`).

## Usage

```shell
# Run full documentation audit
python3 Zoren_lang/docs/audit/audit_docs.py

# Run audit in verbose mode
python3 Zoren_lang/docs/audit/audit_docs.py --verbose

# Run auditor self-test suite
python3 Zoren_lang/docs/audit/audit_docs.py --self-test
```

## Documentation

- [RULES — Audit Rule Reference Manual](./RULES.md)
- [STATUS — Audit Implementation Status](./STATUS.md)
- [REPORT — Latest Audit Execution Report](./REPORT.md)
