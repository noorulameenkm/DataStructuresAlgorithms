import math


"""
Time Complexity - O(2 ^ (C + T))
Space Complexity - O(C + T)
"""
def solve_minimum_no_of_coins(denominations, amount):
    result = solve_minimum_no_of_coins_recursive(denominations, amount, 0)
    return -1 if result == math.inf else result



def solve_minimum_no_of_coins_recursive(denominations, amount, index):
    if amount == 0:
        return 0
    
    n = len(denominations)

    if index >= n or n == 0:
        return math.inf
    
    count_1 = math.inf

    if denominations[index] <= amount:
        res = solve_minimum_no_of_coins_recursive(denominations, amount - denominations[index], index)
        if res != math.inf:
            count_1 = res + 1
    
    count_2 = solve_minimum_no_of_coins_recursive(denominations, amount, index + 1)

    return min(count_1, count_2)



"""
Time Complexity - O(C * T)
Space Complexity - O(C * T + C)
"""
def solve_minimum_coins_memoization(denominations, total):
    if total == 0:
        return 0
    
    if len(denominations) == 0:
        return 0

    dp = [[-1 for _ in range(total + 1)] for _ in range(len(denominations))]

    result = solve_minimum_coins_memoization_recursive(dp, denominations, total, 0)
    return -1 if result == math.inf else result


def solve_minimum_coins_memoization_recursive(dp, denominations, total, index):
    if total == 0:
        return 0
    
    if index >= len(denominations) or len(denominations) == 0:
        return math.inf
    
    if dp[index][total] == -1:
        count_1 = math.inf

        if denominations[index] <= total:
            res = solve_minimum_coins_memoization_recursive(dp, denominations, total - denominations[index], index)
            if res != math.inf:
                count_1 = res + 1

        count_2 = solve_minimum_coins_memoization_recursive(dp, denominations, total, index + 1)

        dp[index][total] = min(count_1,count_2)

    return dp[index][total]

        

"""
Time Complexity - O(C * T)
Space Complexity - O(C * T)
"""
def solve_minimum_coins_tabulations(denominations, total):
    if total == 0:
        return 0
    
    if len(denominations) == 0:
        return math.inf

    dp = [[math.inf for i in range(total + 1)] for j in range(len(denominations))]

    for i in range(len(denominations)):
        dp[i][0] = 0

    for i in range(len(denominations)):
        for j in range(1, total + 1):
            if i > 0:
                dp[i][j] = dp[i - 1][j]
            
            if denominations[i] <= j:
                if dp[i][j - denominations[i]] != math.inf:
                    dp[i][j] = min(dp[i][j], dp[i][j - denominations[i]] + 1)

    return -1 if dp[len(denominations) - 1][total] == math.inf else dp[len(denominations) - 1][total]



def main():
    # Approach 1
    print(solve_minimum_no_of_coins([1, 2, 3], 5))
    print(solve_minimum_no_of_coins([1, 2, 3], 11))
    print(solve_minimum_no_of_coins([1, 2, 3], 7))
    print(solve_minimum_no_of_coins([3, 5], 7))

    # Approach 2
    print(solve_minimum_coins_memoization([1, 2, 3], 5))
    print(solve_minimum_coins_memoization([1, 2, 3], 11))
    print(solve_minimum_coins_memoization([1, 2, 3], 7))
    print(solve_minimum_coins_memoization([3, 5], 7))

    # Approach 3
    print(solve_minimum_coins_tabulations([1, 2, 3], 5))
    print(solve_minimum_coins_tabulations([1, 2, 3], 11))
    print(solve_minimum_coins_tabulations([1, 2, 3], 7))
    print(solve_minimum_coins_tabulations([3, 5], 7))



main()

    


    