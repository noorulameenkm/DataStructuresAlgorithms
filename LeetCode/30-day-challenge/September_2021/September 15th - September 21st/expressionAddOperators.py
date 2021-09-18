from typing import List


"""
    Problem link:- https://leetcode.com/problems/expression-add-operators/
"""


class Solution:
    def addOperators(self, num: str, target: int) -> List[str]:
        def evaluate(s):
            arr = []
            temp = ""
            for c in s:
                if c.isdigit():
                    temp += c
                else:
                    arr.append(int(temp))
                    arr.append(c)
                    temp = ""

            arr.append(int(temp))

            total = arr[0]
            prev = arr[0]
            for i in range(len(arr) - 1):
                if arr[i] == '+':
                    total += arr[i + 1]
                    prev = arr[i + 1]
                elif arr[i] == '-':
                    total -= arr[i + 1]
                    prev = -arr[i + 1]
                elif arr[i] == '*':
                    total = total - prev + prev * arr[i + 1]
                    prev = prev * arr[i + 1]

            return total

        def recurse(i, s, leading):
            if i > n - 1:
                if evaluate(s) == target:
                    ans.append(s)

                return

            if leading != "0":
                recurse(i + 1, s + num[i], leading)

            recurse(i + 1, s + "+" + num[i], num[i])
            recurse(i + 1, s + "-" + num[i], num[i])
            recurse(i + 1, s + "*" + num[i], num[i])

        n = len(num)
        ans = []
        recurse(1, num[0], num[0])
        return ans


print(Solution().addOperators(num="123", target=6))
print(Solution().addOperators(num="232", target=8))
print(Solution().addOperators(num="105", target=5))
print(Solution().addOperators(num="00", target=0))
print(Solution().addOperators(num="3456237490", target=9191))
