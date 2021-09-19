from functools import lru_cache


"""
    Problem Link:- https://leetcode.com/problems/distinct-subsequences/
"""


class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        @lru_cache(None)
        def recurse(si, ti):
            if ti >= tn:
                return 1
            if si >= sn:
                return 0

            count = recurse(si + 1, ti)
            if s[si] == t[ti]:
                count += recurse(si + 1, ti + 1)

            return count

        sn, tn = len(s), len(t)
        return recurse(0, 0)


print(Solution().numDistinct(s="rabbbit", t="rabbit"))
print(Solution().numDistinct(s="babgbag", t="bag"))
