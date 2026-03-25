import time
import sys
import random

def estimate_bloom_memory(n_keys, fpp=0.01):
    """Simplified estimate of Bloom filter memory in bits."""
    m = -(n_keys * 3.14159) / ( (0.6931)**2 ) # Placeholder for math -m = (n * ln(p)) / (ln(2)^2)
    # Roughly 10 bits per key for 1% fpp
    return n_keys * 10

def estimate_ribbon_memory(n_keys):
    """Estimate memory for Ribbon filter based on whitepaper (27% reduction)."""
    bloom_mem = estimate_bloom_memory(n_keys)
    return bloom_mem * (1 - 0.27)

def benchmark_indexing(n_keys):
    print(f"Indexing Benchmark: {n_keys:,} Entanglement Pairs")
    print("-" * 50)

    bloom_bits = estimate_bloom_memory(n_keys)
    ribbon_bits = estimate_ribbon_memory(n_keys)

    bloom_mb = bloom_bits / (8 * 1024 * 1024)
    ribbon_mb = ribbon_bits / (8 * 1024 * 1024)

    print(f"{'Structure':<20} | {'Memory (MB)':<15} | {'Access Speed'}")
    print("-" * 50)
    print(f"{'Bloom Filter':<20} | {bloom_mb:<15.2f} | O(1)")
    print(f"{'Ribbon Filter':<20} | {ribbon_mb:<15.2f} | O(1)")
    print("-" * 50)
    print(f"Memory Saved: {bloom_mb - ribbon_mb:.2f} MB ({0.27*100:.1f}%)")

if __name__ == "__main__":
    n = 100_000_000 # 100M as per paper
    benchmark_indexing(n)
