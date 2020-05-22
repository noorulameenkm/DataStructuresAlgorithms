class MinimumPathSum:
    def findMinPathSum(self, grid):
        if len(grid) == 0:
            return 0
        
        m = len(grid)
        n = len(grid[0])
        dp = [[0 for i in range(n)] for j in range(m)]

        #set 00 value of dp table be equal to the 00 value of grid
        dp[0][0] = grid[0][0]

        # Managing first row
        for i in range(1, n):
            dp[0][i] = grid[0][i] + dp[0][i - 1]
        
        # Managing first col
        for j in range(1, m):
            dp[j][0] = grid[j][0] + dp[j - 1][0]
        
        # Managing rest of the rows and col
        for i in range(1, m):
            for j in range(1, n):
                dp[i][j] = grid[i][j] + min(dp[i - 1][j], dp[i][j - 1])
        

        return dp[m - 1][n - 1]


grid = [
  [1,3,1],
  [1,5,1],
  [4,2,1]
]
print(f'Answer is {MinimumPathSum().findMinPathSum(grid)}')