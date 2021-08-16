"""
    Problem Link:- https://leetcode.com/problems/range-sum-query-immutable/
"""


class NumArray:

    def __init__(self, nums):
        self.nums = nums
        self.prefix = [0] * len(nums)
        self.prefix[0] = self.nums[0]
        for i in range(1, len(nums)):
            self.prefix[i] = self.nums[i] + self.prefix[i - 1]

    def sumRange(self, left, right):
        if left == 0:
            return self.prefix[right]

        return self.prefix[right] - self.prefix[left - 1]
