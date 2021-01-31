"""
Time Complexity - O(2 ^ (C + T))
Space Complexity - O(C + T)
"""

def solve_count_change(denominations, total):
    return count_change_recursive(denominations, total, 0)


def count_change_recursive(denominations, total, index):
    if total == 0:
        return 1
    
    n = len(denominations)

    if n == 0 or index >= n:
        return 0
    
    sum_1, sum_2 = 0, 0

    if denominations[index] <= total:
        sum_1 = count_change_recursive(denominations, total - denominations[index], index)
    
    sum_2 = count_change_recursive(denominations,total, index + 1)

    return sum_1 + sum_2


"""
Time Complexity - O(C * T)
Space Complexity - O(C * T + C)
"""

def solve_count_change_memoization(denominations, total):
    dp = [[-1 for i in range(total + 1)] for j in range(len(denominations))]
    return count_change_memoization_recursive(dp, denominations, total, 0)


def count_change_memoization_recursive(dp, denominations, total, index):
    if total == 0:
        return 1

    n = len(denominations)
    if index >= n or n == 0:
        return 0

    if dp[index][total] == -1:
        sum_1, sum_2 = 0, 0

        if denominations[index] <= total:
            sum_1 = count_change_memoization_recursive(dp, denominations, total - denominations[index], index)

        sum_2 = count_change_memoization_recursive(dp, denominations, total, index + 1)

        dp[index][total] = sum_1 + sum_2
    
    return dp[index][total]


"""
Time Complexity - O(C * T)
Space Complexity - O(C * t)
"""
def solve_count_change_tabulation(denominations, total):
    dp = [[0 for i in range(total + 1)] for j in range(len(denominations))]

    if total == 0:
        return 1

    n = len(denominations)

    if n == 0:
        return 0

    for i in range(n):
        dp[i][0] = 1
    
    for i in range(n):
        for j in range(1, total + 1):
            sum_1, sum_2 = 0, 0
            if denominations[i] <= j:
                sum_1 = dp[i][j - denominations[i]]
            
            if i > 0:
                sum_2 = dp[i - 1][j]

            dp[i][j] = sum_1 + sum_2
        
    return dp[n - 1][total]
        

def main():
    # Approach 1
    print(solve_count_change([1, 2, 3], 5))

    # Approach 2
    print(solve_count_change_memoization([1, 2, 3], 5))

    # Approach 3
    print(solve_count_change_tabulation([1, 2, 3], 5))


main()