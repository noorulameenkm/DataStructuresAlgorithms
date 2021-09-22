from typing import List


"""
Problem Link:-
https://leetcode.com/problems/maximum-length-of-a-concatenated-string-with-unique-characters/
"""


class Solution:
    def maxLength(self, arr: List[str]) -> int:
        def recurse(i, s):
            if i >= n:
                length = len(s)
                self.ans = max(self.ans, length)
                return

            recurse(i + 1, s)
            new_string = s + arr[i]
            if len(new_string) == len(set(new_string)):
                recurse(i + 1, new_string)

        n = len(arr)
        self.ans = 0
        recurse(0, "")

        return self.ans


print(Solution().maxLength(["un", "iq", "ue"]))
print(Solution().maxLength(["cha", "r", "act", "ers"]))
print(Solution().maxLength(["abcdefghijklmnopqrstuvwxyz"]))
