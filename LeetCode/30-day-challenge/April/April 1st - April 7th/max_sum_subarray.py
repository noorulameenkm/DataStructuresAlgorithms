class Solution:
    def maxSubArray(self, nums):
        if len(nums) == 0:
            return 0
        max_current = max_global = nums[0]
        for i in range(1, len(nums)):
            max_current = max(nums[i], max_current + nums[i])
            if max_current > max_global:
                max_global = max_current
        return max_global
        




nums = [-2,1,-3,4,-1,2,1,-5,4]
print(f'Solutions is {Solution().maxSubArray(nums)}')
nums_2 = [-1, -2, -3, -4]
print(f'Second Solution is {Solution().maxSubArray(nums_2)}')
        