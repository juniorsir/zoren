# Visual Studio Code & Editor Integration Guide

This guide covers setting up **Visual Studio Code**, **Vim/Neovim**, **Helix**, and **Sublime Text** for the Zoren Programming Language.

---

## 🎨 Visual Studio Code Setup

The official VS Code extension (`zoren-lang-1.2.0.vsix`) provides enterprise-grade syntax coloring, code intelligence, language server integration, snippet library, and compiler execution commands.

### 📥 1. Installation

#### Method A: From Local VSIX Package (Recommended)
You can install the pre-packaged `.vsix` bundle directly:
```bash
code --install-extension /root/Zoren_lang/dist/zoren-lang-1.2.0.vsix
```
Or in the VS Code GUI:
1. Open the Extensions sidebar (`Ctrl+Shift+X` or `Cmd+Shift+X`).
2. Click the `...` menu in the top-right corner of the Extensions pane.
3. Select **Install from VSIX...**.
4. Select `tools/vscode-zoren/zoren-lang-1.2.0.vsix`.

#### Method B: Building from Source
```bash
cd /root/Zoren_lang
make vsix
```

---

## 🌈 Syntax Highlighting & Token Scopes

The Zoren grammar adheres to standard TextMate scope hierarchies, ensuring beautiful syntax coloring across all VS Code color themes (including Default Dark+, GitHub Dark, One Dark Pro, Dracula, and Monokai):

| Syntax Construct | Examples | Standard Scope | Theme Accent |
|---|---|---|---|
| **Control Flow** | `if`, `else`, `match`, `when`, `repeat`, `while`, `for`, `in`, `maybe`, `ret` | `keyword.control.zoren` | Vivid Purple / Pink |
| **Declarations** | `flow`, `model`, `ability`, `grant`, `bind`, `flex`, `enum`, `pack` | `keyword.declaration.zoren` | Bold Coral Red |
| **AI & SIMD** | `@matrix`, `ai`, `simd` | `keyword.control.ai.zoren` | Electric Sky Blue |
| **Decorators** | `@inline`, `@pure`, `@track`, `@simd`, `@memoize`, `@test`, `@fast` | `entity.name.function.decorator.zoren` | Warm Amber |
| **Primitives** | `int`, `flt`, `str`, `bool`, `byte`, `rune`, `void`, `Int`, `Float` | `support.type.primitive.zoren` | Mint Cyan |
| **Collections** | `vec`, `map`, `dyn`, `Result`, `Option`, `Tensor`, `Embedding` | `support.type.collection.zoren` | Teal Emerald |
| **Flow Names** | `flow compute_hash(...)` | `entity.name.function.zoren` | Bright Cyan |
| **Function Calls** | `print(...)`, `sqrt(...)`, `db.open(...)` | `entity.name.function.call.zoren` | Light Sky Blue |
| **Strings** | `"Hello, world"`, `"${user}"` | `string.quoted.double.zoren` | Sage Green |
| **Numbers** | `100`, `1_000_000`, `3.14159`, `0xFF`, `0b1010` | `constant.numeric.zoren` | Neon Orange |
| **Operators** | `|>`, `->`, `::`, `+=`, `-=`, `==`, `&&` | `keyword.operator.zoren` | Steel Blue |
| **Comments** | `// Single line`, `/* Multi line */`, `@param` | `comment.zoren` | Muted Slate Grey |

---

## 🌌 Official Theme: "Zoren Dark Modern"

The extension includes a dedicated, high-contrast dark theme calibrated specifically for Zoren's syntax tokens.

To activate the theme:
1. Press `Ctrl+K Ctrl+T` (or `Cmd+K Cmd+T`).
2. Select **Zoren Dark Modern**.

---

## ⚡ Language Server Protocol (LSP) Capabilities

When opening any `.zor` file, the extension automatically launches `zoren lsp` in the background:

- **Diagnostics as you type**: Syntax errors and type mismatches appear directly inline with red squiggly underlines and in the *Problems* tab (`Ctrl+Shift+M`).
- **Hover Information**: Hovering over types, flows, or keywords shows quick documentation popups.
- **Document Formatting**: Press `Shift+Alt+F` to format the active file using the standard Zoren formatter.
- **Auto-Completions**: Press `Ctrl+Space` for context-aware symbol suggestions.

---

## ⌨️ Developer Shortcuts & Commands

| Action | Shortcut | Command Palette (`Ctrl+Shift+P`) |
|---|---|---|
| **Run Active File** | `Alt + R` | `Zoren: Run Current File` |
| **Run Doctor Check** | `Alt + D` | `Zoren: Run Doctor Diagnostics` |
| **Open REPL Studio** | `Alt + Z` | `Zoren: Open Interactive REPL Studio` |
| **Compile Binary** | Context Menu | `Zoren: Compile Current File` |
| **Format Document** | `Shift + Alt + F` | `Zoren: Format Document` |
| **Quick Actions Menu** | Click `$(zap) Zoren` | `Zoren: Quick Actions Menu` |

---

## 📝 Code Snippets Reference

Type any of the following snippet prefixes and press `Tab` to expand:

| Prefix | Output Description |
|---|---|
| `main` | Main entrypoint subroutine with standard return |
| `flow` | Typed flow function definition |
| `model` | Struct model with open fields |
| `ability` | Interface ability contract |
| `grant` | Ability implementation for a model |
| `bind` | Immutable constant binding |
| `flex` | Mutable variable binding |
| `for` | Integer range loop (`0..10`) |
| `while` | Conditional while loop |
| `repeat` | Fixed repeat loop |
| `match` | Pattern matching assess block |
| `if` | If / else conditional branch |
| `maybe` | Safe error handling with `ok` / `err` |
| `ai` | Accelerated AI neural tensor forward block |
| `simd` | Vectorized parallel execution block |
| `test` | Automated unit test case with assertion |
| `bptree` | B+ Tree embedded database transaction snippet |
| `raft` | Distributed Raft consensus node snippet |
| `json` | High-throughput streaming JSON parser snippet |

---

## 🛠️ Vim & Neovim Setup

To install Zoren syntax support for Vim or Neovim:

```bash
mkdir -p ~/.vim/syntax ~/.vim/ftdetect
cp /root/Zoren_lang/tools/vim-zoren/syntax/zoren.vim ~/.vim/syntax/
cp /root/Zoren_lang/tools/vim-zoren/ftdetect/zoren.vim ~/.vim/ftdetect/
```

For Neovim (`~/.config/nvim`):
```bash
mkdir -p ~/.config/nvim/syntax ~/.config/nvim/ftdetect
cp /root/Zoren_lang/tools/vim-zoren/syntax/zoren.vim ~/.config/nvim/syntax/
cp /root/Zoren_lang/tools/vim-zoren/ftdetect/zoren.vim ~/.config/nvim/ftdetect/
```

---

## 🌀 Helix Editor Setup

To add Zoren support to Helix:
1. Append the contents of [`tools/editors/helix_languages.toml`](file:///root/Zoren_lang/tools/editors/helix_languages.toml) to your Helix configuration:
```bash
cat /root/Zoren_lang/tools/editors/helix_languages.toml >> ~/.config/helix/languages.toml
```

---

## 💎 Sublime Text Setup

1. Copy the Sublime syntax definition:
```bash
mkdir -p ~/.config/sublime-text/Packages/User
cp /root/Zoren_lang/tools/editors/zoren.sublime-syntax ~/.config/sublime-text/Packages/User/
```
2. Any `.zor` file will now open with full Zoren syntax highlighting.
