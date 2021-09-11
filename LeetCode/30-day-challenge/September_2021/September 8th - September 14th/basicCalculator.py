from collections import deque


"""
    Problem Link:- https://leetcode.com/problems/basic-calculator/
"""


class Solution:
    def calculate(self, s: str) -> int:
        length = len(s)
        sign = 1
        ans, curr_no = 0, 0
        stack = deque([])
        i = 0
        while i < length:
            if s[i].isdigit():
                curr_no = int(s[i])
                while i + 1 < length and s[i + 1].isdigit():
                    curr_no = curr_no * 10 + int(s[i + 1])
                    i += 1

                curr_no = curr_no * sign
                ans += curr_no
                curr_no = 0
                sign = 1
            elif s[i] == '+':
                sign = 1
            elif s[i] == '-':
                sign = -1
            elif s[i] == '(':
                stack.appendleft(ans)
                stack.appendleft(sign)
                ans = 0
                sign = 1
            elif s[i] == ')':
                prev_sign = stack.popleft()
                ans = prev_sign * ans
                prev_ans = stack.popleft()
                ans = ans + prev_ans

            i += 1
        return ans


print(Solution().calculate(s="1 + 1"))
print(Solution().calculate(s=" 2-1 + 2 "))
print(Solution().calculate(s="(1+(4+5+2)-3)+(6+8)"))
