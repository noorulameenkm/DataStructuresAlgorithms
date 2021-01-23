import sys
import math

def numberOfCoins(coins, amount):
    if amount == 0:
        return 0
    
    res = sys.maxsize
    for i in range(len(coins)):
        if coins[i] <= amount:
            curr = numberOfCoins(coins, amount - coins[i])
            if curr != sys.maxsize and curr + 1 < res:
                res = curr + 1

    return res


def numberOfCoins2(coins, amount):
    if amount == 0:
        return 0
    
    n = len(coins)
    dp = [[0 for _ in range(amount + 1)] for _ in range(n + 1)]

    # Initialising first column of list with 0
    # because a sum of 0 can be made with zero coins:
    for i in range(n + 1):
        dp[i][0] = 0

    for j in range(amount + 1):
        dp[0][j] = math.inf

    for i in range(1, n + 1):
        for j in range(1, amount + 1):
            if coins[i - 1] > j:
                dp[i][j] = dp[i - 1][j]
            else:
                dp[i][j] = min(1 + dp[i][j - coins[i - 1]], dp[i - 1][j])

    return -1 if dp[n][amount] == math.inf else dp[n][amount]

    



def main():
    # First Method
    print(numberOfCoins([1,2,5], 11))
    print(numberOfCoins([2], 3))
    print(numberOfCoins([1,2,3], 11))

    # Second Method
    print(numberOfCoins2([1,2,5], 11))
    print(numberOfCoins2([2], 3))
    print(numberOfCoins2([1,2,3], 11))


main()