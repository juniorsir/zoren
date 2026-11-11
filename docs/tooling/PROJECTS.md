# Project Workflows and Workspace Layout

## Standard Workspace Structure
```
my_app/
├── manifest.zor       # Package manifest & metadata
├── lock.zor           # Merkle tree lockfile
├── src/
│   └── main.zor       # Application entrypoint
└── tests/
    └── app_test.zor   # Unit tests
```

## Developer Workflow
1. `zoren new my_app`
2. `cd my_app`
3. Edit `src/main.zor`
4. `zoren fmt src/main.zor`
5. `zoren check .`
6. `zoren forge .`
