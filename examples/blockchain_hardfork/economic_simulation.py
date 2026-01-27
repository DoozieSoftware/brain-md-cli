import numpy as np
import matplotlib.pyplot as plt

def simulate_miner_capitulation(hashrate_drop_percent, price_impact):
    """
    Simulates the probability of chain death spiral given a hashrate drop.
    """
    initial_security_budget = 1000000  # USD/hour

    new_budget = initial_security_budget * (1 - hashrate_drop_percent) * (1 - price_impact)

    attack_cost_1h = new_budget * 0.51

    print(f"New Attack Cost (1h): ${attack_cost_1h:,.2f}")

    if attack_cost_1h < 50000:
        return "CRITICAL: Chain is insecure"
    else:
        return "WARNING: Monitoring required"

if __name__ == "__main__":
    # Scenario: 40% hashrate leaves, 20% price drop
    result = simulate_miner_capitulation(0.40, 0.20)
    print(result)
