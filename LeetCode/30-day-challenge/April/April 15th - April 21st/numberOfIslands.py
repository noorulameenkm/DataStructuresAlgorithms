class Solution:
    def numIslands(self, grid):
        if len(grid) == 0:
            return 0
        m = len(grid)
        n = len(grid[0])
        islands = 0
        visited = [[False for i in range(n)] for j in range(m)]
        for i in range(m):
            for j in range(n):
                if grid[i][j] == '1' and not visited[i][j]:
                    islands = islands + 1
                    self.visitIsland(m,n,i,j,grid,visited)
        return islands
        
        
    def visitIsland(self, row, col, i, j, grid, visited):
        if i >= 0 and i < row and j >= 0 and j < col and grid[i][j] == '1' and not visited[i][j]:
            visited[i][j] = True
            self.visitIsland(row,col,i+1,j,grid,visited)
            self.visitIsland(row,col,i-1,j, grid, visited)
            self.visitIsland(row,col,i,j+1, grid, visited)
            self.visitIsland(row,col,i,j-1, grid, visited)


arr = [
        ['1','1','1','1', '0'],
        ['1','1','0','1','0'],
        ['1','1','0','0','0'],
        ['0','0','0','0','0']
    ]
print(f"Result is {Solution().numIslands(arr)}")
            