class Solution:
    def rob(self, nums):
        if len(nums) == 0:
            return 0
        elif len(nums) == 1:
            return nums[0]
        else:
            dp = [nums[0], max(nums[1], nums[0])]
            
            for i in range(2, len(nums)):
                dp.insert(i, max(nums[i] + dp[i - 2], dp[i - 1]))
                
            return dp[len(dp) - 1]
            
        

print(Solution().rob([1,2,3,1]))