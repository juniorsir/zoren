# Dynamic Vectors

# Problem
You want to create and manage dynamic array collections.

# Solution
Import `std/collections` and instantiate `create_vector[T]()`.

# Code
```zoren
bring collections

flow main() -> Int {
    bind numbers = create_vector[Int]()
    post("Vector initialized cleanly.")
    deliver 0
}
```

# Explanation
- `bring collections` imports vector data structures.
- `create_vector[Int]()` instantiates a typed dynamic array.

# Why this works
`Vector[T]` is monomorphized at compile time for maximum memory efficiency.

# Related
- [Standard Library — std/collections](../../standard-library/collections.md)
