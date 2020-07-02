class Solution:
    def maxUncrossedLines(self, A, B):
        
        m = len(A)
        n = len(B)
        
        dp = [[0 for i in range(m + 1)] for j in range(n + 1)]
            
        
        for i in range(1, n + 1):
            for j in range(1, m + 1):
                
                if B[i - 1] == A[j - 1]:
                    dp[i][j] = 1 + dp[i - 1][j - 1]
                else:
                    dp[i][j] = max(dp[i][j - 1], dp[i - 1][j])
        
        return dp[n][m]


print(f'Solution for [1,3,7,1,7,5] and [1,9,2,5,1] is {Solution().maxUncrossedLines([1,3,7,1,7,5], [1,9,2,5,1])}')