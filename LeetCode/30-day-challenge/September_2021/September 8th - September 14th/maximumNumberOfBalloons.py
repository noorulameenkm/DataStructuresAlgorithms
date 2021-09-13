"""
    Problem Link:- https://leetcode.com/problems/maximum-number-of-balloons/
"""


class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        frequency = {}
        for char in text:
            if char not in frequency:
                frequency[char] = 0

            frequency[char] += 1

        count = 0
        string = "balloon"
        exit = False
        while True:
            for char in string:
                if char not in frequency:
                    exit = True
                    break

                frequency[char] -= 1
                if frequency[char] == 0:
                    del frequency[char]
            if exit:
                break

            count += 1

        return count


print(Solution().maxNumberOfBalloons(text="nlaebolko"))
print(Solution().maxNumberOfBalloons(text="loonbalxballpoon"))
print(Solution().maxNumberOfBalloons(text="leetcode"))
