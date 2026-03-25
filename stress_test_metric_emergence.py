import math
import time

def stress_test_metric_emergence(grid_size=200):
    """
    Computes g^uv = alpha * d^2S / d_xi_u d_xi_v at high resolution.
    Focuses on the "Near-Field" region (r < sigma) to verify linear emergent gravity scaling.
    """
    start_time = time.time()
    step = 0.05 # Higher resolution
    sigma_sq = 10.0
    sigma = math.sqrt(sigma_sq)
    grid = []

    # Pre-calculate S values
    for i in range(grid_size):
        x = (i - grid_size//2) * step
        row = []
        for j in range(grid_size):
            y = (j - grid_size//2) * step
            s = -math.exp(-(x**2 + y**2) / (2 * sigma_sq))
            row.append(s)
        grid.append(row)

    # Compute Hessian components via finite differences
    results = []
    h = step
    for i in range(1, grid_size - 1):
        for j in range(1, grid_size - 1):
            x = (i - grid_size//2) * step
            y = (j - grid_size//2) * step
            r = math.sqrt(x**2 + y**2)

            # Focus on Near-Field region for linear emergent gravity verification
            if r < sigma:
                s_center = grid[i][j]
                s_left = grid[i-1][j]
                s_right = grid[i+1][j]
                s_up = grid[i][j+1]
                s_down = grid[i][j-1]

                g_xx = (s_right - 2*s_center + s_left) / (h**2)
                g_yy = (s_up - 2*s_center + s_down) / (h**2)

                delta_r = g_xx + g_yy
                delta_t = abs(s_center)
                results.append((delta_r, delta_t))

    # Calculate Pearson Correlation Coefficient R
    n = len(results)
    if n < 2: return {"points": 0, "correlation_r2": 0}

    sum_r = sum(r for r, t in results)
    sum_t = sum(t for r, t in results)
    sum_rt = sum(r*t for r, t in results)
    sum_r2 = sum(r**2 for r, t in results)
    sum_t2 = sum(t**2 for r, t in results)

    numerator = n * sum_rt - sum_r * sum_t
    denominator = math.sqrt((n * sum_r2 - sum_r**2) * (n * sum_t2 - sum_t**2))
    correlation = numerator / denominator

    end_time = time.time()

    return {
        "grid_size": grid_size,
        "points": n,
        "correlation_r2": correlation**2,
        "execution_time": end_time - start_time
    }

if __name__ == "__main__":
    res = stress_test_metric_emergence()
    print(f"Grid Size: {res['grid_size']}x{res['grid_size']}")
    print(f"Near-Field Points: {res['points']}")
    print(f"R^2: {res['correlation_r2']:.4f}")
    print(f"Execution Time: {res['execution_time']:.4f}s")
