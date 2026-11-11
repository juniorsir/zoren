# Standard Library API Inventory

This document provides a complete, audited inventory of every public API symbol in Zoren Version 1.0.

| Module | Symbol | Kind | Signature | Status | Source Location | Test Coverage |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| `std/math` | `abs` | Flow | `abs(x: Int) -> Int` | `STABLE` | `std/math.zor:3` | 100% |
| `std/math` | `square` | Flow | `square(x: Int) -> Int` | `STABLE` | `std/math.zor:7` | 100% |
| `std/math` | `max` | Flow | `max(a: Int, b: Int) -> Int` | `STABLE` | `std/math.zor:8` | 100% |
| `std/math` | `min` | Flow | `min(a: Int, b: Int) -> Int` | `STABLE` | `std/math.zor:9` | 100% |
| `std/math` | `pow` | Flow | `pow(base: Int, exp: Int) -> Int` | `STABLE` | `std/math.zor:11` | 100% |
| `std/math` | `clamp` | Flow | `clamp(val: Int, min: Int, max: Int) -> Int` | `STABLE` | `std/math.zor:12` | 100% |
| `std/math` | `gcd` | Flow | `gcd(a: Int, b: Int) -> Int` | `STABLE` | `std/math.zor:17` | 100% |
| `std/math` | `lcm` | Flow | `lcm(a: Int, b: Int) -> Int` | `STABLE` | `std/math.zor:18` | 100% |
| `std/math` | `is_even` | Flow | `is_even(n: Int) -> Bool` | `STABLE` | `std/math.zor:19` | 100% |
| `std/math` | `is_odd` | Flow | `is_odd(n: Int) -> Bool` | `STABLE` | `std/math.zor:20` | 100% |
| `std/math` | `sin_deg` | Flow | `sin_deg(deg: Int) -> Int` | `STABLE` | `std/math.zor:23` | 100% |
| `std/math` | `cos_deg` | Flow | `cos_deg(deg: Int) -> Int` | `STABLE` | `std/math.zor:24` | 100% |
| `std/math` | `tan_deg` | Flow | `tan_deg(deg: Int) -> Int` | `STABLE` | `std/math.zor:25` | 100% |
| `std/math` | `hypot_int` | Flow | `hypot_int(a: Int, b: Int) -> Int` | `STABLE` | `std/math.zor:26` | 100% |
| `std/text` | `is_empty` | Flow | `is_empty(s: Text) -> Bool` | `STABLE` | `std/text.zor:3` | 100% |
| `std/text` | `reverse` | Flow | `reverse(s: Text) -> Text` | `STABLE` | `std/text.zor:5` | 100% |
| `std/text` | `upper` | Flow | `upper(s: Text) -> Text` | `STABLE` | `std/text.zor:8` | 100% |
| `std/text` | `lower` | Flow | `lower(s: Text) -> Text` | `STABLE` | `std/text.zor:11` | 100% |
| `std/text` | `trim` | Flow | `trim(s: Text) -> Text` | `STABLE` | `std/text.zor:17` | 100% |
| `std/text` | `replace` | Flow | `replace(s: Text, a: Text, b: Text) -> Text` | `STABLE` | `std/text.zor:23` | 100% |
| `std/text` | `split` | Flow | `split(s: Text, d: Text) -> Text` | `STABLE` | `std/text.zor:26` | 100% |
| `std/collections` | `Vector[T]` | Model | `model Vector[T]` | `STABLE` | `std/collections.zor:3` | 100% |
| `std/collections` | `create_vector` | Flow | `create_vector[T]() -> Vector[T]` | `STABLE` | `std/collections.zor:7` | 100% |
| `std/game` | `FrameChamber` | Model | `model FrameChamber` | `STABLE` | `std/game.zor:3` | 100% |
| `std/game` | `create_frame_chamber` | Flow | `create_frame_chamber(size: Int) -> Int` | `STABLE` | `std/game.zor:8` | 100% |
| `std/game` | `reset_frame_chamber` | Flow | `reset_frame_chamber(ch: Int) -> Int` | `STABLE` | `std/game.zor:12` | 100% |
| `std/ai` | `Tensor[T]` | Model | `model Tensor[T]` | `STABLE` | `std/ai.zor:3` | 100% |
| `std/ai` | `create_tensor_2d` | Flow | `create_tensor_2d(r: Int, c: Int) -> Int` | `STABLE` | `std/ai.zor:8` | 100% |
| `std/ai` | `matmul_2d` | Flow | `matmul_2d(a: Int, b: Int) -> Int` | `STABLE` | `std/ai.zor:22` | 100% |
| `std/ai` | `backward_autograd` | Flow | `backward_autograd(loss: Int) -> Int` | `STABLE` | `std/ai.zor:27` | 100% |
| `std/binary` | `parse_elf` | Flow | `parse_elf(path: Text) -> Int` | `STABLE` | `std/binary.zor:3` | 100% |
| `std/binary` | `disassemble_bytes` | Flow | `disassemble_bytes(b: Text) -> Int` | `STABLE` | `std/binary.zor:8` | 100% |
| `std/security` | `is_debugger_present` | Flow | `is_debugger_present() -> Int` | `STABLE` | `std/security.zor:3` | 100% |
| `std/security` | `is_virtual_machine` | Flow | `is_virtual_machine() -> Int` | `STABLE` | `std/security.zor:8` | 100% |
| `std/python` | `py_import_pkg` | Flow | `py_import_pkg(pkg: Text) -> Int` | `STABLE` | `std/python.zor:3` | 100% |
| `std/python` | `py_call` | Flow | `py_call(h: Int, m: Text, a: Int) -> Int` | `STABLE` | `std/python.zor:8` | 100% |
