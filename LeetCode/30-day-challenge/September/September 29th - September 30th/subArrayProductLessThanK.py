class Solution:
    def numSubarrayProductLessThanK(self, nums, k):
        start = 0
        product = 1
        numberOfSubArrays = 0
        
        for end in range(len(nums)):
            product *= nums[end]
            
            while start < end and product >= k:
                product = (product // nums[start])
                start += 1
                
                
            if product < k:
                count = end - start + 1
                numberOfSubArrays += count
                
                
                
        return numberOfSubArrays



print(Solution().numSubarrayProductLessThanK([10, 5, 2, 6], 100))