"""
 Problem Link:- https://leetcode.com/problems/swim-in-rising-water/
"""


class Solution:
    def swimInWater(self, grid):
        
        def is_possible(grid_, visited_, i_, j_, N_, val_):
            if i_ < 0 or i_ >= N_ or j_ < 0 or j_ >= N:
                return False
            
            if visited_[i_][j_]:
                return False
            
            if grid_[i_][j_] > val_:
                return False
            
            return True
            
            
        
        def can_swim_with_val(grid_, visited_, i, j, N_, val_):
            visited[i][j] = True
            
            if i == N_ - 1 and j == N_ - 1:
                return True
            
            left = right = top = bottom = False
            
            if is_possible(grid_, visited_, i, j - 1, N_, val_):
                left = can_swim_with_val(grid_, visited_, i, j - 1, N_, val_)
            
            if is_possible(grid_, visited_, i, j + 1, N_, val_):
                right = can_swim_with_val(grid_, visited_, i, j + 1, N_, val_)
            
            if is_possible(grid_, visited_, i - 1, j, N_, val_):
                top = can_swim_with_val(grid_, visited_, i - 1, j, N_, val_)
            
            if is_possible(grid_, visited_, i + 1, j, N_, val_):
                bottom = can_swim_with_val(grid_, visited_, i + 1, j, N_, val_)
            
            return left or right or top or bottom
        
        
        
        N = len(grid)
        low = high = grid[0][0]
        for i in range(N):
            high = max(high, max(grid[i]))
        ans = -1
        
        while low <= high:
            
            mid = low + (high - low) // 2
            visited = [[False for _ in range(N)] for _ in range(N)]
            if grid[0][0] <= mid and can_swim_with_val(grid, visited, 0, 0, N, mid):
                ans = mid
                high = mid - 1
            else:
                low = mid + 1
        
        return ans




print(Solution().swimInWater(grid = [[0,2],[1,3]]))
print(Solution().swimInWater(grid = [[0,1,2,3,4],[24,23,22,21,5],[12,13,14,15,16],[11,17,18,19,20],[10,9,8,7,6]]))
  