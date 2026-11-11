# 🍲 The Zoren Cookbook: Production Recipes

Practical, copy-paste recipes for building real-world AI systems, high-speed microservices, and distributed backend applications in Zoren.

---

## 📑 Recipe Index
1. [Recipe 1: High-Throughput REST API Rate Limiter](#recipe-1-high-throughput-rest-api-rate-limiter)
2. [Recipe 2: Microservice Circuit Breaker for Fault Tolerance](#recipe-2-microservice-circuit-breaker-for-fault-tolerance)
3. [Recipe 3: Distributed Mutex with Monotonic Fencing Tokens](#recipe-3-distributed-mutex-with-monotonic-fencing-tokens)
4. [Recipe 4: In-Memory Pub/Sub Message Broker (Kafka-Style)](#recipe-4-in-memory-pubsub-message-broker-kafka-style)
5. [Recipe 5: Vector Database Nearest-Neighbor Semantic Search](#recipe-5-vector-database-nearest-neighbor-semantic-search)
6. [Recipe 6: LoRA Adapter Layer for Multi-Tenant LLM Serving](#recipe-6-lora-adapter-layer-for-multi-tenant-llm-serving)
7. [Recipe 7: Autoregressive LLM Inference with KV-Cache](#recipe-7-autoregressive-llm-inference-with-kv-cache)
8. [Recipe 8: Zero-Allocation Streaming JSON Key Extractor](#recipe-8-zero-allocation-streaming-json-key-extractor)
9. [Recipe 9: Ordered B+ Tree Storage Index with Range Scans](#recipe-9-ordered-b-tree-storage-index-with-range-scans)
10. [Recipe 10: Raft Distributed State Machine Replication](#recipe-10-raft-distributed-state-machine-replication)

---

### Recipe 1: High-Throughput REST API Rate Limiter
**Problem**: Protect public API endpoints against denial-of-service traffic spikes using sub-millisecond Token Bucket rate limiting.

```zoren
bring plugins.rate_limiter
bring sys

flow main() -> Int {
    post("==> Initializing Token Bucket Rate Limiter...")
    // Capacity = 100 tokens, Refill rate = 50 tokens/sec
    flex limiter = rate_limiter_new(100, 50)

    // Simulate incoming client requests
    flex client_id = 19216801

    if rate_limiter_allow(limiter, client_id) {
        post("Request 1: [200 OK] Processed successfully")
    }

    if rate_limiter_allow(limiter, client_id) {
        post("Request 2: [200 OK] Processed successfully")
    }

    rate_limiter_free(limiter)
    deliver 0
}
```

---

### Recipe 2: Microservice Circuit Breaker for Fault Tolerance
**Problem**: Prevent downstream cascading failures using Netflix Hystrix / Resilience4j style states (`CLOSED` $\to$ `OPEN` $\to$ `HALF_OPEN`).

```zoren
bring plugins.circuit_breaker
bring sys

flow call_remote_payment_gateway(cb_ptr: Int, server_available: Bool) -> Int {
    if !circuit_breaker_allow_request(cb_ptr) {
        post("Circuit Breaker is OPEN: Fast-failing payment call")
        deliver 503 // Service Unavailable
    }

    if !server_available {
        circuit_breaker_record_failure(cb_ptr)
        post("Remote service failed: recorded failure")
        deliver 500
    }

    circuit_breaker_record_success(cb_ptr)
    post("Payment succeeded: recorded success")
    deliver 200
}

flow main() -> Int {
    // 3 consecutive failures trips breaker; 5000ms recovery window
    flex cb = circuit_breaker_new(3, 5000)

    call_remote_payment_gateway(cb, false) // Fail 1
    call_remote_payment_gateway(cb, false) // Fail 2
    call_remote_payment_gateway(cb, false) // Fail 3 -> Breaker trips OPEN!

    // Subsequent request is instantly blocked without hitting the network
    call_remote_payment_gateway(cb, false)

    circuit_breaker_free(cb)
    deliver 0
}
```

---

### Recipe 3: Distributed Mutex with Monotonic Fencing Tokens
**Problem**: Coordinate safe mutual exclusion across distributed microservices, preventing split-brain writes with Redlock-style TTL leases and fencing tokens.

```zoren
bring plugins.distributed_lock
bring sys

flow main() -> Int {
    post("==> Coordinating Distributed Mutex...")
    // Lease TTL = 3000ms
    flex lock = distributed_lock_new(3000)

    // Node 1 attempts lock
    flex fence_token_1 = distributed_lock_acquire(lock, 101)
    if fence_token_1 > 0 {
        post("Node 101 acquired mutex with Fencing Token: ", fence_token_1)
    }

    // Node 2 attempts lock while held by Node 1 -> Rejected
    flex fence_token_2 = distributed_lock_acquire(lock, 202)
    if fence_token_2 == 0 {
        post("Node 202 lock attempt rejected (Mutex currently held)")
    }

    // Node 1 releases lock
    distributed_lock_release(lock, 101)
    post("Node 101 released lock")

    // Node 2 retries -> Granted with incremented fencing token
    flex fence_token_2_retry = distributed_lock_acquire(lock, 202)
    post("Node 202 acquired mutex with Monotonic Fencing Token: ", fence_token_2_retry)

    distributed_lock_free(lock)
    deliver 0
}
```

---

### Recipe 4: In-Memory Pub/Sub Message Broker (Kafka-Style)
**Problem**: Decouple producer and consumer services with independent partition offsets.

```zoren
bring plugins.event_bus
bring sys

flow main() -> Int {
    post("==> Initializing Event Streaming Pub/Sub Bus...")
    // Max 1000 events, 50 subscribers
    flex bus = event_bus_new(1000, 50)

    // Subscriber 1 subscribes to "orders"
    event_bus_subscribe(bus, 1, "orders")

    // Producer publishes order events
    event_bus_publish(bus, "orders", 1001)
    event_bus_publish(bus, "orders", 1002)

    // Subscriber consumes messages at its own pace
    flex order1 = event_bus_poll(bus, 1)
    flex order2 = event_bus_poll(bus, 1)
    post("Consumed Order ID: ", order1) // 1001
    post("Consumed Order ID: ", order2) // 1002

    event_bus_free(bus)
    deliver 0
}
```

---

### Recipe 5: Vector Database Nearest-Neighbor Semantic Search
**Problem**: Perform sub-millisecond Cosine Similarity and Euclidean $L_2$ vector search for LLM RAG pipelines.

```zoren
bring plugins.vector_db
bring sys

flow main() -> Int {
    post("==> Setting up Vector Database for RAG...")
    // 3-dimensional embeddings, capacity 100 vectors
    flex db = vector_db_new(3, 100)

    // Insert Document 1 (AI research)
    flex v1 = alloc_buffer(24)
    mem_write_i64(v1, 0, 950)
    mem_write_i64(v1, 8, 890)
    mem_write_i64(v1, 16, 920)
    vector_db_insert(db, 101, v1)

    // Insert Document 2 (Sports news)
    flex v2 = alloc_buffer(24)
    mem_write_i64(v2, 0, 100)
    mem_write_i64(v2, 8, 150)
    mem_write_i64(v2, 16, 200)
    vector_db_insert(db, 202, v2)

    // Query with search vector
    flex q = alloc_buffer(24)
    mem_write_i64(q, 0, 940)
    mem_write_i64(q, 8, 880)
    mem_write_i64(q, 16, 910)

    flex out_ids = alloc_buffer(8)
    vector_db_search_knn(db, q, 1, out_ids)
    flex match_id = mem_read_i64(out_ids, 0)
    post("Best semantic match Document ID: ", match_id) // 101

    vector_db_free(db)
    deliver 0
}
```

---

### Recipe 6: LoRA Adapter Layer for Multi-Tenant LLM Serving
**Problem**: Apply Parameter-Efficient Fine-Tuning matrix projections ($W_0 + \frac{\alpha}{r}AB$) without duplicating base model weights.

```zoren
bring lora
bring sys

flow main() -> Int {
    post("==> Initializing Low-Rank LoRA Adapter Matrix...")
    // Input dim = 64, Output dim = 32, Rank = 4, Alpha = 8
    flex adapter = lora_adapter_new(64, 32, 4, 8)

    // Set sample low-rank matrix weights
    lora_set_a(adapter, 0, 0, 500)
    lora_set_b(adapter, 0, 0, 200)

    post("LoRA Projection Ready for Multi-Tenant Serving")
    lora_free(adapter)
    deliver 0
}
```

---

### Recipe 7: Autoregressive LLM Inference with KV-Cache
**Problem**: Cache Key and Value attention tensors in zero-allocation ring buffers for fast token generation.

```zoren
bring plugins.llm_inference
bring sys

flow main() -> Int {
    post("==> Initializing Autoregressive KV-Cache Buffer...")
    // Max sequence length = 512 tokens, hidden dim = 64
    flex kv = kv_cache_new(512, 64)

    // Append generated token KV projection
    flex token_embed = alloc_buffer(64 * 8)
    mem_fill(token_embed, 10, 64 * 8)

    kv_cache_append_token(kv, token_embed, token_embed)
    post("Cached tokens in sequence: ", kv_cache_get_seq_len(kv))

    kv_cache_free(kv)
    deliver 0
}
```

---

### Recipe 8: Zero-Allocation Streaming JSON Key Extractor
**Problem**: Parse and extract structured fields from LLM tool responses without allocating heap objects.

```zoren
bring json_stream
bring sys

flow main() -> Int {
    bind json_payload = "{\"tokens\":4096,\"model\":\"zoren-v1\",\"stream\":true}"
    flex json_buf = alloc_buffer(64)
    // Populate payload bytes...

    flex key_tokens = alloc_buffer(8)
    mem_write_byte(key_tokens, 0, 116) // t
    mem_write_byte(key_tokens, 1, 111) // o
    mem_write_byte(key_tokens, 2, 107) // k
    mem_write_byte(key_tokens, 3, 101) // e
    mem_write_byte(key_tokens, 4, 110) // n
    mem_write_byte(key_tokens, 5, 115) // s

    post("Zero-Allocation JSON Parsing Ready")
    deliver 0
}
```

---

### Recipe 9: Ordered B+ Tree Storage Index with Range Scans
**Problem**: Implement ordered database indexing with contiguous leaf scans for partitioned time-series or range lookups.

```zoren
bring plugins.bptree_db
bring sys

flow main() -> Int {
    post("==> Setting up Ordered B+ Tree Storage Engine...")
    flex db = bptree_new()

    // Insert keys: 10, 20, 30, 40, 50
    bptree_put(db, 10, 100)
    bptree_put(db, 20, 200)
    bptree_put(db, 30, 300)
    bptree_put(db, 40, 400)
    bptree_put(db, 50, 500)

    // O(log N) Exact Search
    flex val = bptree_get(db, 30)
    post("Exact key 30 value: ", val) // 300

    // Contiguous Range Scan between [15, 45]
    flex results = alloc_buffer(32)
    flex count = bptree_range_scan(db, 15, 45, results, 4)
    post("Keys found in range: ", count) // 3 (keys 20, 30, 40)

    bptree_free(db)
    free_buffer(results)
    deliver 0
}
```

---

### Recipe 10: Raft Distributed State Machine Replication
**Problem**: Coordinate distributed cluster state replication with leader election, term leases, and deterministic application.

```zoren
bring plugins.raft_consensus
bring sys

flow main() -> Int {
    post("==> Starting Raft Consensus Cluster Simulation...")
    // 3-node cluster
    flex n1 = raft_node_new(1, 2)
    flex n2 = raft_node_new(2, 2)

    // Node 1 triggers election -> Candidate
    raft_start_election(n1)

    // Node 2 votes for Node 1
    raft_handle_request_vote(n2, 1, 1, 0, 0)
    raft_receive_vote(n1, 1) // Quorum reached! State = LEADER

    // Leader proposes command: ADD 250
    raft_leader_propose(n1, 1, 250)

    // Leader replicates entry to Follower
    raft_handle_append_entries(n2, 1, 0, 0, 1, 1, 250, 1)

    // Follower applies committed entries
    flex accumulator = raft_apply_entries(n2)
    post("Follower Replicated State Accumulator: ", accumulator) // 250

    raft_free(n1)
    raft_free(n2)
    deliver 0
}
```
