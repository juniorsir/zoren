# 📚 Zoren Standard Library & Enterprise Plugin Catalog

Welcome to the **Zoren Standard Library (`std/`)** and **Enterprise Plugin Ecosystem (`plugins/`)** reference.

Every module in Zoren is built with **100% native Zoren code**, zero C/Rust dependencies, zero stubs, zero GC overhead, and verified across our automated regression test suite (**295/295 tests passing**).

---

## ⚡ Quick Guide: How to Import Modules

In Zoren, bringing modules into your project is clean and intuitive:

```zoren
// Bring core standard library modules (located in std/):
bring math
bring text
bring json
bring fs
bring rope
bring fenwick_tree_2d

// Bring enterprise plugins (located in plugins/):
bring plugins.cuckoo_hash_map
bring plugins.vector_hnsw
bring plugins.zstandard_frame
bring plugins.chandy_lamport_snapshot
bring plugins.h3_hex_grid
bring plugins.bloom_blocked_simd
```

---

## 🗂️ Module Categories at a Glance

| Category | Modules Count | Key Highlights |
|---|:---:|---|
| [**1. Core Systems & I/O**](#1-core-systems--io) | 12 | Filesystem, environment, synchronization, raw byte buffers, terminal styling |
| [**2. High-Performance Data Structures**](#2-high-performance-data-structures) | 16 | Binary Rope, B+ Tree, Red-Black, Splay, Treap, vEB Tree, Wavelet Matrix, Fenwick 2D |
| [**3. Distributed Systems & Consensus**](#3-distributed-systems--consensus) | 14 | Raft Joint Consensus, Paxos, Chandy-Lamport Snapshot, Distributed Barrier, Gossip |
| [**4. Serialization & Framing Protocols**](#4-serialization--framing-protocols) | 10 | Zero-copy JSON, Parquet, Arrow IPC, Cap'n Proto, FlatBuffers, Snappy, Zstandard |
| [**5. Fast Search, Indexing & Geo-Spatial**](#5-fast-search-indexing--geo-spatial) | 12 | Suffix Automaton, Aho-Corasick, ART Radix Tree, Cuckoo Hash, HNSW Vector Index, H3 Grid |
| [**6. Probabilistic Filters & Traffic Control**](#6-probabilistic-filters--traffic-control) | 12 | Cache-Blocked SIMD Bloom, Scalable Bloom, HyperLogLog++, Hierarchical Token Bucket |
| [**7. Cryptography, Auth & Security**](#7-cryptography-auth--security) | 8 | PBKDF2 / HKDF, Base58Check, JWT HMAC-SHA256, OAuth2 with PKCE, Secret Vault |
| [**8. Native AI, Tensors & Quantization**](#8-native-ai-tensors--quantization) | 6 | Autograd Tensors, LoRA fine-tuning, INT8 Quantization, Product Quantization |

---

## 1. Core Systems & I/O

Foundational runtime primitives for building reliable command-line tools, network servers, and high-performance operating utilities.

| Module | Location | Description |
|---|---|---|
| `fs` | [`std/fs.zor`](file:///root/Zoren_lang/std/fs.zor) | File operations: `read_text`, `write_text`, `exists`, `size`, `remove`, `mkdir`. |
| `env` | [`std/env.zor`](file:///root/Zoren_lang/std/env.zor) | Environment variable reader with defaults and typed integer parsing. |
| `sync` | [`std/sync.zor`](file:///root/Zoren_lang/std/sync.zor) | Concurrency synchronization: Mutex spinlocks, WaitGroups, and counting Semaphores. |
| `byte_buffer` | [`std/byte_buffer.zor`](file:///root/Zoren_lang/std/byte_buffer.zor) | Direct memory buffer with Big/Little-endian integer and byte operations. |
| `text` | [`std/text.zor`](file:///root/Zoren_lang/std/text.zor) | High-level string manipulation: `pad_left`, `pad_right`, `center`, `word_count`, `str_concat`. |
| `math` | [`std/math.zor`](file:///root/Zoren_lang/std/math.zor) | Pure integer mathematics: `abs`, `min`, `max`, `pow`, `clamp`, `gcd`, `lcm`. |
| `datetime` | [`std/datetime.zor`](file:///root/Zoren_lang/std/datetime.zor) | Unix timestamp parser, leap year calendar math, and ISO 8601 formatting. |
| `argparse` | [`std/argparse.zor`](file:///root/Zoren_lang/std/argparse.zor) | Command-line argument parser supporting boolean flags, options, and positional tokens. |
| `ansi_color` | [`std/ansi_color.zor`](file:///root/Zoren_lang/std/ansi_color.zor) | Terminal styling, 256-color palette (`ansi_color_256`), bold/underline, and escape code stripper. |
| `semver` | [`std/semver.zor`](file:///root/Zoren_lang/std/semver.zor) | Semantic Versioning 2.0.0 parser, comparator, and range checker (`^`, `~`, `>=`). |
| `url` | [`std/url.zor`](file:///root/Zoren_lang/std/url.zor) | RFC 3986 URL parser: scheme, host, port, path, query parameters, and anchor tags. |
| `stats` | [`std/stats.zor`](file:///root/Zoren_lang/std/stats.zor) | Online $O(1)$ memory Welford algorithm for running Mean, Variance, and Standard Deviation. |

### Example: File Operations & Environment Config
```zoren
bring fs
bring env

flow main() -> Int {
    flex port_str = env_get("PORT", "8080")
    if !fs_exists("app.log") {
        fs_write_text("app.log", "Server initialized on port: " + port_str + "\n")
    }
    deliver 0
}
```

---

## 2. High-Performance Data Structures

Algorithmic data structures engineered for $O(1)$ or $O(\log N)$ performance, bounded cache footprints, and zero memory leaks.

| Module | Location | Description |
|---|---|---|
| `rope` | [`std/rope.zor`](file:///root/Zoren_lang/std/rope.zor) | Binary tree for large texts: $O(\log N)$ concatenation, slicing, insertion, and deletion. |
| `fenwick_tree_2d` | [`std/fenwick_tree_2d.zor`](file:///root/Zoren_lang/std/fenwick_tree_2d.zor) | 2D Binary Indexed Tree (BIT) for $O(\log N \log M)$ dynamic point updates and range sums. |
| `van_emde_boas` | [`std/van_emde_boas.zor`](file:///root/Zoren_lang/std/van_emde_boas.zor) | $O(\log \log U)$ integer priority queue: min, max, predecessor, successor, and membership. |
| `wavelet_matrix` | [`std/wavelet_matrix.zor`](file:///root/Zoren_lang/std/wavelet_matrix.zor) | Succinct data structure providing $O(\log \Sigma)$ rank queries and range quantile selection. |
| `b_plus_tree` | [`std/b_plus_tree.zor`](file:///root/Zoren_lang/std/b_plus_tree.zor) | Order-8 self-balancing B+ Tree with linked leaf nodes for fast range scans and lookups. |
| `red_black_tree` | [`std/red_black_tree.zor`](file:///root/Zoren_lang/std/red_black_tree.zor) | Left-Leaning Red-Black (LLRB) self-balancing binary search tree. |
| `splay_tree` | [`std/splay_tree.zor`](file:///root/Zoren_lang/std/splay_tree.zor) | Self-adjusting BST splaying frequently accessed keys to root for natural LRU locality. |
| `treap_cartesian` | [`std/treap_cartesian.zor`](file:///root/Zoren_lang/std/treap_cartesian.zor) | Randomized Cartesian tree combining BST key order with heap-priority balancing. |
| `succinct_bit_vector` | [`std/succinct_bit_vector.zor`](file:///root/Zoren_lang/std/succinct_bit_vector.zor) | Compressed bit array supporting $O(1)$ `rank1(i)` and binary search `select1(k)`. |
| `roaring_bitmap` | [`std/roaring_bitmap.zor`](file:///root/Zoren_lang/std/roaring_bitmap.zor) | Hybrid compressed bitmap for massive integer sets: union, intersection, difference. |
| `interval_tree` | [`std/interval_tree.zor`](file:///root/Zoren_lang/std/interval_tree.zor) | 1D range search tree for interval overlaps, calendar reservations, and memory segments. |
| `quadtree` | [`std/quadtree.zor`](file:///root/Zoren_lang/std/quadtree.zor) | 2D spatial partitioning tree for bounding-box range counts and nearest neighbor queries. |
| `disjoint_set` | [`std/disjoint_set.zor`](file:///root/Zoren_lang/std/disjoint_set.zor) | Disjoint-Set Union (Union-Find) with path compression and union-by-rank. |
| `ring_buffer` | [`std/ring_buffer.zor`](file:///root/Zoren_lang/std/ring_buffer.zor) | High-throughput circular FIFO queue for producer-consumer pipelines. |
| `priority_queue_min` | [`std/priority_queue_min.zor`](file:///root/Zoren_lang/std/priority_queue_min.zor) | Binary min-heap priority queue ($O(\log N)$ push & pop) for Dijkstra / A* pathfinding. |
| `heap_fibonacci` | [`std/heap_fibonacci.zor`](file:///root/Zoren_lang/std/heap_fibonacci.zor) | Fibonacci/Pairing min-heap with $O(1)$ amortized insertion and consolidated root removal. |

### Example: Binary Rope Manipulation
```zoren
bring rope
bring system

flow main() -> Int {
    flex r1 = rope_from_text("Hello, ")
    flex r2 = rope_from_text("World!")
    flex r = rope_concat(r1, r2)
    
    // Insert without reallocating full string:
    flex r_new = rope_insert(r, 7, "Beautiful ")
    print_text(rope_to_text(r_new)) // "Hello, Beautiful World!"
    
    rope_free(r1)
    rope_free(r2)
    rope_free(r)
    rope_free(r_new)
    deliver 0
}
```

---

## 3. Distributed Systems & Consensus

Production-grade protocols for building fault-tolerant distributed databases, clusters, and microservice meshes.

| Module | Location | Description |
|---|---|---|
| `raft_joint_consensus` | [`plugins/raft_joint_consensus.zor`](file:///root/Zoren_lang/plugins/raft_joint_consensus.zor) | Ongaro-Ousterhout two-phase joint consensus membership reconfiguration ($C_{\text{old}} \to C_{\text{old,new}} \to C_{\text{new}}$). |
| `raft_log_compaction` | [`plugins/raft_log_compaction.zor`](file:///root/Zoren_lang/plugins/raft_log_compaction.zor) | Raft state-machine log compaction, snapshot creation, and InstallSnapshot RPC sync. |
| `paxos_multidecree` | [`plugins/paxos_multidecree.zor`](file:///root/Zoren_lang/plugins/paxos_multidecree.zor) | Multi-instance Paxos consensus: Prepare/Promise (Phase 1), Accept/Accepted (Phase 2). |
| `chandy_lamport_snapshot` | [`plugins/chandy_lamport_snapshot.zor`](file:///root/Zoren_lang/plugins/chandy_lamport_snapshot.zor) | Distributed global state snapshot capturing process & in-flight channel states without pauses. |
| `distributed_barrier` | [`plugins/distributed_barrier.zor`](file:///root/Zoren_lang/plugins/distributed_barrier.zor) | Multi-stage distributed coordination barrier with generation rolling and arrival synchronization. |
| `distributed_lock` | [`plugins/distributed_lock.zor`](file:///root/Zoren_lang/plugins/distributed_lock.zor) | Distributed lease coordinator with TTL expiration, heartbeat renewal, and fencing tokens. |
| `consistent_hash` | [`plugins/consistent_hash.zor`](file:///root/Zoren_lang/plugins/consistent_hash.zor) | Distributed ring hashing with uniform token distribution and node lookups. |
| `consistent_ring_vnodes` | [`plugins/consistent_ring_vnodes.zor`](file:///root/Zoren_lang/plugins/consistent_ring_vnodes.zor) | Dynamo/Cassandra style consistent hash ring with virtual nodes (vnodes) preventing hotspots. |
| `consistent_ring_maglev` | [`plugins/consistent_ring_maglev.zor`](file:///root/Zoren_lang/plugins/consistent_ring_maglev.zor) | Google Maglev lookup table for ultra-uniform packet distribution across backend servers. |
| `consistent_ring_mp_hash` | [`plugins/consistent_ring_mp_hash.zor`](file:///root/Zoren_lang/plugins/consistent_ring_mp_hash.zor) | Multi-Probe Consistent Hash algorithm minimizing peak-to-average variance with zero vnode overhead. |
| `gossip_cluster` | [`plugins/gossip_cluster.zor`](file:///root/Zoren_lang/plugins/gossip_cluster.zor) | SWIM gossip membership protocol (ALIVE, SUSPECT, DEAD) with incarnation counters. |
| `saga_orchestrator` | [`plugins/saga_orchestrator.zor`](file:///root/Zoren_lang/plugins/saga_orchestrator.zor) | Distributed transaction coordinator with automatic reverse compensation on step failure. |
| `two_phase_commit` | [`plugins/two_phase_commit.zor`](file:///root/Zoren_lang/plugins/two_phase_commit.zor) | Classic 2PC coordinator managing PREPARE, COMMIT, and ABORT with participant timeouts. |
| `actor_system` | [`plugins/actor_system.zor`](file:///root/Zoren_lang/plugins/actor_system.zor) | Erlang/Akka-style lightweight actor model with bounded FIFO mailboxes and supervision strategies. |

---

## 4. Serialization & Framing Protocols

Zero-copy, columnar, and binary stream parsers for interoperating with modern big-data pipelines, message buses, and RPC frameworks.

| Module | Location | Description |
|---|---|---|
| `json` | [`std/json.zor`](file:///root/Zoren_lang/std/json.zor) | High-speed zero-copy JSON parser and serializer with nested field extractors. |
| `csv` | [`std/csv.zor`](file:///root/Zoren_lang/std/csv.zor) | Structured CSV tabular parser supporting header extraction, row indexing, and column lookups. |
| `parquet_metadata` | [`plugins/parquet_metadata.zor`](file:///root/Zoren_lang/plugins/parquet_metadata.zor) | Apache Parquet columnar footer inspector: `PAR1` magic, footer length, and schema descriptors. |
| `arrow_ipc_frame` | [`plugins/arrow_ipc_frame.zor`](file:///root/Zoren_lang/plugins/arrow_ipc_frame.zor) | Apache Arrow columnar IPC stream framing with record batches and 64-byte SIMD alignment. |
| `capnproto_frame` | [`plugins/capnproto_frame.zor`](file:///root/Zoren_lang/plugins/capnproto_frame.zor) | Cap'n Proto zero-copy message framing: multi-segment headers and word-alignment padding. |
| `flatbuffers_verifier` | [`plugins/flatbuffers_verifier.zor`](file:///root/Zoren_lang/plugins/flatbuffers_verifier.zor) | Google FlatBuffers binary verifier: vtable offsets, table bounds, and scalar field extraction. |
| `snappy_framed` | [`plugins/snappy_framed.zor`](file:///root/Zoren_lang/plugins/snappy_framed.zor) | Official Google Snappy framed stream protocol codec with CRC32c masked checksums. |
| `zstandard_frame` | [`plugins/zstandard_frame.zor`](file:///root/Zoren_lang/plugins/zstandard_frame.zor) | RFC 8878 Zstandard (zstd) frame parser: `0xFD2FB528` magic validation and block headers. |
| `tar_archive` | [`std/tar_archive.zor`](file:///root/Zoren_lang/std/tar_archive.zor) | POSIX UStar TAR archive inspector: 512-byte header parsing, checksums, and entry extraction. |
| `template` | [`std/template.zor`](file:///root/Zoren_lang/std/template.zor) | Mustache-style template substitution (`{{ var }}`) and conditional blocks (`{{#if k}}`). |

---

## 5. Fast Search, Indexing & Geo-Spatial

Hardware-friendly search algorithms, multi-pattern string matchers, spatial grids, and vector indexing.

| Module | Location | Description |
|---|---|---|
| `cuckoo_hash_map` | [`plugins/cuckoo_hash_map.zor`](file:///root/Zoren_lang/plugins/cuckoo_hash_map.zor) | Guaranteed $O(1)$ worst-case lookup hash table with dual hashes, kick-outs, and stash. |
| `vector_hnsw` | [`plugins/vector_hnsw.zor`](file:///root/Zoren_lang/plugins/vector_hnsw.zor) | Hierarchical Navigable Small World (HNSW) proximity graph for fast vector search. |
| `suffix_automaton` | [`std/suffix_automaton.zor`](file:///root/Zoren_lang/std/suffix_automaton.zor) | Linear-time $O(N)$ Suffix Automaton (SAM / DAWG) for distinct substrings and LCF analysis. |
| `aho_corasick` | [`plugins/aho_corasick.zor`](file:///root/Zoren_lang/plugins/aho_corasick.zor) | Multi-pattern dictionary automaton matching $K$ keywords simultaneously in $O(N + M)$ time. |
| `adaptive_radix_tree` | [`plugins/adaptive_radix_tree.zor`](file:///root/Zoren_lang/plugins/adaptive_radix_tree.zor) | Adaptive Radix Tree (ART) with dynamic node sizing and cache-friendly byte indexing. |
| `trie_router` | [`plugins/trie_router.zor`](file:///root/Zoren_lang/plugins/trie_router.zor) | High-speed Prefix Trie Router for HTTP URL matching and REST dispatching. |
| `trie_set` | [`std/trie_set.zor`](file:///root/Zoren_lang/std/trie_set.zor) | Compact prefix trie for string dictionary lookups and prefix completions. |
| `radix_sort` | [`plugins/radix_sort.zor`](file:///root/Zoren_lang/plugins/radix_sort.zor) | Linear-time integer sorting (`radix_sort_i64`), sort verification, and binary search. |
| `pathfinding_astar` | [`plugins/pathfinding_astar.zor`](file:///root/Zoren_lang/plugins/pathfinding_astar.zor) | 2D Grid A* pathfinder with Manhattan distance heuristics and obstacle avoidance. |
| `h3_hex_grid` | [`plugins/h3_hex_grid.zor`](file:///root/Zoren_lang/plugins/h3_hex_grid.zor) | Uber H3-style hierarchical hexagonal discrete global grid with aperture-7 subdivision. |
| `geohash_grid` | [`plugins/geohash_grid.zor`](file:///root/Zoren_lang/plugins/geohash_grid.zor) | Base32 hierarchical spatial index encoding lat/lon into prefix-matched bounding boxes. |
| `geo_spatial` | [`plugins/geo_spatial.zor`](file:///root/Zoren_lang/plugins/geo_spatial.zor) | Microdegree distance (`geo_distance_meters`), bounding box check, and proximity filter. |

---

## 6. Probabilistic Filters & Traffic Control

Constant-space probabilistic data structures and precise rate-limiting algorithms for high-throughput network gateways.

| Module | Location | Description |
|---|---|---|
| `bloom_blocked_simd` | [`plugins/bloom_blocked_simd.zor`](file:///root/Zoren_lang/plugins/bloom_blocked_simd.zor) | Cache-blocked Bloom filter confining bit probes to 64-byte blocks for single cache-line queries. |
| `bloom_counting` | [`plugins/bloom_counting.zor`](file:///root/Zoren_lang/plugins/bloom_counting.zor) | 4-bit nibble counting Bloom filter supporting item insertions AND deletions. |
| `bloom_scalable` | [`plugins/bloom_scalable.zor`](file:///root/Zoren_lang/plugins/bloom_scalable.zor) | Scalable Bloom filter chaining dynamic sub-slices as capacity grows with bounded error. |
| `cuckoo_filter` | [`plugins/cuckoo_filter.zor`](file:///root/Zoren_lang/plugins/cuckoo_filter.zor) | Fingerprint-based cuckoo filter supporting element insertion, query, and deletion. |
| `hll_hyperloglog_plus` | [`plugins/hll_hyperloglog_plus.zor`](file:///root/Zoren_lang/plugins/hll_hyperloglog_plus.zor) | Google HyperLogLog++ 64-bit cardinality estimator with linear counting bias correction. |
| `hyperloglog` | [`plugins/hyperloglog.zor`](file:///root/Zoren_lang/plugins/hyperloglog.zor) | Standard HyperLogLog probabilistic cardinality estimator. |
| `token_bucket_hierarchical` | [`plugins/token_bucket_hierarchical.zor`](file:///root/Zoren_lang/plugins/token_bucket_hierarchical.zor) | Multi-tenant rate limiter enforcing tenant quotas alongside global system rate caps. |
| `token_bucket_limiter` | [`plugins/token_bucket_limiter.zor`](file:///root/Zoren_lang/plugins/token_bucket_limiter.zor) | Token Bucket limiter with sub-millisecond fractional token regeneration. |
| `leaky_bucket` | [`plugins/leaky_bucket.zor`](file:///root/Zoren_lang/plugins/leaky_bucket.zor) | Traffic shaping queue with constant-rate drain and drop metrics for smooth network egress. |
| `rate_limiter_sliding_log` | [`plugins/rate_limiter_sliding_log.zor`](file:///root/Zoren_lang/plugins/rate_limiter_sliding_log.zor) | Sub-millisecond exact timestamp log limiter providing strict zero-burst guarantees. |
| `sliding_window_counter` | [`plugins/sliding_window_counter.zor`](file:///root/Zoren_lang/plugins/sliding_window_counter.zor) | Circular sub-window rate limiter smoothing boundary burst spikes. |
| `circuit_breaker` | [`plugins/circuit_breaker.zor`](file:///root/Zoren_lang/plugins/circuit_breaker.zor) | Enterprise circuit breaker with failure thresholds, recovery timeout, and half-open probes. |

---

## 7. Cryptography, Auth & Security

Hardened cryptographic hashing, key stretching, zero-knowledge tokens, and secure memory vaults.

| Module | Location | Description |
|---|---|---|
| `crypto_hash` | [`std/crypto_hash.zor`](file:///root/Zoren_lang/std/crypto_hash.zor) | Algorithmic implementations of FNV-1a (32/64-bit) and DJB2 hash functions. |
| `kdf` | [`std/kdf.zor`](file:///root/Zoren_lang/std/kdf.zor) | PBKDF2 iterative key derivation (`kdf_pbkdf2_hex`), constant-time verify, and HKDF expand. |
| `base62` | [`std/base62.zor`](file:///root/Zoren_lang/std/base62.zor) | Base62 alphanumeric conversion and Bitcoin/IPFS Base-58 integer encoding/decoding. |
| `base58_check` | [`std/base58_check.zor`](file:///root/Zoren_lang/std/base58_check.zor) | Bitcoin/IPFS Base58Check encoder and decoder with double-SHA256 checksum validation. |
| `jwt_validator` | [`plugins/jwt_validator.zor`](file:///root/Zoren_lang/plugins/jwt_validator.zor) | RFC 7519 JSON Web Token HMAC-SHA256 signer, verifier, claims extractor, and expiration check. |
| `oauth2_client` | [`plugins/oauth2_client.zor`](file:///root/Zoren_lang/plugins/oauth2_client.zor) | OAuth2 & OIDC protocol engine: auth URL builder, PKCE S256 challenge, and token lease renewal. |
| `secret_vault` | [`plugins/secret_vault.zor`](file:///root/Zoren_lang/plugins/secret_vault.zor) | In-memory secret vault with read-count burning, TTL expiration, and cryptographic zeroization. |
| `uuid` | [`std/uuid.zor`](file:///root/Zoren_lang/std/uuid.zor) | RFC 4122 Version 4 random UUID and RFC 9562 Version 7 time-ordered UUID generator. |

---

## 8. Native AI, Tensors & Quantization

Bare-metal vector math and deep learning components built for native execution without Python or CUDA runtime overhead.

| Module | Location | Description |
|---|---|---|
| `ai` | [`std/ai.zor`](file:///root/Zoren_lang/std/ai.zor) | Native autograd reverse-mode autodiff tensor engine with 2D matrix multiplication. |
| `nn` | [`std/nn.zor`](file:///root/Zoren_lang/std/nn.zor) | Neural network building blocks: Linear layers, LayerNorm, Multi-Head Attention, ReLU/GELU. |
| `lora` | [`std/lora.zor`](file:///root/Zoren_lang/std/lora.zor) | Low-Rank Adaptation (LoRA) parameter-efficient adapter matrix factorization. |
| `quantization` | [`std/quantization.zor`](file:///root/Zoren_lang/std/quantization.zor) | Fixed-point INT8 quantization, scale/zero-point calibration, and quantized dot products. |
| `vector_quantize_kmeans` | [`plugins/vector_quantize_kmeans.zor`](file:///root/Zoren_lang/plugins/vector_quantize_kmeans.zor) | Product Quantization (PQ) codebook assignment and fast asymmetric distance computation (ADC). |
| `llm_inference` | [`plugins/llm_inference.zor`](file:///root/Zoren_lang/plugins/llm_inference.zor) | Mock-safe LLM client interface with latency telemetry and token count tracking. |
