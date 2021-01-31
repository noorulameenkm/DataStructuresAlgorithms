"""
Time Complexity - O(2 ^ N)
Space Complexity - O(N)
"""
def solve_thief(houses):
    n = len(houses)
    if n == 0:
        return 0

    return solve_thief_recursive(houses, 0)


def solve_thief_recursive(houses, index):

    n = len(houses)
    if index >= n:
        return 0

    option_1 = houses[index] + solve_thief_recursive(houses, index + 2)

    option_2 = solve_thief_recursive(houses, index + 1)

    return max(option_1, option_2)



def find_max_steal_memoization(wealth):
  dp = [0 for x in range(len(wealth))]
  return find_max_steal_recursive(dp, wealth, 0)


def find_max_steal_recursive(dp, wealth, currentIndex):
  if currentIndex >= len(wealth):
    return 0

  if dp[currentIndex] == 0:
    # steal from current house and skip one to steal next
    stealCurrent = wealth[currentIndex] + find_max_steal_recursive(dp, wealth, currentIndex + 2)
    # skip current house to steel from the adjacent house
    skipCurrent = find_max_steal_recursive(dp, wealth, currentIndex + 1)

    dp[currentIndex] = max(stealCurrent, skipCurrent)

  return dp[currentIndex]


"""
Time Compexity - O(N)
Space complexity - O(N)
"""
def find_max_steal_tabulation(wealth):
    n = len(wealth)
    if n == 0:
        return 0

    dp = [0 for _ in range(n)]
    dp[0] = wealth[0]
    dp[1] = max(wealth[0], wealth[1])

    for i in range(2, n):
        dp[i] = max(dp[i - 2] + wealth[i], dp[i - 1])

    return dp[-1]


    


def main():
    # First Approach
    print(solve_thief([2, 5, 1, 3, 6, 2, 4]))
    print(solve_thief([2, 10, 14, 8, 1]))

    # Second Approach2
    print(find_max_steal_memoization([2, 5, 1, 3, 6, 2, 4]))
    print(find_max_steal_memoization([2, 10, 14, 8, 1]))

    # Third Approach2
    print(find_max_steal_tabulation([2, 5, 1, 3, 6, 2, 4]))
    print(find_max_steal_tabulation([2, 10, 14, 8, 1]))


main()
