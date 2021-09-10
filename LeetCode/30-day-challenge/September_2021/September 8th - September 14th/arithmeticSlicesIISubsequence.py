from collections import defaultdict
from typing import List


"""
    Problem Link:- https://leetcode.com/problems/arithmetic-slices-ii-subsequence/
"""


class Solution:
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        n = len(nums)
        ans = 0
        dp = [defaultdict(int) for _ in range(n)]

        for i in range(n):
            for j in range(i):
                diff = nums[i] - nums[j]
                dp[i][diff] += dp[j][diff] + 1
                ans += dp[j][diff]

        return ans


print(Solution().numberOfArithmeticSlices(nums=[2, 4, 6, 8, 10]))
print(Solution().numberOfArithmeticSlices(nums=[7, 7, 7, 7, 7]))
