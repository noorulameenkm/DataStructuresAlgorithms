"""
Problem Link:- https://leetcode.com/problems/climbing-stairs/
"""


class Solution:
    def climbStairs(self, n: int) -> int:

        if n == 1:
            return 1
        if n == 2:
            return 2

        fib = [0] * n
        fib[0], fib[1] = 1, 2
        for i in range(2, n):
            fib[i] = fib[i - 1] + fib[i - 2]

        return fib[n - 1]


print(Solution().climbStairs(2))
print(Solution().climbStairs(3))
