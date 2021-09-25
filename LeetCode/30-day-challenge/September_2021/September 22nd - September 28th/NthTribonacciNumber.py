"""
    Problem Link:- https://leetcode.com/problems/n-th-tribonacci-number/
"""


class Solution:
    def tribonacci(self, n: int) -> int:
        F = [0] * 38
        F[1] = F[2] = 1
        if n <= 2:
            return F[n]

        for i in range(3, n + 1):
            F[i] = F[i - 1] + F[i - 2] + F[i - 3]

        return F[n]


print(Solution().tribonacci(4))
print(Solution().tribonacci(25))
