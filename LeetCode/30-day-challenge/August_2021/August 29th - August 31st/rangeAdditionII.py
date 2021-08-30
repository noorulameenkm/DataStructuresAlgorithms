from math import inf


"""
    Problem Link:- https://leetcode.com/problems/range-addition-ii/
"""


class Solution:
    def maxCount(self, m, n, ops):
        if len(ops) == 0:
            return m * n

        X, Y = inf, inf
        for x, y in ops:
            X = min(X, x)
            Y = min(Y, y)
        return X * Y


print(Solution().maxCount(m=3, n=3, ops=[[2, 2], [3, 3]]))
print(Solution().maxCount(
    m=3, n=3,
    ops=[[2, 2], [3, 3], [3, 3], [3, 3], [2, 2], [3, 3], [3, 3], [3, 3],
         [2, 2], [3, 3], [3, 3], [3, 3]]))
print(Solution().maxCount(m=3, n=3, ops=[]))
