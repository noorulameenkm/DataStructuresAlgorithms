"""
Time Complexity - O(3 ^ (M + N))
Space Complexity - O(M + N)
"""
def longestCommonSubString(s1, s2):
    return findLCSLengthRecursive(s1, s2, 0, 0, 0)


def findLCSLengthRecursive(s1, s2, i1, i2, count):
    if i1 == len(s1) or i2 == len(s2):
        return count
    
    if s1[i1] == s2[i2]:
        count = findLCSLengthRecursive(s1, s2, i1 + 1, i2 + 1, count + 1)
    
    c1 = findLCSLengthRecursive(s1, s2, i1 + 1, i2, 0)
    c2 = findLCSLengthRecursive(s1, s2, i1, i2 + 1, 0)

    return max(count, max(c1, c2))

def find_LCS_length_memoization(s1, s2):
  n1, n2 = len(s1), len(s2)
  maxLength = min(n1, n2)
  dp = [[[-1 for _ in range(maxLength)] for _ in range(n2)]
        for _ in range(n1)]
  return find_LCS_length_memoization_recursive(dp, s1, s2, 0, 0, 0)


def find_LCS_length_memoization_recursive(dp, s1, s2, i1, i2, count):
  if i1 == len(s1) or i2 == len(s2):
    return count

  if dp[i1][i2][count] == -1:
    c1 = count
    if s1[i1] == s2[i2]:
      c1 = find_LCS_length_memoization_recursive(
        dp, s1, s2, i1 + 1, i2 + 1, count + 1)
    c2 = find_LCS_length_memoization_recursive(dp, s1, s2, i1, i2 + 1, 0)
    c3 = find_LCS_length_memoization_recursive(dp, s1, s2, i1 + 1, i2, 0)
    dp[i1][i2][count] = max(c1, max(c2, c3))

  return dp[i1][i2][count]


def find_LCS_length(s1, s2):
    n1, n2 = len(s1), len(s2)
    dp = [[0 for _ in range(n2+1)] for _ in range(n1+1)]
    maxLength = 0
    for i in range(1, n1+1):
        for j in range(1, n2+1):
            if s1[i - 1] == s2[j - 1]:
                dp[i][j] = 1 + dp[i - 1][j - 1]
                maxLength = max(maxLength, dp[i][j])

    return maxLength


def find_LCS_length_optimized(s1, s2):
  n1, n2 = len(s1), len(s2)
  dp = [[0 for _ in range(n2+1)] for _ in range(2)]
  maxLength = 0
  for i in range(1, n1+1):
    for j in range(1, n2+1):
      dp[i % 2][j] = 0
      if s1[i - 1] == s2[j - 1]:
        dp[i % 2][j] = 1 + dp[(i - 1) % 2][j - 1]
        maxLength = max(maxLength, dp[i % 2][j])

  return maxLength

def main():
    # 1
    print(longestCommonSubString("abdca", "cbda"))
    print(longestCommonSubString("passport", "ppsspt"))

    # 2
    print(find_LCS_length_memoization("abdca", "cbda"))
    print(find_LCS_length_memoization("passport", "ppsspt"))

    # 3
    print(find_LCS_length("abdca", "cbda"))
    print(find_LCS_length("passport", "ppsspt"))

main()