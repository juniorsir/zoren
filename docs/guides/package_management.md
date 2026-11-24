# 📦 Package Management in Zoren (Pip + Vercel Model)

Zoren combines the effortless command simplicity of Python’s **pip** (`install`, `list`, `uninstall`) with the iconic, clean, cloud-native aesthetic of **Vercel** (`▲`, inspect URLs, instant feedback, and clean typography).

---

## 1. Installing a Package: `zoren install <pkg>`

Install any package from the Zoren registry or directly from GitHub:

```bash
zoren install jwt_auth
```

Output:
```text
▲ zoren install jwt_auth

  Fetching jwt_auth@1.2.0
  Creator:     Junior Sir (@juniorsir)
  Security:    Sandboxed (zero host permissions)
  Linked:      crypto@2.1.0, base64@1.0.0

✅ Installed jwt_auth v1.2.0 [24ms]
🔗 Inspect: https://zoren.dev/pkg/jwt_auth
```

You can also install directly from GitHub:
```bash
zoren install github.com/juniorsir/zoren-jwt-auth
```

Once installed, use it immediately in any `.zor` file:
```zoren
bring jwt_auth

flow main() -> Int {
    post("Module ready to use!")
    deliver 0
}
```

---

## 2. Publishing a Package: `zoren publish`

Just like typing `vercel` in a folder deploys your project instantly to the world:

```bash
zoren publish .
```

Output:
```text
▲ zoren publish

  Plugin:      jwt_auth
  Version:     1.2.0
  Creator:     Junior Sir (@juniorsir)
  Audit:       Passed (0 capability warnings)
  Signatures:  Ed25519 sealed

✅ Published jwt_auth@1.2.0 [0.8s]
🔗 Package: https://zoren.dev/@juniorsir/jwt_auth
```

---

## 3. Listing Installed Packages: `zoren list`

View all active packages, their creators, and their security access levels:

```bash
zoren list
```

Output:
```text
▲ zoren list

  Package      Version  Creator      Access
  jwt_auth     1.2.0    @juniorsir   sandboxed
  crypto       2.1.0    @zoren_core  sandboxed
  http_fetch   0.4.0    @alex_dev    network

  Total: 3 packages linked
```

---

## 4. Inspecting a Package: `zoren info <pkg>`

Inspect detailed metadata, capabilities, and dependencies:

```bash
zoren info jwt_auth
```

Output:
```text
▲ zoren info jwt_auth

  jwt_auth@1.2.0 by @juniorsir
  Description:   High-performance JSON Web Token authentication
  License:       MIT
  Capabilities:  Pure Memory (no network, no disk)

🔗 https://zoren.dev/@juniorsir/jwt_auth
```

---

## 5. Uninstalling a Package: `zoren uninstall <pkg>`

```bash
zoren uninstall jwt_auth
```

Output:
```text
▲ zoren uninstall jwt_auth

  Removing:    jwt_auth@1.2.0
  Unlinked:    Cleaned from module cache
  Manifest:    Updated zoren.json

✅ Uninstalled jwt_auth in 8ms
```

---

## 6. Project Manifest: `zoren.json` (or `zoren.toml`)

Just like `vercel.json` or `package.json`, project configuration is dead simple, human-readable, and explicit:

### `zoren.json`
```json
{
  "name": "jwt_auth",
  "version": "1.2.0",
  "description": "High-performance JSON Web Token authentication",
  "creator": {
    "name": "Junior Sir",
    "github": "juniorsir"
  },
  "license": "MIT",
  "capabilities": {
    "network": false,
    "filesystem": false
  },
  "dependencies": {
    "crypto": "^2.1.0"
  }
}
```

### Or `zoren.toml`
```toml
name = "jwt_auth"
version = "1.2.0"
description = "High-performance JSON Web Token authentication"
license = "MIT"

[creator]
name = "Junior Sir"
github = "juniorsir"

[capabilities]
network = false
filesystem = false

[dependencies]
crypto = "^2.1.0"
```

---

## 7. Command Summary

| Command | Action |
| :--- | :--- |
| `zoren install <pkg>` | Install a package from registry or Git URL (`add` also supported) |
| `zoren uninstall <pkg>` | Remove a package and clean cache (`remove` also supported) |
| `zoren list` | List all linked packages with security access levels |
| `zoren info <pkg>` | Inspect package details, creator, and capabilities |
| `zoren publish [path]` | Cryptographically seal and publish package to Zoren Hub |
| `zoren repl` | Interactive shell (`:modules` to explore available modules) |
