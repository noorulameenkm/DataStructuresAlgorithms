"""
    Problem Link:- https://leetcode.com/problems/complex-number-multiplication/
"""


class Solution:
    def complexNumberMultiply(self, num1, num2):
        a, b = map(int, num1[:-1].split('+'))
        c, d = map(int, num2[:-1].split('+'))

        return f"{a * c - b * d}+{a * d + b * c}i"


print(Solution().complexNumberMultiply(num1="1+1i", num2="1+1i"))
print(Solution().complexNumberMultiply(num1="1+-1i", num2="1+-1i"))
