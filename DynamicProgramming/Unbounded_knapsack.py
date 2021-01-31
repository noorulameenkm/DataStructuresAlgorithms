
"""
Time Complexity - O(2 ^ (N + C))
Space Complexity - O(N + C)
"""

def solve_unbound_knapsack(profits, weights, capacity):
    return solve_unbound_knapsack_recursive(profits, weights, capacity, 0)



def solve_unbound_knapsack_recursive(profits, weights, capacity, index):
    if index >= len(profits) or capacity <= 0 or len(profits) == 0 or len(weights) != len(profits):
        return 0


    profit_1 = 0

    if weights[index] <= capacity:
        profit_1 = profits[index] + solve_unbound_knapsack_recursive(profits, weights, capacity - weights[index], index)
    
    profit_2 = solve_unbound_knapsack_recursive(profits, weights, capacity, index + 1)

    return max(profit_1,profit_2)



"""
Time Complexity - O(N * C)
Space Complexity - O(N * C + N)
"""
def solve_unbound_knapsack_memoization(profits, weights, capacity):
    dp = [[-1 for i in range(capacity + 1)] for _ in range(len(profits))]
    return solve_unbound_knapsack_memoization_recursive(dp, profits, weights, capacity, 0)


def solve_unbound_knapsack_memoization_recursive(dp, profits, weights, capacity, index):
    if index >= len(profits) or capacity <= 0 or len(profits) == 0 or len(weights) != len(profits):
        return 0

    if dp[index][capacity] != -1:
        return dp[index][capacity]

    profit_1 = 0

    if weights[index] <= capacity:
        profit_1 = profits[index] + solve_unbound_knapsack_recursive(profits, weights, capacity - weights[index], index)
    
    profit_2 = solve_unbound_knapsack_recursive(profits, weights, capacity, index + 1)

    dp[index][capacity] = max(profit_1,profit_2)
    return dp[index][capacity]


"""
Time Complexity - O(N * C)
Space Complexity - O(N * C)
"""
def solve_unbound_knapsack_tabulation(profits, weights, capacity):
    if len(profits) != len(weights) or capacity <= 0 or len(profits) == 0:
        return 0

    dp = [[0 for _ in range(capacity + 1)] for _ in range(len(profits))]


    for i in range(len(profits)):
        for c in range(1, capacity + 1):
            profit_1, profit_2 = 0, 0
            if weights[i] <= c:
                profit_1 = profits[i] + dp[i][c - weights[i]]
            
            if i > 0:
                profit_2 = dp[i - 1][c]

            dp[i][c] = max(profit_1, profit_2)

    return dp[len(profits) - 1][capacity]

    


def main():
    # Approach 1
    print(solve_unbound_knapsack([15, 50, 60, 90], [1, 3, 4, 5], 8))
    print(solve_unbound_knapsack([15, 50, 60, 90], [1, 3, 4, 5], 6))

    # Approach2 
    print(solve_unbound_knapsack_memoization([15, 50, 60, 90], [1, 3, 4, 5], 8))
    print(solve_unbound_knapsack_memoization([15, 50, 60, 90], [1, 3, 4, 5], 6))

    # Approach2 
    print(solve_unbound_knapsack_tabulation([15, 50, 60, 90], [1, 3, 4, 5], 8))
    print(solve_unbound_knapsack_tabulation([15, 50, 60, 90], [1, 3, 4, 5], 6))


main()