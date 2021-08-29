"""
    Problem Link:- https://leetcode.com/problems/patching-array/
"""


class Solution:
    def minPatches(self, nums, n):
        cost, upper = 0, 0
        i = 0

        while upper < n:
            if i < len(nums) and nums[i] <= upper + 1:
                upper += nums[i]
                i += 1
            else:
                upper += upper + 1
                cost += 1

        return cost


print(Solution().minPatches(nums=[1, 3], n=6))
print(Solution().minPatches(nums=[1, 5, 10], n=20))
print(Solution().minPatches(nums=[1, 2, 2], n=5))
