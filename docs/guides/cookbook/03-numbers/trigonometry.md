# Trigonometry and Math

# Problem
You want to calculate sine, cosine, or hypotenuse in Zoren.

# Solution
Import `std/math` and call integer trigonometric functions.

# Code
```zoren
bring math

flow main() -> Int {
    bind sin_val = sin_deg(45)
    bind cos_val = cos_deg(45)
    bind hypot_val = hypot_int(3, 4)

    post("Sin(45 deg) x1000: ", sin_val)
    post("Hypot(3, 4)         : ", hypot_val)
    deliver 0
}
```

# Explanation
- `sin_deg(45)` computes the sine of 45 degrees scaled by 1000.
- `hypot_int(3, 4)` computes $\sqrt{3^2 + 4^2} = 5$.

# Why this works
`std/math` exports 64-bit integer trigonometric functions mapped to CPU registers.

# Performance
Executes natively on CPU registers without floating-point ABI mismatches.

# Common mistakes
```zoren
// Incorrect: using un-imported math functions
bind s = sin_deg(45) // Compiler Error Z2001
```

# Related
- [Standard Library — std/math](../../standard-library/math.md)
