import math

def simulate_hessian():
    """
    Computes g^uv = alpha * d^2S / d_xi_u d_xi_v
    S(x,y) = -exp(-(x^2+y^2)/2)  - Simple Gaussian 'Entropy Well'
    """
    size = 10
    step = 0.5
    grid = []
    for i in range(size):
        x = (i - size//2) * step
        row = []
        for j in range(size):
            y = (j - size//2) * step
            # Entanglement entropy field (S)
            s = -math.exp(-(x**2 + y**2) / 2)
            row.append({'x': x, 'y': y, 's': s})
        grid.append(row)

    # Compute Hessian components via finite differences
    # g_xx = (S(x+h) - 2S(x) + S(x-h)) / h^2
    # R_sim (Simulated Curvature) proportional to trace(g) or det(g)
    results = []
    h = step
    for i in range(1, size - 1):
        for j in range(1, size - 1):
            s_center = grid[i][j]['s']
            s_left = grid[i-1][j]['s']
            s_right = grid[i+1][j]['s']
            s_up = grid[i][j+1]['s']
            s_down = grid[i][j-1]['s']

            g_xx = (s_right - 2*s_center + s_left) / (h**2)
            g_yy = (s_up - 2*s_center + s_down) / (h**2)

            # Curvature Delta R approximated as Laplacian of S (Trace of Hessian)
            delta_r = g_xx + g_yy

            # Stress energy T proportional to mass density (the source of S)
            # In our simple model, T is the absolute value of the Gaussian depth
            delta_t = abs(s_center)

            results.append((delta_r, delta_t))

    # Calculate Pearson Correlation Coefficient R
    n = len(results)
    sum_r = sum(r for r, t in results)
    sum_t = sum(t for r, t in results)
    sum_rt = sum(r*t for r, t in results)
    sum_r2 = sum(r**2 for r, t in results)
    sum_t2 = sum(t**2 for r, t in results)

    numerator = n * sum_rt - sum_r * sum_t
    denominator = math.sqrt((n * sum_r2 - sum_r**2) * (n * sum_t2 - sum_t**2))

    correlation = numerator / denominator

    print(f"Metric Emergence Simulation Results")
    print("-" * 40)
    print(f"Data Points: {n}")
    print(f"Mean Delta R: {sum_r/n:.4f}")
    print(f"Mean Delta T: {sum_t/n:.4f}")
    print(f"Correlation (R): {correlation:.4f}")
    print(f"Correlation (R^2): {correlation**2:.4f}")

    if correlation**2 >= 0.90:
        print("VERIFICATION SUCCESS: R^2 matches whitepaper target (~0.95)")
    else:
        print("VERIFICATION WARNING: R^2 lower than expected.")

if __name__ == "__main__":
    simulate_hessian()
