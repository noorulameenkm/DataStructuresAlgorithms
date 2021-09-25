from queue import Queue
from typing import List


"""
Problem Link:- https://leetcode.com/problems/shortest-path-in-a-grid-with-obstacles-elimination
"""


class Solution:
    def shortestPath(self, grid: List[List[int]], k: int) -> int:
        m, n = len(grid), len(grid[0])
        queue = Queue()
        queue.put((0, 0, 0, k))
        visited = set()
        while not queue.empty():
            x, y, count, k = queue.get()

            if (x, y, k) in visited:
                continue

            visited.add((x, y, k))
            if (x, y) == (m - 1, n - 1):
                return count

            for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                nx, ny = dx + x, dy + y

                if not grid[x][y]:
                    if nx >= 0 and nx < m and ny >= 0 and ny < n:
                        queue.put((nx, ny, count + 1, k))
                elif k:
                    if nx >= 0 and nx < m and ny >= 0 and ny < n:
                        queue.put((nx, ny, count + 1, k - 1))
        return -1


print(Solution().shortestPath(
    [
        [0, 0, 0],
        [1, 1, 0],
        [0, 0, 0],
        [0, 1, 1],
        [0, 0, 0]
    ],
    1
))
print(Solution().shortestPath(
    [
        [0, 1, 1],
        [1, 1, 1],
        [1, 0, 0]
    ],
    1
))
