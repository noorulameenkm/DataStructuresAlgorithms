"""
    Problem Link:- https://leetcode.com/problems/largest-plus-sign/
"""


class Solution:
    def orderOfLargestPlusSign(self, n, mines):

        grid = [[1 for _ in range(n)] for _ in range(n)]
        for i, j in mines:
            grid[i][j] = 0

        # left to right
        for i in range(n):
            value = 1
            for j in range(n):
                if grid[i][j] == 0:
                    value = 1
                    continue

                grid[i][j] = value
                value += 1

        # right to left
        for i in range(n):
            value = 1
            for j in range(n - 1, -1, -1):
                if grid[i][j] == 0:
                    value = 1
                    continue

                grid[i][j] = min(value, grid[i][j])
                value += 1

        # top to bottom
        for i in range(n):
            value = 1
            for j in range(n):
                if grid[j][i] == 0:
                    value = 1
                    continue

                grid[j][i] = min(value, grid[j][i])
                value += 1

        ans = 0
        # bottom to top
        for i in range(n):
            value = 1
            for j in range(n - 1, -1, -1):
                if grid[j][i] == 0:
                    value = 1
                    continue

                grid[j][i] = min(value, grid[j][i])
                ans = max(ans, grid[j][i])
                value += 1

        return ans


print(Solution().orderOfLargestPlusSign(n=5, mines=[[4, 2]]))
print(Solution().orderOfLargestPlusSign(n=1, mines=[[0, 0]]))
