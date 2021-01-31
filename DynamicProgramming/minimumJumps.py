import math


"""
Time Complexity - O(2 ^ N)
Space Complexity - O(N)
"""
def count_min_jumps(jumps):
  return count_min_jumps_recursive(jumps, 0)


def count_min_jumps_recursive(jumps, currentIndex):
  n = len(jumps)
  # if we have reached the last index, we don't need any more jumps
  if currentIndex == n - 1:
    return 0

  if jumps[currentIndex] == 0:
    return math.inf

  totalJumps = math.inf
  start, end = currentIndex + 1, currentIndex + jumps[currentIndex]
  while start < n and start <= end:
    # jump one step and recurse for the remaining array
    minJumps = count_min_jumps_recursive(jumps, start)
    start += 1
    if minJumps != math.inf:
      totalJumps = min(totalJumps, minJumps + 1)

  return totalJumps


def count_min_jumps_memoization(jumps):
    dp = [0 for i in range(len(jumps))]
    return count_min_jumps_memoization_recursive(dp, jumps, 0)


def count_min_jumps_memoization_recursive(dp, jumps, currentIndex):
    n = len(jumps)
    # if we have reached the last index, we don't need any more jumps
    if currentIndex == n - 1:
        return 0

    if jumps[currentIndex] == 0:
        return math.inf

    if dp[currentIndex] != 0:
        return dp[currentIndex]

    totalJumps = math.inf
    start, end = currentIndex + 1, currentIndex + jumps[currentIndex]
    while start < n and start <= end:
        # jump one step and recurse for the remaining array
        minJumps = count_min_jumps_memoization_recursive(dp, jumps, start)
        start += 1
        if minJumps != math.inf:
            totalJumps = min(totalJumps, minJumps + 1)

    dp[currentIndex] = totalJumps

    return dp[currentIndex]


"""
Time Complexity - o(n ^ 2)
Space Complexity - o(n)
"""
def count_min_jumps_tabulation(jumps):
  n = len(jumps)
  # initialize with infinity, except the first index which should be zero as we
  # start from there
  dp = [math.inf for _ in range(n)]
  dp[0] = 0

  for start in range(n - 1):
    end = start + 1
    while end <= start + jumps[start] and end < n:
      dp[end] = min(dp[end], dp[start] + 1)
      end += 1

  return dp[n - 1]


def main():
    # Approach 1
    print(count_min_jumps([2, 1, 1, 1, 4]))
    print(count_min_jumps([1, 1, 3, 6, 9, 3, 0, 1, 3]))

    # Approach 2
    print(count_min_jumps_memoization([2, 1, 1, 1, 4]))
    print(count_min_jumps_memoization([1, 1, 3, 6, 9, 3, 0, 1, 3]))

    # Approach 3
    print(count_min_jumps_tabulation([2, 1, 1, 1, 4]))
    print(count_min_jumps_tabulation([1, 1, 3, 6, 9, 3, 0, 1, 3]))


main()