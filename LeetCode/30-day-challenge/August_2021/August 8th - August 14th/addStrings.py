"""
    Problem Link:- https://leetcode.com/problems/add-strings/
"""


class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        if len(num2) > len(num1):
            num1, num2 = num2, num1

        answer = ""
        carry = 0
        i, j = len(num1) - 1, len(num2) - 1
        while j >= 0:
            sum_ = int(num1[i]) + int(num2[j]) + carry
            answer = str(sum_ % 10) + answer
            carry = sum_ // 10
            j -= 1
            i -= 1

        while i >= 0:
            sum_ = int(num1[i]) + carry
            answer = str(sum_ % 10) + answer
            carry = sum_ // 10
            i -= 1

        if carry > 0:
            answer = str(carry) + answer

        return answer


print(Solution().addStrings(num1="11", num2="123"))
print(Solution().addStrings(num1="456", num2="77"))
print(Solution().addStrings(num1="0", num2="0"))
