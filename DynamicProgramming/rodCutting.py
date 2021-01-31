

"""
Time Complexity - O(2 ^ (N + C))
Space Complexity - O(N + C)
"""
def solve_rod_cutting(lengths, prices, length):
    return solve_rod_cutting_recursive(lengths, prices, length, 0)


def solve_rod_cutting_recursive(lengths, prices, length, index):
    n = len(lengths)

    if index >= n or len(prices) != n or length == 0:
        return 0
    
    price_1, price_2 = 0, 0
    if lengths[index] <= length:
        price_1 = prices[index] + solve_rod_cutting_recursive(lengths, prices, length - lengths[index], index)
    
    price_2 = solve_rod_cutting_recursive(lengths, prices, length, index + 1)

    return max(price_1, price_2)



"""
Time Complexity - O(N * C)
Space Complexity - O(N * C + N)
"""
def solve_rod_cutting_memoization(lengths, prices, length):
    n = len(lengths)
    if len(prices) != n or length == 0:
        return 0

    dp = [[-1 for _ in range(length + 1)] for _ in range(len(prices))]
    return solve_rod_cutting_memoization_recursive(dp, lengths, prices, length, 0)


def solve_rod_cutting_memoization_recursive(dp, lengths, prices, length, index):
    n = len(lengths)
    if index >= n or len(prices) != n or length == 0:
        return 0

    if dp[index][length] == -1:
        price_1, price_2 = 0, 0

        if lengths[index] <= length:
            price_1 = prices[index] + solve_rod_cutting_memoization_recursive(dp, lengths, prices, length - lengths[index], index)

        price_2 = solve_rod_cutting_memoization_recursive(dp, lengths, prices, length, index + 1)
    
        dp[index][length] = max(price_1, price_2)
    
    return dp[index][length]


"""
Time Complexity - O(N * C)
Space Complexity - O(N * C)
"""
def solve_rod_cutting_tabulation(lengths, prices, length):
    n = len(lengths)
    if len(prices) != n or length == 0:
        return 0

    dp = [[0 for _ in range(length + 1)] for _ in range(n)]

    for i in range(n):
        for length_ in range(1, length + 1):
            price_1, price_2 = 0, 0

            if lengths[i] <= length_:
                price_1 = prices[i] + dp[i][length_ - lengths[i]]
            
            if i > 0 :
                price_2 = dp[i - 1][length_]

            dp[i][length_] = max(price_1, price_2)

    return dp[n - 1][length]

def main():
    #Approach_1
    print(solve_rod_cutting([1, 2, 3, 4, 5], [2, 6, 7, 10, 13], 5))

    #Approach_2
    print(solve_rod_cutting_memoization([1, 2, 3, 4, 5], [2, 6, 7, 10, 13], 5))

    #Approach_3
    print(solve_rod_cutting_tabulation([1, 2, 3, 4, 5], [2, 6, 7, 10, 13], 5))

main()
