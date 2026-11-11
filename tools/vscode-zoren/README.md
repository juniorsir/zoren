# Zoren Official Visual Studio Code Extension

[![Version](https://img.shields.io/badge/version-1.2.0-blue.svg)](file:///root/Zoren_lang/tools/vscode-zoren/package.json)
[![Language](https://img.shields.io/badge/language-Zoren%20v1.0-brightgreen.svg)](file:///root/Zoren_lang/README.md)
[![License](https://img.shields.io/badge/license-MIT-green.svg)](file:///root/Zoren_lang/tools/vscode-zoren/LICENSE)

The official full-featured development environment extension for the **Zoren Programming Language** (`.zor`, `.zoren`).

---

## ✨ Features

### 1. 🎨 Comprehensive Syntax Highlighting & Colors
- **Full TextMate Grammar Coverage**: Standard VS Code scope tokens covering all language constructs.
- **Control Flow & Declarations**: `flow`, `model`, `ability`, `grant`, `bind`, `flex`, `match`, `when`, `repeat`, `while`, `for`, `in`, `if`, `else`, `maybe`, `err`, `ret`, `deliver`.
- **Next-Gen AI & SIMD Keywords**: Distinctive neon highlighting for `@matrix`, `ai`, `simd`, `@inline`, `@pure`, `@track`.
- **Rich Type Highlighting**: Primitives (`int`, `flt`, `str`, `bool`, `byte`, `rune`, `void`), collections (`vec`, `map`, `dyn`), and standard models (`Result`, `Option`, `Tensor`, `Embedding`).
- **Decorators & Attributes**: Vivid colors for `@inline`, `@pure`, `@track`, `@matrix`, `@simd`, `@memoize`, `@audit`, `@test`, `@cold`, `@fast`, `@secure`.
- **String Interpolation & Escape Sequences**: Full highlighting for `"${expr}"` template expressions and escape sequences (`\n`, `\t`, `\xHH`, `\uHHHH`).
- **Operators & Pipelines**: Highlighting for pipelines (`|>`, `->`), compound assignments (`+=`, `-=`, etc.), bitwise, logical, and comparison operators.
- **Block & Line Comments**: Single-line (`//`, `#`) and multi-line (`/* ... */`) comments with documentation tag highlighting (`@param`, `@return`, `@brief`, `@note`).

### 2. 🌌 Included Theme: "Zoren Dark Modern"
A custom, hand-crafted dark color theme designed specifically to showcase Zoren's syntax with high-contrast, eye-friendly aesthetics:
- Flows & Functions: **Electric Cyan** (`#61AFEF`)
- Models & Types: **Mint Green** (`#4EC9B0` / `#56B6C2`)
- Decorators & Attributes: **Warm Amber** (`#D19A66`)
- Keywords & Flow Control: **Vivid Purple & Coral** (`#C678DD` / `#E06C75`)
- AI & SIMD Acceleration: **Sky Blue** (`#38BDF8`)
- Literals & Booleans: **Golden Honey** (`#E5C07B`)

### 3. ⚡ Language Server Protocol (LSP) Integration
- **Real-time Diagnostics**: Inline compiler syntax errors and semantic warnings reported directly in the VS Code Problems tab as you type.
- **Hover Documentation**: Hover over keywords, built-in functions, or data types to see descriptions and markdown signatures.
- **Auto-Formatting**: Built-in document formatter (`Shift+Alt+F`) using `zoren fmt`.
- **Context Completions**: Intelligent autocompletion triggered on typing `.`, `:`, `[`, or keywords.

### 4. 📝 20+ Production Snippets
Instantly scaffold common patterns by typing prefixes and pressing `Tab`:
- `main` — Main entrypoint subroutine with typed return.
- `flow` — Typed subroutine definition.
- `model` — Struct data model with open fields.
- `ability` — Trait / interface definition contract.
- `grant` — Trait implementation for concrete models.
- `match` / `assess` — Pattern matching block.
- `for` — Range / sequence loop.
- `maybe` — Safe error-handling block (`err(e)` / `ok(val)`).
- `ai` — High-performance AI tensor forward pass kernel.
- `simd` — Vectorized SIMD loop.
- `test` — Automated unit test flow with assertion.
- `bptree` — B+ Tree database query transaction snippet.
- `raft` — Raft consensus distributed cluster snippet.
- `json` — High-throughput streaming JSON parser snippet.

### 5. 🚀 Integrated Developer Commands & Shortcuts

| Command | Title | Default Shortcut |
|---|---|---|
| `zoren.run` | Run Active File in Terminal | `Alt + R` |
| `zoren.build` | Compile Active File to Binary | Context Menu |
| `zoren.check` | Run Doctor Diagnostics & Linting | `Alt + D` |
| `zoren.format` | Format Current Document | `Shift + Alt + F` |
| `zoren.repl` | Launch Interactive Zoren REPL Studio | `Alt + Z` |
| `zoren.menu` | Open Zoren Quick Actions Menu | Click `$(zap) Zoren` in Status Bar |

---

## 📦 Installation

### From VSIX Package:
1. Open VS Code.
2. Press `Ctrl+Shift+P` (or `Cmd+Shift+P` on macOS) to open the Command Palette.
3. Type and select: `Extensions: Install from VSIX...`.
4. Choose `zoren-lang-1.2.0.vsix` located in:
   ```bash
   /root/Zoren_lang/tools/vscode-zoren/zoren-lang-1.2.0.vsix
   # or
   /root/Zoren_lang/dist/zoren-lang-1.2.0.vsix
   ```
5. Or via terminal:
   ```bash
   code --install-extension /root/Zoren_lang/dist/zoren-lang-1.2.0.vsix
   ```

---

## ⚙️ Extension Settings
You can customize the Zoren extension in VS Code Settings (`Ctrl+,`):
- `zoren.compilerPath`: Absolute path to your `zoren` binary (defaults to auto-detection in PATH, `/usr/local/bin/zoren`, or `~/.zoren/bin/zoren`).

---

## 📄 License
MIT License. Copyright (c) 2026 Zoren Language Authors.
