"""
    Problem Link:- https://leetcode.com/problems/shifting-letters/
"""


class Solution:
    def shiftingLetters(self, s, shifts):

        def get_char(num, c):
            start = ord(c)
            target = start + num
            if 97 <= target <= 122:
                return chr(target)

            return chr((ord(c) - 97 + num) % 26 + 97)

        result = ""
        n = len(shifts)
        sum_ = 0
        for i in range(n - 1, -1, -1):
            sum_ += shifts[i]
            char = get_char(sum_, s[i])
            result = char + result

        return result


print(Solution().shiftingLetters(s="aaa", shifts=[1, 2, 3]))
print(Solution().shiftingLetters(s="abc", shifts=[3, 5, 9]))
