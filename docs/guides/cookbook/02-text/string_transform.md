# String Transformations

# Problem
You want to reverse, uppercase, or replace strings in Zoren.

# Solution
Bring `std/text` and call string manipulation functions.

# Code
```zoren
bring text

flow main() -> Int {
    bind sample: Text = "Hello"
    post("Reversed: ", text_reverse(sample))
    post("Uppercase: ", text_upper(sample))
    post("Replaced:  ", text_replace(sample, "H", "J"))
    deliver 0
}
```

# Explanation
- `bring text` imports string manipulation subroutines.
- `text_reverse(s)` reverses the character sequence.
- `text_upper(s)` converts text to uppercase.
- `text_replace(s, a, b)` replaces substring `a` with `b`.

# Why this works
`std/text` provides pre-compiled string helper functions.

# Variations
```zoren
# Using short function aliases
bind r = rev("Hello")
bind u = up("Hello")
```

# Performance
String operations execute natively on stack buffers without dynamic allocation spikes.

# Common mistakes
```zoren
// Incorrect: using unimported string functions without bring text
bind r = text_reverse("Hello") // Compiler Error Z2001
```

# Related
- [Standard Library — std/text](../../standard-library/text.md)
