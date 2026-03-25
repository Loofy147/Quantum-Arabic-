import math

def calculate_thales_deficit(x, y):
    """
    h = sqrt(xy) - Thales Altitude (geometric mean of Schmidt coefficients)
    delta = 1 - 2h - Entanglement Deficit
    """
    h = math.sqrt(x * y)
    delta = 1 - 2 * h
    return delta

def simulate_scenarios():
    # Schmidt coefficients probabilities (sum to 1)
    scenarios = [
        ("Maximal Entanglement (x=0.5, y=0.5)", 0.5, 0.5),
        ("Hydrogen Atom (x=0.49, y=0.51)", 0.49, 0.51),
        ("Symmetric mass ratio (eta=0.25)", 0.5, 0.5), # wait h = sqrt(eta). If eta=0.25, h=0.5.
        ("Decoherence (x=0.01, y=0.99)", 0.01, 0.99),
        ("Near-Classical (x=0.0001, y=0.9999)", 0.0001, 0.9999),
    ]

    print(f"{'Scenario':<40} | {'Deficit (delta)':<15} | {'Stability'}")
    print("-" * 75)
    for name, x, y in scenarios:
        delta = calculate_thales_deficit(x, y)
        stability = "STABLE" if delta > 0.00000001 else "UNSTABLE"
        if abs(delta) < 1e-10: stability = "THRESHOLD"
        if delta > 0.95: stability = "PINCH-OFF"
        print(f"{name:<40} | {delta:<15.6f} | {stability}")

if __name__ == "__main__":
    simulate_scenarios()
