
"""
    Time Complexity - O(m * n)
    Space Complexity - O(1)
"""
def optimal_path(grid):
    m, n = len(grid) - 1, len(grid[0]) - 1

    for i in range(m + 1):
        for j in range(n + 1):

            if i > 0 and j > 0:
                grid[i][j] = grid[i][j] + min(grid[i - 1][j], grid[i][j - 1])
            elif i > 0 or j > 0:
                if i > 0:
                    grid[i][j] += grid[i - 1][j]
                else:
                    grid[i][j] += grid[i][j - 1]
    
    return grid[m][n]


# Driver code
grid =[[5,1,9,11],[11,4,8,10],[13,3,6,7],[5,14,12,4]]

print(optimal_path(grid)) 
