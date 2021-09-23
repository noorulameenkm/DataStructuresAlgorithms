"""
    Problem Link:- https://leetcode.com/problems/break-a-palindrome/
"""


class Solution:
    def breakPalindrome(self, palindrome: str) -> str:
        if len(palindrome) < 2:
            return ""

        arr = list(palindrome)
        for i in range(len(arr) // 2):
            if arr[i] != 'a':
                arr[i] = 'a'
                return ''.join(arr)

        arr[-1] = 'b'
        return ''.join(arr)


print(Solution().breakPalindrome("abccba"))
print(Solution().breakPalindrome("a"))
print(Solution().breakPalindrome("aa"))
print(Solution().breakPalindrome("aba"))
