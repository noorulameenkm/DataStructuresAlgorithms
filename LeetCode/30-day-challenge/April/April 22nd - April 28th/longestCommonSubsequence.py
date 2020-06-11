class Solution:
    def longestCommonSubsequence(self, text1, text2):
        m , n = len(text1), len(text2)
        dp = [[0 for i in range(n+1)] for j in range(m+1)]
        for l in range(1, m+1):
            for t in range(1, n+1):
                if text1[l - 1] == text2[t - 1]:
                    dp[l][t] = 1 + dp[l - 1][t - 1]
                else:
                    dp[l][t] = max(dp[l - 1][t], dp[l][t - 1])
                    
        return dp[m][n]


print(f'Solution for abcde and ace is {Solution().longestCommonSubsequence("abcde", "ace")}')
        