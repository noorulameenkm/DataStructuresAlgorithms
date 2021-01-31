import math


"""
Time Complexity - O(2 ^ (N + T))
Space Complexity - O(N + T)
"""
def solve_ribbon_cut(lengths, total):
    result = solve_ribbon_cut_recursive(lengths, total, 0)
    return -1 if result == -math.inf else result

def solve_ribbon_cut_recursive(lengths, total, index):
    if total == 0:
        return 0

    n = len(lengths)
    if index >= n or n == 0:
        return -math.inf
    
    c1 = -math.inf
    if lengths[index] <= total:
        result = solve_ribbon_cut_recursive(lengths, total - lengths[index], index)
        if result != -math.inf:
            c1 = 1 + result
        
    c2 = solve_ribbon_cut_recursive(lengths, total, index + 1)

    return max(c1, c2)



"""
Time Complexity - O(N * T)
Space Compexity - o(N * T + T)
"""
def solve_ribbon_cut_memoization(lengths, total):
    if total == 0:
        return 0
    
    if len(lengths) == 0:
        return -math.inf
    
    dp = [[-1 for i in range(total + 1)] for j in range(len(lengths))]

    result = solve_ribbon_cut_memoization_recursive(dp, lengths, total, 0)

    return -1 if result == -math.inf else result
    


def solve_ribbon_cut_memoization_recursive(dp, lengths, total, index):
    if total == 0:
        return 0
    
    n = len(lengths)
    if n == 0 or index >= n:
        return -math.inf
    
    if dp[index][total] == -1:

        c1 = -math.inf
        if lengths[index] <= total:
            res = solve_ribbon_cut_memoization_recursive(dp, lengths, total - lengths[index], index)
            if res != -math.inf:
                c1 = 1 + res

        c2 = solve_ribbon_cut_memoization_recursive(dp, lengths, total, index + 1)

        dp[index][total] = max(c1, c2)

    return dp[index][total]



"""
Time Complexity - O(N * T)
Space Compexity - o(N * T + T)
"""
def ribbon_cut_tabulation(lengths, total):
    if total == 0:
        return 0
    
    n = len(lengths)
    if n == 0:
        return -1
    
    dp = [[-math.inf for _ in range(total + 1)] for _ in range(n)]

    for i in range(n):
        dp[i][0] = 0

    for i in range(n):
        for j in range(1, total + 1):

            if i > 0:
                dp[i][j] = dp[i - 1][j]

            if lengths[i] <= j:
                if dp[i][j - lengths[i]] != -math.inf:
                    dp[i][j] = max(dp[i][j], 1 + dp[i][j - lengths[i]])

    return -1 if dp[n - 1][total] == -math.inf else dp[n - 1][total]

def main():
    # Approach 1
    print(solve_ribbon_cut([2, 3, 5], 5))
    print(solve_ribbon_cut([2, 3], 7))
    print(solve_ribbon_cut([3, 5, 7], 13))
    print(solve_ribbon_cut([3, 5], 7))

    # Approach 2
    print(solve_ribbon_cut_memoization([2, 3, 5], 5))
    print(solve_ribbon_cut_memoization([2, 3], 7))
    print(solve_ribbon_cut_memoization([3, 5, 7], 13))
    print(solve_ribbon_cut_memoization([3, 5], 7))

    # Approach 3
    print(ribbon_cut_tabulation([2, 3, 5], 5))
    print(ribbon_cut_tabulation([2, 3], 7))
    print(ribbon_cut_tabulation([3, 5, 7], 13))
    print(ribbon_cut_tabulation([3, 5], 7))

main()