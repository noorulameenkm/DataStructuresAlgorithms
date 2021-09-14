"""
    Problem Link:- https://leetcode.com/problems/reverse-only-letters/
"""


class Solution:
    def reverseOnlyLetters(self, s: str) -> str:
        s_array = list(s)
        i, j = 0, len(s_array) - 1
        while i < j:
            if not (s_array[i] >= 'a' and s_array[i] <= 'z' or
                    s_array[i] >= 'A' and s_array[i] <= 'Z'):
                i += 1
                continue

            if not (s_array[j] >= 'a' and s_array[j] <= 'z' or
                    s_array[j] >= 'A' and s_array[j] <= 'Z'):
                j -= 1
                continue

            s_array[i], s_array[j] = s_array[j], s_array[i]
            i += 1
            j -= 1

        return ''.join(s_array)


print(Solution().reverseOnlyLetters(s="ab-cd"))
print(Solution().reverseOnlyLetters(s="a-bC-dEf-ghIj"))
print(Solution().reverseOnlyLetters(s="Test1ng-Leet=code-Q!"))
