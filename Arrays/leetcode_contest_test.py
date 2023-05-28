class Solution:
    def numberOfPaths(self, grid, k):
        
        m, n = len(grid), len(grid[0])
        def traverse(i, j, sum_):
            if i >= m or i < 0 or j >= n or j < 0:
                return
            
            if i == m - 1 and j == n - 1:
                if (sum_ + grid[i][j]) % k == 0:
                    self.count += 1
                
                return
            
            traverse(i + 1, j, sum_ + grid[i][j])
            traverse(i, j + 1, sum_ + grid[i][j])
        
        self.count = 0
        traverse(0, 0, 0)
        
        return self.count % (1000000000 + 7)



print(Solution().numberOfPaths(grid = [[5,2,4],[3,0,5],[0,7,2]], k = 3))