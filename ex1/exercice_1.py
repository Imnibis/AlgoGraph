import numpy as np

def parcours(positions):
    positions.sort()
    n = len(positions)
    
    dp = [0] * n
    dp[0] = abs(positions[0])  # Initial waiting time for the first house

    for i in range(1, n):
        dp[i] = dp[i-1] + (positions[i] - positions[i-1]) * (n - i)
    
    return positions, dp

def greedy(positions):
    current_pos = 0
    n = len(positions)
    waiting_times = []
    order = []
    
    while positions:
        # Find the closest house
        closest = min(positions, key=lambda x: abs(x - current_pos))
        positions.remove(closest)
        current_pos = closest
        order.append(closest)
        waiting_times.append(abs(current_pos))
        
    return order, waiting_times

def compare_algorithms():
    positions = np.random.normal(0, 1000, 1000).tolist()
    
    # Dynamic Programming Solution
    dp_positions, dp_waiting_times = parcours(positions.copy())
    dp_avg_waiting_time = sum(dp_waiting_times) / len(dp_waiting_times)
    
    # Greedy Solution
    greedy_positions, greedy_waiting_times = greedy(positions.copy())
    greedy_avg_waiting_time = sum(greedy_waiting_times) / len(greedy_waiting_times)
    
    print("Dynamic Programming:")
    print("Average waiting time:", dp_avg_waiting_time)
    
    print("\nGreedy:")
    print("Average waiting time:", greedy_avg_waiting_time)
    
    print("\nDynamic Programming is better:", dp_avg_waiting_time < greedy_avg_waiting_time)

def main():
    # Run comparison
    compare_algorithms()

if __name__ == "__main__":
    main()
