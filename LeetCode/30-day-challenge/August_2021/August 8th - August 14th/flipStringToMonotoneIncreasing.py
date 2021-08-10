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


def minFlipsMonoIncrease(s):
    flipped_zeroes = s.count("0")
    ones_to_zeroes = 0
    result = flipped_zeroes
    for c in s:
        flipped_zeroes -= c == '0'
        ones_to_zeroes += c == '1'
        result = min(result, flipped_zeroes + ones_to_zeroes)

    return result


print(minFlipsMonoIncrease(s="00110"))
print(minFlipsMonoIncrease(s="010110"))
print(minFlipsMonoIncrease(s="00011000"))
