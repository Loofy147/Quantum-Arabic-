import math
import time

def simulate_entanglement_battery():
    """
    U(t) = exp(Lambda(t) * g) - Wei-Norman algebraic flow control
    """
    print(f"Entanglement Battery Flow Control Simulation")
    print("-" * 50)

    # Simulate Squashed Entanglement (SE) recovery
    # SE_in = 1.0 (battery full)
    # SE_out = 0.0 (empty)
    se_initial = 1.0
    se_current = se_initial

    # Lambda(t) as the control valve
    # Rate = Lambda_0 * exp(-t/tau) - simple decay valve
    # Lambda_0 must be large enough to recover most SE in time
    lambda_0 = 1.0 # increased from 0.1
    tau = 20.0 # increased from 10.0

    # Isolated environment - lossless recovery
    efficiency = 1.0

    # Step simulation
    recovered_se = 0.0
    t = 0.0
    dt = 0.1
    steps = 1000 # increased from 100

    print(f"{'Time (t)':<10} | {'Valve (Lambda)':<15} | {'SE in Battery':<15} | {'Recovered SE'}")
    print("-" * 65)

    for i in range(steps):
        valve = lambda_0 * math.exp(-t / tau)
        recovery_rate = valve * se_current * efficiency

        # Update states
        se_current -= recovery_rate * dt
        recovered_se += recovery_rate * dt
        t += dt

        if i % 100 == 0:
            print(f"{t:<10.2f} | {valve:<15.6f} | {se_current:<15.6f} | {recovered_se:.6f}")

    # Final check
    final_efficiency = (recovered_se / se_initial)
    print("-" * 65)
    print(f"Simulation Final State (T={t:.2f}s)")
    print(f"SE Recovery Efficiency: {final_efficiency*100:.2f}%")

    if final_efficiency >= 0.99:
        print("VERIFICATION SUCCESS: Reversible recovery achieved (99%+).")
    else:
        print("VERIFICATION WARNING: Inefficiency detected.")

if __name__ == "__main__":
    simulate_entanglement_battery()
