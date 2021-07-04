"""
    Problem Link:- https://leetcode.com/problems/max-sum-of-rectangle-no-larger-than-k/submissions/
"""


from math import inf
from bisect import bisect_left, insort
from typing import List

class Solution:
    def maxSumSubmatrix(self, matrix: List[List[int]], k: int) -> int:
        m = len(matrix)
        n = len(matrix[0])
        M = max(m, n)
        N = min(m, n)
        ans = -inf
        for a in range(N):
            sums = [0] * M
            for b in range(a, N):
                list_, num = [], 0
                for c in range(M):
                    sums[c] += matrix[c][b] if m > n else matrix[b][c]
                    num += sums[c]
                    if num <= k:
                        ans = max(ans, num)
                    d = bisect_left(list_, num - k)
                    if d != len(list_):
                        ans = max(ans, num - list_[d])
                    
                    insort(list_, num)
        return ans or 0
                    


print(Solution().maxSumSubmatrix(matrix = [[1,0,1],[0,-2,3]], k = 2))
print(Solution().maxSumSubmatrix(matrix = [[2,2,-1]], k = 3))