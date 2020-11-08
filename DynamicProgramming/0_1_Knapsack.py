
"""
Time Complexity - O(2^n) where n is the number of items.
Space complexity - O(n) stack space
"""

# recursive solution------------------------------------
def knapsack_recursive_1(profits, weights, capacity):
    return knapsack_recursive(profits, weights, capacity, 0)



def knapsack_recursive(profits, weights, capacity, index):
    if capacity <= 0 or index >= len(profits):
        return 0
    
    
    total_1 = 0

    if weights[index] <= capacity:
        total_1 = profits[index] + knapsack_recursive(profits, weights, capacity - weights[index], index + 1)

    total_2 = knapsack_recursive(profits, weights, capacity, index + 1)

    return max(total_1, total_2)
#-----------------------------------------------------------------

"""
Time complexity - O(N * C)
Space Complexity - O(N * C)
"""
# Memoization top-down-----------------------------
def knapsack_memoization_1(profits, weights, capacity):
    dp = [[-1 for i in range(capacity + 1)] for j in range(len(profits))]
    return knapsack_memoization(dp, profits, weights, capacity, 0)


def knapsack_memoization(dp, profits, weights, capacity, index):
    if index >= len(profits) or capacity <= 0:
        return 0
    
    # if we have already solved a similar problem, return the result from memory
    if dp[index][capacity] >= 0:
        return dp[index][capacity]

    # recursive call after choosing the element at the currentIndex
    # if the weight of the element at currentIndex exceeds the capacity, we
    # shouldn't process this
    profit_1 = 0
    
    if weights[index] <= capacity:
        profit_1 = profits[index] + knapsack_memoization(dp, profits, weights, capacity - weights[index], index + 1)

    # recursive call after excluding the element at the currentIndex
    profit_2 = knapsack_memoization(dp, profits, weights, capacity, index + 1)


    dp[index][capacity] = max(profit_1, profit_2)

    return dp[index][capacity]
#----------------------------------------------------------------

"""
Time Complexity - O(N * C)
Space Complexity - O(N * C)
"""

# Tabulation solution--------------------------------------------
def knapsack_tabulation(profits, weights, capacity):
    if capacity <= 0:
        return 0

    dp = [[0 for i in range(capacity + 1)] for y in range(len(profits))]

    n = len(profits)

    for c in range(capacity + 1):
        if weights[0] <= c:
            dp[0][c] = profits[0]

    for item in range(1, n):
        for c in range(1, capacity + 1):
            profit_1 = 0

            if weights[item] <= c:
                profit_1 = profits[item] + dp[item - 1][c - weights[item]]
            
            profit_2 = dp[item - 1][c]

            dp[item][c] = max(profit_1, profit_2)

    return dp[n - 1][capacity]

#----------------------------------------------

# Solve knapsack-------------------------------
def solve_knapsack(profits, weights, capacity):
    if capacity <= 0:
        return 0

    dp = [[0 for i in range(capacity + 1)] for y in range(len(profits))]

    n = len(profits)

    for c in range(capacity + 1):
        if weights[0] <= c:
            dp[0][c] = profits[0]

    for item in range(1, n):
        for c in range(1, capacity + 1):
            profit_1 = 0

            if weights[item] <= c:
                profit_1 = profits[item] + dp[item - 1][c - weights[item]]
            
            profit_2 = dp[item - 1][c]

            dp[item][c] = max(profit_1, profit_2)

    print_selected_items(dp, weights, profits, capacity)

    return dp[n - 1][capacity]


def print_selected_items(dp, weights, profits, capacity):
    print("Selected weights are: ", end="")
    n = len(weights)
    totalProfit = dp[n - 1][capacity]
    for i in range(n - 1, 0, -1):
        if totalProfit != dp[i - 1][capacity]:
            print(str(weights[i]) + " ", end=" ")
            capacity -= weights[i]
            totalProfit -= profits[i]

    if capacity > 0:
        print(str(weights[0]) + " ", end=" ")

    print()

#------------------------------------------------

# Space Optimized -------------------------------

"""
Space Complexity - O(2 * C)
"""

def space_optimized_knapsack(profits, weights, capacity):
  if capacity <= 0:
    return 0
  
  dp = [[0 for i in range(capacity + 1)] for j in range(2)]
  
  n = len(profits)

  for c in range(capacity + 1):
    if weights[0] <= c:
      dp[0][c] = profits[0]

  for i in range(1, n):
    for c in range(1, capacity + 1):

      profit1 = 0
      if weights[i] <= c:
        profit1 = profits[i] + dp[(i - 1) % 2][c - weights[i]] # use ( i - 1 ) % 2 instead of i-1
      
      profit2 = dp[(i - 1) % 2][c]

      dp[i % 2][c] = max(profit1, profit2) # use i % 2 instead of i 

  return dp[(n - 1) % 2][c] 
#-------------------------------------------------

# Knapsack space optimized------------------------
"""
Space Complexity - O(C)
"""

def knapsack_space_optimized_2(profits, weights, capacity):
    n = len(profits)

    if capacity <= 0 or n <= 0 or n != len(weights):
        return 0

    dp = [0 for i in range(capacity + 1)]

    for c in range(capacity + 1):
        if weights[0] <= c:
            dp[c] = profits[0]


    for i in range(1, n):
        for c in range(capacity, -1, -1):
            profit1 = profit2 = 0
            if weights[i] <= c:
                profit1 = profits[i] + dp[c - weights[i]]

            profit2 = dp[c]

            dp[c] = max(profit1, profit2)

    return dp[capacity]
#-------------------------------------------------


def main():
    # recursive
    print(knapsack_recursive_1([1, 6, 10, 16], [1, 2, 3, 5], 7))
    print(knapsack_recursive_1([1, 6, 10, 16], [1, 2, 3, 5], 6))
    # memoization
    print(knapsack_memoization_1([1, 6, 10, 16], [1, 2, 3, 5], 7))
    print(knapsack_memoization_1([1, 6, 10, 16], [1, 2, 3, 5], 6))
    # tabulation
    print(knapsack_tabulation([1, 6, 10, 16], [1, 2, 3, 5], 7))
    print(knapsack_tabulation([1, 6, 10, 16], [1, 2, 3, 5], 6))
    # solve knapsack
    # tabulation
    print(solve_knapsack([1, 6, 10, 16], [1, 2, 3, 5], 7))
    print(solve_knapsack([1, 6, 10, 16], [1, 2, 3, 5], 6))
    # space optimized
    print(space_optimized_knapsack([1, 6, 10, 16], [1, 2, 3, 5], 7))
    print(space_optimized_knapsack([1, 6, 10, 16], [1, 2, 3, 5], 6))
    # space complexity optimized 2
    print(knapsack_space_optimized_2([1, 6, 10, 16], [1, 2, 3, 5], 7))
    print(knapsack_space_optimized_2([1, 6, 10, 16], [1, 2, 3, 5], 6))

main()