# std/python Reference

Foreign Python Enclave Bridge.

- `py_import_pkg(pkg: Text) -> Int` — Loads Python package into CPython enclave.
- `py_call(h: Int, m: Text, a: Int) -> Int` — Invokes method on Python package.
