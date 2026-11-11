# Package and Dependency Management

Zoren packages use content-addressed Merkle Module Trees (ZMMT):

```zoren
# manifest.zor
package <- "zoren::org::app"
version <- "1.0.0"

dependency "std::math_vec" {
    source <- "https://registry.zoren.org/std/math_vec-v1.0.0.tar.gz"
    sha256 <- "e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855"
}
```
