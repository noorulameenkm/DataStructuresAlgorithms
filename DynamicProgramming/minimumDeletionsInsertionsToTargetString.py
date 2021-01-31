def minimum_deletions_to_target_string(string1, string2):
    length_common_subsequence = LCS(string1, string2)
    print("Minimum deletions needed: " + str(len(string1) - length_common_subsequence))
    print("Minimum insertions needed: " + str(len(string2) - length_common_subsequence))



"""
Time Complexity - O(n * m)
Space Complexity - O(n * m)
"""
def LCS(string1, string2):
    n = len(string1)
    m = len(string2)

    dp = [[0 for _ in range(m + 1)] for _ in range(n + 1)]
    maxLength = 0

    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if string1[i - 1] == string2[j - 1]:
                dp[i][j] = 1 + dp[i - 1][j - 1]
            else:
                dp[i][j] = max(dp[i][j - 1], dp[i - 1][j])

            maxLength = max(maxLength, dp[i][j])

    return maxLength




def main():
  minimum_deletions_to_target_string("abc", "fbc")
  minimum_deletions_to_target_string("abdca", "cbda")
  minimum_deletions_to_target_string("passport", "ppsspt")


main()