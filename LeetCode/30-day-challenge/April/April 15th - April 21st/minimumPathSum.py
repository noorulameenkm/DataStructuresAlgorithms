class Solution:
    def minPathSum(self, grid):
        if len(grid) == 0:
            return 0
        
        m = len(grid)
        n = len(grid[0])
        memory = [[-1 for i in range(n)] for j in range(m)]
        minSum = self.findMinSum(0,0,m,n,grid,memory)
        print(memory)
        return minSum
        
        
    def findMinSum(self,i,j,m,n,grid,memory):
        if i >= 0 and j >= 0 and i < m and j < n:
            if memory[i][j] != -1:
                return memory[i][j]
            else:
                memory[i][j] = grid[i][j] + self.maxNeg(self.findMinSum(i + 1, j, m, n, grid, memory), self.findMinSum(i, j + 1, m, n, grid, memory))
                return memory[i][j]
        else:
            return -1
        
    def maxNeg(self, a, b):
        if a == -1 and b == -1:
            return 0
        if a == -1:
            return b
        if b == -1:
            return a
        
        return min(a,b)
            
        
grid = [
  [1,3,1],
  [1,5,1],
  [4,2,1]
]

print(f'Result is {Solution().minPathSum(grid)}')