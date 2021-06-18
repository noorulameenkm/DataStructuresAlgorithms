"""
Problem Link:- https://leetcode.com/problems/range-sum-query-mutable/
"""


class NumArray:

    def __init__(self, nums):
        self.nums = nums
        self.prefix_sum = [0 for _ in range(len(nums))]
        self.add_prefix_sum(0)
        

    def update(self, index, val):
        self.nums[index] = val
        self.add_prefix_sum(index)

    def sumRange(self, left, right):
        if left == 0:
            return self.prefix_sum[right]
        
        return self.prefix_sum[right] - self.prefix_sum[left - 1]
    
    
    def add_prefix_sum(self, index):
        
        if index == 0:
            self.prefix_sum[index] = self.nums[index]
        else:
            self.prefix_sum[index] = self.nums[index] + self.prefix_sum[index - 1]
        
        for i in range(index + 1, len(self.nums)):
            self.prefix_sum[i] = self.prefix_sum[i - 1] + self.nums[i]


class NumArray2:

    def __init__(self, nums):
        self.nums = nums
        self.BIT = [0 for _ in range(len(self.nums) + 1)]
        for i in range(len(self.nums)):
            self.updateBIT(i, self.nums[i])
        

    def update(self, index, val):
        diff = val - self.nums[index]
        self.nums[index] = val
        self.updateBIT(index, diff)

    def sumRange(self, left, right):
        if left == 0:
            return self.getBITSum(right)
        
        return self.getBITSum(right) - self.getBITSum(left - 1)
            
    def updateBIT(self, index, value):
        index += 1
        
        while index < len(self.BIT):
            self.BIT[index] += value
            
            index += (index & -index)
            
            
    def getBITSum(self, index):
        
        index += 1
        sum_ = 0
        while index > 0:
            sum_ += self.BIT[index]
            index -= (index & -index)
        
        return sum_


# Method 1
instance_ = NumArray([1, 3, 5])
print(instance_.sumRange(0, 2))
print(instance_.update(1, 2))
print(instance_.sumRange(0, 2))


# Method 2
instance_ = NumArray2([1, 3, 5])
print(instance_.sumRange(0, 2))
print(instance_.update(1, 2))
print(instance_.sumRange(0, 2))


