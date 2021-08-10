"""
    Problem Link:- https://leetcode.com/problems/flip-string-to-monotone-increasing/
"""


class Solution:
    def minFlipsMonoIncr(self, s: str) -> int:
        ones, zeroes = 0, 0

        i = 0

        while i < len(s) and s[i] == '0':
            i += 1

        for k in range(i, len(s)):
            if s[k] == '0':
                zeroes += 1
            else:
                ones += 1

            if zeroes > ones:
                zeroes = ones

        return zeroes


print(Solution().minFlipsMonoIncr(s="00110"))
print(Solution().minFlipsMonoIncr(s="010110"))
print(Solution().minFlipsMonoIncr(s="00011000"))
