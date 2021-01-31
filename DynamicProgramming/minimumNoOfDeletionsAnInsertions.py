def find_MDI(s1, s2):
  c1 = find_LCS_length(s1, s2)
  print("Minimum deletions needed: " + str(len(s1) - c1))
  print("Minimum insertions needed: " + str(len(s2) - c1))

"""
Time Complexity - O(m * n)
"""
def find_LCS_length(s1,  s2):
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
  find_MDI("abc", "fbc")
  find_MDI("abdca", "cbda")
  find_MDI("passport", "ppsspt")


main()