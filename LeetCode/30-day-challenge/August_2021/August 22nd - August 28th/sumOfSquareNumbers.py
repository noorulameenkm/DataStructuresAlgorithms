from math import sqrt


"""
    Problem Link:- https://leetcode.com/problems/sum-of-square-numbers/
"""


class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        n = int(sqrt(c)) + 1

        for a in range(n):
            b = sqrt(c - a * a)
            if b == int(b):
                return True

        return False


print(Solution().judgeSquareSum(c=5))
print(Solution().judgeSquareSum(c=3))
print(Solution().judgeSquareSum(c=4))
print(Solution().judgeSquareSum(c=2))
print(Solution().judgeSquareSum(c=1))
