# Modules and Imports

## 1. Syntax
```ebnf
ImportDirective = "bring" ModulePath [ "as" Identifier ] [ "use" ( SingleUse | UseBlock ) ] ;
```

## 2. Examples
```zoren
bring math
bring text as txt
bring foreign.python use { numpy as np, pandas as pd }
```

## 3. Implementation Status
`SUPPORTED` (`zoren/src/main.rs`, `parser.rs`)
