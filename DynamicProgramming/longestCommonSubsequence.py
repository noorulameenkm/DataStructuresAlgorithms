def longestCommonSubsequence(s1, s2):
    return longestCommonSubsequenceRecursive(s1, s2, 0, 0)


def longestCommonSubsequenceRecursive(s1, s2, l1, l2):
    if l1 == len(s1) or l2 == len(s2):
        return 0
    
    if s1[l1] == s2[l2]:
        return 1 + longestCommonSubsequenceRecursive(s1, s2, l1 + 1, l2 + 1)

    c1 = longestCommonSubsequenceRecursive(s1, s2, l1 + 1, l2)
    c2 = longestCommonSubsequenceRecursive(s1, s2, l1, l2 + 1)

    return max(c1, c2)


def find_LCS_length_memoization(s1, s2):
  dp = [[-1 for _ in range(len(s2))] for _ in range(len(s1))]
  return find_LCS_length_memoization_recursive(dp, s1, s2, 0, 0)


def find_LCS_length_memoization_recursive(dp, s1, s2, i1, i2):
  if i1 == len(s1) or i2 == len(s2):
    return 0

  if dp[i1][i2] == -1:
    if s1[i1] == s2[i2]:
      dp[i1][i2] = 1 + find_LCS_length_memoization_recursive(dp, s1, s2, i1 + 1, i2 + 1)
    else:
      c1 = find_LCS_length_memoization_recursive(dp, s1, s2, i1, i2 + 1)
      c2 = find_LCS_length_memoization_recursive(dp, s1, s2, i1 + 1, i2)
      dp[i1][i2] = max(c1, c2)

  return dp[i1][i2]


def find_LCS_length_tabulation(s1, s2):
  n1, n2 = len(s1), len(s2)
  dp = [[0 for _ in range(n2+1)] for _ in range(n1+1)]
  maxLength = 0
  for i in range(1, n1+1):
    for j in range(1, n2+1):
      if s1[i - 1] == s2[j - 1]:
        dp[i][j] = 1 + dp[i - 1][j - 1]
      else:
        dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

      maxLength = max(maxLength, dp[i][j])
  return maxLength


def main():
    # 1
    print(longestCommonSubsequence("abdca", "cbda"))
    print(longestCommonSubsequence("passport", "ppsspt"))

    # 2
    print(find_LCS_length_memoization("abdca", "cbda"))
    print(find_LCS_length_memoization("passport", "ppsspt"))

    # 3
    print(find_LCS_length_tabulation("abdca", "cbda"))
    print(find_LCS_length_tabulation("passport", "ppsspt"))


main()