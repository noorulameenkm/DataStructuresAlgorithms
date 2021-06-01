class Solution:
    def maxAreaOfIsland(self, grid):
        count, maxCount = [0], 0
        m, n = len(grid), len(grid[0])
        visited = [[False for _ in range(n)] for _ in range(m)]
        
        def search(grid_, visited_, m_, n_, i_, j_, count):
            if i_ >= 0 and i_ < m_ and j_ >= 0 and j_ < n_ and (not visited_[i_][j_]):
                visited_[i_][j_] = True
                
                if grid_[i_][j_] == 0:
                    return 
                
                count[0] += 1
                search(grid_, visited_, m_, n_, i_, j_ + 1, count)
                search(grid_, visited_, m_, n_, i_ + 1, j_, count)
                search(grid_, visited_, m_, n_, i_ - 1, j_, count)
                search(grid_, visited_, m_, n_, i_, j_ - 1, count)
                
        
        for i in range(m):
            for j in range(n):
                if not visited[i][j]:
                    if grid[i][j] == 0:
                        visited[i][j] = True
                    else:
                        search(grid, visited, m, n, i, j, count)
                        maxCount = max(maxCount, count[0])
                        count = [0]
                
                j += 1
            
            i += 1
        
        return maxCount
        
        
        
        

grid = [[0,0,1,0,0,0,0,1,0,0,0,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,1,1,0,1,0,0,0,0,0,0,0,0],[0,1,0,0,1,1,0,0,1,0,1,0,0],[0,1,0,0,1,1,0,0,1,1,1,0,0],[0,0,0,0,0,0,0,0,0,0,1,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,0,0,0,0,0,0,1,1,0,0,0,0]]
print(Solution().maxAreaOfIsland(grid))
grid = [[0,0,0,0,0,0,0,0]]
print(Solution().maxAreaOfIsland(grid))