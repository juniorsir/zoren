# HTTP Payload Fetching

# Problem
You want to fetch HTTP responses asynchronously.

# Solution
Import `std/net` and call `fetch_http_payload(url)`.

# Code
```zoren
bring net

flow main() -> Int {
    bind payload = await fetch_http_payload("https://zoren.org")
    post("Payload: ", payload)
    deliver 0
}
```

# Related
- [Standard Library — std/net](../../standard-library/net.md)
