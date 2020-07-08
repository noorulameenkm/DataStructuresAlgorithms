class Solution:
    def islandPerimeter(self, grid):
        
        if len(grid) == 0:
            return 0
        
        row, col = len(grid), len(grid[0])
        perimeter = 0
        
        
        for i in range(row):
            for j in range(col):
                
                if grid[i][j] == 1:
                    perimeter += (4 - meterOfLands(grid, i, j, row, col))
        
        return perimeter
    
    
def meterOfLands(grid, i, j, row, col):
    meters = 0
    
    # i+1, j (UP)
    if i > 0 and grid[i  - 1][j]:
        meters += 1
    
    # i, j-1 (LEFT)
    if j > 0 and grid[i][j - 1]:
        meters += 1
    
    # i, j+1 (RIGHT)
    if j < col - 1 and grid[i][j + 1]:
        meters += 1
    
    # i + 1, j (DOWN)
    if i < row - 1 and grid[i + 1][j]:
        meters += 1
        
    return meters


island = [
            [0,1,0,0],
            [1,1,1,0],
            [0,1,0,0],
            [1,1,0,0]
        ]
print(f'Island perimeter for {island} is {Solution().islandPerimeter(island)}')
    
        