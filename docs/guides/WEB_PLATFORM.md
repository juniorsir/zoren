# Zoren Web & WebAssembly Platform Guide

Zoren provides first-class support for compiling applications directly to WebAssembly (Wasm) and running client-side in all modern web browsers and Node.js environments.

---

## 1. Overview

The Zoren Web platform consists of:
1. **Wasm Backend Compiler**: Translates Zoren AST directly to WebAssembly bytecode (`.wasm`) and WebAssembly Text (`.wat`).
2. **HTML Runner Generator**: Automatically creates responsive, dark-themed HTML5 runners equipped with output streams and execution telemetry.
3. **JavaScript Bridge (`zoren_web.js`)**: Bidirectional runtime bridge supporting standard I/O, string passing, DOM manipulation, and system clocks.
4. **Standard Web Module (`std/web.zor`)**: Safe idiomatic abstractions for browser APIs.
5. **Embedded HTTP Server**: Zero-dependency web server for instant local preview and testing.

---

## 2. Compilation and Execution

### Compiling to WebAssembly
To compile any `.zor` program to WebAssembly:
```bash
zoren app.zor --web -o dist/app.wasm
```
This generates:
- `dist/app.wasm` (Optimized Wasm binary)
- `dist/app.wat` (WebAssembly text format)
- `dist/app.html` (Standalone browser runner)
- `dist/zoren_web.js` (JavaScript host bridge)

### One-Command Build and Serve
```bash
zoren web src/main.zor --serve --port 8080
```
This compiles the project to Wasm and starts the development server at `http://localhost:8080`.

### Standalone Web Server
To serve any web directory:
```bash
zoren serve projects/zoren_web/dist --port 8080
```

---

## 3. Web Standard Library (`std/web.zor`)

Import the standard web module using:
```zoren
bring web as web
```

### Available APIs:
- `web_log(msg: Text) -> Nothing`: Output text to the console and web runner stream.
- `web_alert(msg: Text) -> Nothing`: Display native browser alert dialog.
- `web_set_element(id: Text, text: Text) -> Nothing`: Update the `textContent` of a DOM element by ID.
- `web_now_ms() -> Float`: Retrieve high-resolution timestamp from `performance.now()`.
- `web_is_browser() -> Bool`: Check if currently running inside a browser environment.

---

## 4. Headless Execution in Node.js

Zoren WebAssembly binaries can be executed headlessly inside Node.js or Cloudflare Workers:
```javascript
const { ZorenWebRunner } = require('./zoren_web.js');

async function main() {
    const runner = new ZorenWebRunner();
    runner.onOutput = (line) => console.log('[WASM]', line);
    const result = await runner.loadAndExecute('./app.wasm');
    console.log('Returned:', result.returnValue);
}
main();
```
