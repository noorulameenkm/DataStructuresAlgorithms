"""
    Problem Link:- https://leetcode.com/problems/remove-all-adjacent-duplicates-in-string/
"""

from collections import deque

class Solution:
    def removeDuplicates(self, str_):
        stack = deque([])
        for char in str_:
            if len(stack) > 0 and char == stack[0]:
                stack.popleft()
                continue

            stack.appendleft(char)

        result = ""
        while len(stack) > 0:
            result = stack.popleft() + result

        return result


print(Solution().removeDuplicates(str_ = "abbaca"))
print(Solution().removeDuplicates(str_ = "azxxzy"))