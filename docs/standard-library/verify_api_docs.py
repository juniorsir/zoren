#!/usr/bin/env python3
import os

print("Zoren Standard Library API Verification Tool v1.0")
print("==================================================")

std_dir = "Zoren_lang/std"
inventory_path = "Zoren_lang/docs/standard-library/API_INVENTORY.md"

if not os.path.exists(std_dir) or not os.path.exists(inventory_path):
    print("Error: Missing std/ source directory or API_INVENTORY.md!")
    exit(1)

with open(inventory_path, "r", encoding="utf-8") as f:
    inv_text = f.read()

discovered = 0
documented = 0

for root, _, files in os.walk(std_dir):
    for file in sorted(files):
        if file.endswith(".zor"):
            filepath = os.path.join(root, file)
            with open(filepath, "r", encoding="utf-8") as f:
                for line in f:
                    if line.strip().startswith("open flow") or line.strip().startswith("export model") or line.strip().startswith("model"):
                        parts = line.strip().split()
                        if len(parts) >= 3:
                            sym = parts[2].split("(")[0].split("[")[0].strip()
                            discovered += 1
                            if sym in inv_text:
                                documented += 1

print(f"Discovered Public APIs in std/*.zor : {discovered}")
print(f"Documented APIs in API_INVENTORY.md : {documented}")
print("==================================================")
if discovered == documented:
    print("Verification SUCCESS: 100% API Documentation Alignment Verified.")
    exit(0)
else:
    print("Verification WARNING: Mismatch detected in API coverage.")
    exit(1)
