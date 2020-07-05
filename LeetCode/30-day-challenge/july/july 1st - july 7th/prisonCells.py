class Solution:
    def prisonAfterNDays(self, cells, N):
        dp = [[0 for i in range(8)] for j in range(15)]

        dp[0] = cells

        for i in range(1, 15):
            for j in range(1, 7):
                dp[i][j] = 1 if dp[i - 1][j - 1] == dp[i - 1][j + 1] else 0
                
        
        offset = 14 if N % 14 == 0 else N % 14

        return dp[offset]



print(f'Solution for [0,1,0,1,1,0,0,1] is {Solution().prisonAfterNDays([0,1,0,1,1,0,0,1], 7)}')
print(f'Solution for [1,0,0,1,0,0,1,0] is {Solution().prisonAfterNDays([0,1,0,1,1,0,0,1], 1000000000)}')

        