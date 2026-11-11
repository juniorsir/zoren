# Troubleshooting Common Issues

### 1. `Command not found: zoren`
- **Cause:** `~/.zoren/bin` is not present in system `$PATH`.
- **Fix:** Add `export PATH="$HOME/.zoren/bin:$PATH"` to your `~/.bashrc` or `~/.zshrc`.

### 2. `error[Z2001]: Unknown module 'math'`
- **Cause:** Module search path cannot locate `std/math.zor`.
- **Fix:** Ensure `std/` directory exists or run command from project root directory.

### 3. `error[Z4003]: Cannot mutate immutable constant`
- **Cause:** Attempted to re-assign a `bind` constant.
- **Fix:** Change `bind` declaration to `flex` for mutable variables.
