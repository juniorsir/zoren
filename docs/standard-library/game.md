# std/game Reference

Game engine Chamber allocators and frame timing.

- `FrameChamber` — Per-frame arena memory pool model.
- `create_frame_chamber(size: Int) -> Int` — Creates arena.
- `reset_frame_chamber(ch: Int) -> Int` — Resets per-frame arena offset.
