from typing import List


"""
Problem Link:- https://leetcode.com/problems/jump-game/
"""


class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n = len(nums)
        dp = [False] * n
        dp[0] = True
        for i in range(n):

            if not dp[i]:
                continue

            for k in range(1, nums[i] + 1):
                if i + k == n - 1:
                    return True
                if i + k < n:
                    dp[i + k] = True

        return dp[n - 1]


class Solution2:
    def canJump(self, nums: List[int]) -> bool:
        max_index = 0

        for i, num in enumerate(nums):
            if max_index < i:
                return False
            max_index = max(max_index, i + num)

        return True


print(Solution().canJump([2, 3, 1, 1, 4]))
print(Solution().canJump([3, 2, 1, 0, 4]))
print(Solution2().canJump([2, 3, 1, 1, 4]))
print(Solution2().canJump([3, 2, 1, 0, 4]))
