import time
import sys
import random

def stress_test_ribbon_filters(n_keys=1_000_000_000):
    """
    Simulate Ribbon Filter memory and performance at 1-Billion keys.
    """
    start_time = time.time()

    # Estimate Bloom (10 bits/key)
    bloom_mem_bits = n_keys * 10
    bloom_mem_mb = bloom_mem_bits / (8 * 1024 * 1024)

    # Ribbon (27% reduction)
    ribbon_mem_bits = bloom_mem_bits * (1 - 0.27)
    ribbon_mem_mb = ribbon_mem_bits / (8 * 1024 * 1024)

    # Simulated access time (O(1) - mock lookup)
    # n-million lookups to benchmark
    lookup_count = 1_000_000
    for _ in range(lookup_count):
        _ = random.random() # Mock computation

    end_time = time.time()

    return {
        "n_keys": n_keys,
        "bloom_mb": bloom_mem_mb,
        "ribbon_mb": ribbon_mem_mb,
        "memory_saved_mb": bloom_mem_mb - ribbon_mem_mb,
        "memory_reduction_pct": 27.0,
        "lookup_count": lookup_count,
        "execution_time": end_time - start_time
    }

if __name__ == "__main__":
    res = stress_test_ribbon_filters()
    print(f"Number of Keys: {res['n_keys']:,}")
    print(f"Bloom Memory (MB): {res['bloom_mb']:.2f}")
    print(f"Ribbon Memory (MB): {res['ribbon_mb']:.2f}")
    print(f"Memory Saved (MB): {res['memory_saved_mb']:.2f}")
    print(f"Execution Time: {res['execution_time']:.4f}s")
