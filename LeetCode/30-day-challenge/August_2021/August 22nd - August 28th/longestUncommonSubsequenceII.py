"""
    Problem Link:- https://leetcode.com/problems/longest-uncommon-subsequence-ii/
"""


class Solution:
    def findLUSlength(self, strs):
        n = len(strs)

        def is_subsequence(s1, s2):
            i, j = 0, 0

            while i < len(s1) and j < len(s2):

                if s1[i] == s2[j]:
                    i += 1

                j += 1

            return i == len(s1)

        ans = -1
        for i in range(n):
            valid = True
            for j in range(n):

                if i == j:
                    continue

                if is_subsequence(strs[i], strs[j]):
                    valid = False
                    break

            if valid:
                ans = max(ans, len(strs[i]))

        return ans


print(Solution().findLUSlength(strs=["aba", "cdc", "eae"]))
print(Solution().findLUSlength(strs=["aaa", "aaa", "aa"]))
