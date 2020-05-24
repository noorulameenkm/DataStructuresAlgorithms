class Solution:
    def subarraySum(self, nums, k):
        if len(nums) == 0:
            return 0
        prev_sum = {0: 1}
        curr_sum = 0
        total = 0
        for i in range(0, len(nums)):
            curr_sum = curr_sum + nums[i]
            if prev_sum.get(curr_sum - k, None) is not None:
                total = total + prev_sum[curr_sum - k]
            
            
            if prev_sum.get(curr_sum, None) is None:
                prev_sum[curr_sum] = 1
            else:
                prev_sum[curr_sum] = prev_sum[curr_sum] + 1
        
        return total



print(f'Solution is {Solution().subarraySum([1,1,1],2)}')
