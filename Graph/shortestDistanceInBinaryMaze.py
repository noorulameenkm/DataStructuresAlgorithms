from typing import List
from heapq import *
from math import inf

class Solution:
    
    def shortestPath(self, grid: List[List[int]], source: List[int], destination: List[int]) -> int:
        
        # code here
        rows, cols = len(grid), len(grid[0])
        distance = [[inf for _ in range(cols)] for _ in range(rows)]
        data = [[]]
        min_heap = []
        heappush(min_heap, (0, source[0], source[1]))
        distance[source[0]][source[1]] = 0
        
        paths = lambda r, c: [(r - 1, c), (r, c - 1), (r, c + 1), (r + 1, c)]
            
        while min_heap:
            dist, row, col = heappop(min_heap)
            
            for new_row, new_col in paths(row, col):
                if new_row >= 0 and new_row < rows and new_col >= 0 and new_col < cols \
                    and grid[new_row][new_col] == 1 and dist + 1 < distance[new_row][new_col]:
                        distance[new_row][new_col] = dist + 1
                        heappush(min_heap, (distance[new_row][new_col], new_row, new_col))
            
        return -1 if distance[destination[0]][destination[1]] == inf else distance[destination[0]][destination[1]]
    

class SolutionWithQueue:
    
    def shortestPath(self, grid: List[List[int]], source: List[int], destination: List[int]) -> int:
        
        # code here
        rows, cols = len(grid), len(grid[0])
        distance = [[inf for _ in range(cols)] for _ in range(rows)]
        queue = []
        queue.append((0, source[0], source[1]))
        distance[source[0]][source[1]] = 0
        
        paths = lambda r, c: [(r - 1, c), (r, c - 1), (r, c + 1), (r + 1, c)]
            
        while queue:
            dist, row, col = queue.pop(0)
            
            for new_row, new_col in paths(row, col):
                if new_row >= 0 and new_row < rows and new_col >= 0 and new_col < cols \
                    and grid[new_row][new_col] == 1 and dist + 1 < distance[new_row][new_col]:
                        distance[new_row][new_col] = dist + 1
                        queue.append((distance[new_row][new_col], new_row, new_col))
            
        return -1 if distance[destination[0]][destination[1]] == inf else distance[destination[0]][destination[1]]
    

if __name__ == "__main__":
    grid = [[1, 1, 1, 1],
            [1, 1, 0, 1],
            [1, 1, 1, 1],
            [1, 1, 0, 0],
            [1, 0, 0, 1]]
    source = [0, 1]
    destination = [2, 2]
    print(Solution().shortestPath(grid, source, destination))
    print(SolutionWithQueue().shortestPath(grid, source, destination))