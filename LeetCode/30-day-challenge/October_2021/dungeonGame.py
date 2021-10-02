from functools import lru_cache
from typing import List
from math import inf


"""
problem Link:- https://leetcode.com/problems/dungeon-game/
"""


class Solution:
    def calculateMinimumHP(self, dungeon: List[List[int]]) -> int:
        m, n = len(dungeon), len(dungeon[0])

        @lru_cache(None)
        def dfs(x, y):
            if x >= m or y >= n:
                return inf

            if (x, y) == (m - 1, n - 1):
                req = -dungeon[x][y] + 1
                if req <= 0:
                    req = 1

                return req

            req = min(dfs(x + 1, y), dfs(x, y + 1))
            req -= dungeon[x][y]

            return 1 if req <= 0 else req

        return dfs(0, 0)


class Solution2:
    def calculateMinimumHP(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])

        m, n = len(grid), len(grid[0])

        dp = [[inf] * (n + 1) for _ in range(m + 1)]
        dp[m][n - 1] = dp[m - 1][n] = 1

        for x in reversed(range(m)):
            for y in reversed(range(n)):
                dp[x][y] = min(dp[x + 1][y], dp[x][y + 1])
                dp[x][y] -= grid[x][y]
                dp[x][y] = 1 if dp[x][y] <= 0 else dp[x][y]

        return dp[0][0]


print(Solution().calculateMinimumHP([[-2, -3, 3], [-5, -10, 1], [10, 30, -5]]))
print(Solution().calculateMinimumHP([[0]]))
print(Solution2().calculateMinimumHP([[-2, -3, 3], [-5, -10, 1], [10, 30, -5]]))
print(Solution2().calculateMinimumHP([[0]]))
