import math
import time

def stress_test_qec_smoothing(n_tags=1000, suffix_length=10):
    """
    Benchmark recursive smoothing overhead for large-scale QEC selection.
    """
    start_time = time.time()

    # Mock MLE probabilities for large corpus
    # tags = [[7,1,3]], [[5,1,3]], etc.
    tags = [f"[[{i},1,3]]" for i in range(n_tags)]
    test_suffix = "1010101010"[:suffix_length]

    # Simulated MLE data for test_suffix
    # P(tag|suffix) = constant 1/n_tags for simple model
    def get_smoothed_prob(tag_idx, s_len):
        if s_len == 0:
            return 1.0 / n_tags
        # Recursive step with mock MLE = 1/n_tags
        mle = 1.0 / n_tags
        smoothing_lambda = 0.5
        return (1 - smoothing_lambda) * mle + smoothing_lambda * get_smoothed_prob(tag_idx, s_len - 1)

    # Compute smoothed probabilities for all tags
    results = []
    for i in range(n_tags):
        results.append(get_smoothed_prob(i, suffix_length))

    end_time = time.time()

    return {
        "n_tags": n_tags,
        "suffix_length": suffix_length,
        "total_computations": n_tags * suffix_length,
        "execution_time": end_time - start_time
    }

if __name__ == "__main__":
    res = stress_test_qec_smoothing()
    print(f"Number of Tags: {res['n_tags']}")
    print(f"Suffix Length: {res['suffix_length']}")
    print(f"Execution Time: {res['execution_time']:.4f}s")
